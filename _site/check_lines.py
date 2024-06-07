import os
import re

# Define the directory and pattern
directory = './_notes'
pattern = re.compile(r'- ---\n  ---', re.MULTILINE)

# Iterate through the files in the directory
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Remove all occurrences of the matched pattern
            new_content = pattern.sub('', content)
            
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
