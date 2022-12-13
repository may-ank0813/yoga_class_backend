from django.db import migrations
from core.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(
                            name="mayank",
                            email="mayanksaini1913@gmail.com",
                            is_staff=True,
                            is_superuser=True,
                            age=21
                          )
        user.set_password("12345")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
