import os

from fastapi.testclient import TestClient

from app.main import create_app
from app.openrouter_client import OpenRouterTimeoutError


def test_analyze_defaults_to_mock_mode() -> None:
    os.environ.pop("INSIGHT2SPEC_ANALYZE_MODE", None)
    client = TestClient(create_app())

    response = client.post("/analyze", json={"feedback": ["onboarding is confusing"]})

    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "mock"
    assert "Onboarding Friction" in body["themes"]


def test_analyze_openrouter_mode_uses_provider_when_available(monkeypatch) -> None:
    monkeypatch.setenv("INSIGHT2SPEC_ANALYZE_MODE", "openrouter")
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")

    class FakeClient:
        @classmethod
        def from_env(cls):
            return cls()

        def complete_json(self, **kwargs):
            return {
                "choices": [
                    {
                        "message": {
                            "content": (
                                '{"summary":"Provider summary",'
                                '"themes":["Reliability Issues"],'
                                '"opportunities":["Improve incident visibility"],'
                                '"experiments":["Test proactive error nudges"],'
                                '"prd_outline":["Problem","Solution"]}'
                            )
                        }
                    }
                ]
            }

    monkeypatch.setattr("app.main.OpenRouterClient", FakeClient)

    client = TestClient(create_app())
    response = client.post("/analyze", json={"feedback": ["app crashes often"]})

    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "openrouter"
    assert body["summary"] == "Provider summary"
    assert body["themes"] == ["Reliability Issues"]
    assert body["opportunities"] == ["Improve incident visibility"]
    assert body["experiments"] == ["Test proactive error nudges"]


def test_analyze_openrouter_mode_returns_explicit_config_error(monkeypatch) -> None:
    monkeypatch.setenv("INSIGHT2SPEC_ANALYZE_MODE", "openrouter")
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)

    client = TestClient(create_app())
    response = client.post("/analyze", json={"feedback": ["pricing is confusing"]})

    assert response.status_code == 500
    assert response.json()["detail"]["code"] == "openrouter_config_error"


def test_analyze_openrouter_mode_returns_explicit_timeout_error(monkeypatch) -> None:
    monkeypatch.setenv("INSIGHT2SPEC_ANALYZE_MODE", "openrouter")
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")

    class TimeoutClient:
        @classmethod
        def from_env(cls):
            return cls()

        def complete_json(self, **kwargs):
            raise OpenRouterTimeoutError("timed out")

    monkeypatch.setattr("app.main.OpenRouterClient", TimeoutClient)

    client = TestClient(create_app())
    response = client.post("/analyze", json={"feedback": ["app crashes often"]})

    assert response.status_code == 504
    assert response.json()["detail"]["code"] == "openrouter_timeout"
