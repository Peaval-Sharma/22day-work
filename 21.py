import json

# JSON file read karna
filename = input("Enter JSON file name: ")

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print("\n--- JSON Data Processor ---")

    # Display all records
    print("\nAll Records:")
    for item in data:
        print(item)

    # Search
    search = input("\nEnter name to search: ").lower()

    found = False

    for item in data:
        if search in item["name"].lower():
            print("\nRecord Found:")
            print(item)
            found = True

    if not found:
        print("No record found.")

    # Filtering
    print("\n--- Filtering ---")

    for item in data:
        if "salary" in item and item["salary"] > 30000:
            print("Salary greater than 30000:", item)

    # Summary
    print("\n--- Summary ---")

    total_records = len(data)
    print("Total Records:", total_records)

    if total_records > 0 and "salary" in data[0]:
        total_salary = sum(item["salary"] for item in data)
        average_salary = total_salary / total_records

        print("Total Salary:", total_salary)
        print("Average Salary:", average_salary)

except FileNotFoundError:
    print("File not found.")

except json.JSONDecodeError:
    print("Invalid JSON file.")

except KeyError:
    print("Required key is missing.")

except Exception as e:
    print("Error:", e)