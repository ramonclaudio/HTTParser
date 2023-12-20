<p align="center">
    <a href="https://python.org" title="Go to Python homepage"><img src="https://img.shields.io/badge/Python-&gt;=3.x-blue?logo=python&amp;logoColor=white" alt="Made with Python"></a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/maintained-yes-2ea44f" alt="maintained - yes">
    <a href="/CONTRIBUTING.md" title="Go to contributions doc"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f" alt="contributions - welcome"></a>
</p>

<p align="center">
    <a href="https://pypi.org/project/requests"><img src="https://img.shields.io/badge/dependency-requests-critical" alt="dependency - requests"></a>
    <a href="https://pypi.org/project/beautifulsoup4"><img src="https://img.shields.io/badge/dependency-beautifulsoup4-critical" alt="dependency - beautifulsoup4"></a>
    <a href="https://pypi.org/project/selenium"><img src="https://img.shields.io/badge/dependency-selenium-yellow" alt="dependency - selenium"></a>
</p>

<p align="center">
    <img width="450" src="https://raw.githubusercontent.com/RMNCLDYO/HTTParser/main/.github/logo.png">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/dynamic/json?label=HTTParser&query=HTTParser&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2FHTTParser%2Fmain%2F.github%2Fversion.json" alt="HTTParser">
</p>

## Overview
HTTParser is an open-source Python library designed for parsing web content using various HTTP methods. It allows for both static and dynamic content extraction, making it a versatile tool for web scraping and data retrieval tasks.

Key features include:
- Customizable requests with various HTTP methods, headers, and parameters.
- Parsing and processing of JSON and HTML data.
- Handling dynamic web content using Selenium WebDriver.
- Comprehensive error logging and handling mechanism.
- Flexibility in response formats, facilitating integration with different types of web APIs or websites.

This tool is valuable for anyone working with web scraping, API testing, or any application requiring advanced HTTP response handling and parsing. Its modular design allows for easy extension or modification to suit specific needs or handle various web content types.

## Features
- Supports GET and POST methods.
- Handles multiple response formats: JSON, HTML, JavaScript.
- Customizable request headers, parameters, and payload.
- Option to parse dynamic content using Selenium WebDriver.
- Simple and intuitive interface for making HTTP requests.

## Available Variables
- `url`: URL of the page to be parsed. <sub>( *REQUIRED* )</sub>
- `method`: HTTP method, options: `"get"` or `"post"`. <sub>( *REQUIRED* )</sub>
- `response_format`: Response format, options: `"js"`, `"json"`, or `"html"`. <sub>( *REQUIRED* )</sub>
- `headers`: Custom HTTP headers, format: `{ "header_name": "header_value" }`. <sub>( *OPTIONAL* )</sub>
- `params`: URL parameters, format: `{ "param_name": "param_value" }`. <sub>( *OPTIONAL* )</sub>
- `payload`: Data payload for POST requests, format: `{ "payload_name": "payload_value" }`. <sub>( *OPTIONAL* )</sub>
- `browser_path`: Path to the web browser, used for JavaScript rendering. <sub>( *OPTIONAL* )</sub>
- `chromedriver_path`: Path to ChromeDriver, used for JavaScript rendering. <sub>( *OPTIONAL* )</sub>

## Prerequisites (HTML & JSON Rendering)
- Python 3.x
- `requests`, `beautifulsoup4` packages

### Installation
To install HTTParser, ensure you have Python 3.x installed. Then, you can install the repo via git clone:

```bash
git clone https://github.com/RMNCLDYO/HTTParser.git
cd HTTParser
pip install -r requirements.txt
```

## Prerequisites (Dynamic Content Rendering with Javascript) <sub>( *OPTIONAL* )</sub>
- `selenium` package
- Chromedriver
- Compatible web browser (Chrome, Brave, Opera, etc...)

### Installation <sub>( *OPTIONAL* )</sub>
```bash
pip install selenium
```

## Setting Up ChromeDriver and WebDrivers <sub>( *OPTIONAL* )</sub>

To ensure HTTParser works effectively, especially for content that requires JavaScript rendering, you'll need to download and set up ChromeDriver and a compatible WebDriver.

### Downloading ChromeDriver <sub>( *OPTIONAL* )</sub>

1. Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) to download the latest ChromeDriver.
2. Choose the version that matches your Chrome browser's version. To check your browser version, navigate to 'Help > About Google Chrome' in your browser.
3. Download the appropriate ChromeDriver for your operating system (Windows, Mac, or Linux).

### Installing ChromeDriver <sub>( *OPTIONAL* )</sub>

Follow the detailed instructions on the [ChromeDriver Getting Started](https://chromedriver.chromium.org/getting-started) page for your specific operating system.

### Choosing a Compatible WebDriver <sub>( *OPTIONAL* )</sub>

While ChromeDriver is designed for Chrome, you can also use it with other Chromium-based browsers. Here are some options:

- Google Chrome
- Brave Browser
- Opera Browser

Visit [Supported WebDrivers](https://alternativeto.net/category/browsers/chromium-based/) to explore other Chromium-based browsers.

## Usage

### HTML Response Format

```python
from httparser import HTTParser

# Example: GET request for a simple HTML page
request = HTTParser(
    url="https://httpbin.org/html",
    method="get",
    response_format="html"
)

response = request.response()
print(response)
```

### JSON Response Format

#### GET Request
```python
from httparser import HTTParser

# Example: GET request for JSON data
request = HTTParser(
    url="https://httpbin.org/json",
    method="get",
    response_format="json"
)

response = request.response()
print(response)
```

#### POST Request
```python
from httparser import HTTParser

# Example: POST request to create new data
request = HTTParser(
    url="https://httpbin.org/anything",
    method="post",
    response_format="json",
    payload={"HTTParser":"Example Payload"}
)

response = request.response()
print(response)
```

### JS Response Format

```python
from httparser import HTTParser

# Example: GET request for a page with dynamic JS content
request = HTTParser(
    url="https://httpbin.org/delay/3",
    method="get",
    response_format="js",
    browser_path="/path/to/browser",
    chromedriver_path="/path/to/chromedriver"
)

response = request.response()
print(response)
```

## Error Handling
HTTParser logs errors in 'Error.log'. Check this file for error details.

## Contributing
Contributions are welcome. Please follow the guidelines in [CONTRIBUTING](.github/CONTRIBUTING.md).

## Reporting Issues
Report issues via the GitHub issue tracker.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.
