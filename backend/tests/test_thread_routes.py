import pytest
from fastapi import HTTPException
from src.sections.thread import thread_routes

@pytest.mark.parametrize(("threads", "has_more"), [([{"id": 1}, {"id": 2}], False), ([{"id": 1}, {"id": 2}, {"id": 3}], True)])
def test_feed_limits_results_and_reports_more_threads(monkeypatch, threads, has_more):
    def load_feed(limit, group_id):
        assert limit == 3
        assert group_id == 7
        return threads

    monkeypatch.setattr(thread_routes, "get_thread_feed", load_feed)

    assert thread_routes.get_thread_feed_route(limit=2, group_id=7) == {
        "threads": [{"id": 1}, {"id": 2}],
        "hasMore": has_more
    }

def test_search_rejects_whitespace_without_calling_service(monkeypatch):
    def unexpected_search(*args):
        pytest.fail("A blank search must not call the search service")

    monkeypatch.setattr(thread_routes, "search_threads", unexpected_search)

    with pytest.raises(HTTPException) as error:
        thread_routes.search_threads_route(search_term="   ", limit=2)

    assert error.value.status_code == 400

@pytest.mark.parametrize(("result", "status_code"), [(None, 404), (False, 500)])
def test_thread_detail_reports_missing_thread_or_service_error(monkeypatch, result, status_code):
    monkeypatch.setattr(thread_routes, "get_thread_by_id", lambda thread_id: result)

    with pytest.raises(HTTPException) as error:
        thread_routes.get_thread_by_id_route(thread_id=7)

    assert error.value.status_code == status_code
