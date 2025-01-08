# NeuralNine Book Price Scraper

This Python script automates the process of extracting paperback book prices from NeuralNine.com. It uses Selenium WebDriver to navigate the website, locate specific book titles (currently focusing on titles containing "7 IN 1"), and extract their corresponding paperback prices.

## Features

*   Automates website navigation using Selenium.
*   Locates book titles containing "7 IN 1".
*   Extracts paperback prices.
*   Prints extracted prices to the console.
*   Uses `webdriver-manager` for automatic ChromeDriver management.
*   Includes user-agent spoofing to mimic a real browser.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [invalid URL removed] # Replace with your repo URL
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd neuralnine-book-scraper
    ```

3.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv  # macOS/Linux
    python -m venv venv    # Windows
    ```

4.  **Activate the virtual environment:**

    ```bash
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
    ```

5.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file in your project directory with the following content:

    ```
    selenium
    webdriver-manager
    ```

## Usage

1.  **Run the script:**

    ```bash
    python neuralnine_scraper.py # Replace with your script's name if different
    ```

    The script will print the extracted paperback prices to the console.

## Code Explanation (Key Parts)

*   **User-Agent Spoofing:** The script uses a user-agent string to mimic a real web browser, which helps prevent detection as a bot.

    ```python
    options = Options()
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
    ```

*   **XPath Locators:** XPath is used to locate specific elements on the page. These locators are crucial and might need adjustments if the website structure changes. For example, the XPath for finding book links with "7 IN 1" is:

    ```xpath
    //div[contains(@class,'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a
    ```

*   **Price Extraction:** The script extracts the price from elements containing "Paperback" and a dollar sign.

    ```python
    buttons_xpath = "//a[.//span[contains(text(),'Paperback')] and .//span[contains(text(),'$')]]"
    ```

## Disclaimer

This script is for educational purposes only. Web scraping should be performed responsibly and ethically, respecting the target website's terms of service and `robots.txt`. Avoid overloading the website with requests. The authors of this script are not responsible for any misuse.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## License

[Choose a license](https://choosealicense.com/) (e.g., MIT License) and add a `LICENSE` file to your repository.

## Future Enhancements

*   Support for extracting prices for other book formats (e.g., Kindle).
*   More robust error handling and logging.
*   Command-line arguments for specifying book titles or other search criteria.
*   Saving the extracted data to a file (e.g., CSV, JSON).

## Known Issues

*   This script is dependent on the specific HTML structure of NeuralNine.com. Changes to the website's layout may break the script. Regular maintenance and updates may be required.
*   The script currently focuses on books with "7 IN 1" in the title. Expanding to other titles would require modifying the XPath locators.
