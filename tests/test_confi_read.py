import pytest
from src.confi_read.confi_read import extract_variables
from unittest.mock import mock_open, patch

@pytest.fixture
def confi_file_content():
    return """
#########################################
#                                       #
#          link to bracket-er           #
#                                       #
#########################################
#
#  Print below '*' word to be placed before link
* link_word
static
"""

def test_extract_variables(confi_file_content):
    m = mock_open(read_data=confi_file_content)
    with patch('builtins.open', m):
        variables = extract_variables('confi.txt')
        assert variables == {"link_word": "static"}
