# Library
Create CRUD APp using ClassBasedViews 
models :
    1.Authors[name, age]
    2.Books[title, author, summary, published_date]
HTML Pages :
    1.Author List Page
    2.Book List Page
    3.Book Create Page
    4.Book Details Page
    5.Book Update Page
    6.Book Delete Page

## Creating virtual environment and activate
    python -m venv Env
    source /Env/bin/activate

## Installing the django 
    pip install django

## Creating the project named 'Config'
    django-admin startproject Config

## Move into the project folder
    cd Config

## Creating the app named 'Library'
    python manage.py startapp Library

# Setting.py

### import os
    import os

### Add app(Library) into the installed apps
    INSTALLED_APPS = [
        'Library',
    ]

### Adding Templates folder in templates
    os.path.join(BASE_DIR, 'templates')

# Create template folder in the project root directory

# Library

## Create a new file urls.py in Library folder

## Library/models.py
    from django.db import models

    class Author(models.Model):
        name = models.CharField(max_length=100,unique=True,null=False)
        age = models.IntegerField()

        def __str__(self):
            return self.name

    class Books(models.Model):
        title = models.CharField(max_length=200,unique=True, null=False)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        summary = models.TextField()
        published_date = models.DateField()

        def __str__(self):
            return self.title

## Makemigrations and Migrate
    python manage.py makemigrations
    python manage.py migrate

## Create Super User
    python manage.py createsuperuser

## Register the models in admin panel
### Library/admin.py
    from django.contrib import admin
    from Library.models import Author, Books

    admin.site.register(Author)
    admin.site.register(Books)

## Create form.py in Library folder
### Library/form.py
    from Library.models  import Books
    from django import forms

    class BookForm(forms.ModelForm):

        class Meta:
            model = Books
            fields = '__all__'

# TemplateView
## Library/views.py
### import the files and packages
    from django.shortcuts import render, redirect
    from django.urls import reverse_lazy
    from .models import Author, Books
    from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

### TemplateView
    class Home(TemplateView):
        template_name = 'home.html'
#### base.html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        {% block title %}
        <title>Library</title>
        {% endblock title %}

    </head>
    <body>
        <nav class="navbar navbar-light bg-light">
            <div style="display: flex;">
                <img src="https://media4.giphy.com/media/fVbtV4grwKBj2yinwD/giphy.gif?cid=790b7611c3c807b45e3f36eabb60c1375a1e7639cf1a6d54&rid=giphy.gif&ct=s" style="width: 50px;height: 50px; margin-left: 100px;">
                <a class="navbar-brand" href="{% url 'home' %}">
                    <h1>Library</h1>
                </a>
            </div>
            <ul style="list-style: none; display: flex; margin-right: 20px;">
                <li>
                    <a href="{% url 'authors' %}" style="margin-right: 100px; text-decoration: none;"> <h4>Author List</h4></a>
                </li>&emsp;&emsp;
                <li>
                    <a href="{% url 'books' %}" style="margin-right: 100px; text-decoration: none;"> <h4>Book List</h4></a>
                </li>
            </ul>
        </nav>
        <br>
        {% block content %}
        {% endblock content %}
    </body>
    </html>
#### home.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Home</title>
    {% endblock %}

    {% block content %}

    <div class="container">
        <div class="card shadow" style="border-radius: 1rem; width: fit-content;">
            <div class="card-title">
                <h1 style="text-align: center;">Home Page</h1>
            </div>
            <div class="card-body">
                <p>
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
                </p>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tempus, eros id placerat imperdiet, dui arcu rhoncus velit, sit amet interdum justo odio sed elit. Nam vitae leo vel urna aliquam egestas. Nullam ullamcorper interdum mauris sit amet tincidunt. Quisque tempor dictum neque eu molestie. 
                </p>
            </div>
        </div>
    </div>
    {% endblock%}


# ListView
## Author List
### Library/views.py
    class AuthorList(ListView):
        model = Author
        template_name = 'author_list.html'
        context_object_name = 'authors'
### author.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Author List</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="card shadow" style="border-radius: 1rem;">
            <div class="card-header">
                <h3 style="text-align: center;">Author List</h3>
            </div>
            <div class="card-body">
                <table class="table">
                    <thead>
                        <th>Author ID</th>
                        <th>Author Name</th>
                        <th>Age</th>
                    </thead>
                    <tbody>
                        {% for author in authors %}
                        <tr>
                            <td>{{author.id}}</td>
                            <td>{{author.name}}</td>
                            <td>{{author.age}}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    {% endblock%}

