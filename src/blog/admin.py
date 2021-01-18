from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category, Like, PostView

class PostAdmin(SummernoteModelAdmin): 
    summernote_fields = ("post_content",)

class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ("comment_content",)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)
admin.site.register(PostView)
admin.site.register(Category)
