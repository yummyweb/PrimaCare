from django.contrib import admin
from data.models import Access, Document, Medicine

# Register your models here.
admin.site.register(Medicine)
admin.site.register(Document)
admin.site.register(Access)