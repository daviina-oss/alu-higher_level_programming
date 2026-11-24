# python-network_0

Bash scripts that use `curl` to talk to a web server.

Run a script with the URL as the first argument, for example:

```
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
```

| File | Description |
|------|-------------|
| 0-body_size.sh | Sends a request to the URL and prints the size of the body in bytes |
| 1-body.sh | Sends a GET request and prints the body only if the status code is 200 |
| 2-delete.sh | Sends a DELETE request and prints the body of the response |
| 3-methods.sh | Prints all the HTTP methods the server accepts for the URL |
| 4-header.sh | Sends a GET request with the header `X-HolbertonSchool-User-Id: 98` and prints the body |
| 5-post_params.sh | Sends a POST request with `email` and `subject` and prints the body |
