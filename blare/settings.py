from dotenv import dotenv_values

env = dotenv_values(".env")

blesta_usr = env['BLESTA_USR']
blesta_key = env['BLESTA_KEY']

blesta_url = env['BLESTA_URL']
blesta_format = env['BLESTA_FORMAT']

# Model variable

service_client_id = env['CLIENT_ID']
service_package_id = env['PACKAGE_ID']
