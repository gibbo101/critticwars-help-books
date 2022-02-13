from django.contrib import admin
from .models import Category, Subject, Comments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)


@admin.register(Subject)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


@admin.register(Comments)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
