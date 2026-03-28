import os

# Step 1: Terminal setup (Make sure you are in week3_project folder)
filename = "database.txt"

print("--- Team Daily Status System ---")

# Step 2: Persistent creation (Write/Append)
# We ask the user for their blocker
user_blocker = input("What is your Daily Blocker? ")

# Use 'a' to add text without deleting the old information
with open(filename, "a") as file:
    file.write(user_blocker + "\n")
    print("Status saved!")

# Step 4: Error handling and logic
# Check if the file exists before reading
if os.path.exists(filename):
    print("\n--- Reading Daily Blockers ---")
    
    # Step 3: Data retrieval (Read)
    with open(filename, "r") as file:
        # Use a simple for loop to read the file
        for line in file:
            print("Blocker found: " + line.strip())
else:
    print("Warning: The file does not exist yet.")


"""
-------------------------------------------------------------------------
STEP 5: ENGLISH PRACTICE (Basic English)
-------------------------------------------------------------------------

Protocol selection:
1. I will reach out to the team via Slack because the issue is an immediate blocker.
2. I will send a clear and short message about the file error.
3. I will be courteous and wait for a reply from my teammates.

Vocabulary integration:
My script uses simple code to fetch information from a text file. 
I use 'Append' mode so I do not overwrite my old data. 
This is important for data persistence in my project. 
If I have a problem, I will reach out to the team for help.
"""
