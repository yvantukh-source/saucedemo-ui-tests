import pytest
from pages.login_page       import LoginPage
from pages.inventory_page   import InventoryPage
from pages.cart_page        import CartPage

@pytest.fixture
def cart_page(page, logger):
    login = LoginPage(page, logger)
    inv   = InventoryPage(page, logger)
    login.load()
    login.login("standard_user", "secret_sauce")
    inv.add_all_items()
    inv.go_to_cart()
    return CartPage(page, logger)

def test_navigate_to_cart(cart_page, logger, page):
    logger.info("TEST navigate_to_cart")
    assert page.url.endswith("/cart.html")
    assert cart_page.item_count() == 6

def test_remove_one_item(cart_page, logger):
    logger.info("TEST remove_one_item")
    initial = cart_page.item_count()
    cart_page.remove_one()
    assert cart_page.item_count() == initial - 1

def test_continue_shopping(cart_page, logger, page):
    logger.info("TEST continue_shopping")
    cart_page.continue_shopping()
    from pages.inventory_page import InventoryPage
    inv = InventoryPage(page, logger)
    assert inv.is_loaded()
    assert page.locator(".shopping_cart_badge").is_visible()
