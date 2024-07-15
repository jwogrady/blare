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
    

class packageName(models.Model):
    lang = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class packageDescription(models.Model):
    lang = models.CharField(max_length=10)
    html = models.TextField(blank=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.html

class Package(models.Model):
    id_format = models.CharField(max_length=255)
    id_value = models.CharField(max_length=255)
    id_code = models.CharField(max_length=255)
    module_id = models.IntegerField()
    name = models.CharField(max_length=255)
    qty = models.IntegerField(null=True, blank=True)
    client_qty = models.IntegerField(null=True, blank=True)
    module_row = models.IntegerField()
    module_group = models.IntegerField(null=True, blank=True)
    module_group_client = models.IntegerField()
    taxable = models.BooleanField()
    single_term = models.BooleanField()
    status = models.CharField(max_length=255)
    hidden = models.BooleanField()
    company_id = models.IntegerField()
    prorata_day = models.IntegerField(null=True, blank=True)
    prorata_cutoff = models.IntegerField(null=True, blank=True)
    upgrades_use_renewal = models.BooleanField()
    manual_activation = models.BooleanField()
    override_price = models.BooleanField()
    module_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)

    names = models.ManyToManyField(packageName, related_name='packages')
    descriptions = models.ManyToManyField(packageDescription, related_name='packages')

    def __str__(self):
        return self.name