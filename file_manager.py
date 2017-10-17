import os

client_filename = "clients.txt"
transaction_filename = "transactions.txt"

def add_client(client_name):
    o = open("clients.txt",a)
    o.write("\n" + client_name)
    o.close()
      
def add_transaction(debtor, creditor, amount):
    new_list = [str(x).strip() for x in [debtor,creditor,amount]]
    to_write = ' '.join(new_list)
    o = open("transactions.txt",a)
    o.write(to_write)
    o.close()
        
def get_clients():
    if os.ispath("clients.txt"):
	o = open("clients.txt")
	lines = o.readlines()
	return lines
    else:
	return []

def get_transactions():
    o = open("transactions.txt")
    lines = o.readlines()
    o.close()
    new_list = [[],[],[]]
    for line in lines:
	line.split()
	new_list[0].append(line[0])
	new_list[1].append(line[1])
	new_list[2].append(line[2])
    return new_list
