#  copy the directory to the server system

 1. scp -r directory_name  user@0.0.0.0:~/(sample server ) ## this will copy to the home folder of the sever

 2. sudo apt-get install python3-venv
 3. python-3 -m venv venv ( create a virutal enviorment in side the project directory, here its marslab_iitg)
 4. source venv/bin/activate (activate the enviorment)
 5. pip install -r requirements.txt ( install all the requirements)
 6. sudo nano settings.py 
 in ALLOWED_HOSTS = ['0.0.0.0'] ( pass the ip address inside the array)
 7. above the STATIC_URL
###  add STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
### save the file

## 8. now back to terminal type 
### python manage.py collectstatic
## 9 runs the code to check if the site is working on the host 
### python manage.py runserver 0.0.0.0:8000



