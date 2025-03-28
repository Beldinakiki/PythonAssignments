try:
    # Read the contents of input.txt
    with open("input.txt", 'r') as file:
        data = file.read()

    # Count the number of words in the file
    word_count = len(data.split())

    # Convert all text to uppercase
    processed_text = data.upper()

    # Write the processed text and word count to output.txt
    with open("output.txt", 'w') as output_file:
        output_file.write(processed_text)
        output_file.write(f"\n\nWord Count: {word_count}")

    # Print a success message
    print("The file has been processed and saved as 'output.txt' successfully.")

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")