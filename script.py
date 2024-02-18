import os
from collections import Counter
import socket
import re

# Function to count words in a file and find the top 3 most common words
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the file, convert to lowercase, and remove non-alphanumeric characters
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_count = re.findall(r"[\w']+", text)
        top_three_words = Counter(words).most_common(3)
    return len(word_count), top_three_words

# Define directories
data_dir = "/app/home/data"
output_dir = "/app/home/output"
output_file_path = os.path.join(output_dir, "result1.txt")

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# List text files and process each file
files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
total_words = 0
results = []

for filename in files:
    file_path = os.path.join(data_dir, filename)
    word_count, top_three_words = process_file(file_path)
    total_words += word_count
    results.append(f"{filename}: {word_count} words")
    if filename.lower() == "if.txt":
        top_words_info = "\n".join([f"{word}: {count}" for word, count in top_three_words])
        results.append(f"Top 3 words in IF.txt:\n{top_words_info}")

# Get the IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Write the results to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write("List of text files:\n" + "\n".join(files) + "\n\n")
    output_file.write("\n".join(results) + "\n")
    output_file.write(f"Grand Total: {total_words} words\n")
    output_file.write(f"IP Address: {ip_address}\n")

# Print the contents of the result file
with open(output_file_path, 'r') as output_file:
    print(output_file.read())
