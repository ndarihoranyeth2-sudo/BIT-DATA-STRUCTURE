# Village Savings Group Integers
group_counts = [15, 20, 12, 18, 25, 17]
total_members = sum(group_counts)
average_members = total_members / len(group_counts)
min_members = min(group_counts)
max_members = max(group_counts)

# Strings: Formatted report with f-strings
report = (
    f"Village Savings Group Report\n"
    f"Total Members Across Groups: {total_members}\n"
    f"Average Members per Group: {average_members:.2f}\n"
    f"Minimum Group Size: {min_members}\n"
    f"Maximum Group Size: {max_members}\n"
)

print(report)

# Booleans: Apply threshold condition and compound boolean
threshold = 16
status = ""
if average_members > threshold and max_members > 20:
    status = "Above Standard"
else:
    status = "Below Standard"
print(f"Group Status: {status}")

# Lists: Maintain and modify a list of group names
group_names = ["Sunrise", "Unity", "Hope", "Progress", "Trust"]
print(f"Original group names: {group_names}")

# Add a new group
group_names.append("Empowerment")

# Remove a group whose name starts with 'H'
group_names = [name for name in group_names if not name.startswith("H")]

# Sort the list
group_names.sort()
print(f"Modified and sorted group names: {group_names}")

# Arrays: Use Python's array module
import array

# Select a fixed-size subset: e.g., top 3 group counts
group_counts_subset = group_counts[:3]
group_array = array.array('i', group_counts_subset)
array_sum = sum(group_array)
list_sum = sum(group_counts_subset)
print(f"Sum of array values: {array_sum}, compared to list sum: {list_sum}")

# Dictionaries: List of group records
group_records = [
    {"id": 1, "name": "Sunrise", "value": 15},
    {"id": 2, "name": "Unity", "value": 20},
    {"id": 3, "name": "Hope", "value": 12},
    {"id": 4, "name": "Progress", "value": 18}
]

# Update one record (change 'value' for 'Unity')
for record in group_records:
    if record["name"] == "Unity":
        record["value"] = 22

# Delete a record with id == 3
group_records = [rec for rec in group_records if rec["id"] != 3]

# Compute total of 'value' field
total_value = sum(rec["value"] for rec in group_records)
print(f"Total value across remaining group records: {total_value}")
