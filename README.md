# InsecureMail

[Cyber Security Base](https://cybersecuritybase.mooc.fi/), Project I (University of Helsinki)

**The purpose of this sofware is to demostrate [security holes!](essay.txt)**

InsecureMail is a very unsecure internal mail system, made with [Django framework](https://www.djangoproject.com/).

Instructions to install Python 3 and Django are found in the [course material](https://cybersecuritybase.mooc.fi/installation-guide)

Before running this application, please run `python3 manage.py migrate`

Then you can start InsecureMail server with command `python3 manage.py runserver` and go to [http://localhost:8000/](http://localhost:8000/)

To add more mailboxes, please use Django admin panet at [http://localhost:8000/admin](http://localhost:8000/admin)
Admin username and password is not too hard to guess.
