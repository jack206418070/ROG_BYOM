from flask import Flask, render_template
import os

app = Flask(
  __name__,
  static_folder='public',
  static_url_path='/'
)

@app.route('/')
def index():
  return render_template('BYOA.html')

if __name__ == "__main__":
 app.run()