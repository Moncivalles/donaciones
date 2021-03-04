
from django.shortcuts import render  #! libreruia que acer refercia a regresar una vista 
import pyrebase


Config = { # config es un diccionario de python en otros lenguajes seria mapa
    'apiKey': "AIzaSyAe_6gpBKlBiqpBaa737ia078-YW9pyYxI",
    'authDomain': "login-9f8c4.firebaseapp.com",
    'projectId': "login-9f8c4",
    'databaseURL': "xxxxxx", #! valor ficticio 
    'storageBucket': "login-9f8c4.appspot.com",
    'messagingSenderId': "601525647964",
    'appId': "1:601525647964:web:88ec4ede429dad6707c499",
    'measurementId': "G-MVRL5ZLBGD"
  }


# Inicializando la base de datos, la autenticación y la base de fuego para su uso posterior
firebase = pyrebase.initialize_app(Config)  #inicializar 
authe = firebase.auth() #comenzar una instancia de autenticacio  
database = firebase.database() #inicializa la base de datos en este caso no la usaremos 



def signIn(request): 
    return render(request,"Login.html") 

def home(request): 
    return render(request,"Home.html") 
  
def postsignIn(request): 
    email=request.POST.get('email') 
    pasw=request.POST.get('pass') 
    try: 
        # if there is no error then signin the user with given email and password 
        user=authe.sign_in_with_email_and_password(email,pasw) 
    except: 
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message}) 
    session_id=user['idToken'] 
    request.session['uid']=str(session_id) 
    return render(request,"Home.html",{"email":email}) 
  
def logout(request): 
    try: 
        del request.session['uid'] 
    except: 
        pass
    return render(request,"Login.html") 
  
def signUp(request): 
    return render(request,"Registration.html") 
  
def postsignUp(request): 
     email = request.POST.get('email') 
     passs = request.POST.get('pass') 
     name = request.POST.get('name') 
     try: 
        # creating a user with the given email and password 
        user=authe.create_user_with_email_and_password(email,passs) 
        uid = user['localId'] 
        idtoken = request.session['uid'] 
        print(uid) 
     except: 
        return render(request, "Registration.html") 
     return render(request,"Login.html")