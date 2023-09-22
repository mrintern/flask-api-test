from flask import Flask, request, jsonify

app = Flask(__name__)

# hello endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!", random=str(type(123.123)))

"""
expects a POST request containing json that looks like this:
{"numbers": [5, 3, 2, 10]}
"""
@app.route('/api/add', methods=['POST'])
def add_numbers():
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
