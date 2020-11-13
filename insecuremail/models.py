from django.db import models
from django.utils.timezone import now

# Create your models here.

class Mailbox(models.Model) :
    name = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.name

class Message(models.Model) :
    sender = models.ForeignKey(Mailbox, on_delete=models.CASCADE, related_name="msg_sender")
    receiver = models.ForeignKey(Mailbox, on_delete=models.CASCADE, related_name="msg_receiver")
    subject = models.TextField(null=True)
    body = models.TextField(null=True)
    send = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return "{0} -> {1} : {2}".format(self.sender.name, self.receiver.name, self.subject)