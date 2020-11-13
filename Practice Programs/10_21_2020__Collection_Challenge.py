# PROGRAM NAME: 10_21_2020__Collection_Challenge.py
# PROGRAM PURPOSE: To practice lists
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-21-2020
# PYTHON VER. USED: 3.8

# starting list
collection = [3.14159, "Ahoy", True, 42, -1000, "Mmmmmm, ice cream"]
print("starting collection:",collection)

## Fixing list to requested list...
collection.remove(-1000)
collection.remove("Mmmmmm, ice cream")
collection.append("Second")
collection.append("Cookies")
collection.reverse()
					  
# Print out the final list 
print("   final collection:",collection)
