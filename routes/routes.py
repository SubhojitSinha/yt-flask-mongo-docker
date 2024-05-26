from flask import Blueprint
from controllers.test import hello_world,init_database,get_all,get_all_3,update_name
bp_routes = Blueprint('blueprint', __name__)

bp_routes.route('/', methods=['GET'])(hello_world)
bp_routes.route('/init-database', methods=['GET'])(init_database)
bp_routes.route('/get-all', methods=['GET'])(get_all)
bp_routes.route('/get-all-3', methods=['GET'])(get_all_3)
bp_routes.route('/update-name/<id>/<name>', methods=['GET'])(update_name)