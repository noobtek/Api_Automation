from requests import request
from json import loads
import pytest

headers = "code, expected_branch"
data = [
    ("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
        ("SBIN0040014", "GANDHI BAZZAR"),
        ("ICIC0000002", "BANGALORE - M G ROAD")
]

@pytest.mark.parametrize(headers, data)
def test_bank(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    print(url)
    response = request("GET", url)
    response_text = response.text
    print(response_text)
    d = loads(response_text)
    # Parse the Response
    actual_branch = d['BRANCH']
    assert actual_branch == expected_branch


