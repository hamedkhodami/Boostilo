from django_q.tasks import async_task


def handler_send_notif_to_admins(fullname,email):
    print(f'New contact from{fullname (email)}')


def send_notif_to_admins(fullname, job_title, email):
    async_task(handler_send_notif_to_admins, (fullname,email))
