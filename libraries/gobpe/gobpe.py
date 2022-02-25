from libraries.common import act_on_element, capture_page_screenshot, log_message, check_file_download_complete, files
from config import OUTPUT_FOLDER


class GobPe:

    def __init__(self, rpa_selenium_instance, credentials: dict):
        self.browser = rpa_selenium_instance
        self.infogob_url = "https://www.gob.pe/"
        self.data_dict_list = []

    def access_infogob(self):
        """
        Access Infogob from the browser.
        """
        self.browser.go_to(self.gobpe_url)
