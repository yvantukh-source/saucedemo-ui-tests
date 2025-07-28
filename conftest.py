import pytest
import logging

def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

@pytest.fixture(scope="session")
def logger():
    return logging.getLogger("swag-tests")
