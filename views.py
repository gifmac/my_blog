from django.shortcuts import render

# Create your views here.



# Create your views here.
# It is python function that returns some html, each url is connected a view or html response
# view takes users request and they return something to them. For example, they take the request for a url and returns
# the webpage.
# Views is the logic of the appication. It requests  information from  the model and pass it to a template

#  A view is a “type” of Web page in your Django application that generally serves a specific function and has a
# specific template.For example,  Blog homepage – displays the latest few entries
#Question “results” page – displays results for a particular question.


# we will add views to blog/views.py
# Create your views here.
# It is python function that returns some html, each url is connected a view or html response
# view takes users request and they return something to them. For example, they take the request for a url and returns
# the webpage.
# Views is the logic of the appication. It requests  information from  the model and pass it to a template

#  A view is a “type” of Web page in your Django application that generally serves a specific function and has a
# specific template.For example,  Blog homepage – displays the latest few entries
#Question “results” page – displays results for a particular question.


# we will add views to blog/views.py
from  django.http import Http404, HttpResponse   # import error that displays when the user request is not avaliable
#from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
#rom .models import Post, Author,AboutMe,Albums # dot means both model and view are in the same directory


# The render() function takes the request object as its first argument, a template name as its second argument and
# a dictionary as its optional third argument. It returns an HttpResponse object of
# the given template rendered with the given context.

# we want the index page to list the five recent post if the total post is greater than 5, if not list all the post

def index(request):
    return (HttpResponse("<h1>hi own os n</h>)"))

    #all_posts = Post.objects.all().order_by("published_date")  # get all the published post and order them by date

    # A QuerySet is evaluated when you call len() on it, returns the length of the result list.
    #if len(Post.objects.order_by("published_date")) >= 5:    # we use len because post.object is a list.
       # latest_post_list = Post.objects.order_by("published_date")[:5] # get the first 5 post
    #else:
        #latest_post_list = Post.objects.all()
    #context = {"all_posts": all_posts,"latest_post_list": latest_post_list}
    #return render(request, "blog/index.html",context)


# def post_list(request, post_id):
#  return render (request, "blog/post_list.html", {})
#  render means to put together  our template blog/post_list.html

# we will need to create the html template
# template are saved in blog/template/blog directory, we will create a directory called templates inside blog directory
# Then create another directory called blog inside template directory, them create post_list.html inside


# Dynamic data in Templates
# view connects our templates and models. take our models and display them in our template htmls. Views takes the models
# want to display and pass them to  the templates
# we will add our models to the view.


# we will use queryset, to get the model data
# we want  published Post  that have published date before now , and we want to sort
# them by the date they were published or published_date note:  Ite = less than or equal to

#  Post.objects.filter(published_date__lte=timezone.now()).order_by ("published_date")

#view for Post, list all the Posts
#def post_user_id(request, post_id):  # post id represent id , which are integers that are entered by user
    # get the post with id or pk that is equal to the post_id entered by user
    #try:
        #Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date").exists()

    #  exist() : Returns True if the QuerySet contains any results, and False if not.
       # request_post_id = Post.objects.get(pk=post_id)

    #except Post.DoesNotExist:
        #raise Http404("There is no post with such id")
    #return render(request, "blog/post_user_id.html", {"request_post_id": request_post_id})

    # the curly bracket is a dictionary and takes arguments


# we will pass the instant of the model class we want to display in html to it
# that we not write g/blog/post_list.html" in the url domain because our template are already in template.blog,
# django look there to location to locate the html file post_list


# The concept here: The view raise if there is no post details for the post id or pk
#  the user requested  return the error post does not exist
# But if the post exist return the string object  for the post with the id.

#the view for Post
#def post_details(request, post_id):

   # try:
        #each_post = Post.objects.get(pk=post_id)
   # except Post.DoesNotExist:
        #raise Http404("Post does not exist")
   # return render(request, "blog/post_details.html", {"each_post": each_post})

    # we want django to return each_post to the blog/details.html


# we will use get_object_or_404  to implement error check as in above.
# we want to write a function that will give back the details of post author to the user

# the view for Author
#def post_author(request, post_id):  # post_id get the pk of the post we want ot research the author.
    # get the Author object  that have  the post_id= pk if it does not exist raise the 404 error
    #author_detail = get_object_or_404(Author, pk=post_id)

   # return render(request, "blog/post_author.html", {"author_detail": author_detail})

# the view for Aboutme
# the first about me will assign pk of 1 so when used enter 1 it will appear.
#def about_me(request, post_id):
   # try:
        #aboutme = AboutMe.objects.get(pk=post_id)
    #except AboutMe.DoesNotExist:
        #raise Http404("Sorry About me does not exist, check back later")
    #return render(request,"blog/about_me.html",  {"aboutme": aboutme})

# the view for form
#def favorite(request, post_id):
   # favorite_post = get_object_or_404(Post,pk =post_id)
    #try:
       # selected_post = favorite_post.posting_set.get(pk= request.POST["posting"])
   # except(KeyError,Post.DoesNotExist):
        #return render(request,"blog/post_details.html",{favorite_post : "favorite_post", "error message": "wrong"})
   # else:
        #selected_post.is_favorite =True
       # selected_post.save()
       # return render(request, "blog/post_details.html" ,{"favorite_post": favorite_post})

# The view for Albums
#def album(request, album_id):
   # myalbum = get_object_or_404(Albums,pk= album_id )
    #return render(request, "blog/album.html", {"myalbum":myalbum})

                            # Display post list template
#  we gave our template a list of posts in the posts variable called post_list. Now we will display it in HTML.
#  Django template allows us  to display python like tags in html.
#  print a variable in Django templates, we use double curly brackets with the variable's name inside, like this:
#  blog/templates/blog/post_list.html {{post}}
#  For python code that we need to manipulate we represent the as {% function %}, the variables we want to displacce as
# they are wtakes the form {{ variable}}

# In the template, you should use quotes when the url pattern name is a string:
# # {% url 'adminview' %}
# # {% url 'eventview' %}
                              # creating static directory.
# Static directory is used for storing static files such as css, static images,
# To create them, we will go to blog create a directory : blog/static/blog/images

