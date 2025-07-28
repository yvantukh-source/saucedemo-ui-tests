import logging

class CheckoutOverviewPage:
    def __init__(self, page, logger: logging.Logger):
        self.page   = page
        self.logger = logger.getChild("CheckoutOverviewPage")
        self.subtotal_label = ".summary_subtotal_label"
        self.tax_label      = ".summary_tax_label"
        self.total_label    = ".summary_total_label"
        self.finish_btn     = "#finish"
        self.cancel_btn     = "#cancel"

    def get_totals(self) -> dict:
        totals = {
            "item_total": self.page.locator(self.subtotal_label).inner_text(),
            "tax":        self.page.locator(self.tax_label).inner_text(),
            "total":      self.page.locator(self.total_label).inner_text(),
        }
        self.logger.info(f"Checkout totals: {totals}")
        return totals

    def finish(self):
        self.logger.info("Finishing checkout")
        self.page.click(self.finish_btn)

    def cancel(self):
        self.logger.info("Cancelling checkout")
        self.page.click(self.cancel_btn)
