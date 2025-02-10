# Arqiva API Testing

This repository contains the necessary files and configurations to perform API testing for the Arqiva API using Locust. The testing process is automated using a Makefile and a GitHub Actions workflow.

## Prerequisites

* Python 3.x (https://www.python.org/downloads/)
* Locust (https://locust.io/)
* Node.js (https://nodejs.org/)

## Makefile

The Makefile contains various targets to install dependencies, run tests, and clean up the project. Below are some of the key targets:

### Install Dependencies

To install all necessary dependencies, run:

```sh
make install
```

### Run API Automation Tests

To execute the API automation tests using Locust, run:

```sh
make run-api-automation
```

This will generate multiple HTML reports for different API tests.

### Clean Up

To clean up non-version controlled directories, run:

```sh
make clean
```

### GitHub Actions Workflow

The GitHub Actions workflow is defined in the `api-automation-template.yaml` file. It automates the process of setting up the environment, running the tests, and uploading the test reports as artifacts.

### Workflow Steps

1. Set up Python: Installs the specified Python version.
2. Install Locust: Installs Locust and its plugins.
3. Run API Automation Tests: Executes the API tests defined in the Makefile.
4. Upload Test Reports: Uploads the generated HTML reports as artifacts.

### Example Workflow Configuration

```yaml
name: API Automation

on:
  push:
    branches:
      - main

jobs:
  api-automation:
    runs-on: ubuntu-latest
    environment:
      name: ${{ inputs.DEPLOYMENT_ENVIRONMENT }}
    env:
      LOCUST_TAG: ${{ inputs.LOCUST_TAG }}
      API_URL: ${{ vars.API_URL }}
      AUTH_TOKEN_URL: ${{ vars.AUTH_TOKEN_URL }}
      AUTH_CLIENT_CREDENTIALS: ${{ secrets.AUTH_CLIENT_CREDENTIALS }}

    steps:
      - name: Sleep for 60 seconds
        run: sleep 60s
        shell: bash
        if: inputs.MUST_WAIT == 'true'

      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: 3.x

      - name: Install Locust
        run: make install-locust

      - name: Run API Automation Tests
        run: make run-api-automation

      - name: Upload API Automation Reports
        if: ${{ always() }}
        uses: actions/upload-artifact@v4
        with:
          name: Arqiva_reports
          path: Arqiva_*_report*.html
```

### Running Locally

To run the tests locally, ensure you have all the prerequisites installed and then execute the following commands:

1. Install dependencies:

```sh
pip install -r requirements.txt
```

2. Run the API automation tests:

```sh
python arqiva_website_tests.py
```

Check the generated HTML reports in the project directory.

### Cleaning Up

To clean up the project directory, run:

```sh
git clean -fdx
```

This will remove all non-version controlled directories and files.
