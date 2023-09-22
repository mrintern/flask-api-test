from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    """
    Returns:
    JSON response that looks like this:
    {
        "message": "Hello, World!",
        "random": "<class 'float'>"
    }
    """
    return jsonify(message="Hello, World!", random=str(type(123.123)))


@app.route('/api/add', methods=['POST'])
def add_numbers():
    """
    Add numbers provided in a JSON list.

    Expects a JSON payload that looks like this:
    {
        "numbers": [num1, num2, ...]
    }

    Returns a JSON response with the result of adding all the numbers together.

    Example:
    - Input: {"numbers": [5, 3, 2, 10]}
    - Output: {"result": 20}

    If the input is invalid or contains fewer than two numbers, it returns an error response.

    Returns:
    - JSON response with the result or error message.
    """
    data = request.get_json()

    if "numbers" in data and isinstance(data['numbers'], list):
        
        numbers = data['numbers']

        if len(numbers) < 2:
            return jsonify({'error': 'At least two numbers are required to perform addition.'}), 400
        
        result = sum(numbers)
        
        return jsonify({'result': result})

    else:
        return jsonify({'error': 'Invalid input. Please provide a list of numbers.'}), 400




if __name__ == '__main__':
    app.run(debug=True)
