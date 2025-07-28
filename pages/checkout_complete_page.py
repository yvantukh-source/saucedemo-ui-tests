# pages/checkout_complete_page.py
import logging

class CheckoutCompletePage:
    def __init__(self, page, logger: logging.Logger):
        self.page   = page
        self.logger = logger.getChild("CheckoutCompletePage")
        self.header = ".complete-header"
        self.back_btn = "#back-to-products"

    def is_complete(self) -> bool:
        self.logger.info("Waiting for completion header to appear")
        # Wait for the header to be visible
        self.page.wait_for_selector(self.header, timeout=5000)
        text = self.page.locator(self.header).inner_text()
        complete = "THANK YOU FOR YOUR ORDER" in text
        self.logger.info(f"Completion header text: {text!r} → complete={complete}")
        return complete

    def back_home(self):
        self.logger.info("Clicking Back Home")
        self.page.click(self.back_btn)
