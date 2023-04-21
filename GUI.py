import tkinter as tk
from Merkle_Tree import *


def submit_claim():
    name = name_input.get()
    policy = policy_input.get()
    incident_date = incident_date_input.get()
    incident_location = incident_location_input.get()
    description = description_input.get()
    injured_person = injured_person_input.get()
    medical_bills = medical_bills_input.get()
    witness = witness_input.get()

    append_treelist(name.strip() + policy.strip() + incident_date.strip() + incident_location.strip() + description.strip() + injured_person.strip() + medical_bills.strip() + witness.strip())
    
     # clear the entry fields
    name_input.delete(0, tk.END)
    policy_input.delete(0, tk.END)
    incident_date_input.delete(0, tk.END)
    incident_location_input.delete(0, tk.END)
    description_input.delete(0, tk.END)
    injured_person_input.delete(0, tk.END)
    medical_bills_input.delete(0, tk.END)
    witness_input.delete(0, tk.END)

    # output_label.config(text="Claim submitted successfully!")

def Make_Claims():
    
    global name_input, policy_input, incident_date_input, incident_location_input, description_input, injured_person_input,medical_bills_input, witness_input

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
    submit_button = tk.Button(root, text="Submit Claim", command= lambda: (submit_claim(), on_next()))
    submit_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
    


def on_next():
    try:
        value = next(values)
        # label.config(text=value)
        print(value)
        Make_Claims()
    except StopIteration:
        print("No more values")
        print(tree_list)
        MerkleTree(tree_list)

        # label.config(text="No more values")

def generate_values():
    Claim_number.grid_forget()
    Claim_label.grid_forget()

    for i in range(2):
        yield i

def append_treelist(val : str):
    tree_list.append(val)



values = generate_values()

root = tk.Tk()

tree_list=[]

root.title("Insurance Claim Form")

Claim_label = tk.Label(root, text="How many Claims:")
Claim_label.grid(row=7, column=0, padx=5, pady=5)

Claim_number = tk.Entry(root)
Claim_number.grid(row=7, column=1, padx=5, pady=5)

# create proceed button
proceed_button = tk.Button(root, text="proceed", command=lambda:on_next())
proceed_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)


# # create label to show output
# output_label = tk.Label(root, text="")
# output_label.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
