# from django import forms
# from posts.models import Post

# class PostForm(forms.ModelForm):
#     tages = forms.CharField(widget=forms.TextInput(attrs={'class':"input"}), label="Tages (Comma seperated)")
#     class Meta:
#         model = Post
#         exclude = ('author','published_date','is_deleted','categories')


#         widgets = {
#             "time_to_read" : forms.TextInput(attrs={'class':"input"}),
#             "title" : forms.TextInput(attrs={'class':"input"}),
#             "short_description" : forms.Textarea(attrs={'class':"input"}),
#         }
#         error_messages = {
#             "title" : {
#                 "required" : "Title field is required"
#             },
#             "description" : {
#                 "required" : "Description field is required",
#             },
#             "short_description" : {
#                 "required" : "Short description field is required",
#             },
#             "time_to_read" :{
#                 "required" : "Time to read filed is requird",
               
#             },
#             "featured_image" : {
#                 "required" : "featured image field is required",
#             },
#             "is_draft" : {
#                 "required" : "is draft field is required",
#             },

#         }
         