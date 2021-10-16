from typing import cast
from unittest.mock import Mock

from _pytest.config import Config
import pytest
from pytest_mock import MockFixture

from astraszab_hypermodern_python import wikipedia


def pytest_configure(config: Config) -> None:
    config.addinivalue_line("markers", "e2e: mark as end-to-end test.")


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    mock = cast(Mock, mocker.patch("requests.get"))
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    mock = cast(
        Mock, mocker.patch("astraszab_hypermodern_python.wikipedia.random_page")
    )
    mock.return_value = wikipedia.Page(
        title="Lorem Ipsum", extract="Lorem ipsum dolor sit amet"
    )
    return mock
