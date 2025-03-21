import requests

BASE_URL = "https://hackdiversity.xyz/api"
SESSION_ENDPOINT = "/start-session"
ROUTES_ENDPOINT = "/navigation/routes"
SORTED_ROUTES_ENDPOINT = "/navigation/sorted_routes"
TEST_MOCK_ENDPOINT = "/test/mockRoutes"
TEST_SUBMIT_ENDPOINT = "/test/submit-sorted-routes"


def start_session(first_name, last_name):
    response = requests.post(
        f"{BASE_URL} {SESSION_ENDPOINT}",
        json={"firstName": first_name, "lastName": last_name}
    )
    response.raise_for_status()
    return response.json().get("session_id")
    # expected return of "session_id": "uuid string"


def fetch_routes(session_id, endpoint):
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    response.raise_for_status()
    return response.json()


def filter_accessible_routes(routes):
    return [route for route in routes if route.get("accessible")]


def sort_routes_by_distance(routes):
    for i in range(len(routes)):
        for j in range(0, len(routes) - i - 1):
            if routes[j]["distance"] > routes[j + 1]["distance"]:
                routes[j], routes[j + 1] = routes[j + 1], routes[j]
    return routes


def submit_routes(session_id, endpoint, sorted_routes):
    headers = {"Authorization": f"Bearer {session_id}"}
    response = requests.post(
        f"{BASE_URL}{endpoint}", json=sorted_routes, headers=headers)
    response.raise_for_status()
    return response.json()


def main():

    session_id = start_session("Christopher", "Alphonse")
    routes = fetch_routes(session_id, ROUTES_ENDPOINT)
    accessible_routes = filter_accessible_routes(routes)
    sorted_routes = sort_routes_by_distance(accessible_routes)
    result = submit_routes(session_id, SORTED_ROUTES_ENDPOINT, sorted_routes)
    print("Submission Result:", result)


if __name__ == "__main__":
    main()
