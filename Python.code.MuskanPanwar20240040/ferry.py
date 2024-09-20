"""
ferry py
Author : Muskan
Whitecliffe college,AKL
"""

class BookingSysytem():
     unique_id_ticket = 20000   #global unique ID ticket


     def __init__(self):
        self.request = []  # List to store all requests

    

     def custumer_info(self):
        """collect basic custumer information."""
        form_of_id = input("Enter form_of_id:")
        return {"form_of_id : form_of_id"}


     def service_details(self):
        """collects service name and calculates total price to pay."""
        service_list = []
        total_value = 0
        while True:
            item = input("Enter item name(or 'done' to finish): ")
            if item.lower() =='done':
                break
            
            price = float(input (f"Enter price for{item}:"))
            service_list.append({"item": item, "price":price})
            total_price += price

        return total_price, service_list



     def generate_unique_id(self):
        """Generate a ticket ID and increment the global counter."""
        unique_id = ServiceRequst.unique_id_ticket+ 1
        ServiceRequest.unique_id_ticket += 1
        return unique_id


     def generate_approval_ID(self,form_of_id,unique_id):
        """Generate an approval reference number based on the last 3 cvharachters of the form of id and unique Id."""
        form_of_id_part = form_of_id[-3:] if len(form_of_id) >= 3 else form_of_id
        id_part = str(unique_id) [-3:]
        return f"{form_of_id_part}{id_part}"


     def ticket_approval(self, total_price):
        """Approve if total price < 0, else  mark as approved."""
        return "approved" if total_price > 0 else "approved"


     def submit_request(self):
        """Submit a new request."""
        custumer = self.custumer_info()
        total_price, service_list = self.request_details()
        status = self.request_approval(total_price)
        unique_id = self.generate_unique_id()
        approval_ref = self.generate_approval_ref(user["form_of_id"], unique_id)


        request = {
            "id": unique_id,
            "user":user,
            "service_list": service_list,
            "total": total_price,
            "status" : status,
            "approval_ID": approval_id
        }

        self.requests.append(request)
        print(f"Request submitted with ID{unique_id} and status '{status}'.")
        print(f"Approval ID number: {approval_id}")

     def display_request_neatly(self):
        """Prints all the requests neatly with headers."""
        print("\n===================")
        print("    All Request     ")
        print("=====================")
        if not self.requests:
            print("No requests have been submitted yet.")
        else:
            print(f"{'ID':<5}" {f'form_of_id':<1} {'Total price':<12} {'Status':<10} {'Approval id':<15})
            print("_"* 60)
            for req in self.requests:
                print(f"{req['id']} ${req['user'][form_of_id]:<15}"{req['total']:<12})
                print("=================")

     def display_request_details(self_request_id):
        """Prints the details of a speicfic request."""
        for req in self.requests:
            if req['id'] == request_id:
                print("\n=====================")
                print("     Request Details     ")
                print("===================")
                print(f"ID: {req[ 'id']}")
                print(f"form_of_id: {req['user']['form_of_id']}")
                print("Items:")
                for service_list in req['service_list']:
                    print(f"- {item['item']}:${item['cost']:.2f}")
                    print(f"Status: {req['total']:.2f}")
                    print(f"Approval ID: {rew['approva_id']}")
                    print("=============================")
                    return


                print("Request not found.")


      #main program
    def main():
        system = RequestSystem()

        while True:
            choice = input("\n1. Submit Request\n2. Display Requests\n3. Display Request Details\n4. Exit\nChose an option:")
            if choice == "1"
                system.submit_request()
            elif choice == "2":
                system.display_requests_neatly()
            elif choice == "3":
                request_id = int(input("Enter the request ID:"))"
                system.display_request_details(request_id)

            elif choice == "4":
                break
            else:
                print("Invalid option. Try again.")


    if __name__ =="__main__":
        main()
        
        


    
            




            

    
    




