# Importing necessary modules
import sys  # Provides access to system-specific parameters and functions
import datetime  # For displaying the current date and time

def main():
    print("Hello, World!")  # Printing the message
    print(f"Current Date and Time: {datetime.datetime.now()}")  # Displaying current date and time
    print(f"Python Version: {sys.version}")  # Displaying Python version

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    main()
