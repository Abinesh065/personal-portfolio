from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Ensure files exist
for file in ["names.txt", "counts.txt"]:
    if not os.path.exists(file):
        open(file, "w").close()

# Serve your homepage
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to save data
@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    name = data.get('name')
    count = data.get('count')

    if name:
        with open("names.txt", "a") as f:
            f.write(name + "\n")
    if count is not None:
        with open("counts.txt", "a") as f:
            f.write(str(count) + "\n")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
