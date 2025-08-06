from flask import Flask, request, jsonify

app = Flask(__name__)

# Store data in memory
stored_data = {}

@app.route('/set')
def set_params():
    a = request.args.get('a')
    b = request.args.get('b')
    stored_data['a'] = a
    stored_data['b'] = b
    return jsonify({"message": "Params saved!", "a": a, "b": b})

@app.route('/get')
def get_params():
    return jsonify(stored_data)

if __name__ == '__main__':
    app.run(debug=True)
