from flask import Flask, request, redirect, jsonify, session
from google.oauth2 import id_token # OpenID Connect
from google.auth.transport import requests
import json
from flask_cors import CORS # Import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = 'YOUR CLIENT SECRETE' #very important to change this.
CLIENT_ID = 'YOUR CLIENT ID'

  
@app.route('/process-auth-google', methods=['POST'])
def process_auth():
    try:
        print(f"in process-auth")
        #print(f"request.form: {request.form}")
        token = request.form['credential'] #google sends the token in the credential field
        g_csrf_token = request.form['g_csrf_token']
        
        print(f"token: {token}")
        print(f"-----")
        print(f"g_csrf_token: {g_csrf_token}")
        
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        print(f"-----")
        print(f"idinfo: {idinfo}")
        
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        user_email = idinfo['email']
        
        # verify your user
        
        # create user if they don't exist
        
        # session['user_id'] = user['id'] #or generate a jwt. # !! Do NOT store jwts client side !!

        return redirect("http://localhost:8000/dashboard.html") # Replace with your desired URL.

    except Exception as e:
        print(f"Exception {e}")
        return jsonify({'error': 'Invalid token'}), 401     

if __name__ == '__main__':
    app.run(debug=True, port=5000)  
