import pytest
import urls
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_extract_variables():
    with patch('urls.confi_read.extract_variables') as mock:
        mock.return_value = {"link_word": "static"}
        yield mock

@pytest.fixture
def mock_find_html_files():
    with patch('urls.find_files.find_html_files') as mock:
        mock.return_value = ["test1.html", "test2.html"]
        yield mock

@pytest.fixture
def mock_replacer():
    with patch('urls.replacer.TextReplacer.replace') as mock:
        mock.return_value = ["{% static %}\n", 'some text href = "{% static \'address\' %}"']
        yield mock

@pytest.fixture
def mock_file_read():
    m = mock_open(read_data='some text href = "address"')
    with patch('builtins.open', m):
        yield m

@pytest.fixture
def mock_file_write():
    m = mock_open()
    with patch('builtins.open', m, create=True):
        yield m

def test_link_to_bracket(mock_extract_variables, mock_find_html_files, mock_replacer, mock_file_read, mock_file_write):
    import link_to_bracket  # Importing after patching to use mocks
    # Ensure the mocks were called correctly
    mock_extract_variables.assert_called_once_with(urls.CONFI)
    mock_find_html_files.assert_called_once_with(urls.RAWS)
    assert mock_replacer.call_count == 2
    assert mock_file_read.call_count == 2
    assert mock_file_write.call_count == 2

    # Check the written contents
    handle = mock_file_write()
    handle.write.assert_called_with("{% static %}\n")
