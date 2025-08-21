# File Handling Assignment
# Power Learn Project - Python

def read_and_write_file(filename):
    """Reads a file and writes a modified version to a new file."""
    try:
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ File has been read successfully!")
        print(f"✅ Modified content has been saved to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file you entered was not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Main program
if __name__ == "__main__":
    filename = input("Enter the name of the file to read: ")
    read_and_write_file(filename)