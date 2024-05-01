import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


if not firebase_admin._apps:
	cred = credentials.Certificate("./firebase_utils/rhythmx-test-firebase-adminsdk-imtx4-c1a19edf4b.json")
	default_app = firebase_admin.initialize_app(cred, {
		'databaseURL': 'https://rhythmx-test-default-rtdb.firebaseio.com/'
		})


ref = db.reference("/patient-data")

def write_to_fb(obj):
    ref.push().set(obj)
    
def get_all_patients():
	ref = db.reference("/patient-data")
	patient_records = ref.get()
	return patient_records