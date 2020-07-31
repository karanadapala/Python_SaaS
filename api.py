from flask import Flask
import sort
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    content = request.json
    return jsonify(
        sorted_list= sort.process_json(content)
    )
    

if __name__ == '__main__':
    app.run(debug=True)