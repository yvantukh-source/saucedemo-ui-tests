import logging

class InventoryPage:
    def __init__(self, page, logger: logging.Logger):
        self.page   = page
        self.logger = logger.getChild("InventoryPage")
        self.url          = "https://www.saucedemo.com/"
        self.container    = ".inventory_container"
        self.products     = ".inventory_item"
        self.names        = ".inventory_item_name"
        self.prices       = ".inventory_item_price"
        self.add_buttons  = ".inventory_item button"
        self.cart_icon    = ".shopping_cart_link"
        self.sort_dropdown= ".product_sort_container"
        self.menu_button  = "#react-burger-menu-btn"
        self.logout_link  = "#logout_sidebar_link"

    def load(self):
        self.logger.info("Navigating to inventory page")
        self.page.goto(self.url + "inventory.html")

    def is_loaded(self) -> bool:
        loaded = self.page.locator(self.container).is_visible()
        self.logger.info(f"Inventory loaded: {loaded}")
        return loaded

    def product_count(self) -> int:
        cnt = self.page.locator(self.products).count()
        self.logger.info(f"Product count: {cnt}")
        return cnt

    def add_all_items(self):
        buttons = self.page.locator(self.add_buttons)
        cnt     = buttons.count()
        self.logger.info(f"Adding all {cnt} items to cart")
        for i in range(cnt):
            buttons.nth(i).click()

    def add_first_item(self):
        self.logger.info("Adding first item to cart")
        self.page.locator(self.add_buttons).first.click()

    def go_to_cart(self):
        self.logger.info("Navigating to cart")
        self.page.click(self.cart_icon)

    def sort_by(self, option: str):
        self.logger.info(f"Sorting by: {option}")
        self.page.select_option(self.sort_dropdown, label=option)
        self.page.wait_for_timeout(300)

    def open_menu_and_logout(self):
        self.logger.info("Opening menu and logging out")
        self.page.click(self.menu_button)
        self.page.wait_for_selector(self.logout_link)
        self.page.click(self.logout_link)
