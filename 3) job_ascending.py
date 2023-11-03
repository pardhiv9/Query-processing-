import pandas as pd
data = pd.read_csv("C:\\Users\\USER\\OneDrive\\Documents\\job_title_ascen.csv")
sorted_column = data.sort_values(by="JOB_TITLE",ascending=False)
print(sorted_column)

