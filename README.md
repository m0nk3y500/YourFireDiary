# YourFireDiary
### -- It is currently still under _development_. But the basic functions work. --
A little Django-Webapp for logging fire operations.

This **small and easy** webapp was created using Django and Bootstrap.

You can use it to write down your firefighting operations.

_The interface is developed in German. Of course you can change the few words.<br>
Maybe I'll bring out a combination again, where you can choose._


<img width="720" alt="Bildschirmfoto 2022-04-01 um 10 09 34" src="https://user-images.githubusercontent.com/61576500/161223757-1a9eee06-8fd8-4000-99fa-a3406639248a.png">


<img width="1664" alt="Bildschirmfoto 2022-04-01 um 10 13 47" src="https://user-images.githubusercontent.com/61576500/161223835-8dd483ff-59fe-485d-acfa-ab69c3d0b4f5.png">


<img width="1350" alt="Bildschirmfoto 2022-04-01 um 10 18 14" src="https://user-images.githubusercontent.com/61576500/161224098-461d01dc-fcd9-463c-803b-afa70cd95866.png">


## Example user

You can test the interface. 
Whether local or via the link in the description you can log in with a "muster" user.

user: `muster`

password:`123456`


## instructions for running locally

Clone the Resp from here: `git clone https://github.com/m0nk3y500/YourFireDiary.git`

Go into the workfolder: `cd YourFireDiary`

Creation of virtual environments: `python -m venv venv`

To activate the virtual environments: `. venv/bin/activate`

for deactivate: `deactivate`

Install some packeges with pip: `pip install Django django-bootstrap4`

Go in file of site: `cd ffs_site`

Open `settings.py` in editor or in terminal with `nano  settings.py`
You still have to change the DB settings, in line 85, 86

This is what it should look like after the change:
```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': BASE_DIR / 'db_main.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

To run the env-server from django: `python manage.py runserver`

Now you can visit the site over: `localhost:8000/web/login`
