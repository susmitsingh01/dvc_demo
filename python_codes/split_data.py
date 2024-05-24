import pandas as pd

# Load the data and have a look at it
file_path = '/Users/susmitsingh/Susmit_Singh/python_codes/dvc_demo/data/Airline_customer_satisfaction.csv'
data = pd.read_csv(file_path)

# Step 1: Calculate the starting index for the last 50 percent
total_rows = len(data)
start_index = total_rows // 2

# Step 2: Read the CSV file from the start_index onward
data_last_50_percent = pd.read_csv(file_path, skiprows=range(1, start_index + 1))

# Step 3: Save the last 50 percent data to a new CSV file
output_file_path = '/Users/susmitsingh/Susmit_Singh/python_codes/dvc_demo/data/half_data.csv'
data_last_50_percent.to_csv(output_file_path, index=False)

# Display confirmation message
print(f"The last 50 percent of the data has been saved to {output_file_path}")