from user import User
from werkzeug.security import safe_str_cmp

users=[
	User(1, "kiki", "duolingo"),
	User(2, "luli", "luli")
	
]

user_mapping = {u.username: u for u in users}
id_mapping ={u.id: u for u in users	}

def authenticate(username, password):
	user = user_mapping.get(username, None)
	#never compare strings directly because of encodings
	if user and safe_str_cmp(user.password, password):
		return user

def identity(payload):
	user_id = payload['identity']
	return id_mapping.get(user_id, None)
