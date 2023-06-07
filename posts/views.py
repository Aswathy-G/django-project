# import datetime
# import json

# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# from posts.forms import PostForm
# from posts.models import Author,Category, Post
# from main.functions import generate_form_errors, paginate_instances
# from main.decorators import allow_self


# @login_required(login_url="/users/login/")
# def create_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():

#             tages =form.cleaned_data['tages']

#             if not Author.objects.filter(user=request.user).exists():
#                 author = Author.objects.create(user=request.user,name=request.user.username)
#             else:
#                 author = request.user.author

#             instance = form.save(commit=False)
#             instance.published_date = datetime.date.today()
#             instance.author =  author
#             instance.save()

#             tages_list = tages.split(",")
#             for tage in tages_list:
#                 category,created = Category.objects.get_or_create(title=tage.strip())
#                 instance.categories.add(category)

#             response_data = {
#                 "title" : "Sucessfully Submited",
#                 "message" : "Sucessfully Submited",
#                 "status" : "Sucess",
#                 "redirect" : "yes",
#                 "redirect_url" : "/"
#             }  
#         else:
#             error_message = generate_form_errors(form)
#             print(error_message)

#             response_data = {
#                 "title" : "form validation error",
#                 "message" : str(error_message),
#                 "status" : "error",
#                 "stable" : "yes"
#             }
#         return HttpResponse(json.dumps(response_data),content_type="application/json") 
#     else:
#         data = {
#             "title" : "Hello",
#             "description" : "Hello",
#             "short_description" : "Hello",
#             "time_to_read" : "8 min",
#             "tages" : "techonology,programming,coding"       
#              }
#         form = PostForm(initial=data)
#         context = {
#             "title":"create new post",
#             "form":form
        
#         }
#         return render(request, "posts/create.html", context=context)
