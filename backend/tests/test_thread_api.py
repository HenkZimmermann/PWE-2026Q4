import pytest
from src.sections.thread import thread_routes

def test_create_thread_requires_title(client, monkeypatch):
    def unexpected_create(request):
        pytest.fail("An invalid request must not call the thread service")

    monkeypatch.setattr(thread_routes, "create_thread", unexpected_create)

    response = client.post(
        "/threads/create",
        json={"message": "Testbeitrag", "user_id": 7, "group_id": 2},
    )

    assert response.status_code == 422
    assert [error["loc"] for error in response.json()["detail"]] == [["body", "title"]]

def test_search_requires_search_term(client, monkeypatch):
    def unexpected_search(*args):
        pytest.fail("A request without a search term must not call the search service")

    monkeypatch.setattr(thread_routes, "search_threads", unexpected_search)

    response = client.get("/threads/search", params={"limit": 2})

    assert response.status_code == 422
    assert [error["loc"] for error in response.json()["detail"]] == [
        ["query", "search_term"]
    ]

def test_feed_returns_json(client, monkeypatch):
    def load_feed(limit, group_id):
        assert limit == 3
        assert group_id == 7
        return [{"id": 1}, {"id": 2}, {"id": 3}]

    monkeypatch.setattr(thread_routes, "get_thread_feed", load_feed)

    response = client.get("/threads/feed", params={"limit": 2, "group_id": 7})

    assert response.status_code == 200
    assert response.json() == {"threads": [{"id": 1}, {"id": 2}], "hasMore": True}