## Book List
### Library/views.py
    class BookList(ListView):
        model = Books
        template_name = 'book_list.html'
        context_object_name = 'books'
### book_list.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Book List</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="card shadow" style="border-radius: 1rem;">
            <div class="card-header">
                <h3 style="text-align: center;">Book List</h3>
            </div>
            <div class="card-body">
                <a href="{% url 'book_create' %}" class="btn btn-primary btn-sm">Add New Book</a><br><hr>
                <table class="table">
                    <thead>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Actions</th>
                    </thead>
                    <tbody>
                        {% for book in books %}
                        <tr>
                            <td>{{book.title}}</td>
                            <td>{{book.author}}</td>
                            <td>
                                <a href="{% url 'book_detail' book.id %}" class="btn btn-sm btn-warning">View</a>
                                <a href="{% url 'book_update' book.id %}" class="btn btn-sm btn-success">Edit</a>
                                <a href="{% url 'book_delete' book.id %}" class="btn btn-sm btn-danger">Delete</a>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
    {% endblock%}


# CreateView
## Library/views.py
    class CreateBook(CreateView):
        model = Books
        fields = '__all__' 
        template_name = 'book_create.html'
        success_url = '/books/'
## book_create.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Create Book</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="card">
            <div class="card-title">
                <h3 style="text-align: center;">Create New Book</h3>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    {{form.as_p}}
                    <input type="submit" placeholder="Submit" class="btn btn-success">
                </form>
            </div>
        </div>
    </div>
    {% endblock content %}

# DetailView
## Library/views.py
    class ViewBook(DetailView):
        model = Books
        template_name = 'book_detail.html'
        context_object_name = 'book'
## book_detail.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Book Detail</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="card shadow" style="border-radius: 1rem;">
            <div class="card-header">
                <h1 style="text-align: center;">Book Details</h1>
            </div>
            <div class="card-body">
                <p style="margin: 20px;">
                    <label style="font-size: x-large;font-weight: bold;">Book : </label>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{{book.title}}<br>
                    <label style="font-size: x-large;font-weight: bold;">Author : </label>&emsp;&emsp;&emsp;&emsp;&ensp;{{book.author}}<br>
                    <label style="font-size: x-large;font-weight: bold;">Publish : </label>&emsp;&emsp;&emsp;&emsp;{{book.published_date}}<br>
                    <label style="font-size: x-large;font-weight: bold;">Summary : </label>&emsp;{{book.summary}}<br>
                </p>
            </div>
        </div>
    </div>
    {% endblock%}

# UpdateView
## Library/views.py
    class UpdateBook(UpdateView):
        model = Books
        template_name = 'book_update.html'
        fields = '__all__'
        success_url = '/books/'
## book_update.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Edit  Book</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="card shadow" style="border-radius: 1rem;">
            <div class="card-header">
                <h3 style="text-align: center;">Update Book</h3>
            </div>
            <div class="card-body">
                <form  method="post">
                    {% csrf_token %}
                    {{form.as_p}}
                    <input type="submit" placeholder="Submit" class="btn btn-success">
                </form>
            </div>
        </div>
    </div>
    {% endblock content %}

# DeleteView
## Library/views.py
    class DeleteBook(DeleteView):
        model = Books
        template_name = 'book_delete.html'
        success_url = reverse_lazy('books')

        def post(self, request, *args, **kwargs):
            if request.POST["cancel"]:
                return redirect('/books/')
            else:
                return super(DeleteBook, self).post(request, *args, **kwargs)
## book_delete.html
    {% extends 'base.html' %}
    {% block title %}
    <title>Book Detail</title>
    {% endblock %}

    {% block content %}
    <div class="container">
        <div class="card shadow" style="border-radius: 1rem;">
            <div class="card-body">
                <form method="post">  
                {% csrf_token %}  
                <p>Are you sure you want to delete "{{ object }}"?</p> 
                <input type="submit" class="btn btn-danger" value="Confirm">
                <input type="submit"  class="btn btn-secondary" name="cancel" value="Cancel" /> 
            </form>  
            </div>
        </div>
    </div>
    {% endblock content %}
