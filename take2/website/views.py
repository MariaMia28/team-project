from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) #defining a blueprint


@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_data = request.form.get('note')
        # is_task = request.form.get('is_task') == 'on'

        if len(note_data) < 1:
            flash('Note is too short', category = 'error')
        else:
            new_note = Note(data = note_data, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category = 'success')

    notes = Note.query.filter_by(user_id = current_user.id).all()
    return render_template("home.html", user = current_user)

# @views.route('/complete-task', methods=['POST'])
# def complete_task():
#     task_data = json.loads(request.data)
#     note_id = task_data['noteId']
#     is_completed = task_data['isCompleted']
#     note = Note.query.get(note_id)
#     if note and note.user_id == current_user.id:
#         note.is_completed = is_completed
#         db.session.commit()
#     return jsonify({})


@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})