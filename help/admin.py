from django.contrib import admin
from .models import Category, Subject, Comments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}


@admin.register(Subject)
class SubjectAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')


@admin.register(Comments)
class CommentAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
