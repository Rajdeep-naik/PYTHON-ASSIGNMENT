"""Assignment 1: Different Operations on Dictionary and Tuple Data Structure."""


def tuple_operations():
    print(f'{"=" * 110}')
    print(f"{"TUPLE OPERATIONS":^110}")
    print(f'{"=" * 110}')

    # 1. Creation
    my_tuple = (10, 20, 30, 40, 20)
    print(f"Original Tuple: {my_tuple}")

    # 2. Built-in Methods
    print(f"Count of 20: {my_tuple.count(20)}")
    print(f"Index of 30: {my_tuple.index(30)}")

    # 3. Appending via concatenation
    my_tuple = my_tuple + (50,)
    print(f"After Appending (50): {my_tuple}")

    # 4. Removing an element via list conversion
    temp_list = list(my_tuple)
    temp_list.remove(20)  # Removes first occurrence
    my_tuple = tuple(temp_list)
    print(f"After Removing 20: {my_tuple}")

    # 5. Slicing
    print(f"Sliced Elements (index 1 to 3): {my_tuple[1:4]}\n")


def dictionary_operations():
    print(f'{"=" * 110}')
    print(f"{"DICTIONARY OPERATIONS":^110}")
    print(f'{"=" * 110}')

    # 1. Creation
    student = {"id": 101, "name": "Aarav", "course": "B.Tech"}
    print(f"Original Dictionary: {student}")

    # 2.Adding elements
    student["semester"] = 4
    student.update({"city": "Pune", "grade": "A"})
    print(f"After Additions: {student}")

    # 3. Accessing Methods
    print(f"Keys: {list(student.keys())}")
    print(f"Values: {list(student.values())}")
    print(f"Value for 'name': {student.get('name')}")

    # 4. Removing elements
    removed_grade = student.pop("grade")
    print(f"Popped 'grade': {removed_grade}")

    del student["city"]
    print(f"After 'del student[\"city\"]': {student}\n")


if __name__ == "__main__":
    tuple_operations()
    dictionary_operations()