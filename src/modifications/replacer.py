import re
from typing import List

class TextReplacer:
    """A class to replace links to brackets."""

    def __init__(self, given_word: str):
        self.given_word = given_word

    def replace_href(self, lines: List[str]) -> List[str]:
        """Replaces all occurrences of href="address" with href="{% given_word 'address' %}", skipping those already in the correct format."""
        pattern = r'href\s*=\s*"([^"]+)"'
        replacement = r'href = "{% ' + self.given_word + r" '\1' %}" + r'"'
        proper_format_pattern = r'href\s*=\s*"{%\s*' + self.given_word + r"\s*'[^']+'\s*%}"
        new_lines = ["{" + "% " + self.given_word + " %}\n"]

        for line in lines:
            if re.search(proper_format_pattern, line):
                new_lines.append(line)
            else:
                new_lines.append(re.sub(pattern, replacement, line))

        return new_lines

    def replace_src(self, lines: List[str]) -> List[str]:
        """Replaces all occurrences of src="address" with src="{% given_word 'address' %}", skipping those already in the correct format."""
        pattern = r'src\s*=\s*"([^"]+)"'
        replacement = r'src = "{% ' + self.given_word + r" '\1' %}" + r'"'
        proper_format_pattern = r'src\s*=\s*"{%\s*' + self.given_word + r"\s*'[^']+'\s*%}"
        new_lines = ["{" + "% " + self.given_word + " %}\n"]

        for line in lines:
            if re.search(proper_format_pattern, line):
                new_lines.append(line)
            else:
                new_lines.append(re.sub(pattern, replacement, line))

        return new_lines

    def replace(self, lines: List[str]) -> List[str]:
        """Replaces both href's and src's, skipping those already in the correct format."""
        replaced_0 = self.replace_href(lines)
        return self.replace_src(replaced_0)[1:]
