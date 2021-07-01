import csv
import os
from pathlib import Path

home = str(Path.home())
path = os.path.join(home, "temp")
print("Working Directory: " + path)
suffix_array = ["jr", "sr", "ii", "iii", "iv", "v", "vi", "vii", "iix" "ix", "x", "esq", "esq."]
with open(os.path.join(path, "InfoSecEmployeesReport.csv"), newline='', encoding="utf8") as csvfile:
	reader = csv.DictReader(csvfile)

	with open("InfoSec_to_upload.csv", "w", newline='', encoding="utf8") as newcsv:
		fieldnames = ['first_name', 'last_name', 'email', 'group', 'title', 'department', 'phone', 'address1', 'address2', 'city', 'state', 'zip', 'country', 'custom', 'manager_name', 'manager_email', 'Infosec_IQ_start_date']
		writer = csv.DictWriter(newcsv, fieldnames = fieldnames)
		writer.writeheader()
		a = ''
		for row in reader:
			if row['Office Field'] == 'O': #distinct non-dynamic, static groups for office and field staff.
				group = 'Office Staff'
			if row['Office Field'] == 'F':
				group = 'Field Staff'

			#removes suffixes, like II, Jr., Sr., etc.
			if row['emp name'].split()[-1].lower() in suffix_array:
				last_name = row['emp name'].split()[-2]
				print("last name will be: " + last_name)
			else:
				last_name = row['emp name'].split()[-1]
			#variable "a" allows users with supervisors to have their email listed. Some users don't have supervisors. This if statement prevents users without supervisors from having just "@mcdean.com" as their supervisor email.
			if row['Primary Evaluator Username'] == '':
				a = ''
			else:
				a = '@mcdean.com'

			#ADDENDUM 3/3/2021 - DEAN | FLUOR should and will be included, below lines commented out
			#Dean/Fluor is a separate company that does not need to be enrolled in training.
			#if "@deanfluor.com".lower() in row['Emp Email'].lower():
			#	pass

			if "F".lower() in row["Office Field"].lower():
				pass
			## This removes any row with no email field, which means that the account is disabled. For some reason, most of the rows with no email field have 40 spaces instead of nothing (" ")
			if row['Emp Email'].strip(" ") == '':
				pass
			else:
				writer.writerow({'first_name': row['emp name'].split(' ', 1)[0],
						'last_name': last_name,
						'email': row['Emp Email'],
#						'email': row['emp_name'].split(' ', 1)[0]+"."+last_name+"@mcdean.com",
						'group': group, ##row['emp_division'],
						'title': row['EMP TITLE'],
						'department': row['emp dept'],
						'phone': '',
						'address1': '',
						'address2': '',
						'city': '',
						'state': '',
						'zip': '',
						'country': '',
						'custom': '',
						'manager_name': row['Primary Evaluator Username'][7:],
						'manager_email': row['Primary Evaluator Username'][7:].replace(" ",".")+a})
		

if os.path.exists(os.path.join(path, "InfoSec_to_upload.csv")):
	print("SUCCESS.")

	print("exlcude von, exclude la, le, de, da, etc., anything")
			