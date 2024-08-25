from flask import Flask, request, jsonify
from collections import OrderedDict

app = Flask(__name__)

def segregate_data(input_array):
    numbers = [str(item) for item in input_array if isinstance(item, (int, float))]
    alphabets = [str(item) for item in input_array if isinstance(item, str) and item.isalpha()]
    highest_lowercase = max([item for item in alphabets if item.islower()], default="")
    return numbers, alphabets, highest_lowercase

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()

    # Example user data
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    input_array = data.get('input', [])
    numbers, alphabets, highest_lowercase = segregate_data(input_array)

    # Constructing the response using OrderedDict to maintain key order
    response = OrderedDict([
        ("is_success", True),
        ("user_id", user_id),
        ("email", email),
        ("roll_number", roll_number),
        ("numbers", numbers),
        ("alphabets", alphabets),
        ("highest_lowercase_alphabet", [highest_lowercase] if highest_lowercase else [])
    ])

    return jsonify(response), 200

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
