import pytest

@pytest.fixture():
def set_up():
    print('start test')

    yield
    
    print('finish test')

