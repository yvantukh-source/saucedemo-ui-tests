import logging

class CheckoutInfoPage:
    def __init__(self, page, logger: logging.Logger):
        self.page   = page
        self.logger = logger.getChild("CheckoutInfoPage")
        self.first_name   = "#first-name"
        self.last_name    = "#last-name"
        self.postal_code  = "#postal-code"
        self.continue_btn = "#continue"
        self.error_message= "[data-test='error']"

    def fill_form(self, first="", last="", code=""):
        self.logger.info(f"Filling checkout info: {first!r}, {last!r}, {code!r}")
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.postal_code, code)

    def continue_checkout(self):
        self.logger.info("Clicking continue on checkout info")
        self.page.click(self.continue_btn)

    def get_error(self) -> str:
        err = self.page.locator(self.error_message).inner_text()
        self.logger.info(f"Checkout info error: {err!r}")
        return err
