
# http://flask.pocoo.org/docs/0.11/patterns/fileuploads/
import os
import subprocess
import time
import datetime
import uuid
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

from simple_print_server.database import db_session
from simple_print_server.models import PrintedFile
from simple_print_server import app


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def make_today_folder():
    today_str = datetime.datetime.today().strftime('%Y%m%d') # Ex) '20161114'
    full_today_path = os.path.join(app.config['BASE_UPLOAD_FOLDER'], today_str)

    if not os.path.exists(full_today_path):
        os.mkdir(full_today_path)
        app.config['TODAY_UPLOAD_FOLDER'] = full_today_path


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(request.url)

    file_to_upload = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file_to_upload.filename == '':
        flash('No selected file', 'danger')
    elif file_to_upload and allowed_file(file_to_upload.filename):
        # filename = secure_filename(file_to_upload.filename)
        filename = str(uuid.uuid4())
        f = PrintedFile(file_to_upload.filename, filename)

        make_today_folder()
        fullpath = os.path.join(app.config['TODAY_UPLOAD_FOLDER'], filename)
        file_to_upload.save(fullpath)

        db_session.add(f)
        db_session.commit()

        # subprocess.Popen(["lpr", fullpath])
        subprocess.Popen([app.config['PRINT_COMMAND'], fullpath])
        flash('Printing!', 'success')
    elif not allowed_file(file_to_upload.filename):
        flash('Bad filetype', 'danger')
    else:
        flash('Unknown error!', 'danger')

    return redirect(request.url)


@app.route('/', methods=['GET'])
def main_page():
    recent_files = list(PrintedFile.query.order_by(PrintedFile.id.desc()).limit(5))
    return render_template('index.html', recent=recent_files)
