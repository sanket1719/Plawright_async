from playwright.async_api import expect

class ViewOrganizationGeneralInformationPage :
    def __init__(self, page) :
        self.page = page
        self.url = 'admin/viewOrganizationGeneralInformation'
        self.section = page.get_by_text("General InformationEditOrganization NameNumber of Employees79Registration Number")
        self.title = page.get_by_role("heading", name="General Information")
        self.edit_toggle = page.locator("label").filter(has_text="Edit").locator("span")
        self.organization_name_field = page.locator("div:nth-child(2) > .oxd-input").first
        self.registration_number_field = page.locator("div:nth-child(2) > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-input").first
        self.tax_id_field = page.locator("div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input").first
        self.phone_field = page.locator("div:nth-child(4) > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-input").first
        self.fax_field = page.locator("div:nth-child(4) > .oxd-grid-3 > div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input")
        self.email_field = page.locator("div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-input").first
        self.street_1_field = page.locator("div:nth-child(6) > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-input").first
        self.street_2_field = page.locator("div:nth-child(6) > .oxd-grid-3 > div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input")
        self.city_field = page.locator("div:nth-child(6) > .oxd-grid-3 > div:nth-child(3) > .oxd-input-group > div:nth-child(2) > .oxd-input")
        self.state_province_field = page.locator("div:nth-child(7) > .oxd-grid-3 > div > .oxd-input-group > div:nth-child(2) > .oxd-input").first
        self.zip_code_field = page.locator("div:nth-child(7) > .oxd-grid-3 > div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-input")
        self.country_dropdown = page.locator("form i")
        self.note_field = page.locator("textarea")
        self.save_button = page.get_by_role("button", name="Save")
    
    async def goto(self) :
        await self.page.goto(self.url)
    
    async def verify_page_loaded(self) :
        await expect(self.section).to_be_visible()
        await expect(self.title).to_be_visible()
        
    
    async def enable_editing(self) :
        if await expect(self.organization_name_field).to_be_enabled() :
            print("Form already enabled")
        else :
            self.edit_toggle.click()
            await expect(self.organization_name_field).to_be_enabled()
    
    async def disable_editing(self) :
        if await expect(self.organization_name_field).to_be_disabled() :
            print("Form already disabled")
        else :
            self.edit_toggle.click()
            await expect(self.organization_name_field).to_be_disabled()
    
    async def fill_organization_name(self, org_name : str) :
        if await expect(self.organization_name_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.organization_name_field.fill(org_name)
    
    async def fill_registration_numer(self, registration_num : str) :
        if await expect(self.registration_number_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.registration_number_field.fill(registration_num)
    
    async def fill_tax_id(self, tax_id: str) :
        if await expect(self.tax_id_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.tax_id_field.fill(tax_id)
    
    async def fill_phone_number(self, phone_num : str) :
        if await expect(self.phone_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.phone_field.fill(phone_num)
    
    async def fill_fax_number_field(self, fax_num: str) :
        if await expect(self.fax_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.fax_field.fill(fax_num)
    
    async def fill_email(self, email: str) :
        if await expect(self.email_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.email_field.fill(email)
    
    async def fill_street1(self, street: str) :
        if await expect(self.street_1_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.street_1_field.fill(street)
    
    async def fill_street2(self, street: str) :
        if await expect(self.street_2_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.street_2_field.fill(street)
    
    async def fill_city(self, city: str) :
        if await expect(self.city_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.city_field.fill(city)
    
    async def fill_state_province(self, state_province : str) :
        if await expect(self.state_province_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.state_province_field.fill(state_province)
    
    async def fill_zip_code(self, zip_code: str) :
        if await expect(self.zip_code_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.zip_code_field.fill(zip_code)
    
    async def select_country(self, country: str) :
        if await expect(self.country_dropdown).to_be_disabled() :
            raise ValueError("Dropdown disabled")
        else :
            await self.country_dropdown.click()
            await self.page.get_by_role("option", name=f"{country}").click()
    
    async def fill_notes(self, notes: str) :
        if await expect(self.note_field).to_be_disabled() :
            raise ValueError("Field disabled")
        else :
            await self.note_field.fill(notes)


    async def verify_num_of_employees(self, num_employees: int) :
        await expect(self.page.get_by_text(f"Number of Employees{str(num_employees)}")).to_be_visible()
    
    async def save(self) :
        await self.save_button.click()
    
