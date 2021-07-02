from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from .utils import generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from main.models import Student
from django.core.mail import EmailMessage
from django.conf import settings


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Activate your email"
    email_body = render_to_string('activation.html', {
        'user': user,
        'domain': current_site,
        'uid' : urlsafe_base64_encode(force_bytes(user.id)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,from_email=settings.EMAIL_FROM_USER,to=[user.email])
    email.send()    

def confirm_email(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Student.objects.get(id=uid)
    
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        return user
    return None 
