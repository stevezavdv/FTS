from flask import Flask, render_template
from datetime import datetime

app=Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name="Гость"):
  current_hour=datetime.now().hour
  if current_hour>= 6 and current_hour<12:
    message="Доброе утро"
  elif 12<= current_hour <18:
    message="Добрый день"
  elif 18<=current_hour<=23:
    message="Добрый вечер"
  else:
    message="Доброй ночи"
  return render_template('index.html', name=name, houк=current_hour, msg=message)

test_list=[
  {'id':1,'name':'test1'},
  {'id':2,'name':'test2'},
  {'id':3,'name':'test3'}
]

@app.route('/tests')
def get_tests():
  return render_template('test_list.html', tests=test_list)

@app.route('/test/<int:test_id>')
def test_detail(test_id):
  test=next((t for t in test_list if t['id']==test_id), None)
  return render_template('test_detail.html', test=test)

@app.route('/surprise')
def surprise():
    return render_template('surprise.html')

def method_name():
    pass
if __name__=='__main__':
  app.run(debug=True)

