from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
     print(args, kwargs)
     print(request.user)
     #return HttpResponse("<h1>Home Page</h1>") #string of HTML code
     return render(request, 'home.html');

def about_view(request, *args, **kwargs): #*args, **kwargs
     print(args, kwargs)
     print(request.user)
     #return HttpResponse("<h1>Home Page</h1>") #string of HTML code
     return render(request, 'about.html');

def contact_view(request, *args, **kwargs): #*args, **kwargs
     #return HttpResponse("<h1>Contact Page</h1>") #string of HTML code
     return render(request, 'contact.html');

def aboutProduct_view(request, *args, **kwargs): #*args, **kwargs
     my_context = {
          "title":"solisite",
          "my_text": "contact information or other text",
          "this_is_true": True,
          "my_number": 123456789,
          "my_list": [123, 312, 78890, 3432, 53254, "abc", "xyz"],
          "my_html": "<h1>hello world</h1>"
     }

     #return HttpResponse("<h1>About Page/h1>") #string of HTML code
     return render(request, 'aboutProduct.html', my_context);



