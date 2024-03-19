import os
import re

def extract_domain(line):
    # Use regular expression to extract the domain
    match = re.search(r'address=/([^/]+)/MY_IP_SERVER', line)
    if match:
        domain = match.group(1)
        # Remove whitespaces and any space from the domain
        domain = ''.join(domain.split())
        return domain
    else:
        return None


def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    domains = []
    for line in lines:
        domain = extract_domain(line)
        if domain:
            domains.append(domain)

    with open(output_file, 'w') as f:
        for domain in domains:
            f.write(f'address=/{domain}/MY_IP_SERVER\n')


# Function to modify lines
def modify_line(line, start_text, end_text):
    modified_line = start_text + line.strip().rstrip().lstrip() + end_text + '\n'
    return modified_line


# Input directory path
directory_path = './domains/domain-list-community-master/data'

# Text to add at the beginning and end of each line
start_text = "address=/."
end_text = "/MY_IP_SERVER"

# Output file path
output_file_path = './domains/domain-list-community-main/data/16merged_output.txt'

# String to be removed from each line
string_to_remove = "@cn"
string_to_remove3 = "@!cn"
string_to_remove2 = "@ads"

# Regex pattern to match domain lines
domain_pattern = re.compile(r'\b[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')

# Iterate through all files in the directory
with open(output_file_path, 'w') as output_file:
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            print("Reading file:", filename)  # Print the name of each file being read
            with open(file_path, 'r') as input_file:
                for line in input_file:
                    # Remove extra spaces and empty lines
                    cleaned_line = line.strip().lstrip().rstrip()
                    if cleaned_line:
                        # Filter out non-domain lines
                        if domain_pattern.match(cleaned_line):
                            # Modify line by removing the specified string
                            modified_line = modify_line(cleaned_line, start_text, end_text)
                            modified_line = modified_line.replace(string_to_remove, '')
                            modified_line = modified_line.replace(string_to_remove2, '')
                            modified_line = modified_line.replace(string_to_remove3, '')
                            output_file.write(modified_line)

p_input_file = "./domains/domain-list-community-main/data/16merged_output.txt"  # Change this to your input file name
p_output_file = "./domains/domain-list-community-main/data/166merged_output.txt"  # Change this to your output file name
process_file(p_input_file, p_output_file)

print("Merge and string removal completed!")
