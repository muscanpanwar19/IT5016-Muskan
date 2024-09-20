"""
Requisition Approval Decision Based On Conditions
Author : Muskan
"""

def requisition_approval(total_value,staff_id,requisition_id):

    if total_value < 500:
        status = "Approved"
        Reference_Number = staff_id,requisition_id


    else:
        stautus + "Pending"


    print(f"Requisition Approval:")
    print(f"Total:${total_value:.2f}")
    print(F"Status:{status}")
    print(f"Approval Reference Number :{Reference_Number}")


    return status, Reference_Number


staff_id = input("Enter Staff ID:")
requisition_id = input(f"Enter REquisition ID:")
total_value = float(input("Enter Total:"))
requisition_approval(total_value,staff_id,requisition_id)


