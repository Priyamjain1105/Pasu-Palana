from flask import render_template,request,jsonify,redirect, url_for
from model import Animal_record
# sno  name position salary

def register_routes(app,db):
    @app.route('/')
    def index():
        return render_template('index2.html')
    
    @app.route('/view')
    def view():
        return render_template('home.html')

    
    @app.route('/data',methods = ['GET','POST'] )
    def data():
        if request.method == 'GET':
            practise1 = Animal_record.query.all()
           #  result = {"data": [item.to_dict() for item in practise1]}  # Serialize 
            result = [item.to_dict() for item in practise1]
            print(result)
            jsonify(result)
            #return jsonify(result)
            #return render_template('dar.html', animal_data=result)
            return render_template('new.html',animals = result)
        
    @app.route('/search',methods = ['GET','POST'] )
    def search():
        if request.method == 'GET':
            practise1 = Animal_record.query.all()
           #  result = {"data": [item.to_dict() for item in practise1]}  # Serialize 
            result = [item.to_dict() for item in practise1]
            print(result)
            jsonify(result)
            #return jsonify(result)
            #return render_template('dar.html', animal_data=result)
            return render_template('search.html',animals = result)

    @app.route('/submit-animal-record',methods = ['GET','POST'])
    def form():
        if request.method == 'POST':
            name = request.form.get('name')
            species = request.form.get('species')
            breed = request.form.get('breed')
            dob = request.form.get('dob')
            gender = request.form.get('gender')
            date_added = request.form.get('date_added')
            disease_history = request.form.get('disease_history')
            treatement_history = request.form.get('treatment_history')
            status = request.form.get('status')
            remark = request.form.get('remark')
           
            details = Animal_record(name = name, species = species, breed = breed, dob = dob, gender = gender, date_added = date_added, disease_history = disease_history,
                                 treatement_history = treatement_history, status = status, remark = remark)
            db.session.add(details)
            db.session.commit()
            print("Data submited")
            
            
            return redirect(url_for('data'))
           
           