from django.contrib import admin

from notes.models import Notes

class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'note',
        )

    search_fields = (
        'title',
        'note',
        )

admin.site.register(Notes, NoteAdmin)