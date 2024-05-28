import re

def extract_variables(file_path: str) -> dict:
    "Extracts variable names and their values from the configuration file."

    variables = {}

    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match variable pattern
    pattern = r"\* (\w+)\n(.*?)\n"
    matches = re.findall(pattern, content, re.DOTALL)

    for match in matches:
        variable_name, value = match
        variables[variable_name] = value.strip()

    return variables
