import logging
from src.helpers.helper_methods import current_full_time
from playwright.async_api import Page, expect

logging.basicConfig(level=logging.INFO)
class DashboardPage :
    def __init__(self, page: Page) :
        self.page = page
        self.url = 'dashboard/index'
        self.dashboard_title = page.get_by_role("heading", name="Dashboard")
        self.time_at_work_section = page.get_by_text("Time at Work")
        self.my_actions_section = page.get_by_text("My Actions")
        self.quick_launch_section = page.get_by_text("Quick Launch")
        self.buzz_latest_price_section = page.get_by_text("Buzz Latest Posts")
        self.employees_on_leave_section = page.get_by_text("Employees on Leave Today")
        self.employees_distribution_by_unit = page.get_by_text("Employee Distribution by Sub Unit")
        self.employees_distribution_by_location = page.get_by_text("Employee Distribution by Location")
        logging.info(f"{current_full_time()}: Dashboard page initialized")
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self):
        await expect(self.dashboard_title).to_be_visible()
        logging.info(f"{current_full_time()}: Dashboard page loaded")
    
    
