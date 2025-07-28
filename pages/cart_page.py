import logging

class CartPage:
    def __init__(self, page, logger: logging.Logger):
        self.page   = page
        self.logger = logger.getChild("CartPage")
        self.items_button = ".cart_item"
        self.remove_buttons = ".cart_item button"
        self.continue_button = "#continue-shopping"
        self.checkout_button = "#checkout"

    def item_count(self) -> int:
        cnt = self.page.locator(self.items_button).count()
        self.logger.info(f"Cart contains {cnt} items")
        return cnt

    def remove_one(self):
        self.logger.info("Removing one item from cart")
        self.page.locator(self.remove_buttons).first.click()
        self.page.wait_for_timeout(200)

    def continue_shopping(self):
        self.logger.info("Continuing shopping")
        self.page.click(self.continue_button)

    def proceed_to_checkout(self):
        self.logger.info("Proceeding to checkout")
        self.page.click(self.checkout_button)
