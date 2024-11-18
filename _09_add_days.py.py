import os

# Initialize a counter to keep track of the index
counter = 1

# Get the list of all files in the current directory
for filename in os.listdir():
    if filename.endswith(".txt"):
        # Create the new filename with the index and .py extension
        new_filename = filename.replace(".txt", f"_{counter:02d}.py")
        os.rename(filename, new_filename)
        
        # Increment the counter for the next file
        counter += 1

print("Files renamed successfully!")
