import pytest
from pages.login_page       import LoginPage
from pages.inventory_page   import InventoryPage

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def inventory_page(page, logger):
    login = LoginPage(page, logger)
    inv   = InventoryPage(page, logger)
    login.load()
    login.login("standard_user", "secret_sauce")
    return inv

def test_inventory_requires_login(page, logger):
    logger.info("TEST inventory_requires_login")
    page.goto(BASE_URL + "inventory.html")
    assert page.locator("#login-button").is_visible()

def test_inventory_loaded(inventory_page, logger):
    logger.info("TEST inventory_loaded")
    assert inventory_page.is_loaded()

def test_product_count_is_6(inventory_page, logger):
    logger.info("TEST product_count_is_6")
    assert inventory_page.product_count() == 6

@pytest.mark.parametrize("option,locator,parse,sort_fn", [
    ("Name (A to Z)",     ".inventory_item_name", lambda t: t,                  lambda v: sorted(v)),
    ("Name (Z to A)",     ".inventory_item_name", lambda t: t,                  lambda v: sorted(v, reverse=True)),
    ("Price (low to high)"," .inventory_item_price", lambda t: [float(x.replace('$','')) for x in t], lambda v: sorted(v)),
    ("Price (high to low)"," .inventory_item_price", lambda t: [float(x.replace('$','')) for x in t], lambda v: sorted(v, reverse=True)),
])
def test_sorting(inventory_page, page, logger, option, locator, parse, sort_fn):
    logger.info(f"TEST sorting by {option}")
    inv = inventory_page
    inv.sort_by(option)
    raw = page.locator(locator).all_inner_texts()
    vals= parse(raw)
    assert vals == sort_fn(vals)

def test_add_all_items_to_cart(inventory_page, logger):
    logger.info("TEST add_all_items_to_cart")
    inv = inventory_page
    inv.add_all_items()
    badge = inventory_page.page.locator(".shopping_cart_badge").inner_text()
    assert int(badge) == inv.product_count()
