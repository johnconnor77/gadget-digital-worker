from libraries.common import act_on_element, capture_page_screenshot, log_message, check_file_download_complete, files, file_system, pdf
from config import OUTPUT_FOLDER
import pandas as pd


class GobPe:

    def __init__(self, rpa_selenium_instance):
        self.browser = rpa_selenium_instance
        self.gobpe_url = "https://www.gob.pe/"
        self.data_dict_list = []

    def access_gobpe(self):
        """
        Access Infogob from the browser.
        """
        self.browser.go_to(self.gobpe_url)

    def steps_going_to_category(self, category_filename):
        """

        """
        act_on_element("//a[@data-origin='footer-link']", "click_element")
        act_on_element("//a[@class='power-card']/descendant::div[contains(text(), 'Organismos Autónomos')]", "click_element")
        act_on_element("//a[@data-origin='estado-onpe-link']", "click_element")

        with open(category_filename) as f:
            lines = f.readlines()

        category = lines[0]

        act_on_element(f"//a[@data-origin='onpe-menu-institutional' and contains(text(),'{category}')]", "click_element")
        act_on_element("//a[@data-origin='onpe-publicaciones-ver-más-link' and contains(text(),'Buscar informes y publicaciones')]","click_element")

    def extract_info_onpe(self, date_since, date_to):
        """

        """
        print(date_since)
        self.browser.go_to(f"https://www.gob.pe/busquedas?contenido[]=publicaciones&desde={date_since}&hasta={date_to}&institucion[]=onpe&sheet=1&sort_by=recent")

        data = pd.read_excel("Files_To_Download.xlsx")

        print(data)

        elements_download = data[data.DownloadRequired == "Yes"].Name.tolist()

        for element_download in elements_download:
            xpath_2_name = f"//article[@class='bg-blue-300 mt-4 p-8']//a[contains(text(),'{element_download}')]"
            xpath_2_top_parent = "/parent::h3/parent::div/parent::div/parent::div/following-sibling::div"
            xpath_2_button = "/a[@class='bg-transparent border-2 border-blue-700 font-bold py-2 px-3 text-blue-700 flex']"
            act_on_element(xpath_2_name+xpath_2_top_parent+xpath_2_button, "click_element")

    def pdf_information(self):
        """
        Extracts information from the PDF's downloaded from ONPE.
        """

        files_downloaded = file_system.find_files("{}/*.{}".format(OUTPUT_FOLDER, "pdf"))
        for file_downloaded in files_downloaded:
            text_dict = pdf.get_text_from_pdf(file_downloaded)
            pages_amount = len(text_dict)
            print(f"file_name: {file_system.get_file_name(file_downloaded)} and amount_pages: {pages_amount}")


