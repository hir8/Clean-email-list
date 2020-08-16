import pandas as pd 

# Read csv data
data = pd.read_csv("your csv path")
# Drop unsued columns
data.drop(columns=['Team','Organization','Phone','Location'], inplace=True)
# Drop empty email addresses
data.dropna(subset=['Email'], inplace=True)
# Search for addresses gmail or hotmail, .com or .ca
# Change it to match your desired email address
print(data[data['Email'].str.contains(r'^[A-Za-z0-9._%+-]+@(gmail|hotmail).(com|ca)$', regex=True)])




