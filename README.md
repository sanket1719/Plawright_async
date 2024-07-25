# OrangeHRM Automation

This project contains automation tests for the OrangeHRM platform using Playwright and pytest. The tests include logging into the platform and verifying the dashboard page's elements.
It uses async playwright.
## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- Pip (Python package installer)

## Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/orangehrm-automation.git
    cd orangehrm-automation
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

      ```sh
      .\venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```sh
      source venv/bin/activate
      ```

4. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` includes:

    ```plaintext
    pytest
    pytest-asyncio
    pytest-html
    playwright
    ```

5. **Install Playwright browsers**:

    ```sh
    python -m playwright install
    ```

## Running the Tests

1. **Prepare your JSON data file**:

    Create a `user_data.json` file with the following structure:

    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```

2. **Run the tests**:

    ```sh
    pytest --datafile=path/to/your/user_data.json
    ```

## Generating Reports

To generate an HTML report of your test runs, use the `--html` option with pytest:

```sh
pytest --datafile=path/to/your/user_data.json --html=report.html
