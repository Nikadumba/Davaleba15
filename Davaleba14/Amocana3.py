

import csv

with open("organizations-100.csv", "r") as orgs_csv:    
   
    orgs_reader = csv.DictReader(orgs_csv)
    ssl_comps = [row for row in orgs_reader if row["Website"][4] == "s"]


with open("ssl_companies.csv", "w", newline='') as ssl_csv:    
       
        headers = ["Organization Id","Name","Website","Industry","Number of employees"]
        
        writer = csv.DictWriter(ssl_csv, fieldnames=headers)    
        writer.writeheader()

        for r in ssl_comps:
            del r["Index"]
            del r["Country"]
            del r["Description"]
            del r["Founded"]
            writer.writerow(r)