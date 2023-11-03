from flask import Blueprint, current_app, render_template, request, url_for, flash, redirect
from app.database import db, db_init
from app.database import operations as db_oper
from flask_login import login_required, current_user
from flask_restful import Resource, Api  
from os import path


BASE_DIR = path.dirname(path.abspath(__file__))
main = Blueprint('main', __name__)


''' Exhibit all accesses in the room system, need to be logged
    All accesses are stored in a local database
'''
@main.before_app_first_request
def create_tables():
    if not path.exists(current_app.config['SQLALCHEMY_DATABASE_URI']):
        db.app = main
        db.drop_all()
        db.create_all()
        db_init.create_admin_user()
        db_init.create_tree_locks()
        db_init.create_tree_lock_users()
        db_init.set_tree_permissions()
        db_init.create_tree_access()

''' List last access to locks.
'''
@main.route('/')
#@login_required
def index():
    rows = db_oper.get_entry_table()
    #print(rows[0].as_row)
    return render_template('index.html', current_user=current_user, rows=rows) 

''' A page used to add users
    It can be used a enrollment_id to add user to room_number
    After the request for adding, a message is displayed
    indicating success or error with its 'error type'
    'error type' can be one of {WrongUser, WrongRoom, AlreadyAdded, Unknown}
'''
@main.route('/users', methods=('GET', 'POST'))
#@login_required
def users():
    if request.method == 'POST':
        user = None
        room = None
        if grant_permission(user, room) == True:
            msg = 'Usuário '+user+' adicionado à sala '+room+'.'
            flash(msg, 'alert_ok')
    permissions = db_oper.get_permission_table()
    return render_template('users.html', permissions=permissions) 

def grant_permission(user, room):
    try:
        user = request.form['user']
        room = request.form['room']
    except:   
        if not user or not room:
            if not room:
                flash('Ientificador da sala em branco!', 'alert_fail')
            if not user:
                flash('Identificador de usuário em branco!', 'alert_fail')
            return False
    # Case doing POST of invalid data (inexistent lock)
    if not db_oper.is_valid_user(db, room, 'lock'):
        flash('Sala invália, por favor, **cadastre-a aqui**.', 'alert_fail')
        return False

    if not db_oper.is_valid_user(db, user, 'user') or \
       not db_oper.is_valid_user(db, user, 'lock_user'):
        flash('Usuário "'+user+'" inválido.', 'alert_fail')
        return False
    if db_oper.check_permission(room, user):
        msg = 'Usuário "'+user+'" já possui a permissão para a sala '+room+'.'
        flash(msg, 'alert_warn')
        return None # case have the permission
    elif db_oper.set_permission(room, user):
        return True
    else:
        flash('Erro ao adicionar usuário.', 'alert_fail') # motivo adverso
        return False


''' Get list of rooms and exhibit them in a table
'''
@main.route('/rooms', methods=('GET', 'POST'))
#@login_required
def rooms():
    if request.method == 'POST':
        room = None
        name = None
        if add_room(room, name):
            msg = 'Sala número "'+room+'" adicionada ao sistema.'
            flash(msg, 'alert_ok')
    
    rooms = db_oper.get_all_table_users(db, 'lock')
    return render_template('rooms.html', rooms=rooms)

def add_room(room, name):
    try:
        room = request.form['room'] # username
        #password = request.form['password']
        name = request.form['name']
        
        
    except:
        if not name or not room:
            if not room:
                flash('Por favor, forneça um ID de sala válido.', 'alert_fail')
            if not name:
                flash('Por favor, forneça um nome para a sala.', 'alert_fail')
            return False
    if db_oper.is_valid_user(db, room, 'lock'):
        flash('Sala "'+room+'" já existe.', 'alert_warn')
        return None
    elif db_oper.insert_user(db, 'lock', atributes={'username': room, 
                                                    'password': 'password', 
                                                    'name': name, 
                                                    'role': 'lock'}):
        return True
    else:
        flash('Erro ao adicionar sala.', 'alert_fail')
        return False

@main.route('/help')
def help():
    return render_template('help.html')

