from playwright.async_api import expect
from typing import Literal

class SaveJobTitlePage :
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/saveJobTitle'
        self.add_job_section = page.get_by_text("Add Job TitleJob TitleJob DescriptionJob SpecificationBrowseNo file chosenAccept")
        self.title = page.get_by_role("heading", name="Add Job Title")
        self.job_title_field = page.get_by_role("textbox").nth(1)
        self.description_field = page.get_by_placeholder("Type description here")
        self.upload_browser_button = page.get_by_text("Browse")
        self.no_file_chosen_text = page.get_by_text("No file chosen")
        self.upload_icon = page.locator("div").filter(has_text=re.compile(r"^Job SpecificationBrowseNo file chosen$")).locator("i")
        self.note_field = page.get_by_placeholder("Add note")
        self.cancel_button = page.get_by_role("button", name="Cancel")
        self.save_button = page.get_by_role("button", name="Save")
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self) :
        await expect(self.add_job_section).to_be_visible()
        await expect(self.title).to_be_visible()
    
    async def fill_job_title(self, job_title: str) :
        await self.job_title_field.fill(job_title)
    
    async def fill_description(self, description: str) :
        await self.description_field.fill(description)
    
    async def upload_job_specification_file(self) :
        await print("empty")
        # needs to be completed
    
    async def fill_note(self, note: str) :
        await self.note_field.fill(note)
    
    async def cancel(self) :
        await self.cancel_button.click()
    
    async def save(self) :
        await self.save_button.click()
    
        