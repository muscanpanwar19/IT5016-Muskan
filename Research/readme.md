                                                     **** Booking System Program ****
Author: Muskan

                                                                     Overview

The Booking System is a command-line application that allows users to submit service requests, manage customer information, and display request details. The application generates unique IDs for each request and provides an approval ID based on customer input. The design focuses on simplicity and usability, making it easy to manage service requests.

                                                                    Features

Submit Requests: Collects customer information and service details.
Display Requests: Lists all submitted requests with relevant details.
Display Request Details: Shows detailed information about a specific request.
Unique ID Generation: Automatically generates unique IDs for each request.

                                                                Code Structure

The code consists of a single class, BookingSystem, which encapsulates all functionality related to managing booking requests. The methods are designed to handle different tasks, such as collecting customer information, calculating total prices, and generating unique identifiers.

                                                                 Key Methods

customer_info(): Gathers customer identification details.
service_details(): Collects service names and prices, calculating the total amount.
generate_unique_id(): Creates a unique ticket ID for each request.
generate_approval_id(): Generates an approval ID based on customer input and unique ID.
ticket_approval(): Determines if a request is approved based on total price.
submit_request(): Combines the previous methods to submit a new service request.
display_requests_neatly(): Displays all submitted requests in a structured format.
display_request_details(): Provides detailed information for a specific request.

                                                           Software Design Principles

1. DRY (Don't Repeat Yourself)
The DRY principle is about minimizing the repetition of software patterns. In the BookingSystem class, each method has a single responsibility, which avoids code duplication. For instance, the generate_unique_id method is used wherever a unique ID is needed, ensuring that changes to ID generation logic need to be made in one place only.

2. SOLID Principles
The SOLID principles are a set of design principles aimed at making software designs more understandable, flexible, and maintainable.

Single Responsibility Principle (SRP): Each method in the BookingSystem class has a distinct purpose. For example, customer_info() only collects customer data, while service_details() focuses on service information.

Open/Closed Principle (OCP): The class is designed to be open for extension (e.g., adding new service types) but closed for modification. New features can be added by introducing new methods without altering existing code.