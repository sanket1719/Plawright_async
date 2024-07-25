from playwright.async_api import expect

class ViewJobTitleListPage :
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/viewJobTitleList'
        self.title = page.get_by_role("heading", name="Job Titles")
        self.record_table_title = page.get_by_text("Records Found")
        self.record_table = page.locator(".orangehrm-container")
        self.add_button = page.get_by_role("button", name=" Add")

    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self) :
        await expect(self.title).to_be_visible()
    
    async def add_title(self) :
        await self.add_button.click()
    
        