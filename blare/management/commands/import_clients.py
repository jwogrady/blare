import os
import requests
from django.core.management.base import BaseCommand
from blare.models.client import Client
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth

class Command(BaseCommand):
    help = 'Import clients from a JSON API with basic authentication'

    def handle(self, *args, **kwargs):
        """
        Handles the command to import clients from an API into the Client model.

        This method fetches data from an API using the provided API URL, username, and API key.
        It then imports the fetched data into the Client model by creating Client objects.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        # Load environment variables from the .env file

        env = dotenv_values(".env")

        # Get the API URL and credentials from the environment variables
        api_url = env['BLESTA_URL']
        api_username = env['BLESTA_USR']
        api_key = env['BLESTA_KEY']

        model = "clients"
        action = "getAll.json"

        url_parts = [api_url, model, action]

        api_url = "/".join(url_parts)

        if not api_url or not api_username or not api_key:
            self.stdout.write(self.style.ERROR('API_URL, API_USERNAME, and API_KEY environment variables must be set'))
            return
        
        print(api_url)

        # Fetch data from the API with basic authentication
        response = requests.get(api_url, auth=HTTPBasicAuth(api_username, api_key))
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {response.status_code}'))
            return

        data = response.json()

        # Import data into the Client model
        for item in data['response']:
            Client.objects.create(
                id_format=item['id_format'],
                id_value=item['id_value'],
                user_id=item['user_id'],
                client_group_id=item['client_group_id'],
                primary_account_id=item.get('primary_account_id'),
                primary_account_type=item.get('primary_account_type'),
                status=item['status'],
                id_code=item['id_code'],
                contact_id=item['contact_id'],
                first_name=item['first_name'],
                last_name=item['last_name'],
                company=item['company'],
                email=item['email'],
                address1=item['address1'],
                address2=item.get('address2', ''),
                city=item['city'],
                state=item['state'],
                zip=item['zip'],
                country=item['country'],
                group_name=item['group_name'],
                company_id=item['company_id'],
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))