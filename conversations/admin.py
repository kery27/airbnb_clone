from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversation Admin Definition"""

    pass


# Register your models here.
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Message Admin Definition"""

    pass

