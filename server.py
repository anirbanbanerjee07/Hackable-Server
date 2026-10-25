
from flask import Flask, request

app = Flask(__name__)

@app.route('/test')
def test():
    value = request.args.get('value')

    if not value:
        return 'Missing value', 400

    with open('test_data.txt', 'a', encoding='utf-8') as f:
        f.write(value + '\n')

    return 'Received', 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
