import sys

def generate_markdown_table(rows, columns, insert_content):
    # Prompt for table header names
    headers = []
    for col in range(1, columns + 1):
        header = input(f"Enter the name for Column {col}: ")
        headers.append(header)

    # Initialize an empty table with custom headers
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---" for _ in range(columns)]) + " |\n"

    if not insert_content:
        # Generate the specified number of rows with empty cells
        for row in range(1, rows + 1):
            empty_cells = [" " for _ in range(columns)]
            markdown_table += "| " + " | ".join(empty_cells) + " |\n"

    return markdown_table, headers

def append_content_to_table(file, values):
    with open(file, "a") as f:
        # Append each row separately
        f.write("| " + " | ".join(values) + " |\n")

if __name__ == "__main__":
    # Get the number of rows and columns from the command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python generate.py <output_filename> <num_rows> <num_columns>")
        sys.exit(1)

    output_filename = sys.argv[1]
    rows = int(sys.argv[2])
    columns = int(sys.argv[3])

    # Prompt for content insertion
    insert_content = input("Do you want to insert content into the table? (yes/no): ").lower() == 'yes'

    # Generate the markdown table and get headers
    markdown_table, headers = generate_markdown_table(rows, columns, insert_content)

    # Append the markdown table to the specified output file
    with open(output_filename, "a") as f:
        f.write("\n" + markdown_table)

    print(f"Markdown table structure generated and saved to {output_filename}")

    if insert_content:
        # Prompt for content insertion based on custom headers
        for row in range(1, rows + 1):
            values = []
            for col in range(1, columns + 1):
                value = input(f"Enter value for Row {row}, Column {col} ({headers[col-1]}): ")
                values.append(value)
            # Append each row separately
            append_content_to_table(output_filename, values)

        print(f"Content inserted and saved to {output_filename}")
    else:
        # If no content insertion, print a message
        print(f"Table structure without content insertion saved to {output_filename}")
