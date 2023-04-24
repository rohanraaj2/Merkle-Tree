import tkinter as tk
from Merkle_Tree import *


def generate_values(iterator: int):
    Claim_number.grid_forget()
    # Claim_label.grid_forget()

    for i in range(iterator):
        yield i

root = tk.Tk()

tree_list = []

root.title("Insurance Claim Form")

operation_type= []

def insert(): 
#     # clear the entry fields
    operation_type.append("I")
    clearer()
    Make_Claims()

def Choice():
    
    global Choice_Label, build_button, insert_button, delete_button, verify_button

    Choice_Label = tk.Label(root, text="Choose from the following options:")
    Choice_Label.grid(row=7, column=0, sticky="W")

    build_button = tk.Button(root, text="Build", command=lambda: claims())
    build_button.grid(row=8, column=1, sticky="W")

    insert_button = tk.Button(root, text="Insert", command=lambda: insert())
    insert_button.grid(row=8, column=2, sticky="W")

    delete_button = tk.Button(root, text="Delete", command=lambda: delete())
    delete_button.grid(row=8, column=3, sticky="W")

    verify_button = tk.Button(root, text="Verify", command=lambda: verify())
    verify_button.grid(row=8, column=4, sticky="W")

Choice()

def append_treelist(val: str):
    tree_list.append(val)    

def submit_claim():

    name = name_input.get()
    policy = policy_input.get()
    incident_date = incident_date_input.get()
    incident_location = incident_location_input.get()
    description = description_input.get()
    injured_person = injured_person_input.get()
    medical_bills = medical_bills_input.get()
    witness = witness_input.get()

    append_treelist(name.strip() + policy.strip() + incident_date.strip() + incident_location.strip() +
                    description.strip() + injured_person.strip() + medical_bills.strip() + witness.strip())

    # clear the entry fields
    name_input.delete(0, tk.END)
    policy_input.delete(0, tk.END)
    incident_date_input.delete(0, tk.END)
    incident_location_input.delete(0, tk.END)
    description_input.delete(0, tk.END)
    injured_person_input.delete(0, tk.END)
    medical_bills_input.delete(0, tk.END)
    witness_input.delete(0, tk.END)
    delete_claim_fields()

    print(tree_list[-1])

    if (operation_type[-1]=='I'):
        # Main_tree.insert(tree_list[-1])
        return_to_main_screen()




def Make_Claims():

    global name_input, policy_input, incident_date_input, incident_location_input, description_input, injured_person_input, medical_bills_input, witness_input
    global name_label, policy_label, incident_date_label, incident_location_label, description_label, injured_person_label, medical_bills_label, witness_label

    # create input fields
    name_label = tk.Label(root, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_input = tk.Entry(root)
    name_input.grid(row=0, column=1, padx=5, pady=5)

    policy_label = tk.Label(root, text="Policy Number:")
    policy_label.grid(row=1, column=0, padx=5, pady=5)

    policy_input = tk.Entry(root)
    policy_input.grid(row=1, column=1, padx=5, pady=5)

    incident_date_label = tk.Label(root, text="Incident Date:")
    incident_date_label.grid(row=2, column=0, padx=5, pady=5)

    incident_date_input = tk.Entry(root)
    incident_date_input.grid(row=2, column=1, padx=5, pady=5)

    incident_location_label = tk.Label(root, text="Incident Location:")
    incident_location_label.grid(row=3, column=0, padx=5, pady=5)

    incident_location_input = tk.Entry(root)
    incident_location_input.grid(row=3, column=1, padx=5, pady=5)

    description_label = tk.Label(root, text="Description of Incident:")
    description_label.grid(row=4, column=0, padx=5, pady=5)

    description_input = tk.Entry(root)
    description_input.grid(row=4, column=1, padx=5, pady=5)

    injured_person_label = tk.Label(root, text="Injured Person(s):")
    injured_person_label.grid(row=5, column=0, padx=5, pady=5)

    injured_person_input = tk.Entry(root)
    injured_person_input.grid(row=5, column=1, padx=5, pady=5)

    medical_bills_label = tk.Label(root, text="Medical Bills:")
    medical_bills_label.grid(row=6, column=0, padx=5, pady=5)

    medical_bills_input = tk.Entry(root)
    medical_bills_input.grid(row=6, column=1, padx=5, pady=5)

    witness_label = tk.Label(root, text="Witnesses:")
    witness_label.grid(row=7, column=0, padx=5, pady=5)

    witness_input = tk.Entry(root)
    witness_input.grid(row=7, column=1, padx=5, pady=5)

    # create submit button
    print(".............operation type: ",operation_type[-1],"..............")
    global submit_button
    if (operation_type[-1] == "C"):
        submit_button = tk.Button(
            root, text="Submit Claim", command=lambda: (submit_claim(), on_next()))
        submit_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    elif (operation_type[-1] == "I"):
        submit_button = tk.Button(
            root, text="Submit Claim", command=lambda: (submit_claim()))
        submit_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)


