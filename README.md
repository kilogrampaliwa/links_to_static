 # Link to Bracket

 **Link to Bracket** is a Python program designed to automate the process of modifying HTML and HTML5 files by replacing certain patterns with specified format strings.

 ## Purpose

 The program serves as a convenient tool for developers and webmasters who need to perform batch modifications on HTML and HTML5 files, particularly when updating links to match a specific template or framework.

 ## Functionality

 The program offers the following key features:

 1. **Variable Extraction**: Reads variables from a configuration file (`confi.txt`). These variables are used as parameters for the modification process, allowing users to customize the replacement strings according to their requirements.

 2. **File Discovery**: Locates HTML and HTML5 files in a specified directory (`templates_raw`). This directory serves as the input source for the modification process.

 3. **Modification**: Modifies the contents of the HTML and HTML5 files, replacing specific patterns (e.g., `href="address"` or `src="address"`) with `{% given_word 'address' %}` format strings. The modification process ensures consistency and adherence to the desired template or framework.

 4. **Output**: Writes the modified contents to a new directory (`templates_new`). The output directory contains the updated files, preserving the original file structure while incorporating the necessary modifications.

 ## Usage

 To use the program, follow these steps:

 1. Ensure that the `confi.txt` file contains the necessary variables, such as the word to be used in the replacement strings.
 2. Place your HTML and HTML5 files in the `templates_raw` directory.
 3. Run the `link_to_bracket.py` script using Python 3.x.

 ## Components

 The program consists of the following components:

 - `link_to_bracket.py`: Main script that orchestrates the program's functionality, including variable extraction, file discovery, modification, and output handling.
 - `urls.py`: Module containing paths and imports for the program, facilitating modularity and organization.
 - `src/`: Directory containing submodules for specific tasks.
   - `confi_read/`: Module for extracting variables from the configuration file (`confi_read.py`).
   - `find_htmls/`: Module for finding HTML and HTML5 files (`find_files.py`).
   - `modifications/`: Module for performing modifications on files (`replacer.py`).

 ## Dependencies

 The program relies on Python 3.x and the following standard libraries:
 - `os`
 - `fnmatch`
 - `re`

 ## License

 This program is released under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for more details.
