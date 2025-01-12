from app import db

class Animal_record(db.Model):
    __tablename__ = 'animal_record'
    animal_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    species = db.Column(db.String(255), nullable = False)
    breed = db.Column(db.String(255), nullable = False)
    dob = db.Column(db.Date, nullable = False)   #date
    gender = db.Column(db.String(255), nullable = False) 
    date_added = db.Column(db.Date, nullable = False) #date
    disease_history = db.Column(db.String(255), nullable = False)
    treatement_history = db.Column(db.String(255), nullable = False)
    status = db.Column(db.String(255), nullable = False)
    remark = db.Column(db.String(255), nullable = False)
    
    

    def to_dict(self):
        return {
            "animal_id": self.animal_id,
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "dob":self.dob,
            "gender":self.gender,
            "date_added":self.date_added,
            "disease_history":self.disease_history,
            "treatement_history":self.treatement_history,
            "status":self.status,
            "remark":self.remark
        }