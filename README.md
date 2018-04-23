# Bar-App
A Bar app to see Popular Bars being posted by users along with a review


#Steps
#First create your Virtualenv
Virtualenv 'yournewvirtualenv'
cd 'yournewvirtualenv'
pip install django
Pillow==5.1.0


#activate your virtualenv
.\scripts\activate

#Create your djangoproject
django-admin startproject 'projectname'
cd 'projectname'

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

#Now Create APP
python manage.py startapp hotlocalbars


#Next you will build your Model sit and think of what data or info you want to incorporate into your model
#Then go to settings.py and Add your new app into the INSTALLED APPS

#Next create your VIEWs
#Next create your URLS
#NEXT create your TEMPLATES

#Run Command python manage.py runserver this gets the Server up and running 
#IF your using a local machine you can go to 127.0.0.0.1:8000 it will show you your APP
python manage.py runserver
