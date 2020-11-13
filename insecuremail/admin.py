from django.contrib import admin
from .models import Mailbox, Message

# Register your models here.

admin.site.register(Mailbox)
admin.site.register(Message)