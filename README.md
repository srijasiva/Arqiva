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
    git clone https://github.com/srijasiva/Arqiva.git
    cd arqiva-website-tests
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium unittest-xml-reporting html-testRunner chromedriver-autoinstaller
    ```

3. Download the WebDriver for your browser and ensure it is in your system's PATH.

## Running the Tests

To run the tests and generate `output.xml` and `results.html/log.html`, execute the following command:
```sh
python arqiva_website_tests.py
```

## Continuous Integration (CI) Pipeline

This project uses GitHub Actions for continuous integration. The CI pipeline is defined in the `.github/workflows/CI.yml` file. The pipeline is triggered on pushes and pull requests to the `main` branch.

### Setting Up the CI Pipeline

1. Ensure that your repository contains the `.github/workflows/CI.yml` file.

2. Commit and push the `.github/workflows/CI.yml` file to your repository.

3. The CI pipeline will automatically run when you push changes to the `main` branch or create a pull request targeting the `main` branch.

### Viewing CI Pipeline Results

1. Navigate to the "Actions" tab in your GitHub repository.
2. Select the workflow run you want to view.
3. You can see the details of each job and step, including the test results and screenshots.

By following these steps, you can set up and run the CI pipeline for your Arqiva website tests using GitHub Actions.
