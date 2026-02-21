import os

from fastapi.testclient import TestClient

from app.main import create_app


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
            return {"choices": [{"message": {"content": "Provider summary"}}]}

    monkeypatch.setattr("app.main.OpenRouterClient", FakeClient)

    client = TestClient(create_app())
    response = client.post("/analyze", json={"feedback": ["app crashes often"]})

    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "openrouter"
    assert body["summary"] == "Provider summary"


def test_analyze_openrouter_mode_falls_back_to_mock_on_error(monkeypatch) -> None:
    monkeypatch.setenv("INSIGHT2SPEC_ANALYZE_MODE", "openrouter")
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)

    client = TestClient(create_app())
    response = client.post("/analyze", json={"feedback": ["pricing is confusing"]})

    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "mock"
    assert "Pricing Confusion" in body["themes"]
