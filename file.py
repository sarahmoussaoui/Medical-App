import tkinter as tk
from tkinter import ttk

# Function to insert text into the editor when a dropdown option is selected
def insert_phrase(phrase):
    text_editor.insert(tk.END, phrase + '\n')

# Create the main window
root = tk.Tk()
root.title("Text Editor with Dropdowns")

# Create the text editor widget
text_editor = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_editor.grid(row=0, column=0, padx=10, pady=10)

# Add an Undo feature (Ctrl+Z)
def undo_action(event=None):
    text_editor.edit_undo()

root.bind("<Control-z>", undo_action)

# Function to create a dropdown menu for each button
def create_dropdown(parent, options, label):
    frame = ttk.Frame(parent, padding="5")
    frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    
    label = ttk.Label(frame, text=label, font=('Arial', 8, 'bold'))  # Smaller font size
    label.grid(row=0, column=0, padx=5)
    
    combobox = ttk.Combobox(frame, values=options, width=18, state="readonly", font=('Arial', 8))  # Smaller font size
    combobox.grid(row=0, column=1, padx=5)
    combobox.set(options[0])  # Set default value
    combobox.bind("<<ComboboxSelected>>", lambda event, phrase=combobox.get(): insert_phrase(phrase))

    return frame

# Group definitions with dropdown options
groups = {
    "EN-TETE": {
        "FC 2lames": {
            "exo endo": ["option1", "option2"],
            "jonction endo": ["option1", "option2"],
            "exojonc endo": ["option1", "option2"],
            "exo jondo": ["option1", "option2"],
            "OCE/OCI": ["option1", "option2"]
        },
        "FC 3lames": {
            "exo jonction endo": ["option1", "option2"]
        },
        "FCV": {
            "vagin exo endo": ["option1", "option2"]
        },
        "Autres": {
            "Col seul": ["option1", "option2"],
            "vagin seul": ["option1", "option2"]
        }
    },
    "INFLAMMATION": {
        "0/10": {
            "nulle": ["option1", "option2", "option3"]
        },
        "1-2/10": {
            "faible": ["option1", "option2", "option3"]
        },
        "2-3/10": {
            "limitee": ["option1", "option2", "option3"]
        },
        "3-4/10": {
            "modeste": ["option1", "option2", "option3"]
        },
        "4-5/10": {
            "modere": ["option1", "option2", "option3"]
        },
        "5-6/10": {
            "nulle": ["option1", "option2", "option3"]
        },
        "6-7/10": {
            "nulle": ["option1", "option2", "option3"]
        },
        ">7/10": {
            "nulle": ["option1", "option2", "option3"]
        },
        "moderee": {
            "nulle": ["option1", "option2", "option3"]
        }         
    },
    "FOND":{
        " ": {
            "tres propre": ["option1", "option2"],
            "globalement propre": ["option1", "option2"],
            "a peine granuleux": ["option1", "option2"],
            "granuleux mais propre": ["option1", "option2"],
            "modere granuleux": ["option1", "option2"],
            "tres granuleux": ["option1", "option2"],
            "granuleux": ["option1", "option2"],
            "sale": ["option1", "option2"]
        }
    }
}

# Scrollable Frame
canvas = tk.Canvas(root)
canvas.grid(row=1, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.grid(row=1, column=1, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

# Frame to hold the dropdown menus
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Creating the groups with dropdowns
group_row = 0
for group_name, subgroups in groups.items():
    group_frame = ttk.LabelFrame(frame, text=group_name, relief="solid", padding="5")
    group_frame.grid(row=group_row, column=1, padx=10, pady=10)
    
    subgroup_row = 0
    for subgroup_name, buttons in subgroups.items():
        subgroup_frame = ttk.LabelFrame(group_frame, text=subgroup_name, relief="flat", padding="5")
        subgroup_frame.grid(row=subgroup_row, column=0, padx=10, pady=5)
        
        for button_name, options in buttons.items():
            create_dropdown(subgroup_frame, options, button_name)
        
        subgroup_row += 1
    
    group_row += 1

# Update scrollable region
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Start the Tkinter loop
root.mainloop()
