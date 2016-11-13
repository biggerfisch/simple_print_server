
# http://flask.pocoo.org/docs/0.11/patterns/fileuploads/
import os
import subprocess
import time
import uuid
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

from simple_print_server.database import db_session
from simple_print_server.models import PrintedFile
from simple_print_server import app


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file_to_upload = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file_to_upload.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file_to_upload and allowed_file(file_to_upload.filename):
            # filename = secure_filename(file_to_upload.filename)
            filename = str(uuid.uuid4())
            f = PrintedFile(file_to_upload.filename, filename)
            fullpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file_to_upload.save(fullpath)

            db_session.add(f)
            db_session.commit()

            # subprocess.Popen(["lpr", fullpath])
            subprocess.Popen([app.config['PRINT_COMMAND'], fullpath])
            flash('Printing!', 'success')
            return redirect(request.url)
        else:
            flash('Bad file or something', 'danger')
            return redirect(request.url)
    else:
        recent_files = list(PrintedFile.query.order_by(PrintedFile.id.desc()).limit(5))
        return render_template('index.html', recent=recent_files)
