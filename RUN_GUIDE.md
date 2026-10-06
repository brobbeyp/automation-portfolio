Ticket Classification Program
Description: 
    This program accepts a JSON array, a list of  dictionaries, and outputs a resulting list that includes each ticket's ID and classification
Author: 
    Peter, Date: 10.5.26
Input:
    JSON array that becomes a Python list of dictionaries. Each ticket requires a string id and string message; IDs must be unique.
Rules:
    Tickets must have a unique "id". Urgent requires the exact whitespace-separated word outage; outages and outage! are normal. Empty or whitespace-only messages are invalid. Tickets with anything else are considered "normal". Capitalization and whitespace handling apply to message classification; field names remain case-sensitive.
Run Instructions:
    from a Powershell window, run: "python session_07.py". Must be run from the same folder as the loaded tickets.json file. 
Output: 
    A successful run will output the classified tickets in a new file, it will create a report file called "ticket_report.json", and then it will run validation tests to verify each of the tests works.
Failure Behavior:
    Initially, tickets are validated to make sure they do not have duplicate "id" , they contain all required fields (such as "id" and "message"), and that the top-level input is a list, and each item is a dictionary. The required fields are checked to make sure they are the proper type. When an invalid ticket is input, the function raises a ValueError that includes a short description of the error. If a report already exists in the working directory, a FileExistsError is raised. The handler prints an error message to the user and the existing file is not edited. 
Scope and limitation:
    This is a learning project using fictional ticket data. The program requires manual intervention if the user wants to run it multiple times in the same directory. After the first run, subsequent runs will produce a FileExistsError until the user deletes "ticket_report.json" or moves it.


