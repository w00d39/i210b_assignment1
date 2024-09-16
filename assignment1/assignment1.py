def infer_type(value): #function to infer the type the variable is
    try: #it tries to first convert it into an int
        int(value)
        return int
    except ValueError: #if it cant int then it will try float
        try:
            float(value)
            return float
        except ValueError: #all else fails it will string
            return str

with open("pokemon_data.csv", "r") as file:  # Open the file in read mode
    # Read the contents of the file
    content = file.read()

# Split the content by lines
lines = content.splitlines()

# Split the first line to get the headers
headers = lines[0].split(',')

# Split the second line to get the first data row
first_data_row = lines[1].split(',')

# Infer the data types based on the first data row
data_types = [infer_type(value) for value in first_data_row]

# Print the variable names and their inferred data types
for header, data_type in zip(headers, data_types):
    print(f"{header} <class '{data_type.__name__}'>")