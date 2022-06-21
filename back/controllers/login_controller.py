from flask import request, jsonify,Flask
from flask.blueprints import Blueprint
from models.models import *
from db import db
import flask_login
from werkzeug.security import generate_password_hash, check_password_hash

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
    ''' トップページ（ログイン不要） '''
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
        #usernameに登録された名前が入力された場合
        if User.query.filter_by(username=form.user_id.data).one_or_none():
        #Userからusernameとpasswordを引っこ抜いてif form.user_id.data=="username" and form.password.data=="password"にしたい
        #Userにpasswordを登録して直でpassword=passwordとするのかハッシュ化するのか、みてくれだけならusernameあったら通しちゃっても…
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





