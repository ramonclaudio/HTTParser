# HTTParser

Every scraping project I'd write the same conditional: `requests` + BeautifulSoup for static pages, Selenium for JavaScript-heavy ones. Two implementations to maintain. I wanted one call with a format flag. So I built this.

Python library for parsing web content over HTTP, with optional JavaScript rendering via Selenium.

## Install

```bash
git clone https://github.com/ramonclaudio/HTTParser.git
cd HTTParser
pip install -r requirements.txt
```

Optional for JavaScript rendering:

```bash
pip install selenium
```

## Usage

### HTML

```python
from httparser import HTTParser

r = HTTParser(url="https://httpbin.org/html", method="get", response_format="html")
print(r.response())
```

### JSON

```python
from httparser import HTTParser

# GET
r = HTTParser(url="https://httpbin.org/json", method="get", response_format="json")

# POST
r = HTTParser(
    url="https://httpbin.org/anything",
    method="post",
    response_format="json",
    payload={"key": "value"},
)
print(r.response())
```

### JavaScript (dynamic)

```python
from httparser import HTTParser

r = HTTParser(
    url="https://httpbin.org/delay/3",
    method="get",
    response_format="js",
    browser_path="/path/to/browser",
    chromedriver_path="/path/to/chromedriver",
)
print(r.response())
```

## Parameters

| Parameter | Required | Format |
| --- | --- | --- |
| `url` | yes | string |
| `method` | yes | `"get"` or `"post"` |
| `response_format` | yes | `"html"`, `"json"`, or `"js"` |
| `headers` | no | `{"header": "value"}` |
| `params` | no | `{"param": "value"}` |
| `payload` | no | `{"key": "value"}` (POST only) |
| `browser_path` | no | path to any Chromium-based browser binary (`js` only) |
| `chromedriver_path` | no | path to ChromeDriver (`js` only) |

## JavaScript rendering setup

Download ChromeDriver at https://chromedriver.chromium.org/downloads matching your browser version. Works with Chrome, Chromium, Edge, Brave, Arc, Dia, Vivaldi, Opera, Helium, and other Chromium-based browsers.

## Errors

Errors log to `Error.log`.

## License

MIT
