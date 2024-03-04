import sys

clients = [
    {
        "name": "Mizraim Medina",
        "company": "Google",
        "email": "jomizraim47@gmail.com",
        "position": "Back-End Developer"
    }
]

def create_client(client):
    global clients
    if(client not in clients):
        clients.append(client)
    else:
        print("Client already is in the client\'s list")
        

def list_clients():
    for index, client in enumerate(clients):
        print("{}: {} | {} | {} | {}".format(index, client["name"], client["company"], client["email"], client["position"]))


def update_client(index, client):
    global clients
    if 0 <= index < len(clients):
        clients[index] = client
    else:
        print("Client is not in clients list")
        
        
def delete_client(index):
    global clients
    if 0 <= index < len(clients):
        del clients[index]
        list_clients()
    else:
        print("Client is not in clients list")

def search_client(index):
    return 0 <= index < len(clients)

# def _add_comma(): 
#     global clients
#     clients += ','


def _print_welcome():
    print("WELCOME TO...")
    print("*" * 30)
    print("What would you like to do today?")
    print("[C]reate client")
    print("[D]elete client")
    print("[U]pdate client")
    print("[S]earch client")
    print("... ", end="")


def _get_client_field(field):
    client_field = None
    while not client_field:
        client_field = input("What's the client {}?: ".format(field))
        if client_field == "exit":
            client_field = None
            break
    if not client_field:
        sys.exit()
    return client_field
 
    
# def _get_client_name():
#     client_name = None
#     while not client_name:
#         client_name = input("What's the client name?: ")
#         if client_name == "exit":
#             client_name = None
#             break
#     if not client_name:
#         sys.exit()
#     return client_name


if __name__ == "__main__":
    
    _print_welcome()
    
    command = input().upper()
    
    match command:
        case "C":
            client = {
                "name": _get_client_field("name"),
                "company": _get_client_field("company"),
                "email": _get_client_field("email"),
                "position": _get_client_field("position")
            }
            create_client(client)
            list_clients()
        case "D":
            index = _get_client_field("index")
            delete_client(int(index))
            list_clients()
        case "U":
            index = _get_client_field("index")
            clientUpdatedData = {
                "name": _get_client_field("name"),
                "company": _get_client_field("company"),
                "email": _get_client_field("email"),
                "position": _get_client_field("position")
            }
            update_client(int(index), clientUpdatedData)
            list_clients()
        case "S":
            index = _get_client_field("index")
            found = search_client(int(index))
            if found:
                print("The client is in the client's list")
            else: 
                print("The client with index: {} isn't in our client's list".format(index))
        case _:
            print("Invalid command!")