# Author: Nathaniel Price

import requests
import json

URL = "http://127.0.0.1:6002"


def test_fernet():
    print("=== Test 1: Password Strength ===")
    payload = {"password": "mySecretPassword123"}

    response = requests.get(URL, json=payload)
    response_json = response.json()

    print(f"Match: {response_json}")
    return


if __name__ == "__main__":
    print("\nStarting Password Strength Microservice Tests")
    print("---------------------------------------")

    test_fernet()

    print("\nAll tests complete.")
