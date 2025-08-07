from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)
stored_data = {}

# HTML template
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Data App</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .box {
            background: white;
            padding: 20px;
            border-radius: 12px;
            max-width: 400px;
            margin: auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input, button {
            width: 100%%;
            padding: 10px;
            margin-top: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>Set Parameters</h2>
        <form method="post" action="/set">
            <input type="text" name="a" placeholder="Enter value A" required>
            <input type="text" name="b" placeholder="Enter value B" required>
            <button type="submit">Save</button>
        </form>

        <h3>Current Data</h3>
        <form method="get" action="/get">
            <button type="submit">View Stored Data</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/set', methods=['POST'])  # ✅ changed to POST
def set_params():
    a = request.form.get('a')  # ✅ read from form
    b = request.form.get('b')
    stored_data['a'] = a
    stored_data['b'] = b
    return jsonify({"message": "Params saved!", "a": a, "b": b})

@app.route('/get', methods=['GET'])
def get_params():
    return jsonify(stored_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    app.run(host="0.0.0.0", port=port)
