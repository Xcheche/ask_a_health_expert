from django.contrib import admin
from .models import *
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'add_time')
    search_fields = ('title',)
    list_filter = ('add_time', 'user')
    ordering = ('-add_time',)
    date_hierarchy = 'add_time'
    list_per_page = 10
    list_editable = ('title',)
    list_display_links = ('id', 'user')
    list_select_related = ('user',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'add_time')
    search_fields = ('detail',)
    list_filter = ('add_time', 'user')
    ordering = ('-add_time',)
    date_hierarchy = 'add_time'
    list_per_page = 10
    list_display_links = ('id', 'user')
    list_select_related = ('user', 'question')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'answer', 'comments', 'add_time')
    search_fields = ('user__username',)
    list_filter = ('add_time', 'user')
    ordering = ('-add_time',)
    list_display_links = ('id', 'user')
    list_select_related = ('user', 'answer')

class UpvoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'answer')
    search_fields = ('user__username',)
    list_filter = ('user',)
    ordering = ('-id',)
    list_display_links = ('id', 'user')
    list_select_related = ('user', 'answer')

class DownvoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'answer')
    search_fields = ('user__username',)
    list_filter = ('user',)
    ordering = ('-id',)
    list_display_links = ('id', 'user')
    list_select_related = ('user', 'answer')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Upvote, UpvoteAdmin)
admin.site.register(Downvote, DownvoteAdmin)