from playwright.async_api import expect
from typing import Literal

class ViewSystemUsersPage :
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/viewSystemUsers'
        self.fold_unfold_button = page.get_by_role("button", name="")
        self.system_users_section = page.get_by_text("System UsersUsernameUser Role-- Select --Employee NameStatus-- Select -- Reset S")
        self.system_users_title = page.get_by_text("Username", exact=True)
        self.username_field = page.get_by_text("Username", exact=True)
        self.user_role_dropdown = page.locator("form i").first
        self.employee_name_field = page.locator(".oxd-select-text").first
        self.status_dropdown = page.locator("form i").nth(1)
        self.reset_button = page.get_by_role("button", name="Reset")
        self.search_button = page.get_by_role("button", name="Search")
        self.add_user_button = page.get_by_role("button", name="Add")
        self.record_table_title = page.get_by_text("Records Found")
        self.record_table = page.locator(".orangehrm-container")
    
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self) :
        await expect(self.system_users_title).to_be_visible()
        await expect(self.system_users_section).to_be_visible()
    
    async def fill_username_field(self, username : str) :
        await self.username_field.fill(username)
    
    async def select_user_role(self, user_role : Literal['-- Select --', 'Admin', 'EES']) :
        if user_role != '-- Select --' and user_role != 'Admin' and user_role != 'EES' :
            raise ValueError('User role must be : -- Select -- , Admin or EES')
        await self.user_role_dropdown.click()
        await self.page.get_by_role("option", name=f"{user_role}").click()
    
    async def fill_employee_name(self, employee_name : str) :
        await self.employee_name_field.fill(employee_name)
    
    async def select_user_status(self, user_status : Literal['-- Select --', 'Enabled', 'Disabled']) :
        if user_status != '-- Select --' and user_status != 'Enabled' and user_status != 'Disabled' :
            raise ValueError('User role must be : -- Select -- , Enabled or Disabled')
        await self.status_dropdown.click()
        await self.page.get_by_role("option", name=f"{user_status}").click()
    
    async def reset(self) :
        await self.reset_button.click()
    
    async def search(self) :
        await self.search_button.click()
    
    async def click_add(self) :
        await self.add_user_button.click()
    
    async def perform_search(self, username: str, user_role: Literal['Admin', 'EES'], employee_name: str, user_status: Literal['Enabled', 'Disabled']) :
        await self.fill_username_field(username)
        await self.select_user_role(user_role)
        await self.fill_employee_name(employee_name)
        await self.select_user_status(user_status)
        await self.search()
        
        
        