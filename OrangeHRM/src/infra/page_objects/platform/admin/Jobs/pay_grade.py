from playwright.async_api import expect


class PayGradePage :
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/payGrade'
        self.section = page.get_by_text("Add Pay GradeName * Required Cancel Save")
        self.title = page.get_by_role("heading", name="Add Pay Grade")
        self.pay_grade_name = page.locator("form").get_by_role("textbox")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.save_button = page.get_by_role("button", name="Save")
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def ill_pay_grade_name(self, pay_grade_name: str) :
        await self.pay_grade_name.fill(pay_grade_name)
    
    async def cancel(self) :
        await self.cancel_button.click()
    
    async def save(self) :
        await self.save_button.click()
    
    
