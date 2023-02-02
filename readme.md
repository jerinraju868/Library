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
![Screenshot from 2023-02-02 17-06-52](https://user-images.githubusercontent.com/117073931/216314668-b9d8ca18-190c-4206-9d9f-9f5030b4eaa2.png)


### Add app(Library) into the installed apps
    INSTALLED_APPS = [
        'Library',
    ]
![Screenshot from 2023-02-02 17-07-40](https://user-images.githubusercontent.com/117073931/216314828-5b2ac7b9-3419-4869-b849-72d05bfd57df.png)

### Adding Templates folder in templates
    os.path.join(BASE_DIR, 'templates')
![Screenshot from 2023-02-02 17-08-26](https://user-images.githubusercontent.com/117073931/216314957-0b8b8386-20b2-4b5b-b242-263ef2512f5d.png)

# Create template folder in the project root directory
![Screenshot from 2023-02-02 17-11-06](https://user-images.githubusercontent.com/117073931/216315460-f82dee34-3a9d-406f-9725-867626198ffb.png)

# Library

## Create a new file urls.py in Library folder
![Screenshot from 2023-02-02 17-10-38](https://user-images.githubusercontent.com/117073931/216315370-8bdf10b7-7db1-4918-8804-abc7602c6526.png)

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
![Screenshot from 2023-02-02 17-12-21](https://user-images.githubusercontent.com/117073931/216315710-f12832c0-fbce-466d-833b-e395dbf2c8a6.png)

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
![Screenshot from 2023-02-02 17-13-09](https://user-images.githubusercontent.com/117073931/216315844-830286f7-c228-4284-92fa-f9efebbbc02f.png)

# Runserver
    python manage.py runserver

# Open Browser and search
    127.0.0.1:8000/admin
![Screenshot from 2023-02-02 17-38-52](https://user-images.githubusercontent.com/117073931/216320858-e97b429c-9700-4025-8f83-cf4b0f12d949.png)


## Create form.py in Library folder
### Library/form.py
    from Library.models  import Books
    from django import forms

    class BookForm(forms.ModelForm):

        class Meta:
            model = Books
            fields = '__all__'
![Screenshot from 2023-02-02 17-13-37](https://user-images.githubusercontent.com/117073931/216315937-8bba3892-c267-4e39-a698-c36a5de819c0.png)

# TemplateView
## Library/views.py
### import the files and packages
    from django.shortcuts import render, redirect
    from django.urls import reverse_lazy
    from .models import Author, Books
    from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
![Screenshot from 2023-02-02 17-14-36](https://user-images.githubusercontent.com/117073931/216316148-b3b494b1-eba0-4897-a23c-8cede8b31ea1.png)

### TemplateView
    class Home(TemplateView):
        template_name = 'home.html'
![Screenshot from 2023-02-02 17-15-27](https://user-images.githubusercontent.com/117073931/216316301-89becb1f-deac-4864-9b86-84b2539bea90.png)

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
![Screenshot from 2023-02-02 17-16-28](https://user-images.githubusercontent.com/117073931/216316462-8644583c-ba1d-414e-b784-416582f3a9db.png)

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
![Screenshot from 2023-02-02 17-17-25](https://user-images.githubusercontent.com/117073931/216316665-22f43115-8376-428e-a39c-14f036e78f26.png)
### Browser View
![Screenshot from 2023-02-02 17-18-50](https://user-images.githubusercontent.com/117073931/216316910-d8858e8c-bc90-4059-9bc2-26def75ed01f.png)

# ListView
## Author List
### Library/views.py
    class AuthorList(ListView):
        model = Author
        template_name = 'author_list.html'
        context_object_name = 'authors'
![Screenshot from 2023-02-02 17-19-52](https://user-images.githubusercontent.com/117073931/216317073-604e8bdb-e356-450a-b7a1-fa0e5d8fc408.png)

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
![Screenshot from 2023-02-02 17-20-32](https://user-images.githubusercontent.com/117073931/216317236-ddf5d7fd-e9aa-4f60-a704-cb288b68d650.png)

### Browser view
![Screenshot from 2023-02-02 17-22-43](https://user-images.githubusercontent.com/117073931/216317618-feff4530-817d-4763-86e5-1104f4d95c38.png)

## Book List
### Library/views.py
    class BookList(ListView):
        model = Books
        template_name = 'book_list.html'
        context_object_name = 'books'
![Screenshot from 2023-02-02 17-21-24](https://user-images.githubusercontent.com/117073931/216317351-d82cc896-5631-416b-aa99-a84d28fc022d.png)

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
![Screenshot from 2023-02-02 17-23-32](https://user-images.githubusercontent.com/117073931/216317739-06cea523-656d-4e3a-9f27-04b759e1b757.png)

### Browser view
![Screenshot from 2023-02-02 17-24-00](https://user-images.githubusercontent.com/117073931/216317844-ada737d2-eca9-40b4-80fe-b9715b0a041c.png)

# CreateView
## Library/views.py
    class CreateBook(CreateView):
        model = Books
        fields = '__all__' 
        template_name = 'book_create.html'
        success_url = '/books/'
![Screenshot from 2023-02-02 17-25-02](https://user-images.githubusercontent.com/117073931/216318040-36a1ab61-e71c-47c7-86e7-c7cb04637c8f.png)

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
![Screenshot from 2023-02-02 17-25-39](https://user-images.githubusercontent.com/117073931/216318168-ea6c3752-c810-46f7-a961-4f73609d6716.png)

### Browser View
![Screenshot from 2023-02-02 17-26-24](https://user-images.githubusercontent.com/117073931/216318341-18d6fafa-00b9-4478-b963-eb6b189625b9.png)

# DetailView
## Library/views.py
    class ViewBook(DetailView):
        model = Books
        template_name = 'book_detail.html'
        context_object_name = 'book'
![Screenshot from 2023-02-02 17-27-19](https://user-images.githubusercontent.com/117073931/216318485-bd5ddeaf-2fc2-4de7-b2ca-ee6a43886e1a.png)

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
![Screenshot from 2023-02-02 17-27-52](https://user-images.githubusercontent.com/117073931/216318608-78035b1c-b5a1-4001-af13-60c9fe037ac9.png)

### Browser View
![Screenshot from 2023-02-02 17-28-29](https://user-images.githubusercontent.com/117073931/216318744-95226368-9322-4ebc-a7b2-da9187454864.png)

# UpdateView
## Library/views.py
    class UpdateBook(UpdateView):
        model = Books
        template_name = 'book_update.html'
        fields = '__all__'
        success_url = '/books/'
![Screenshot from 2023-02-02 17-29-23](https://user-images.githubusercontent.com/117073931/216318892-53b1e3d8-ebb2-4609-8251-634c372d4cc6.png)

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
![Screenshot from 2023-02-02 17-30-06](https://user-images.githubusercontent.com/117073931/216319009-c9788e92-12b3-41b0-bc59-1862057fa40b.png)

### Browser View
![Screenshot from 2023-02-02 17-30-38](https://user-images.githubusercontent.com/117073931/216319158-dbacfba3-0a76-489f-95e6-c184777a0117.png)

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
![Screenshot from 2023-02-02 17-31-40](https://user-images.githubusercontent.com/117073931/216319302-e079f6ad-b847-46f2-9e62-835c53a090e7.png)

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
![Screenshot from 2023-02-02 17-32-28](https://user-images.githubusercontent.com/117073931/216319437-79fdc9bc-a154-4079-a46a-55ff5c89a411.png)

### Browser View
![Screenshot from 2023-02-02 17-33-01](https://user-images.githubusercontent.com/117073931/216319552-007e461a-8f4d-4562-af43-093cb010d584.png)

# Library/urls.py
    from django.urls import path
    from Library import  views
    
    urlpatterns = [
        path('', views.Home.as_view(), name='home'),
        path('books/', views.BookList.as_view(), name='books'),
        path('authors/',views.AuthorList.as_view(), name='authors'),
        path('create/',views.CreateBook.as_view(), name='book_create'),
        path('detail/<int:pk>/',views.ViewBook.as_view(), name='book_detail'),
        path('update/<int:pk>/', views.UpdateBook.as_view(),name='book_update'),
        path('delete/<int:pk>/', views.DeleteBook.as_view(),name='book_delete'),
    ]
![Screenshot from 2023-02-02 17-35-18](https://user-images.githubusercontent.com/117073931/216320003-18df1ad0-c4a3-42e5-8e52-d53528a030d5.png)
