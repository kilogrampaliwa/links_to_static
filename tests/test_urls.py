import pytest
import urls

def test_urls_imports():
    assert hasattr(urls, 'confi_read')
    assert hasattr(urls, 'find_files')
    assert hasattr(urls, 'replacer')

def test_urls_constants():
    assert urls.CONFI == 'confi.txt'
    assert urls.RAWS == 'templates_raw'
    assert urls.NEWS == 'templates_new'
