import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

creds =  {
    "type": "service_account",
  "project_id": "rhythmx-test",
  "private_key_id": "c1a19edf4b2c125bda4d7cb532edfc9df303c2b6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCqukv1FWA+tEnA\njYxtYQCH4SBvENbrXAih1MY0pZgrFWfReoDpbtRSgPWsyTnK5d+erz0yhLHxUxEf\nSCwqbteOBCu37/TSCKbWPx/2PsZqZkZTUfPruEf1bKQPPmVQ9u2890K6dyQjlpMo\nvxqwNGHlscgeDj7RBEtQaqHjMipQGaJS4Wtoh3ktsTX6qLsIYbU35tZUN+YSNsVc\nsjJzSp5NtNOkBev26+2DvEmOkIuvKcR6J7ZWiTwCtJlrLv4/BS25VOXssU+6pmGf\nNvEJe9J6QpS+f2ENMfN6RcCbInk6zusyRjboVQrJWZHVXsUlN6JSw//qub0oqne1\n1XqOI9CbAgMBAAECgf8XAgQ6gyb1TFakHG9QTkJEDZLRZPORxFVlecc8URSwubHE\nCT5WNxlmBPsWzgd70H7SY8tbg4Z3fzpPfOp2zXk/KlC5+RyFMaVKOjeUd+FFdYME\nt4anva305S823rHIt35SeQAFIQk9wo0ScK6oEGchDVRquIC+qlV8AOLQO3J4WMOA\ndlW9axQOtc+JCdGlFp70v0KKexqoI07FS8VXuoigHkLgGMozJXqqH8+Ej6Jd70Fo\nQDHTV78Ls8tWe1p8y41vPUABvkybEwcWF4+2csXlPdJvjwVpyfmuiIPyGPTZ0FTE\n4XOsNWTqYjFTO7AdrMJhDxe2ksXlAZY/xTD7pQkCgYEA4mQCYH14HV4aO+rXt3GB\nWblUNTEXYcLKkpWu0KTh3U6OnzGBuXf1f8xpM8y26jWIwLlPLqSttY4dMad84rIO\nExXcKSVlXjtLtAKRUTDXXxMbiAR5I/wisqtVPyQ6jjjmVzMfiWPMjV0XKQ56AWfu\nnC1NZU6rbwZF+c5VYyGw+eMCgYEAwQ6WDSDVWEfiKHjSGH2X5HC2INrY8pfUWI6X\ner+Se5YjVeLfuZH8hWE5TFrrDZqCbM+j1QqfoUEH5ZyLljaHgNGJ6y861O+Ywq5P\nMf2r+iCNUeducTeR72b94hWauyi2/vnei7r+t902ecdxpy2bkrs3vbEV0/AWt19I\n4Zov6+kCgYEA2uiPr9PDMMqMnYGBI5360NK3DVQx4tMjZEieqJu213Mdz+tkH/5S\nAkibNX5vJNutJ4ZIfba5TcRkkF3/EYnQuD28DIFfmpXFpwOQlqyepQ1p4sVIijZF\nKvUnUg3rHRkCCjGh/gzlf5ATVBzudquT+6qGmz5N4OZ1BY+x21B5u7cCgYEAtfXT\ng+gwbZbDGLZX/3FQ2qVJZEohNPXZ1OYA7Fbn78gg4fCGQdfRFL4ATXFcHmRFDd3f\nYwsyTcCHeulDv38B1G6q+Zp4bv6tEsFML6gSkhxgVpQ1SkzAJc8C+Da4sjK72DMW\niMjlD9NWZw2Ol62q9m+zJ/1iv3GJV6hdfxXemRECgYBrMg0AAfXC/GEPp0YnZj5+\n9VgWemRb3qv6StjU2bf8Df4sj9goXvz8OLoSCVyK+msl2KeGGUZS3v8bIb7CEVef\n11lEt1Vc7h97COSSG7jGxXE5DEOwvPRVknY+z3NrjERb/g/02W4q+bQN1FYZXQJ5\n8JNHKp4bpLQMfSppDMIaJg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-imtx4@rhythmx-test.iam.gserviceaccount.com",
  "client_id": "107450724592715024093",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-imtx4%40rhythmx-test.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


if not firebase_admin._apps:
	# "./firebase_utils/rhythmx-test-firebase-adminsdk-imtx4-c1a19edf4b.json"
	cred = credentials.Certificate(creds)
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

def update_patient(patient_id, key, new_value):
	ref = db.reference("/patient-data")
	patient_records = ref.get()
	for id, patient in patient_records.items():
		if id == patient_id:
			if key not in patient:
				patient[key] = []
			patient[key].append(new_value)
			ref.child(id).set(patient)
			
	