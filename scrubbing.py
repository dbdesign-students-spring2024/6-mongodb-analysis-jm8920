import csv

def scrub_data(input_file_path, output_file_path):
    columns_to_remove = ['picture_url']
    columns_to_remove.append('description')
    
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = None
        
        for row in reader:
            # Initialize writer with adjusted headers on the first row
            if writer is None:
                headers = [key.replace('★', '*') for key in row.keys() if key not in columns_to_remove]
                writer = csv.DictWriter(outfile, fieldnames=headers)
                writer.writeheader()
            
            # Replace ★ with * in all fields
            adjusted_row = {key.replace('★', '*'): value.replace('★', '*') for key, value in row.items() if key not in columns_to_remove}
            
            writer.writerow(adjusted_row)

# File paths
input_file_path = 'data/listings.csv'
output_file_path = 'data/listings_clean.csv'

scrub_data(input_file_path, output_file_path)

output_file_path
