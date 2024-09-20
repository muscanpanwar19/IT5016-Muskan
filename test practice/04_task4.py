"""
Display of staff's basic information and total requisition
Author: Muskan
"""

def staff_info(unique_id=10000):
    date = input("Enter today's date:")
    staff_id = input("Enter your staff ID:")
    staff_name = input("Enter your name: ")


    requisition_id = unique_id + 1
    unique_id + requisition_id


    print(f"\npriniting staff information:")
    print(f"Date:{date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name : {staff_name} ")
    print(f"requisition ID: {requisition_id}")


    return unique_id

unique_id = 10000
staff_info = staff_info(unique_id)


def requisition_total():
    total_value  = 0
    while True:
        price_of_item = input("Enter each item name with a price(e.g., tea$20):")
        if price_of_item.lower() == 'finish':
            break
    
        try:
            item_name, price = price_of_item.rsplit(maxsplite=1)
            item_name = str(item_name)
            price = price.replace("$","")
            price = float(price)
            total_value += price


        except ValueError:
            print("invalid input. please follow the format (e.g., Tea $20):")
    return total_value



def requisition_approval(total_value,staff_id,reuisition_id):

    if total_value < 500:
        status = "Approved"
        Reference_Number = staff_id,requisition_id

    else:
        status + "Pending"

    print(f"Requistion Approval:")
    print(f"Total:${total_value:.2f}")
    print(F"Stauts:{status}")
    print(f"Approval Reference Number :{Reference_Number}")


    return status, Reference_Number


def display_requisitions(date,requisition_id,staff_name,total_value,status,reference_number):

    print(f"\nprinting Requisitions:")
    print(f"Date:{date}")
    print(f"Requisition ID:{requisition_id}")
    print(f"Staff name: {staff_name}")
    print(f"Toral:${total_value:.2f}")
    print(f"Status:{status}")
    print(f"Approval Reference Number:{reference_number}")


def main():
    unique_id = 10000
    date,requisition_id,staff_id,staff_name,unique_id = staff_info(unique_id)
    print(f"\nRequisition Items (type 'finish to end):")
    total_value = requisition_total()
    status,Reference_Number = requisition_approval(total_value,staff_id,requisition_id)
    display_requisitions(date,requisition_id,staff_name,total_value,status,Reference_Number)



main()

