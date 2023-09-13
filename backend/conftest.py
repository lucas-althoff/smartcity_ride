import pytest
from fastapi.testclient import TestClient
from backend.app import api
import os

os.environ["PROMETHEUS_MULTIPROC_DIR"] = os.getcwd()
os.environ["MODE"] = "teste"
os.environ["username"] = "usuario"
os.environ["senha"] = "senha"
os.environ["clientid"] = "123"
os.environ["clientsecret"] = "1j2k3l4"


@pytest.fixture
def cliente():
    cliente = TestClient(api)
    yield cliente
