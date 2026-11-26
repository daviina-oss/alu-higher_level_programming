# python-network_1

Making HTTP requests in Python, first with `urllib` and then with `requests`.

| File | Description |
|------|-------------|
| 0-hbtn_status.py | Fetches `https://alu-intranet.hbtn.io/status` with `urllib` and shows the body |
| 1-hbtn_header.py | Shows the `X-Request-Id` header of the response from a URL (`urllib`) |
| 2-post_email.py | Sends a POST request with an email and shows the body (`urllib`) |
| 3-error_code.py | Shows the body of the response, or `Error code: <status>` on an HTTP error (`urllib`) |
| 4-hbtn_status.py | Fetches `https://alu-intranet.hbtn.io/status` with `requests` and shows the body |
| 5-hbtn_header.py | Shows the `X-Request-Id` header of the response from a URL (`requests`) |
| 6-post_email.py | Sends a POST request with an email and shows the body (`requests`) |
| 7-error_code.py | Shows the body, or `Error code: <status>` if the status is 400 or more (`requests`) |
| 8-json_api.py | Sends a letter to the search API and shows the user found (`requests`) |
| 10-my_github.py | Shows the GitHub id of a user, with Basic Authentication (`requests`) |

The `requests` scripts need the package: `pip install requests`.

For `10-my_github.py` use a personal access token as the password:

```
./10-my_github.py <username> <personal access token>
```
