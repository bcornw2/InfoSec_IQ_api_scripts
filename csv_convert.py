import csv
import os
from pathlib import Path

home = str(Path.home())
path = os.path.join(home, "temp")
print("working directory = " + path)
new_hires = []
with open(os.path.join(path, "All__org_Users.csv"), newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    with open(os.path.join(path, "2020_Hires_formatted.txt"), "r") as f:
        new_hires = f.read()
        new_hires = new_hires.split("\n")
        new_hires = list(filter(None, new_hires))


#        print(str(new_hires))
    with open('org_infosec.csv', 'w', newline='') as newcsv:
        fieldnames = ['first_name', 'last_name', 'email', 'group', 'title', 'department', 'phone', 'address1', 'address2', 'city', 'state', 'zip', 'country', 'custom', 'manager_name', 'manager_email', 'Infosec_IQ_start_date']
        writer = csv.DictWriter(newcsv, fieldnames = fieldnames)
        writer.writeheader()
        print(len(new_hires))
        for row in reader:
            if 'O' in row['OfficeField']:
#                print('le')
                if(row['mail'] in new_hires):
                    print(row['mail'])
                    writer.writerow({'first_name': row['givenName'], 
				    'last_name': row['sn'],
				    'email': row['mail'],
                                    'group': row['company'], 
				    'title': row['title'],
				    'department': row['department'],
				    'phone': '',
				    'address1': '',
				    'address2': '',
				    'city': '',
				    'state': '',
				    'zip': '',
				    'country': '',
				    'custom': '',
				    'manager_name': row['manager'],
				    'manager_email': row['managerEmail']})

if os.path.exists(os.path.join(path, "mcd_infosec.csv")):
    print("CSV has been converted successfully. Please find it in: " + path)
