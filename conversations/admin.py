from django.contrib import admin
from . import models


@admin.register(models.Message)
class MesaageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    list_display = (
        "__str__",
        "created",
    )


@admin.register(models.Conversation)
class MesaageAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    list_display = ("__str__", "count_messages", "count_participants")
