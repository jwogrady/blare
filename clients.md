````shell
getAll( string $status = null, integer $client_group_id = null )
Fetches all clients

Parameters
$status
The status type of the clients to fetch ('active', 'inactive', 'fraud', default null for all)

$client_group_id
The ID of the client group whose clients to fetch (optional, default null for all)
Returns
array
An array of stdClass objects representing each client, or false if no results]\

"response": [
    {
      "id": "1",
      "id_format": "{num}",
      "id_value": "1500",
      "user_id": "2",
      "client_group_id": "1",
      "primary_account_id": null,
      "primary_account_type": null,
      "status": "active",
      "id_code": "1500",
      "contact_id": "1",
      "first_name": "John",
      "last_name": "O'Grady",
      "company": "Status26 Inc.",
      "email": "john@status26.com",
      "address1": "PO BOX 608",
      "address2": "",
      "city": "Denton",
      "state": "TX",
      "zip": "76202",
      "country": "US",
      "group_name": "Status26",
      "company_id": "1"
    },
````