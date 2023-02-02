from flask import Flask, render_template, url_for, request, flash, session, redirect
import os
from werkzeug.utils import secure_filename
import sqlite3
from flask_sqlalchemy import SQLAlchemy
key = os.urandom(12).hex()
import datetime
from send_mail_2 import *
from model import *

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG'])
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = '23e200204cd2174c275875a2'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///usr_feedback.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


#Create a new table
class Usr_feedback(db.Model):

    name = db.Column(db.String(250), unique=False, nullable=True)
    email = db.Column(db.VARCHAR(250), nullable=True, unique=False, primary_key=True)
    Feedback = db.Column(db.String(250), nullable=True, unique=False)
    cur_date = db.Column(db.DateTime(100))
 
db.create_all()

#homepage
@app.route('/')
def index():
    return render_template('index.html')

#detect page
@app.route('/detect', methods=['GET', 'POST'])
def detect():
    
    if request.method == 'GET':
        return render_template('detect.html')
    else:
        img_name = request.form.get('user_img')
        name_of_plant = request.form.get('plant_name')
        # Storing an image in uploads folder
        file = request.files['user_img']
        filename = secure_filename(file.filename)
        file_ext = filename.split('.')[1]
        #print(file_ext)
        img_path = '/static/uploads/' + filename
        my_prediction = []
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        try:
            my_prediction = matrix(file, name_of_plant).split('\n') 
        except:
            print("could not predict.")
        #get_my_path('static/uploads/potato_late_blight_2.jpg')
        temp_l = len(my_prediction)
        d = str(dis_percent())
        return render_template('result.html', final_res = my_prediction[:temp_l-1:1], plant_img = img_path, dis_name=get_name(), plant=name_of_plant, d_percent=d[:3:])
           
        

#feedback page
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'GET':
        return render_template('feedback.html')
    else:
        resp = request.form.get('feedback')
        user_name = request.form.get('user-name')
        email = request.form.get('user_email')
        cur_today = datetime.datetime.now()
        new_feedback = Usr_feedback(name=user_name, email=email, Feedback=resp, cur_date=cur_today)
        try:
            send_email(email)
            print(f'Email sent to {email}.')
        except:
            print('Could not send an email')
        db.session.add(new_feedback)
        db.session.commit()
        return ('', 204)



@app.route('/faq')
def faq():
    return render_template('faq.html')

    
#webpage to view the database
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        #Basic authentication
        admin_name = request.form.get('usr_name')
        admin_password = request.form.get('usr_pass')
        if (admin_name.lower() == 'chandu' and admin_password == 'Chandu@vodaphone') or (admin_name.lower() == 'kausthub' and admin_password == 'Pichaino1') or (admin_name.lower() == 'abhishek' and admin_password == 'Abhi8431126009') or (admin_name.lower() == 'suraj' and admin_password == 'Suraj@vodaphone') or (admin_name.lower() == 'aniketh' and admin_password == 'Aniketh@vodaphone'):
            con = sqlite3.connect("finale.db")
            con.row_factory = sqlite3.Row
        
            cur = con.cursor()
            cur.execute("select * from usr_feedback")
        
            rows = cur.fetchall(); 
            return render_template("admin.html",rows = rows)
        else:
            return "Wrong username or password"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

