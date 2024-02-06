

import csv

with open("organizations-100.csv", "r") as orgs_csv:    
   
    orgs_reader = csv.DictReader(orgs_csv)
    sorted_lst = sorted(orgs_reader, key=lambda row:int(row["Number of employees"]), reverse=False)


with open('sorted_csv.csv', 'w', newline='') as sorted_csv:
    headers = ["Index","Organization Id","Name","Website","Country","Description","Founded","Industry","Number of employees"]
    
    writer = csv.DictWriter(sorted_csv, fieldnames=headers)
    writer.writeheader()
    for row in sorted_lst:
        writer.writerow(row)
