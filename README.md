# flask-api-test
Just a simple repo I made to test out making an api using flask.

## API Usage

### Endpoint: /api/add (POST)

To use this endpoint to add some numbers together, make a POST request to the `/api/add` endpoint with a JSON payload containing a list of numbers. The API will add all the numbers together and return the result.

example using curl: ```curl -X POST -H "Content-Type: application/json" -d '{"numbers": [5, 2343, 2, 10]}' http://127.0.0.1:5000/api/add```
