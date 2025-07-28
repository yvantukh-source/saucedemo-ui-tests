import logging

class LoginPage:
    def __init__(self, page, logger: logging.Logger):
        self.page   = page
        self.logger = logger.getChild("LoginPage")
        self.url    = "https://www.saucedemo.com/"
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button   = "#login-button"
        self.error_message  = "[data-test='error']"

    def load(self):
        self.logger.info("Loading login page")
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.logger.info(f"Logging in: username={username!r}")
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error(self) -> str:
        err = self.page.locator(self.error_message).inner_text()
        self.logger.info(f"Error shown: {err!r}")
        return err
