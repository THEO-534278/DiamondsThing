
from flask import Flask, render_template, request, jsonify
from songsearch import *


app = Flask(__name__)



@app.route('/')
def main():
    return render_template('main.html')

@app.route('/process', methods=['POST'])

def process():
    data = request.get_json()
    print(data)
    input = data['input']


    output = song(input)

    print('JSONIFY: ', jsonify(output))
    return jsonify(output)

    

if __name__ == '__main__':
    app.run(debug=True)


