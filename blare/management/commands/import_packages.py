import os
import requests
from django.core.management.base import BaseCommand
from blare.models.package import Package, packageName, packageDescription
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth

class Command(BaseCommand):
    help = 'Import clients from a JSON API with basic authentication'

    def handle(self, *args, **kwargs):
        # Load environment variables from the .env file

        env = dotenv_values(".env")

        # Get the API URL and credentials from the environment variables
        api_url = env['BLESTA_URL']
        api_username = env['BLESTA_USR']
        api_key = env['BLESTA_KEY']

        model = "packages"
        action = "getList.json"

        url_parts = [api_url, model, action]

        api_url = "/".join(url_parts)

        print(api_url)

        if not api_url or not api_username or not api_key:
            self.stdout.write(self.style.ERROR('API_URL, API_USERNAME, and API_KEY environment variables must be set'))
            return

        # Fetch data from the API with basic authentication
        response = requests.get(api_url, auth=HTTPBasicAuth(api_username, api_key))
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data: {response.status_code}'))
            return

        data = response.json()

        # Import data into the Client model
        for item in data['response']:
            package = Package.objects.create(
                id_format=item['id_format'],
                id_value=item['id_value'],
                id_code=item['id_code'],
                module_id=item['module_id'],
                name=item['name'],
                qty=item.get('qty'),
                client_qty=item.get('client_qty'),
                module_row=item['module_row'],
                module_group=item['module_group'],
                module_group_client=item['module_group_client'],
                taxable=item['taxable'] == "1",
                single_term=item['single_term'] == "0",
                status=item['status'],
                hidden=item['hidden'] == "0",
                company_id=item['company_id'],
                prorata_day=item.get('prorata_day'),
                prorata_cutoff=item.get('prorata_cutoff'),
                upgrades_use_renewal=item['upgrades_use_renewal'] == "1",
                manual_activation=item['manual_activation'] == "0",
                override_price=item['override_price'] == "0",
                module_name=item['module_name'],
                description=item['description'],
                description_html=item['description_html'],
            )

            for name_data in item['names']:
                name, created = packageName.objects.get_or_create(
                    lang=name_data['lang'],
                    name=name_data['name']
                )
                package.names.add(name)

            for desc_data in item['descriptions']:
                description, created = packageDescription.objects.get_or_create(
                    lang=desc_data['lang'],
                    html=desc_data['html'],
                    text=desc_data['text']
                )
                package.descriptions.add(description)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))