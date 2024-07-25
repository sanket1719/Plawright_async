from playwright.async_api import expect

class ViewPayGradesPage :
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/viewPayGrades'
        self.section = page.locator("#app div").filter(has_text="Pay Grades Add (5) Records FoundNameCurrencyActionsGrade 1United States DollarGr").nth(2)
        self.title = page.get_by_role("heading", name="Pay Grades")
        self.record_table_title = page.get_by_text("Records Found")
        self.record_table = page.locator(".orangehrm-container")
        self.add_button =  page.get_by_role("button", name=" Add")
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self) :
        await expect(self.section).to_be_visible()
        await expect(self.title).to_be_visible()
    
    async def add_pay_grade(self) :
        await self.add_button.click()
    