import os
import pytest


@pytest.fixture(scope="module")
def data_path() -> str:
    return os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "../data/test_setup.yaml"
    )
