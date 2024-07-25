# import sys
# sys.path.append('../')
# import pytest
# from src.infra.page_objects.login.login_page import LoginPage
# from src.infra.page_objects.platform.dashboard.dashboard_page import DashboardPage
# from src.tests.test_data.test_data import User


# from playwright.async_api import async_playwright, expect

# @pytest.mark.asyncio
# async def test_login_with_valid_credentials(login_page: LoginPage, dashboard_page: DashboardPage) :

#     async with async_playwright():
#         user =  await User()
#         await login_page.fill_username(user.username)
#         await login_page.fill_password(user.password)
#         await login_page.click_login_button()

#         await dashboard_page.verify_page_loaded()





