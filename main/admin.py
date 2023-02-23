from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Post, Team, Feedback, Subscriptions


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class TeamAdminForm(forms.ModelForm):
    resume = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Team
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['id', 'title', 'slug', 'author', 'date_event', 'created_at', 'get_photo', 'views', 'category']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ['category']
    readonly_fields = ['views', 'created_at', 'get_photo']
    fields = ['title', 'slug', 'author', 'content', 'date_event', 'created_at', 'image', 'get_photo',
              ('views', 'category')]

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        else:
            return 'нет фото'

    get_photo.short_description = 'миниатюра'


class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = ('id', 'name', 'surname', 'email', 'get_resume', 'get_photo', 'created_at')
    list_display_links = ('id', 'name', 'surname', 'email')
    search_fields = ('name', 'surname', 'email')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'нет фото'

    get_photo.short_description = 'Фото'

    def get_resume(self, obj):
        return obj.resume[:20]

    get_resume.short_description = "Опыт работы"


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'get_message', 'created_at')
    list_display_links = ('name', 'email')

    def get_message(self, obj):
        return obj.message[:20]

    get_message.short_description = "Отзыв"


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_group', 'name', 'phone', 'connection')
    list_display_links = ('id', 'name_group')


admin.site.register(Subscriptions, SubscriptionsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
