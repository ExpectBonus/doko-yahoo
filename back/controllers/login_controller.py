from flask import request, jsonify,Flask
from flask.blueprints import Blueprint
from models.models import *
from db import db
import flask_login

app = Flask(
        __name__,
        template_folder='templates')

app.secret_key = b'ExpectBonus'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# loginカテゴリのエンドポイント定義
login_blueprint = Blueprint('user', __name__, url_prefix="/api/login")

@app.route('/logout', methods=['GET'])
def logout():
    ''' ログアウト '''
    flask_login.logout_user()
    return 'ログアウトしました'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/', methods=['GET'])
def index():
    ''' トップページ（ログイン不要） '''#html直打ちなんとかしたい
    return '''<h1>top page</h1><p><a href="/login">ログイン</a><p><a href="/member">メンバー</a><p><a href="/logout">ログアウト</a>'''

@app.route('/member', methods=['GET'])
@flask_login.login_required#ログイン必須化
def member():
    ''' 会員ページ（要ログイン） '''
    return '会員ページ'

@login_manager.unauthorized_handler
def unauthorized():
    return flask.redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' ログイン '''
    form = LoginForm(flask.request.form)
    # validationチェック
    if form.validate_on_submit():
        # DBからうまいことform.user_idとform.passwordを引っこ抜いてif form.user_id.data=="正しいid" and form.password.data=="正しいpassword"にしたい
        if form.user_id.data == '' and form.password.data == '':
            # ログインの実行
            user = User(form.user_id.data)
            flask_login.login_user(user)
            # ログインに成功したらmemberページへ
            return flask.redirect('/member')
        else:
            pass

    # GET時やログイン
    return flask.render_template(
            'login.html',
            form=form)





