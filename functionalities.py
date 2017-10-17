import file_manager as fM

def say_hi():
    print("Hi!")

def new_client():
    new_cl = raw_input("Insert the name of the new client:")
    prev_cl = fM.get_clients()
    if new_cl not in prev_cl:
	fM.add_client(new_cl)
    
def new_transaction():
    deb = raw_input("Insert the name of the debtor:")
    cred = raw_input("Insert the name of the creditor:")
    amo = raw_input("Insert the name of the amount:")
    cl = fM.get_clients()
    if (deb in cl) and (cred in cl):
	fM.add_transaction(deb,cred,amo)
    elif deb not in cl:
	print("Debtor does not exist!")
    elif cred not in cl:
	print("Creditor does not exist!")
    elif deb not in cl:
	print("Debtor and creditor do not exist!")

def look_credit():
    cl = fM.get_clients()
    print(cl)
    curr = raw_input("Please login:")
    trans = fM.get_transactions()
    curr_cash = 0
    for tran in trains:
	if curr in tran[0]:
	    curr_cash = curr_cash - tran[2]
	if curr in tran[1]:
	    curr_cash += tran[2]
