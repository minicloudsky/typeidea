from django.contrib import admin
from .models import Comment
from typeidea.custom_site import custom_site
import xadmin


# Register your models here.

@xadmin.sites.register(Comment)
class CommentAdmin():
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
