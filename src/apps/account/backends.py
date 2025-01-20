from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                print(f"Password does not match for {username}")
        except User.DoesNotExist:
            print(f"User with email {username} does not exist.")
            return None