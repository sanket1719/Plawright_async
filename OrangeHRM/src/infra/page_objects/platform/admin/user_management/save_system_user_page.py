from playwright.async_api import expect
from typing import Literal

class SaveSystemUserPage :
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/saveSystemUser'
        self.add_user_section = page.get_by_text("Add UserUser Role-- Select --Employee NameStatus-- Select --UsernamePasswordFor ")
        self.add_user_title = page.get_by_role("heading", name="Add User")
        self.user_role_dropdown = page.locator("form i").first
        self.employee_name_field = page.get_by_placeholder("Type for hints...")
        self.user_status_dropdown = page.locator("form i").nth(1)
        self.username_field = page.get_by_role("textbox").nth(2)
        self.password_field = page.get_by_role("textbox").nth(2)
        self.confirm_password_field = page.get_by_role("textbox").nth(4)
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.save_button = page.get_by_role("button", name="Save")
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self) :
        await expect(self.add_user_section).to_be_visible()
        await expect(self.add_user_title).to_be_visible()
    
    async def select_user_role(self, user_role : Literal['-- Select --', 'Admin', 'EES']) :
        if user_role != '-- Select --' and user_role != 'Admin' and user_role != 'EES' :
            raise ValueError('User role must be : -- Select -- , Admin or EES')
        await self.user_role_dropdown.click()
        await self.page.get_by_role("option", name=f"{user_role}").click()

    async def fill_employee_name(self, employee_name: str) :
        await self.employee_name_field.fill(employee_name)
    

    async def select_user_status(self, user_status : Literal['-- Select --', 'Enabled', 'Disabled']) :
        if user_status != '-- Select --' and user_status != 'Enabled' and user_status != 'Disabled' :
            raise ValueError('User role must be : -- Select -- , Enabled or Disabled')
        await self.user_status_dropdown.click()
        await self.page.get_by_role("option", name=f"{user_status}").click()
    
    async def fill_username(self, username: str) : 
        await self.username_field.fill(username)
    
    async def fill_password(self, password: str) :
        await self.password_field.fill(password)
    
    async def confirm_password(self, confirmed_password: str) :
        await self.confirm_password_field.fill(confirmed_password)
    
    async def cancel(self) :
        await self.cancel_button.click()
    
    async def save(self) :
        await self.save_button.click()
    
    