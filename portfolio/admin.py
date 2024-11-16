from django.contrib import admin

from .models import Project, Backend, Frontend, Tools, Files

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")

class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "iconlink")

class FileAdmin(admin.ModelAdmin):
    list_display = ("filename", "cvlink")

admin.site.register(Project, PostAdmin)
admin.site.register(Backend, SkillAdmin)
admin.site.register(Frontend, SkillAdmin)
admin.site.register(Tools, SkillAdmin)
admin.site.register(Files, FileAdmin)
