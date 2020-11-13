from django.shortcuts import render, redirect
from .models import Mailbox, Message
from django.template import loader

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
    box = Mailbox.objects.filter(name=request.GET.get("user"))[0]
    message = Message.objects.get(id=request.GET.get("id"))
    return render(request, "message.html", {"message": message, "box":box})
    