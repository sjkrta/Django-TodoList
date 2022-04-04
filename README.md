1. Pre-requirements
> Python
> Django
> code editor (vscode)

2. Virtual Environment & Install Packages
> mkdir foldername
> python -m venv foldername
> .\foldername\Scripts\activate
> pip install django (optional:djangorestframework)
> pip freeze > requirements.txt
	> help: pip install -r requirements.txt

3. Create Project and App and Migrate it
> django-admin startproject foldername .
> django-admin app appname
> python manage.py migrate

4. Start configurations
> settings.py

6. Create database, register model, makemigrations
> models.py
	- class className(models.Model):
		..........
> admin.py
	- admin.site.register(className)
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver

7. Templates and Static
> mkdir templates 
	> mkdir includes
		- style.css
		- script.js
	- index.html
	- base.html
> mkdir static/images

8. Views and Urls
> def index(request):
	return render('', 'index.html', context={})
> render ' ' to index.html

9. Create Main User
> python manage.py createsuperuser
	- username: (admin)
	- password: (admin)

10. 