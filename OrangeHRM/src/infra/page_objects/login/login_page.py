import logging
from src.helpers.helper_methods import current_full_time
from playwright.async_api import Page, expect

logging.basicConfig(level=logging.INFO)


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
        logging.info(f"{current_full_time()}: Login page initialized")

    @property
    def page_url(self):
        return 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    @property
    def header(self):
        return self.page.locator(".orangehrm-login-branding")

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def header_logo(self):
        return self.page.get_by_role("img", name="company-branding")

    @header_logo.setter
    def header_logo(self, value):
        self._header_logo = value

    @property
    def login_title(self):
        return self.page.get_by_role("heading", name="Login")

    @login_title.setter
    def login_title(self, value):
        self._login_title = value

    @property
    def username_field(self):
        return self.page.get_by_placeholder("Username")

    @username_field.setter
    def username_field(self, value):
        self._username_field = value

    @property
    def password_field(self):
        return self.page.get_by_placeholder("Password")

    @password_field.setter
    def password_field(self, value):
        self._password_field = value

    @property
    def username_text(self):
        return self.page.get_by_text("Username", exact=True)

    @username_text.setter
    def username_text(self, value):
        self._username_text = value

    @property
    def password_text(self):
        return self.page.get_by_text("Password", exact=True)

    @password_text.setter
    def password_text(self, value):
        self._password_text = value

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @login_button.setter
    def login_button(self, value):
        self._login_button = value

    @property
    def forgot_password_link(self):
        return self.page.get_by_text("Forgot your password?")

    @forgot_password_link.setter
    def forgot_password_link(self, value):
        self._forgot_password_link = value

    @property
    def footer(self):
        return self.page.get_by_text("© 2005 - 2023 OrangeHRM, Inc. All rights reserved.")

    @footer.setter
    def footer(self, value):
        self._footer = value

    @property
    def error_message(self):
        return self.page.get_by_text("Invalid credentials")
    
    @error_message.setter
    def error_message(self, value):
        self._error_message = value

    async def goto(self):
        await self.page.goto(self.url)

    
    async def verify_page_loaded(self):
        await expect(self.header).to_be_visible()
        await expect(self.login_title).to_be_visible() 
        logging.info(f"{current_full_time()}: Login page loaded ")

    async def login(self, username: str, password: str):
        await self.fill_username(username)
        await self.fill_password(password)
        await self.click_login_button()

    async def fill_username(self, username:str):
        await self.username_field.fill(username)
        logging.info(f"{current_full_time()}: Username: {username} filled. ")

    async def fill_password(self, password: str):
        await self.password_field.fill(password)
        logging.info(f"{current_full_time()}: Password filled")

    async def click_login_button(self):
        await self.login_button.click()
        logging.info(f"{current_full_time()}: Login button clicked")

    async def click_forgot_password(self):
        await self.forgot_password_link.click()

    async def verify_error_message_visible(self):
        await expect(self.error_message).to_be_visible()
        logging.info(f"{current_full_time()}: Error message appeared")
