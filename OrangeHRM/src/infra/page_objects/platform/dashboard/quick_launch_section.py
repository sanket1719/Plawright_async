from playwright.async_api import expect

class QuickLaunchSection :
    def __init__(self, page) :
        self.page = page
        self.title = page.get_by_text("Quick Launch")
        self.assign_leave_button = page.get_by_role("button", name="Assign Leave")
        self.leave_list_button = page.get_by_role("button", name="Leave List")
        self.timesheets_button = page.get_by_role("button", name="Timesheets")
        self.apply_leave_button =page.get_by_role("button", name="Apply Leave")
        self.my_leave_button = page.get_by_role("button", name="My Leave")
        self.my_timesheets_button = page.get_by_role("button", name="My Timesheet")
    
    async def verify_section_loaded(self) :
        await expect(self.title).to_be_visible()
    
    async def assign_leave(self) :
        await self.assign_leave.click()
    
    async def open_leave_list(self) :
        await self.leave_list_button.click()
    
    async def open_timesheets(self) :
        await self.timesheets_button.click()
    
    async def apply_leave(self) :
        await self.apply_leave_button.click()
    
    async def open_my_leave(self) :
        await self.my_leave_button.click()
    
    async def open_my_timesheets(self) :
        await self.my_timesheets_button.click()