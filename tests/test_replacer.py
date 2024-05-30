import pytest
from src.modifications.replacer import TextReplacer

@pytest.fixture
def text_replacer():
    return TextReplacer(given_word="static")

def test_replace_href(text_replacer):
    lines = ['some text href="address"']
    expected = ["{% static %}\n", 'some text href = "{% static \'address\' %}"']
    assert text_replacer.replace_href(lines) == expected

def test_replace_src(text_replacer):
    lines = ['some text src="address"']
    expected = ["{% static %}\n", 'some text src = "{% static \'address\' %}"']
    assert text_replacer.replace_src(lines) == expected

def test_replace_both(text_replacer):
    lines = ['some text href="address"', 'another text src="another_address"']
    expected = ["{% static %}\n", 
                'some text href = "{% static \'address\' %}"', 
                'another text src = "{% static \'another_address\' %}"']
    assert text_replacer.replace(lines) == expected

def test_no_replace_if_already_formatted(text_replacer):
    lines = ['some text href = "{% static \'address\' %}"']
    expected = ["{% static %}\n", 'some text href = "{% static \'address\' %}"']
    assert text_replacer.replace_href(lines) == expected

    lines = ['some text src = "{% static \'address\' %}"']
    expected = ["{% static %}\n", 'some text src = "{% static \'address\' %}"']
    assert text_replacer.replace_src(lines) == expected
