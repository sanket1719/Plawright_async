from playwright.async_api import expect
from typing import Literal


class AdminPage : 
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/viewSystemUsers'
        self.header = page.get_by_role("heading", name="/ User Management")
        self.filters = page.get_by_text("User Management Job Organization Qualifications NationalitiesCorporate BrandingC")
        self.results_chart = page.locator(".orangehrm-container")
    
    async def goto(self) :
        await self.page.goto(self.url)

    
    async def verify_page_loaded(self) :
        await expect(self.header).to_be_visible()
        await expect(self.filters).to_be_visible()
    
    async def filter_user_management(self, filter_type: Literal['User Management', 'Job', 'Organization', 
                                                                'Qualifications', 'Nationalities', 'Corporate Branding', 'Configuration'], 
                                                                sub_filter_type: Literal['NONE', 'Users', 'Job Titles', 'Pay Grades', 'Employment Status', 
                                                                                         'Job Categories', 'Work Shifts', 'General Information', 'Locations', 'Structure', 
                                                                                         'Skills', 'Education', 'Licenses', 'Languages', 'Memberships', 'Email Configuration', 'Email Subscriptions']) :
        if filter_type == 'Nationalities' or filter_type == 'Corporate Branding' :
            if sub_filter_type != 'NONE':
                raise ValueError(f"{filter_type} can't have a sub_filter")
            
        await self.page.get_by_role("listitem").filter(has_text=f"{filter_type}").locator("i").click()

        if filter_type == 'User Management' or filter_type == 'Job' or filter_type == 'Organization' or filter_type == 'Qualifications' or filter_type == 'Configuration' :
            if filter_type == 'User Management' :
                if sub_filter_type != 'Users' :
                    raise ValueError(f"{filter_type} has only a 'Users' filter")
                await self.page.get_by_role("listitem").filter(has_text=re.compile(rf"^{sub_filter_type}$"))     

            if filter_type == 'Job' :
                if sub_filter_type != 'Job Titles' and sub_filter_type != 'Pay Grades' and sub_filter_type != 'Employment Status' and sub_filter_type != 'Job Categories' and sub_filter_type != 'Work Shifts' :
                    raise ValueError(f"{filter_type} doesn't match to sub-filter")
                await self.page.get_by_role("listitem").filter(has_text=re.compile(rf"^{sub_filter_type}$"))

            if filter_type == 'Organization' :
                if sub_filter_type != 'General Information' and sub_filter_type != 'Locations' and sub_filter_type != 'Structure' :
                    raise ValueError(f"{filter_type} doesn't match to sub-filter")
                await self.page.get_by_role("listitem").filter(has_text=re.compile(rf"^{sub_filter_type}$"))   
            
            if filter_type == 'Qualifications' :
                if sub_filter_type != 'Skills' and sub_filter_type != 'Education' and sub_filter_type != 'Licenses' and sub_filter_type != 'Languages' and sub_filter_type != 'Memberships' :
                    raise ValueError(f"{filter_type} doesn't match to sub-filter")
                await self.page.get_by_role("listitem").filter(has_text=re.compile(rf"^{sub_filter_type}$"))
            
            if filter_type == 'Configuration' :
                if sub_filter_type != 'Email Configuration' and sub_filter_type != 'Email Subscriptions' :
                    raise ValueError(f"{filter_type} doesn't match to sub-filter")
                await self.page.get_by_role("listitem").filter(has_text=re.compile(rf"^{sub_filter_type}$"))
                


