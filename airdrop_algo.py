import csv

# Function to split the addresses into multiple files for ThirdWeb, as the dashboard currently only let's you airdrop to 250 addresses. This will create separate .csv files ready for separate airdrops.
def split_addresses(input_file, output_prefix, quantity, chunk_size=250):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        addresses = list(reader)
        
    # Add the quantity to each address
    modified_addresses = [[address[0], quantity] for address in addresses]
    
    # Split into chunks and write to separate files
    for i in range(0, len(modified_addresses), chunk_size):
        chunk = modified_addresses[i:i + chunk_size]
        output_file = f"{output_prefix}_{i//chunk_size + 1}.csv"
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["address", "quantity"])  # Write header
            writer.writerows(chunk)

# Usage
split_addresses('addresses.csv', 'output_addresses', 1000)
