from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=20)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="contacts", null=True
    )