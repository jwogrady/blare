
"""

getAll( integer $company_id, array $order = ['name' => 'ASC'], string $status = null, string $type = null, array $filters = [] )
Fetch all packages belonging to the given company

Parameters
$company_id
The ID of the company to fetch pages for
$order
The sort order in key = value order, where 'key' is the field to sort on and 'value' is the order to sort (asc or desc)

$status
The status type of packages to retrieve ('active', 'inactive', 'restricted', default null for all)

$type
The type of packages to retrieve ('standard', 'addon', default null for all)
$filters
A list of package filters including:

status The status type of packages to retrieve ('active', 'inactive', 'restricted', default null for all)
name The name or part of the name of the packages to fetch
module_id The module ID to filter packages on
hidden Whether or nor to include the hidden packages
Returns
array
An array of stdClass objects each representing a package

#getList( integer $company_id, integer $page = 1, array $order_by = ['name' => 'ASC'] )
Fetches a list of all client groups

Parameters
$company_id
The company ID
$page
The page to return results for (optional, default 1)
$order_by
The sort and order conditions (e.g. array('sort_field'=>"ASC"), optional)
Returns
mixed
An array of objects or false if no results.
"""


from blare import load_json, dump_json
from blare.api import packages_getall, packages_getlist


resp = packages_getall(company_id=1, order={'name': 'ASC'})

print(resp.url)

list = []

r = load_json(resp.content)
for x in r['response']:
    list.append([x['id']])

data = dump_json(r)
print(data, file=open('output/packages.json', 'w'))
print(data)

print(80 * "-")

print(*list, sep="\n")
print(80 * "-")
print(f"Count: {len(list)}")
