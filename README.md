# test-cosmed
This project automates the shopping process on the Cosmed website using Python, Selenium, pytest, and Chrome (version 126.0.6478.62).
1. Go to the official website of the store.
2. Search for the product.
3. Click on the first product.
4. On the product page, click on "Add to Cart".

# Installation
[Python](https://www.python.org/downloads/)

pytest
```bash
pip install pytest
```
selenium
```bash
pip install selenium
```
Update/Download Chrome
```bash
version 126.0.6478.62
```

# Usage
clone the project
```bash
git clone https://github.com/YuMin29/test-cosmed.git
```

go to folder and execute pytest：
```bash
cd test-cosmed

python3.x -m pytest .\test_shopping_process.py -v
```

# Result
![image](https://github.com/YuMin29/test-cosmed/assets/31217649/ef476777-0165-4c37-a638-84ad25ef93cd)


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate and provide a brief description of the project's purpose.
