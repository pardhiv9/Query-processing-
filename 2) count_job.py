import pandas as pd
data = pd.read_csv("C:\\Users\\USER\\OneDrive\\Documents\\employee.csv")
em_id = list(data['EMPLOYEE_ID'])
unique_id = sorted(set(em_id))
print("employee_id   jobsCount")
for i in unique_id:
    if(em_id.count(i)>1):
        print(i,"\t\t",em_id.count(i))
        
    
