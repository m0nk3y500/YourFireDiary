# YourFireDiary
### -- It is currently still under _development_. But the basic functions work. --
A little Django-Webapp for logging fire operations.

This small webapp was created using Django and Bootstrap.

You can use it to write down your firefighting operations.

<img width="1680" alt="Bildschirmfoto 2022-03-31 um 11 25 29" src="https://user-images.githubusercontent.com/61576500/161023382-775910bb-c62d-4cbc-a9ad-b4152eece673.png">

<img width="1306" alt="Bildschirmfoto 2022-03-31 um 11 25 59" src="https://user-images.githubusercontent.com/61576500/161023507-7951f324-f2b4-4cea-a1cd-6ec7247bdd0c.png">

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
