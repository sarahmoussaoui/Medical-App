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

# Function to create buttons within each group
def create_button(frame, label, options, bg_color, row, column):
    # Create the button
    button = tk.Button(frame, text=label, bg=bg_color)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="w")

    # Define the command for the button to show the dropdown menu
    button.config(command=lambda opts=options, btn=button: show_dropdown(btn, opts))

# Define button groups with their corresponding dropdown options
button_groups = [
    # 1st group
    {
        "name": "En-tete",
        "bg_color": "yellow",
        "buttons": [
            {
            "sub_name": "FC 2lames",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("exo endo", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("jonction endo", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("exojonc endo", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("exo jondo", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),  
                ("OCE/OCI", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "FC 3lames",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("exo jonction endo", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])            ]
            },

            {
            "sub_name": "FCV",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("vagin exo jondo", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])            ]
            },

            {
            "sub_name": "Autres",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("col seul", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("vagin seul", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            }
        ]
    },
    # 2nd group
    {
        "name": "Inflammation",  # Example second group
        "bg_color": "lightblue",
        "buttons": [
            {
            "sub_name": "0/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("nulle", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "1-2/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("faible", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "2-3/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("limitée", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "3-4/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("modeste", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },


            {
            "sub_name": "4-5/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("modere", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "5-6/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("moyen abondance", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "6-7/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("importante", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": ">7/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("tres importante", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "modérée/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("modérée", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            }
            
        ]
    },

    # 3rd group
    {
        "name": "Fond",
        "bg_color": "red",
        "buttons": [
            ("tres propre", ["Sur ces prélèvements, l'examen va montrer:\n\n--sur l'exocol: \n\n--sur l'endocol:  "]),
            ("gloabelement propre", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "]),
            ("a peine granuleux", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
            ("granuleux", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
            ("moderement granuleux", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
            ("tres granuleux", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
            ("granuleux", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
            ("sale", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
        ]
    },

    # 4th group
    {
        "name": "Mucus",
        "bg_color": "red",
        "buttons": [
            ("mucus++", ["Sur ces prélèvements, l'examen va montrer:\n\n--sur l'exocol: \n\n--sur l'endocol:  "]),
            ("trainées mucus+", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "])
        ]
    },

    # 5th group
    {
        "name": "Mucus + sang",
        "bg_color": "red",
        "buttons": [
            ("mucus++ Hgie+", ["Sur ces prélèvements, l'examen va montrer:\n\n--sur l'exocol: \n\n--sur l'endocol:  "]),
            ("mucus trainées hgie ", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "]),
            ("hemorragie ", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "])

        ]
    },

    # 6th group
    {
        "name": "floral",
        "bg_color": "red",
        "buttons": [
            ("lactobacillaire+", ["Sur ces prélèvements, l'examen va montrer:\n\n--sur l'exocol: \n\n--sur l'endocol:  "]),
            ("lactobacillaire++", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "])
        ]
    },

    # 7th group
    {
        "name": "germes / parasites",
        "bg_color": "red",
        "buttons": [
            ("trichomonas", ["Sur ces prélèvements, l'examen va montrer:\n\n--sur l'exocol: \n\n--sur l'endocol:  "]),
            ("mycose", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "]),
            ("actinomycose ", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "])

        ]
    },


    # 8th group
    {
        "name": "fond heterogene",
        "bg_color": "red",
        "buttons": [
            ("muqueux++ granuleux", ["Sur ces prélèvements, l'examen va montrer:\n\n--sur l'exocol: \n\n--sur l'endocol:  "]),
            ("granuleux++ mucus+", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "]),
            ("granuleux++ mucus ", ["L’étude microscopique retrouve sur ces frottis:\n\n--au niveau de la jonction: \n\n--au niveau de l’endocol:  "])

        ]
    },

    #9th group
    {
        "name": "Malpighien régulier",
        "bg_color": "yellow",
        "buttons": [
            {
            "sub_name": "Hautes",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("superieures modéré", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("superieures moyen", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("superieures abondant", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("superieures tres abondant", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "polymorphes majorite superieures",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("polymorphes modéré superieur+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("polymorphes moyen superieur+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("polymorphes abondant superieur+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "polymorphes majorite profondes",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("polymorphes modéré profondes+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("polymorphes moyen profondes+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("polymorphes abondant profondes+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "profondes",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("atrophique modéré", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("atrophique moyen", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("atrophique abondant", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "Hautes + cytolyse",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("superieures modéré cytolyse+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("superieures moyen cytolyse+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("superieures abondant cytolyse+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "Cylindriques",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("Cylindriques rares", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Cylindriques modere", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Cylindriques abondant", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "Cylindriques + Métaplasie",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("Cylindriques rares Métaplasie+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Cylindriques modere Métaplasie++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Cylindriques abondant Métaplasie+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Cylindriques abondant Métaplasie++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])

            ]
            },
          
            {
            "sub_name": "Cytolyse",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("Cytolyse", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "Malpighien particulier",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("clue-cells+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("clue-cells++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("koilocytes", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("koilocytes et dyskeratocytes", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("dyskératocytes", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("binuclées", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])

            ]
            },

            {
            "sub_name": "irritation",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("irritation+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("irritation++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("irritation+++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("exocytose+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("exocytose++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("exocytose+++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),

            ]
            },

            {
            "sub_name": "Dystrophique",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("Dystrophique seul+", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Dystrophique seul++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Dystrophique type Métaplasique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Dystrophique type hyperplasie", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Dystrophique type hyperplasie + Métaplasie", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Métaplasie seule", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("Métaplasie immature", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("squames rares", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("squames++", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("squames anuclées+parakeratosiques", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            }
        ]
    },

    #10TH group
    {
        "name": "Conclusion",
        "bg_color": "yellow",
        "buttons": [
            {
            "sub_name": "RAS",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("OK", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
            ]
            },

            {
            "sub_name": "dystrophique",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("ectropion", ["Leectropions prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ectropion inflammatoire", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ectropion metaplasique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ectropion inflammatoire metaplasique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ectropion minime inflammatoire metaplasique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ectropion minime", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ectropion minime inflammatoire", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ectropion minime metaplasique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col atrophique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col dystrophique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col dystrophique atrophique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])  
            ]
            },

            {
            "sub_name": "specifique",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("col gardnerella", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col mycose", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col actinomycose", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col trichomonas", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
           ]
            },


            {
            "sub_name": "inflammatoire",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("col inflammatoire faible", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col inflammatoire modere", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col inflammatoire", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("col tres inflammatoire controle", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])
           ]
            },

            {
            "sub_name": "atypies",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("ASC-US*", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("ASC-H*", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("AGC*", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("note asc-us", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("note asc-h", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("note AGC", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("HPV faible", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("HPV", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("HPV+CIN1", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("CIN1", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("CIN2", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("CIN13", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("suspect de magnilite", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])

            ]
            },

            {
            "sub_name": "Vagin",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("V. mycose", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("V. gardnerella", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("V. HPV", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("V. RAS", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("V. atrophique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("V. dystrophique", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "]),
                ("V. infm", ["Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: "])

            ]
            }
        ]
    }
]

# Create the main window
root = tk.Tk()
root.title("Medical Report Editor")
root.geometry("700x500")

# Create a text editor with undo functionality
text_editor = tk.Text(root, height=10, width=80, undo=True)
text_editor.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="ew")

# Enable "Ctrl + Z" for undo action
root.bind("<Control-z>", lambda event: text_editor.edit_undo())

# Create a canvas and scrollbar for the groups
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

# Configure the canvas and scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scrollbar
canvas.grid(row=1, column=0, columnspan=2, sticky="nsew")
scrollbar.grid(row=1, column=2, sticky="ns")

# Configure grid weights to make the layout responsive
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create groups dynamically
row_offset = 0
for group in button_groups:
    # Create a frame for the group
    frame = tk.Frame(scrollable_frame, bg=group["bg_color"], padx=10, pady=5)
    frame.grid(row=row_offset, column=0, padx=5, pady=5, sticky="nsew")

    # Add a label for the group
    label = tk.Label(frame, text=group["name"], bg=group["bg_color"], font=("Arial", 12, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=2, sticky="w")

    # Create buttons inside the group
    button_row = 1
    button_column = 0

    for item in group["buttons"]:
        if isinstance(item, tuple):  # Regular button (label, options)
            label, options = item
            create_button(frame, label, options, group["bg_color"], button_row, button_column)
            button_column += 1
            if button_column > 1:  # Adjust the number of columns as needed
                button_column = 0
                button_row += 1
        elif isinstance(item, dict):  # Subcategory (sub_name, buttons)
            sub_frame = tk.Frame(frame, bg=item["bg_color"], padx=10, pady=5)
            sub_frame.grid(row=button_row, column=0, columnspan=2, padx=5, pady=5, sticky="w")

            sub_label = tk.Label(sub_frame, text=item["sub_name"], bg=item["bg_color"], font=("Arial", 12, "bold"))
            sub_label.grid(row=0, column=0, columnspan=2, pady=2, sticky="w")

            sub_button_row = 1
            sub_button_column = 0

            for sub_button in item["buttons"]:
                create_button(sub_frame, sub_button[0], sub_button[1], item["bg_color"], sub_button_row, sub_button_column)
                sub_button_column += 1
                if sub_button_column > 1:  # Adjust the number of columns as needed
                    sub_button_column = 0
                    sub_button_row += 1

            button_row = sub_button_row + 1

    row_offset += 1

# Run the Tkinter event loop
root.mainloop()