import tkinter as tk

# Function to insert predefined text into the text editor
def insert_text(text):
    text_editor.insert(tk.END, text + "\n")

# Create the main window
root = tk.Tk()
root.title("Medical Report Editor")
root.geometry("700x500")

# Create a text editor with undo functionality
text_editor = tk.Text(root, height=10, width=80, undo=True)
text_editor.pack(pady=10)

# Enable "Ctrl + Z" for undo action
root.bind("<Control-z>", lambda event: text_editor.edit_undo())

# Define button groups with colors
button_groups = [
    {
        "name": "En-tete",
        "bg_color": "yellow",
        "buttons": [
            ("Exo Endo", "Sur ces prélèvements, l'examen va montrer:\n\n--sur l'exocol: \n\n--sur l'endocol:  "),
            ("Jonction Endo", "L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "),
            ("Exojonc Endo", "Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: ")
        ]
    },
    {
        "name": "Autre Groupe",  # Example second group
        "bg_color": "lightblue",
        "buttons": [
            ("HPV faible", "Conclusion : Présence de quelques signes d'HPV (lésion intra-épithéliale de bas grade)."),
            ("HPV élevé", "Conclusion : Présence de signes d'HPV à haut risque (lésion intra-épithéliale de haut grade)."),
            ("Normal", "Conclusion : Aucune anomalie détectée.")
        ]
    }
]

# Create groups dynamically
for group in button_groups:
    # Create a frame for the group
    frame = tk.Frame(root, bg=group["bg_color"], padx=10, pady=5)
    frame.pack(fill="x", padx=5, pady=5)

    # Add a label for the group
    label = tk.Label(frame, text=group["name"], bg=group["bg_color"], font=("Arial", 12, "bold"))
    label.pack(anchor="w", pady=2)

    # Create buttons inside the group
    for label, text in group["buttons"]:
        tk.Button(frame, text=label, command=lambda t=text: insert_text(t)).pack(side=tk.LEFT, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
