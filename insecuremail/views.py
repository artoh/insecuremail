from django.shortcuts import render, redirect
from .models import Mailbox, Message
from django.template import loader
from django.http import JsonResponse
import sqlite3

def index(request):
    failed = False
    if request.method == "POST" :
        box = Mailbox.objects.filter(name=request.POST.get("mailbox")).filter(password=request.POST.get("password"))
        if len(box) == 1:
            return redirect("/mailbox?user=" + request.POST.get("mailbox"))
        failed = True

    context = {"failed":failed, "boxes": Mailbox.objects.all()}
    return render(request, "index.html", context)

def mailbox(request):
    box = Mailbox.objects.filter(name=request.GET.get("user"))[0]
    messages = Message.objects.filter(receiver=box)
    context = {"box":box, "messages": messages}
    return render(request, "mailbox.html", context)

def newmail(request):
    box = Mailbox.objects.filter(name=request.GET.get("user"))[0]
    if request.method == "POST" :
        receiver = Mailbox.objects.filter(name=request.POST.get("receiver"))[0]
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        message = Message.objects.create(sender=box, receiver=receiver, subject=subject, body=body)
        message.save()
        return redirect("/mailbox?user=" + box.name)
    boxes = Mailbox.objects.all()
    context = {"box": box, "boxes": boxes}
    return render(request, "newmail.html", context)

def message(request):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT subject, s.name AS sender, r.name AS receiver, send, body FROM insecuremail_message AS m "+
        "JOIN insecuremail_mailbox AS s ON m.sender_id=s.id JOIN insecuremail_mailbox AS r ON m.receiver_id=r.id WHERE m.id = " + request.GET.get("id") )


    # box = Mailbox.objects.filter(name=request.GET.get("user"))[0]
    # messages = Message.objects.filter(id=request.GET.get("id"))
    return JsonResponse(list( cursor.fetchone() ), safe=False)
    # return render(request, "message.html", {"message": message, "box":box})
    