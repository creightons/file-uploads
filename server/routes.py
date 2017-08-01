import os
from flask import render_template, request, redirect, flash, url_for, send_from_directory
from models import File
from database import db
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
                existing_file = File.query.filter(File.filename == filename).first()

                if existing_file != None:
                    flash('File already exists')
                    return redirect(request.url)

                else:
                    new_file_record = File(filename)
                    db.session.add(new_file_record)
                    db.session.commit()

                    return redirect(url_for('uploaded_file', filename=filename))
            else:
                flash('failed to upload file')
                

        file_records = File.query.all()

        context = [{ 'filename': record.filename, 'uploaded': record.uploaded_date, 'link': url_for('uploaded_file', filename=record.filename) }
                for record in file_records ]

        return render_template('index.html', context=context)

    @app.route('/uploads/<filename>', methods = ['GET', 'POST'])
    def uploaded_file(filename):
        dir_path = get_path(app, '')
        return send_from_directory(dir_path, filename)

    @app.route('/upload-list', methods = ['GET'])
    def upload_list():
        filelist = os.listdir(get_path(app, ''))

        display_list = [filename for filename in filelist if filename != '.gitignore']

        return render_template('upload-list.html', files = display_list)
