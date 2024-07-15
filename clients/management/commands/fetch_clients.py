import requests
from django.core.management.base import BaseCommand
from clients.models import Client


class Command(BaseCommand):
    help = 'Fetch clients from external API and save to database'

    def handle(self, *args, **kwargs):

        url = ""
        payload = {}
        headers = {
        'Authorization': '',
        'Cookie': ''
        }

        response = requests.request("GET", url, headers=headers, data=payload)


        if response.status_code == 200:
            data = response.json()
            for item in data['response']:
                client, created = Client.objects.update_or_create(
                    id=item['id'],
                    defaults={
                        'id_format': item['id_format'],
                        'id_value': item['id_value'],
                        'user_id': item['user_id'],
                        'client_group_id': item['client_group_id'],
                        'primary_account_id': item.get('primary_account_id'),
                        'primary_account_type': item.get('primary_account_type'),
                        'status': item['status'],
                        'id_code': item['id_code'],
                        'contact_id': item['contact_id'],
                        'first_name': item['first_name'],
                        'last_name': item['last_name'],
                        'company': item['company'],
                        'email': item['email'],
                        'address1': item['address1'],
                        'address2': item.get('address2', ''),
                        'city': item['city'],
                        'state': item['state'],
                        'zip': item['zip'],
                        'country': item['country'],
                        'group_name': item['group_name'],
                        'company_id': item['company_id'],
                    }
                )
                print(client)