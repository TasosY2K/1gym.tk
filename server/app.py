from flask import Flask, request, jsonify, render_template, redirect
from db import get_all_confessions, insert_confession

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def create_post():
    if request.method == "POST":
        insert_confession(request.form['username'], request.form['confession'])

        return jsonify({"message": "Created sucessfully"})

@app.route('/posts', methods=['GET'])
def list_posts():
    confessions = get_all_confessions()
    return jsonify(confessions)

app.run()