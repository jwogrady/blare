from django.db import models

class Client(models.Model):
    """A class to represent a client.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    mailing_address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# TODO: A contact has many profiles.
# TODO: Validate email, phone, and mailing address
# TODO: Create a table to link Clients and Aware Contacts
