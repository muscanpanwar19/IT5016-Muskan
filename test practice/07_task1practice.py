"""
collecting user information
Author : Muskan
"""

def staff_info(unique_id = 10000):
    date = input("Enter toady's date:")
    staff_id = input("Enter your staff ID:")
    staff_name = input("Enter your name:")


    requistion_id = unique_id + 1
    unique_id + requisition_id


    print(f"\nprinting staff information:")
    print(f"Date:{date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name : {staff_name}")
    print(f"requistion ID: {requistion_id}")


    return unique_id

unique_id = 10000
staff_info = staff_info(unique_id)
    
