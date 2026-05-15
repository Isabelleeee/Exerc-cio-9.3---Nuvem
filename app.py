from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World - Deploy via GitHub Web'

if __name__ == '__main__':
    # O Azure usa a porta 8080 ou a definida pelo sistema
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
