# Installation & Test Execution Guide

## 1. Setting Up Dependencies
Before launching tests, you need to install the required dependencies. There are two options:
### A. Using the current environment:
```bash
pip install -r misc/requirements.txt
```
### B. Creating a separate Conda environment:
```bash
conda create --name facesdk_python_tests python=3.8
```
```bash
conda activate facesdk_python_tests
pip install -r misc/requirements.txt
```

## 2. Running the Tests

Run the tests using:
```bash
pytest -v
```

## 3. Configuration
Ensure you refer to the file `tests/misc/paths_and_urls.py` for paths to images and service URLs. Make sure to use the correct URL.

## 4. Generating Allure Report
You can access the run using report portal on http://172.20.40.141:8080/

To run tests with report portal use 
```bash
pytest -v --reportportal
```
Happy Testing!
