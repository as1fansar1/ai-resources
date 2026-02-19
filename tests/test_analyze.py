from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_analyze_returns_deterministic_mock_contract() -> None:
    response = client.post(
        "/analyze",
        json={
            "feedback": [
                "The signup setup is confusing for new users.",
                "Slack integration is missing and export API is limited.",
            ],
            "context": "B2B SaaS collaboration tool",
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert body["mode"] == "mock"
    assert body["themes"] == ["Onboarding Friction", "Missing Integrations"]
    assert body["summary"].startswith("Analyzed 2 feedback item(s).")
    assert len(body["opportunities"]) >= 1
    assert len(body["prd_outline"]) == 4
    assert len(body["experiments"]) == 2


def test_analyze_requires_at_least_one_feedback_item() -> None:
    response = client.post("/analyze", json={"feedback": []})

    assert response.status_code == 422
