from django.db import models

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
        return f"{self.name} | {self.module_name}"