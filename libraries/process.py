from libraries.common import log_message, capture_page_screenshot, browser
from config import OUTPUT_FOLDER
from libraries.gobpe.gobpe import GobPe
import datetime


class Process:
    def __init__(self):
        log_message("Initialization")
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }
        browser.open_available_browser(preferences = prefs) #browser_selection=["firefox"]
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()

    def start(self):

        log_message("Go to Peruvian Government WebPage")
        gob_pe = GobPe(browser)
        gob_pe.access_gobpe()
        log_message("Go to Cageroy inside .txt file")
        gob_pe.steps_going_to_category(category_filename="Category.txt")
        log_message("Extract Info from certain dates")
        gob_pe.extract_info_onpe(date_since=datetime.datetime(2021, 10, 28).strftime("%d-%m-%Y"),
                                 date_to=datetime.datetime.now().strftime("%d-%m-%Y"))

    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()
