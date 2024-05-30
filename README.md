
 # Link to Bracket Converter

 This project converts HTML file links (href and src attributes) into Django template static file tags. The conversion ensures that only links not already formatted with `{% static 'address' %}` are modified. The project uses configuration from a file to determine the tag to be used in the conversion.

 ## Project Structure

 ```
 project_root/
 ├── link_to_bracket.py
 ├── urls.py
 ├── confi.txt
 ├── templates_raw/
 │   ├── raw html files...
 ├── templates_new/
 │   ├── new html files...
 ├── src/
 │   ├── confi_read/
 │   │   └── confi_read.py
 │   ├── find_htmls/
 │   │   └── find_files.py
 │   ├── modifications/
 │   │   └── replacer.py
 ├── tests/
 │   ├── test_link_to_bracket.py
 │   ├── test_urls.py
 │   ├── test_confi_read.py
 │   ├── test_find_files.py
 │   ├── test_replacer.py
 ```

 ## Description

 ### link_to_bracket.py

 This script orchestrates the conversion process. It:
 1. Reads the configuration to get the tag word.
 2. Finds all HTML files in the specified directory.
 3. Reads each HTML file and performs the link conversion.
 4. Writes the converted content to a new directory.

 ### urls.py

 This script contains paths and imports the necessary modules:
 - `confi_read` for reading the configuration file.
 - `find_files` for finding HTML files.
 - `replacer` for performing the text replacement.

 ### confi.txt

 A configuration file to specify the word to be placed before links.

 Example:
 ```
 #########################################
 #                                       #
 #          link to bracket-er           #
 #                                       #
 #########################################
 #
 #  Print below '*' word to be placed before link
 * link_word
 static
 ```

 ### src/confi_read/confi_read.py

 Contains a function to extract variables from the configuration file.

 ### src/find_htmls/find_files.py

 Contains a function to find all HTML and HTML5 files in a given directory.

 ### src/modifications/replacer.py

 Contains a class `TextReplacer` that replaces `href` and `src` attributes in the HTML files with the specified tag word.

 ### tests/

 Contains test files to ensure the functionality of the entire project using `pytest`.

 ## How to Use

 1. **Clone the repository:**
    ```sh
    git clone <repository_url>
    cd project_root
    ```

 2. **Install dependencies:**
    This project uses Python 3. Make sure you have it installed, along with `pytest` for testing.

 3. **Run the main script:**
    ```sh
    python link_to_bracket.py
    ```
    This will read the configuration from `confi.txt`, find all HTML files in the `templates_raw` directory, convert the links, and save the new files in the `templates_new` directory.

 4. **Run the tests:**
    To run the tests and ensure everything is working correctly:
    ```sh
    pytest
    ```

 ## License

 This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

 ## Contributing

 Contributions are welcome! Please create a pull request with your changes or open an issue for any bugs or feature requests.

 ## Contact

 For any questions or suggestions, please contact [your email/contact information].
