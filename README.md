# Oauth_Google
Code to implement Oauth on a front end website, python backend to exchange for access token
Code walkthrough: https://youtu.be/OK_j05bxmH4 

## Theme: Knight-One, Bootstrap 5 theme

### Current code on html page uses ajax, but feel free to eliminate jquery and use fetch

## 1. Install pythons flask by running this in command prompt:
pip install flask

## 2. Google console:
Navigate to the Google console, https://console.cloud.google.com/ and click on 'Apis & Services' <br />
Create a project if you have not yet <br />
Create an app if you have not yet <br />
- Give it a name, your email
- Select 'External'
- Give it your email as Contact
- Agree to terms
- Create App

In the left menu, click on "OAuth consent screen' <br />
In the left menu, click on 'Clients' <br />
Click 'Create Client' <br />
For a web application, select 'Web application' in the drop down <br />
Give it a name <br />
For Authorized Javascript origins, add 3 uris: <br />
- http://localhost:5000
- http://localhost:8000
- http://localhost (it will give an error without this as a base)

For Authorized redirect URI's, add 1 uri (this must match exactly to what you specify as the redirect in auth.html and oauth-google.py) <br />
   -  http://localhost:5000/process-auth-google 

Click 'Create'  <br />
Download the JSON file with your credentials <br />


## 3. For local testing, launch 1 python server in the local directory of the html file
In command prompt or terminal, navigate to the directory where the html file is and run:
- python -m http.server <br />

This will default to port 8000 <br />

In a second command prompt, navigate to where your python file is and run: <br />
- python oauth-google.py <br />

This will launch a web server with the port specified in app.run() command <br />

## 4. In a browser, load http://localhost:5000/auth-google.html



