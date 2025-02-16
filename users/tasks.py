from celery import shared_task

@shared_task
def send_async_email(user_id):
    from .models import User
    user = User.objects.get(id=user_id)
    print('Email sent to {}'.format(user.email))
