from django.contrib import admin
from .models import Artist, Format, Genre, Record

admin.site.register(Artist)
admin.site.register(Format)
admin.site.register(Genre)
admin.site.register(Record)

