#!/usr/bin/env python3
"""Practicing how to save file attachments to database"""

from flask import Flask, flash, request, redirect, url_for
from attachment import Attachment
import os
from werkzeug.utils import secure_filename

projectDirectory = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(projectDirectory, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "kdkd"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            attachment = Attachment(name=filename)
            attachment.save()
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/download/<string:name>', methods=['GET'])
def download_file(name):
    return f'''
    <!doctype html>
    <h1>File {name} Uploaded Successfully</h1>
    '''


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
