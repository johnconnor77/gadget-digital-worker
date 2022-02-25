from libraries.common import log_message, capture_page_screenshot, browser
from config import OUTPUT_FOLDER
from libraries.gobpe.gobpe import GobPe


class Process:
    def __init__(self, credentials: dict):
        log_message("Initialization")
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }
        browser.open_available_browser(preferences = prefs)#browser_selection=["firefox"]
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()

        gob_pe = GobPe(browser, {"url": "https://infogob.jne.gob.pe/Eleccion/FichaEleccion/segunda-vuelta-de-elecci%C3%B3n-presidencial-2016-presidencial_candidatos-y-resultados_7p675u8oH7Q=6u"})





    def start(self):
        pass

    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()
