# Scenario 1: Data ValidationTask: 
# Write a function validate_data(data) that checks if a list of dictionaries 
# (e.g., [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}])
#  contains valid integer values for the "age" key. Return a list of invalid entries.


def validate_data(data):
    invalid_list = []
    for item in data:
        if not isinstance(item.get("age"), int):
            invalid_list.append(item)
    return invalid_list


data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}]
print(validate_data(data))