def Main_and_Choice():
    return_to_main.grid_forget()
    Choice()

def delete_claim_fields():
    print("I AM CALLLLLEDDDD")
    submit_button.grid_forget()
    name_label.grid_forget()
    name_input.grid_forget()
    policy_label.grid_forget()
    policy_input.grid_forget()
    incident_date_label.grid_forget()
    incident_date_input.grid_forget()
    incident_location_label.grid_forget()
    incident_location_input.grid_forget()
    description_label.grid_forget()
    description_input.grid_forget()
    injured_person_label.grid_forget()
    injured_person_input.grid_forget()
    medical_bills_label.grid_forget()
    medical_bills_input.grid_forget()
    witness_label.grid_forget()
    witness_input.grid_forget()

def return_to_main_screen():
    global return_to_main
    delete_claim_fields()
    return_to_main = tk.Button(root, text="Your Task has ended! Click to return_to_main", command=lambda: (Main_and_Choice()))
    return_to_main.grid(row=11, column=4, columnspan=2, padx=2, pady=2)



def on_next():
    try:
        value = next(values)
        print(value)
        Make_Claims()
    except StopIteration:
        print("No more values")
        print(tree_list)
        global Main_tree
        Main_tree = MerkleTree(tree_list)
        return_to_main_screen()

def set_values() -> int :
    global values
    Total_Claims = Claim_number.get() 
    print("...........",Total_Claims,"...........")
    values = generate_values( int(Total_Claims) )


def remove_Claim_widgets():
    Claim_label.grid_forget()
    Claim_number.grid_forget()
    proceed_button.grid_forget()


def claims():
    
    # remove the existing widgets
    clearer()
    global operation_type
    operation_type.append("C")
    widgets_to_remove = [Choice_Label, build_button, insert_button, delete_button, verify_button]
    for widget in widgets_to_remove:
        widget.grid_forget()

    # create the new widgets
    global Claim_number, Claim_label

    Claim_label = tk.Label(root, text="Enter the number of claims:")
    Claim_label.grid(row=0, column=0, padx=5, pady=5)

    Claim_number = tk.Entry(root)
    Claim_number.grid(row=0, column=1, padx=5, pady=5)

    # create proceed button
    global proceed_button
    proceed_button = tk.Button(root, text="Proceed", command=lambda: (set_values(),remove_Claim_widgets(), on_next()))
    proceed_button.grid(row=11, column=4, columnspan=2, padx=1, pady=1)


# def clear_entries(*entries):
#     for entry in entries:
#         entry.delete(0, tk.END)

def delete(): pass
    
#     # clear the entry fields
#     clearer()

#     tk.Label(root, text="Registration ID:").grid(row=0, column=0)
#     delete_ID = tk.Entry(root)
#     delete_ID.grid(row=0, column=1)

#     proceed_button = tk.Button(root, text="Delete", command=lambda: clear_entries(delete_ID))
#     proceed_button.grid(row=16, column=3, sticky="SE")

def clearer():
    # clear the entry fields
    Choice_Label. grid_forget()
    build_button. grid_forget()
    insert_button. grid_forget()
    delete_button. grid_forget()
    verify_button. grid_forget() 

def verify():
    pass

# # create label to show output
# output_label = tk.Label(root, text="")
# output_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
