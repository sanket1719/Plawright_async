
import logging
from datetime import datetime


def pytest_configure(config):
    logging.basicConfig(level=logging.INFO)
    root = logging.getLogger()
    root.setLevel(logging.INFO)


def validate_response_status(response, expected_status: int, expected_status_text: str):
    if response.status != expected_status:
        logging.info(f"Expected status: {expected_status}, but got: {response.status}")
        raise ValueError(f"Expected status: {expected_status}, but got: {response.status}")
    
    if response.status_text != expected_status_text:
        logging.info(f"Expected status text: {expected_status_text}, but got: {response.status_text}")
        raise ValueError(f"Expected status text: {expected_status_text}, but got: {response.status_text}")

def current_full_time():
    return datetime.now()
    