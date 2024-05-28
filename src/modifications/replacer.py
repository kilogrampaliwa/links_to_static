import re
from typing import List

class TextReplacer:
    "A class to replace links to brackets."

    def __init__(self, given_word: str):
        self.given_word = given_word

    def replace_href(self, lines: List[str]) -> List[str]:
        """Replaces all occurrences of href="address" with href="{% given_word 'address' %}"."""

        pattern = r'href\s*=\s*"([^"]+)"'
        replacement = r'href = "{% ' + self.given_word + r" '\1' %}"
        new_lines = ["{"+"%"+ self.given_word +"%"+"}\n"]
        new_lines+=[re.sub(pattern, replacement, line) for line in lines]

        return new_lines

    def replace_src(self, lines: List[str]) -> List[str]:
        """Replaces all occurrences of src="address" with src="{% given_word 'address' %}"."""

        pattern = r'src\s*=\s*"([^"]+)"'
        replacement = r'src = "{% ' + self.given_word + r" '\1' %}"
        new_lines = ["{"+"%"+ self.given_word +"%"+"}\n"]
        new_lines+=[re.sub(pattern, replacement, line) for line in lines]

        return new_lines

    def replace(self, lines: List[str]) -> List[str]:
        "replaces both href's and src's."
        replaced_0 = self.replace_href(lines)
        return       self.replace_src (replaced_0)[1:]
