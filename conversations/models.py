from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
