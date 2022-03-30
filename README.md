# YourFireDiary
### -- It is currently still under _development_. But the basic functions work. --
A little Django-Webapp for logging fire operations.

This small webapp was created using Django and Bootstrap.

You can use it to write down your firefighting operations.

## Example user

You can test the interface. 
Whether local or via the link in the description you can log in with a "muster" user.

user:
```
muster
```

password:
```
123456
```


## instructions for running locally

Clone the Resp from here:

```
git clone https://github.com/m0nk3y500/YourFireDiary.git
```

Go into the workfolder:
```
cd YourFireDiary
```

Creation of virtual environments:
```
python -m venv venv
```

To activate the virtual environments:
```
. venv/bin/activate
```

for deactivate:
```
deactivate
```

Install some packeges with pip:
```
pip install Django django-bootstrap4
```

Go in file of site:
```
cd ffs_site
```

To run the env-server from django:
```
python manage.py runserver
```
