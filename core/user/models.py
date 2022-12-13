from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)

    username = None
    # modifying default username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    age = models.IntegerField(default=0)

    session_token = models.CharField(max_length=10, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


