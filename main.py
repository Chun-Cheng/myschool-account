from flask import Flask, request, redirect, render_template, url_for, flash, jsonify


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xd9\xb9\x07\xad\x9d[\xe0e\xd2\x84\x9eU\xd8s\xe0\x15W\xcf\xf2n\x93\x01\xdc\xe4'  # 要換
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=180)

@app.route('/')
def index():
    return 'hi~'

if __name__ == "__main__":
    app.run()
