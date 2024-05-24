import pandas as pd

# Step 1: Read the original CSV file
file_path_1 = '/Users/susmitsingh/Susmit_Singh/python_codes/dvc_demo/data/Airline_customer_satisfaction.csv'

df1 = pd.read_csv(file_path_1)

# Step 2: Read the smaller CSV file
file_path_2 = '/Users/susmitsingh/Susmit_Singh/python_codes/dvc_demo/data/half_data.csv'
df2 = pd.read_csv(file_path_2)

# Step 3: Append the second DataFrame to the first DataFrame
df_combined = pd.concat([df1, df2])

# Step 4: Save the combined DataFrame to a new CSV file
output_file_path = '/Users/susmitsingh/Susmit_Singh/python_codes/dvc_demo/data/merged_1.csv'
df_combined.to_csv(output_file_path)

# Step 5: Display the first few rows of the combined DataFrame
df_combined.head()