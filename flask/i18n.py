#!/usr/bin/env python3

from flask import Flask, jsonify, flash


app = Flask(__name__)
app.secret_key = 'Rock'


@app.route('/')
def home():
    flash("Here we go!!!")
    return jsonify({"message": "We Live!"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
