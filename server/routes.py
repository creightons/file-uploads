import os
from flask import render_template, request, redirect, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = frozenset(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_path(app, filename):
    directory_path = os.path.abspath(app.config['UPLOAD_FOLDER'])
    filepath = os.path.join(directory_path, filename)
    return filepath

def apply_routes(app):

    @app.route('/', methods = ['GET', 'POST'])
    def index():
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)

            file = request.files['file']

            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = get_path(app, filename)

                file.save(filepath)

                return redirect(url_for('uploaded_file', filename=filename))
            else:
                flash('failed to upload file')
                

        return render_template('index.html')

    @app.route('/uploads/<filename>', methods = ['GET', 'POST'])
    def uploaded_file(filename):
        dir_path = get_path(app, '')
        return send_from_directory(dir_path, filename)
