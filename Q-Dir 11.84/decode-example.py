import base64

# Read the Base64 content from the .txt file
with open("encoded_file.txt", "r") as file:
    base64_content = file.read()

# Decode the Base64 content
decoded_data = base64.b64decode(base64_content)

# Write the decoded content to a .zip file
with open("output_file.zip", "wb") as zip_file:
    zip_file.write(decoded_data)

print("Decoded zip file saved successfully.")
