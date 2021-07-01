import csv
import os
from pathlib import Path

home = str(Path.home())
path = os.path.join(home, "temp")
print("Working Directory: " + path)
persistent = []s

with open(os.path.join(path, "Admin_List2.csv"), newline='') as csvfile:
	one_reader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
	with open(os.path.join(path,"Admin_tmp_List2.csv"), newline='') as csvfile2:
		two_reader = csv.reader(csvfile2, delimiter=' ', quotechar = '|')
		


		with open(os.path.join(path,"local_admin_cumulative.csv"), "w", newline='') as newcsv:
			fieldnames = ['name', 'title', 'department', 'office', 'managerName', 'managerEmail']
			writer = csv.DictWriter(newcsv, fieldnames = fieldnames)
			writer.writeheader()
			for row in one_reader:
				for row2 in two_reader:
					if row['Name'] == row2['Name']:
						pass
					else:
						writer.writerow({'name': row['Name'],
							'title': row['Title'],
							'department': row['Department'],
							'office': row['Office'],
							'managerName': row['ManagerName'],
							'managerEmail': row['ManagerEmail']
							})
				

