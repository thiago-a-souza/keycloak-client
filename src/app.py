""""Sample keycloak client"""
import logging
from flask import Flask
from flask_oidc import OpenIDConnect

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.config.update(dict(SECRET_KEY='my-sample-secret',
                       OIDC_CLIENT_SECRETS='client_secrets.json',
                       OIDC_ID_TOKEN_COOKIE_SECURE=False,
                       OIDC_REQUIRE_VERIFIED_EMAIL=False))

oidc = OpenIDConnect(app)


@app.route('/')
def index():
    if oidc.user_loggedin:
        return 'Welcome {}.<br><a href="/logout">Log out</a>'.format(oidc.user_getfield('email'))
    return 'Not logged in. <a href="/login">Log in</a>'


@app.route('/login')
@oidc.require_login
def login():
    return 'Welcome {}.<br><a href="/logout">Log out</a>'.format(oidc.user_getfield('email'))


@app.route('/logout')
def logout():
    oidc.logout()
    return 'Logged out. <a href="/">Return</a>'


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
