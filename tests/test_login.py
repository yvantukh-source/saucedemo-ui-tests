# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

BASE_URL = "https://www.saucedemo.com/"

@pytest.mark.parametrize("username,password,expected", [
    ("standard_user", "secret_sauce", None),
    ("invalid_user", "secret_sauce", "Username and password do not match"),
    ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("a", "secret_sauce", "Username and password do not match"),
    ("a"*100, "secret_sauce", "Username and password do not match"),
    ("standard_user", "a", "Username and password do not match"),
    ("standard_user", "a"*100, "Username and password do not match"),
])
def test_login_variants(page, logger,  username, password, expected):
    logger.info(f"TEST login_variants: {username!r}, {password!r}")
    login = LoginPage(page, logger)
    inventory = InventoryPage(page, logger)
    login.load()
    login.login(username, password)
    if expected is None:
        assert page.url == BASE_URL + "inventory.html"
        assert inventory.is_loaded()
        logger.info("Login success verified")
    else:
        assert expected.lower() in login.get_error().lower()
        logger.info("Expected error verified")