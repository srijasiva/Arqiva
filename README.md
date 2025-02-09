# Arqiva Website Tests

This project contains automated tests for the Arqiva website using Selenium and Python's `unittest` framework.

## Prerequisites

- Python 3.11
- Selenium
- WebDriver for the browser you are testing (e.g., ChromeDriver for Google Chrome)
- `unittest-xml-reporting` for XML reports
- `html-testRunner` for HTML reports

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/arqiva-website-tests.git
    cd arqiva-website-tests
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium unittest-xml-reporting html-testRunner
    ```

3. Download the WebDriver for your browser and ensure it is in your system's PATH.

## Running the Tests

To run the tests and generate `output.xml` and `results.html/log.html`, execute the following command:
```sh
python arqiva_website_tests.py
```
