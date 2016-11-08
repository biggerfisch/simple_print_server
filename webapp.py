
# http://flask.pocoo.org/docs/0.11/patterns/fileuploads/
import os
import subprocess
import time
import uuid
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024 # 128 MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file_to_upload = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file_to_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            # filename = secure_filename(file_to_upload.filename)
            filename = uuid.uuid4()
            file_to_upload.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            subprocess.Popen(["lpr", filename])

            return '''
            Thanks! Filename: {}
            '''.format(filename)

    return render_template('index.html')
