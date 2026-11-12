
# Email Extraction using Python

import re

# Read text file
with open("emails.txt", "r") as file:
    text = file.read()

# Extract email addresses
emails = re.findall(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    text
)

# Display extracted emails
print("===== EMAIL EXTRACTION =====")

for email in emails:
    print(email)

# Save emails into output file
with open("output.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("----------------------------")
print("Total Emails:", len(emails))
print("Extraction Completed!")
print("Emails saved in output.txt")
