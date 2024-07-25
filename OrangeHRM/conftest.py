import asyncio
import pytest
import json
import pytest_asyncio
from playwright.async_api import async_playwright

def pytest_addoption(parser):
    parser.addoption("--datafile", action="store", help="Path to the JSON data file")
    print("pytest_addoption executed")

@pytest.fixture(scope='session')
def datafile(request):
    filename = request.config.getoption("--datafile")
    if not filename:
        pytest.fail('Datafile not specified. Use --datafile to specify the path to the data file.')
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

@pytest_asyncio.fixture
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

@pytest_asyncio.fixture
async def context(browser):
    context = await browser.new_context()
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    await context.tracing.stop(path="trace.zip")
    await context.close()

@pytest_asyncio.fixture
async def page(context):
    page = await context.new_page()
    yield page
