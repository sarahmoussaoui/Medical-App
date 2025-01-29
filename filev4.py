import tkinter as tk
from tkinter import ttk

# Function to insert predefined text into the text editor when a menu option is selected
def insert_text(text):
    text_editor.insert(tk.END, text + "\n")

# Function to create the dropdown menu for each button
def show_dropdown(button, options):
    # Create a menu tied to the button
    menu = tk.Menu(button, tearoff=0)
    
    # Add options to the menu
    for option in options:
        menu.add_command(label=option, command=lambda opt=option: insert_text(opt))
    
    # Get the screen position of the button
    x = button.winfo_rootx()
    y = button.winfo_rooty() + button.winfo_height()  # Position it right below the button
    
    # Show the menu at the button's location with a slight offset if necessary
    menu.post(x, y)

# Create the main window
root = tk.Tk()
root.title("Medical Report Editor")
root.geometry("700x500")

# Create a text editor with undo functionality
text_editor = tk.Text(root, height=10, width=80, undo=True)
text_editor.pack(pady=10)

# Enable "Ctrl + Z" for undo action
root.bind("<Control-z>", lambda event: text_editor.edit_undo())

# Define button groups with their corresponding dropdown options
button_groups = [
    {
        "name": "En-tete",
        "bg_color": "yellow",
        "buttons": [
            {
            "sub_name": "Subcategory 1",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("exo jondo", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("OCE/OCI", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            }
        ]
    },
    {
        "name": "Autre Groupe",  # Example second group
        "bg_color": "lightblue",
        "buttons": [
            ("HPV faible", ["Conclusion : Présence de quelques signes d'HPV (lésion intra-épithéliale de bas grade)."]),
            ("HPV élevé", ["Conclusion : Présence de signes d'HPV à haut risque (lésion intra-épithéliale de haut grade)."]),
            ("Normal", ["Conclusion : Aucune anomalie détectée."])
        ]
    }
]

# Function to create buttons within each group
def create_button(frame, label, options, bg_color):
    # Create the button
    button = tk.Button(frame, text=label, bg=bg_color)
    button.pack(side=tk.LEFT, padx=5, pady=5, anchor='w')

    # Define the command for the button to show the dropdown menu
    button.config(command=lambda opts=options, btn=button: show_dropdown(btn, opts))

# Create groups dynamically
for group in button_groups:
    # Create a frame for the group
    frame = tk.Frame(root, bg=group["bg_color"], padx=10, pady=5)
    frame.pack(fill="x", padx=5, pady=5, anchor='w')

    # Add a label for the group
    label = tk.Label(frame, text=group["name"], bg=group["bg_color"], font=("Arial", 12, "bold"))
    label.pack(anchor="w", pady=2)

    # Create buttons inside the group
    for item in group["buttons"]:
        if isinstance(item, tuple):  # Regular button (label, options)
            label, options = item
            create_button(frame, label, options, group["bg_color"])
        elif isinstance(item, dict):  # Subcategory (sub_name, buttons)
            sub_frame = tk.Frame(frame, bg=item["bg_color"], padx=10, pady=5)
            sub_frame.pack(fill="x", padx=5, pady=5, anchor='w')

            sub_label = tk.Label(sub_frame, text=item["sub_name"], bg=item["bg_color"], font=("Arial", 12, "bold"))
            sub_label.pack(anchor="w", pady=2)

            for sub_button in item["buttons"]:
                create_button(sub_frame, sub_button[0], sub_button[1], item["bg_color"])

# Run the Tkinter event loop
root.mainloop()
