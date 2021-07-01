import csv
import os
from pathlib import Path

home = str(Path.home())
path = os.path.join(home, "temp")
print("working directory = " + path)


    

with open("2020_hires_formatted.csv", "w", newline='\n') as newfile:
    writer = csv.writer(newfile)
    with open(os.path.join(path, "2020_Hires.csv"), newline = '\n') as csvfile:
        reader = csv.reader(csvfile, delimiter='\n', skipinitialspace=True, quoting=csv.QUOTE_NONE)



        for row in reader:
#            row = str(row).replace(" ", "")
#            row = (str(row).replace("\n", ","))
            print(str(row).replace(" ",""))
            writer.writerow(str(row).replace(" ", ""))
        

            