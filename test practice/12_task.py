"""
calculating requisition total
Auhtor : Muskan
"""

def requisition_total():
    total_value = 0
    while True:
        price_of_item = ("Enter each item name with a prace(e.g., tea$20):")
        if price_of_item.lower() == 'finish':
            break

        try:
            item_name,price = price_of_item.rsplit(maxsplite=1)
            item_name = str(item_name)
            price = price.replace("$","")
            price = float(price)
            total_value += price


        except ValueError:
            print("invalid input. please follow the format (e.g., Tea $20):")

    return total_value


def main():
    print(f"\nRequisition Items ( type 'finish' to end):")
    total_value = requisition_total()

    if not total_value:
        print("Invalid")

    else:
        print(f"Requisition Total\n${total_value:.2f}")


main()