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

product_list=[
  {'id':1,'name':'Ноутбук','price':50000},
  {'id':2,'name':'Монитор', 'price':25000},
  {'id':3,'name':'Клавиатура','price':5000}
]

@app.route('/products')
def get_products():
  return render_template('products.html', products=product_list)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
  product=next((p for p in product_list if p['id']==product_id), None)
  return render_template('product_detail.html', product=product)

@app.route('/surprise')
def surprise():
    return render_template('surprise.html')

def method_name():
    pass
if __name__=='__main__':
  app.run(debug=True)

