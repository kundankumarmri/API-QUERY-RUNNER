import requests
import time

API_URL = "https://example.com/icoralmssql/1/customDataQuery/customQuery"

TOKEN = "YOUR_API_TOKEN"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

TENANT_ID = 1


def read_queries(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def execute_queries(queries):
    for i, query in enumerate(queries, start=1):

        payload = {
            "query": query,
            "tenant": TENANT_ID
        }

        print(f"\nRunning Query {i}/{len(queries)}")
        print(query)

        try:
            response = requests.post(API_URL, json=payload, headers=HEADERS)

            if response.status_code == 200:
                print("✅ Success")
                print(response.json())
            else:
                print("❌ Failed:", response.status_code)
                print(response.text)

        except Exception as e:
            print("Error:", e)

        time.sleep(1)


if __name__ == "__main__":
    queries = read_queries("queries.txt")
    print(f"Total Queries Found: {len(queries)}")
    execute_queries(queries)