# Error Handling Assignment
# Power Learn Project - Python

def read_file_with_error_handling(filename):
    """Reads a file and handles errors gracefully."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n✅ File content:\n")
            print(content)

    except FileNotFoundError:
        print("❌ Error: The file you entered does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Main program
if __name__ == "__main__":
    filename = input("Enter the name of the file to open: ")
    read_file_with_error_handling(filename)