from django.db import models

class Client(models.Model):
    id_format = models.CharField(max_length=255)
    id_value = models.CharField(max_length=255)
    user_id = models.IntegerField()
    client_group_id = models.IntegerField()
    primary_account_id = models.IntegerField(null=True, blank=True)
    primary_account_type = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255)
    id_code = models.CharField(max_length=255)
    contact_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    company_id = models.IntegerField()

    def __str__(self):
        return f'{self.company} | {self.first_name} {self.last_name}'
    

