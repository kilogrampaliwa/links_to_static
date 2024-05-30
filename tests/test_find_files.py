import pytest
import os
from src.find_htmls.find_files import find_html_files
from unittest.mock import patch

@pytest.fixture
def mock_listdir():
    with patch('os.listdir') as mock:
        mock.return_value = ['file1.html', 'file2.html5', 'file3.txt']
        yield mock

def test_find_html_files(mock_listdir):
    html_files = find_html_files('templates_raw')
    assert html_files == ['file1.html', 'file2.html5']
