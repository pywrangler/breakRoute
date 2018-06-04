from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/<stryng>', methods=['GET'])
def get_tasks(stryng):
    return jsonify(stryng+"is not available")

if __name__ == '__main__':
    app.run(debug=True)
