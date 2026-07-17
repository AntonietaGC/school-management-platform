from app import create_app


def test_home_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Colegio Biling" in response.data


def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["status"] == "healthy"
    assert payload["application"] == "school-management-platform"
    assert payload["version"] == "1.0.0"
