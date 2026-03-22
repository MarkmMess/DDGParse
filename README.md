# 🔍 Website Position Finder (Selenium)

A simple Python script that finds the position of a specified website in DuckDuckGo search results using Selenium.

---

## 📌 Description

The script:
- Opens DuckDuckGo
- Performs a search query
- Checks the first 5 pages of results
- Determines the position of the specified URL in search results

If the website is found — it returns its position and the page number.

---

## ⚙️ Requirements

Before running, make sure you have installed:

- Python 3.10+
- Selenium
- browser (Firefox, Chrome, Edge, Ie or Safari)

### Clone the repository

```bash
git clone https://github.com/MarkmMess/DDGParse.git
cd DDGParse
```

### Install dependencies

```bash
pip install selenium
```

## Browser Configuration

Basic browser is Chrome
You can change which browser is used directly in the code.
In main.py you will find this line:
```bash
driver = webdriver.Chrome()
```
You can replace it with:
```bash
driver = webdriver.Firefox()
```
or 
```bash
driver = webdriver.Edge()
```
or 
```bash
driver = webdriver.Safari()
```
A comment is already added in the code indicating where this change can be made.

## Usage

Run the script:
```bash
python main.py
```
Then enter:
```bash
enter your request: example
enter url to find it's position: example.com
```

## Example output

```bash
example.com is found at 3 position, from page 2
```
or
```bash
None
```
(if website is not found)