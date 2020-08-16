import pandas as pd 

# Read csv data
data = pd.read_csv("/Users/hiroito/Documents/Python/Clean_emails/OWEB_Small_Grant_Teams.csv")
# Drop unsued columns
data.drop(columns=['Team','Organization','Phone','Location'], inplace=True)
# Drop empty email addresses
data.dropna(subset=['Email'], inplace=True)
# Search for addresses gmail or hotmail, .com or .ca
print(data[data['Email'].str.contains(r'^[A-Za-z0-9._%+-]+@(gmail|hotmail).(com|ca)$', regex=True)])




