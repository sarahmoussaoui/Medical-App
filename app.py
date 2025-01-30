import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox
from tkinter import filedialog
from docx import Document  # Import python-docx to create and manipulate Word documents

# Function to append content to an existing Word document
def append_to_word():
    # Get the content from the text editor
    content = text_editor.get("1.0", tk.END)
    
    if content.strip():  # Only append if there is any content
        # Ask the user to select an existing Word document to append the content
        file_path = filedialog.askopenfilename(defaultextension=".docx", filetypes=[("Word documents", "*.docx")])
        
        if file_path:
            try:
                # Load the existing document
                doc = Document(file_path)
                
                # Append the content to the document
                doc.add_paragraph(content)
                
                # Save the document (overwrite the existing document)
                doc.save(file_path)
                print(f"Content appended to {file_path}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("No file selected.")
    else:
        print("No content to append.")

# Function to prompt before closing
def on_close():
    if text_editor.get("1.0", tk.END).strip() != "":  # Check if there is content
        response = messagebox.askyesnocancel("Unsaved Changes", "You have unsaved changes. Do you want to save before closing?")
        if response:  # Save and close
            save_file()
            root.destroy()
        elif response is None:  # Cancel the closing
            pass
        else:  # Close without saving
            root.destroy()
    else:
        root.destroy()

# Function to save the content automatically
def auto_save():
    content = text_editor.get("1.0", tk.END)  # Get the current content of the text editor
    with open("auto_backup.txt", "w") as file:
        file.write(content)
    print("Auto-saved")

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
                ("exo endo", [
                    "Les prélèvements adressés montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: ",
                    "A l'examen, on constate:\n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "A l'examen, on constate:\n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: ",
                    "L'étude microscopique retrouve sur ces frottis:\n\n--sur l'exocol: \n\n--sur l'endocol: ",
                    "L'examen montre:\n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: ",
                    "On observe successivement:\n\n--sur l'exocol: \n\n--sur l'endocol: ",
                    "Sur les frottis confiés, l'examen cytologique montre:\n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "L'observation cytologique permet de constater:\n\n--sur l'exocol: \n\n--sur l'endocol: ",
                    "On observe respectivement sur ces frottis:\n\n--sur l'exocol: \n\n--sur l'endocol: ",
                    "Sur ces prélèvements, l'examen va montrer:\n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: ",
                    "L'examen microscopique met en évidence:\n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: ",
                    "Les frottis reçus montrent:\n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: "
                ]),
                ("jonction endo", [
                    "Sur les frottis confiés, l'examen cytologique montre:\n\n--sur la jonction: \n\n--sur l'endocol: ",
                    "Les préparations adressées se présentent ainsi:\n\n--sur le frottis jonctionnel: \n\n--sur le frottis endocervical: ",
                    "L'examen effectué permet de retrouver:\n\n--au niveau de la jonction: \n\n--au niveau de l'endocol: ",
                    "L'examen montre:\n\n--au niveau de la jonction: \n\n--au niveau de l'endocol: ",
                    "A l'examen, on constate:\n\n--sur la jonction: \n\n--sur l'endocol: ",
                    "Les frottis reçus montrent:\n\n--sur la jonction: \n\n--sur l'endocol: ",
                    "L'observation cytologique permet de constater:\n\n--au niveau de la jonction: \n\n--au niveau de l'endocol: "
                ]),
                ("exojonc endo", [
                    "On retrouve successivement:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: ",
                    "Les frottis reçus montrent:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: ",
                    "Les frottis reçus montrent:\n\n--au niveau de l'exocol/jonction: \n\n--au niveau de l'endocol: ",
                    "Sur ces frottis, on observe respectivement:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: ",
                    "L'examen montre:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: ",
                    "L'observation cytologique permet de constater:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: ",
                    "Les prélèvements adressés montrent:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: ",
                    "Sur ces prélèvements, l'examen va montrer:\n\n--sur le frottis exocervical/jonctionnel: \n\n--sur le frottis endocervical: ",
                    "L'étude microscopique retrouve sur ces frottis:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: ",
                    "L'examen effectué permet de retrouver:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: ",
                    "On observe successivement:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: ",
                    "On observe respectivement sur ces frottis:\n\n--au niveau de l'exocol/jonction: \n\n--au niveau de l'endocol: ",
                    "Sur ces frottis, on observe respectivement:\n\n--au niveau de l'exocol/jonction: \n\n--au niveau de l'endocol: ",
                    "L'examen montre:\n\n--sur l'exocol/jonction: \n\n--sur l'endocol: "
                ]),
                ("exo jondo", [
                    "L'observation cytologique permet de constater:\n\n--au niveau de l'exocol: \n\n--au niveau de la jonction/endocol: ",
                    "A l'examen, on constate:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel/endocervical: ",
                    "Les préparations adressées se présentent ainsi:\n\n--l'exocol: \n\n--la jonction/endocol: ",
                    "On observe respectivement sur ces frottis:\n\n--au niveau de l'exocol: \n\n--au niveau de la jonction/endocol: ",
                    "Les prélèvements adressés montrent:\n\n--sur l'exocol: \n\n--sur la jonction/endocol: ",
                    "L'examen effectué permet de retrouver:\n\n--sur l'exocol: \n\n--sur la jonction/endocol: ",
                    "L'examen microscopique met en évidence:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel/endocervical: ",
                    "L'examen microscopique met en évidence:\n\n--sur l'exocol: \n\n--sur la jonction/endocol: ",
                    "L'étude cytologique retrouve:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel/endocervical: ",
                    "Les préparations adressées se présentent ainsi:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel/endocervical: ",
                    "Sur les frottis confiés, l'examen cytologique montre:\n\n--au niveau de l'exocol: \n\n--au niveau de la jonction/endocol: ",
                    "L'examen montre:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel/endocervical: ",
                    "On observe successivement:\n\n--sur l'exocol: \n\n--sur la jonction/endocol: ",
                    "L'observation cytologique permet de constater:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel/endocervical: "
                ]),
                ("OCE/OCI", [
                    "Sur ces prélèvements, l'examen va montrer:\n\n--sur l'orifice cervical externe: \n\n--sur l'orifice cervical interne: ",
                    "L'examen montre:\n\n--au niveau de l'OCE: \n\n--au niveau de l'OCI: ",
                    "L'observation cytologique permet de constater:\n\n--sur l'OCE: \n\n--sur l'OCI: ",
                    "Sur ces frottis, on observe respectivement:\n\n--sur l'OCE: \n\n--sur l'OCI: ",
                    "L'étude microscopique retrouve sur ces frottis:\n\n--au niveau de l'OCE: \n\n--au niveau de l'OCI: ",
                    "L'examen microscopique met en évidence:\n\n--sur l'orifice cervical externe: \n\n--sur l'orifice cervical interne: ",
                    "A l'examen, on constate:\n\n--au niveau de l'OCE: \n\n--au niveau de l'OCI: ",
                    "Les préparations adressées se présentent ainsi:\n\n--sur l'orifice cervical externe: \n\n--sur l'orifice cervical interne: ",
                    "Les frottis reçus montrent:\n\n--au niveau de l'OCE: \n\n--au niveau de l'OCI: ",
                    "Les prélèvements adressés montrent:\n\n--au niveau de l'OCE: \n\n--au niveau de l'OCI: "
                ]),
            ]
            },

            {
            "sub_name": "FC 3lames",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("exo jonction endo", [
                    "Les prélèvements adressés montrent:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel: \n\n--sur le frottis endocervical: ",
                    "Les préparations adressées se présentent ainsi:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel: \n\n--sur le frottis endocervical: ",
                    "L'étude cytologique retrouve:\n\n--sur l'exocol: \n\n--sur la jonction: \n\n--sur l'endocol: ",
                    "On observe respectivement sur ces frottis:\n\n--sur l'exocol: \n\n--sur la jonction: \n\n--sur l'endocol: ",
                    "L'étude microscopique retrouve sur ces frottis:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel: \n\n--sur le frottis endocervical: ",
                    "On observe successivement:\n\n--sur le frottis exocervical: \n\n--sur le frottis jonctionnel: \n\n--sur le frottis endocervical: ",
                    "L'observation cytologique permet de constater:\n\n--sur l'exocol: \n\n--sur la jonction: \n\n--sur l'endocol: ",
                    "Sur les frottis confiés, l'examen cytologique montre:\n\n--au niveau de l'exocol: \n\n--au niveau de la jonction: \n\n--au niveau de l'endocol: ",
                    "Sur les frottis confiés, l'examen cytologique montre:\n\n--sur l'exocol: \n\n--sur la jonction: \n\n--sur l'endocol: "
                ]),
            ]
            },

            {
            "sub_name": "FCV",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("vagin exo jondo", [
                    "L'examen microscopique met en évidence:\n\n--au niveau du vagin: \n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: ",
                    "L'examen montre:\n\n--sur le frottis vaginal: \n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "L'étude cytologique retrouve:\n\n--sur le vagin: \n\n--sur l'exocol: \n\n--sur l'endocol: ",
                    "On observe successivement:\n\n--sur le vagin: \n\n--sur l'exocol: \n\n--sur l'endocol: ",
                    "L'examen effectué permet de retrouver:\n\n--sur le cul-de-sac: \n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "Sur ces prélèvements, l'examen va montrer:\n\n--sur le vagin: \n\n--sur l'exocol: \n\n--sur l'endocol: ",
                    "Les prélèvements adressés montrent:\n\n--sur le frottis vaginal: \n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "On observe successivement:\n\n--sur le cul-de-sac: \n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "L'examen effectué permet de retrouver:\n\n--au niveau du vagin: \n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: ",
                    "L'étude microscopique retrouve sur ces frottis:\n\n--sur le cul-de-sac: \n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "L'étude cytologique retrouve:\n\n--sur le frottis vaginal: \n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: ",
                    "L'examen montre:\n\n--au niveau du vagin: \n\n--au niveau de l'exocol: \n\n--au niveau de l'endocol: ",
                    "L'examen microscopique met en évidence:\n\n--sur le frottis vaginal: \n\n--sur le frottis exocervical: \n\n--sur le frottis endocervical: "
                ]),
            ]
            },

            {
            "sub_name": "Autres",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("col seul", [
                    "L'étude microscopique a concerné le col.",
                    "Le prélèvement cervical est reçu pour examen microscopique.",
                    "L'examen microscopique est effectué sur ce prélèvement cervico-utérin.",
                    "Le prélèvement confié représente le col utérin.",
                    "L'analyse microscopique a intéressé le col utérin.",
                    "L'examen cytologique a porté sur un prélèvement cervical.",
                    "Un prélèvement cervical est adressé pour examen."
                ]),
                ("vagin seul", [
                    "L'étude microscopique a concerné le vagin.",
                    "Un prélèvement vaginal est adressé pour examen.",
                    "L'examen microscopique a porté sur un prélèvement vaginal.",
                    "L'observation microscopique a porté sur un prélèvement vaginal.",
                    "L'analyse microscopique a intéressé le vagin.",
                    "L'étude microscopique a intéressé un prélèvement vaginal.",
                    "Un prélèvement vaginal est adressé pour étude microscopique."
                ])
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
                ("nulle", [
                    "L'afflux de cellules inflammatoires est presque nul.",
                    "On ne retrouve pas d'infiltrat inflammatoire.",
                    "La participation inflammatoire est pratiquement nulle.",
                    "Le contingent inflammatoire est quasiment absent.",
                    "On ne rencontre pas de contingent inflammatoire.",
                    "On n'observe pas de participation inflammatoire.",
                    "On ne constate pas de présence inflammatoire.",
                    "Il n'y a pas d'infiltrat inflammatoire.",
                    "Il n'y a pas de participation inflammatoire."
                ])
            ]
            },

            {
            "sub_name": "1-2/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("faible", [
                    "L'infiltrat leucocytaire est négligeable.",
                    "L'afflux d'éléments inflammatoires est négligeable.",
                    "On ne rencontre que quelques éléments inflammatoires.",
                    "On ne rencontre que peu de polynucléaires.",
                    "Faible afflux inflammatoire.",
                    "La présence d'éléments inflammatoires est insignifiante.",
                    "Pauvre présence inflammatoire.",
                    "On ne constate qu'une bien faible participation inflammatoire.",
                    "Les éléments inflammatoires sont rares.",
                    "L'inflammation est très discrète.",
                    "On n'observe qu'une faible présence inflammatoire.",
                    "La présence de cellules inflammatoires n'est pas significative.",
                    "Rares éléments inflammatoires.",
                    "La participation inflammatoire est très faible."
                ])
            ]
            },

            {
            "sub_name": "2-3/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("limitée", [
                    "On ne constate qu'une discrète participation inflammatoire.",
                    "L'inflammation est minime.",
                    "Quant à la participation inflammatoire, elle est bien modeste.",
                    "L'infiltrat leucocytaire est sans importance.",
                    "L'afflux d'éléments inflammatoires est discret.",
                    "On ne rencontre que peu d'éléments inflammatoires.",
                    "La présence de cellules inflammatoires est peu significative."
                ])
            ]
            },

            {
            "sub_name": "3-4/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("modeste", [
                    "Quant à la participation inflammatoire, elle se montre modeste, leucocytaire.",
                    "L'infiltrat inflammatoire se limite à quelques traînées leucocytaires.",
                    "Le contingent leucocytaire associé est modeste.",
                    "Il s'agit d'un infiltrat inflammatoire modeste.",
                    "La présence d'éléments inflammatoires est modeste.",
                    "La participation d'éléments inflammatoires n'est pas importante.",
                    "Présence d'un infiltrat modeste de polynucléaires.",
                    "La présence de cellules inflammatoires se révèle modeste."
                ])
            ]
            },


            {
            "sub_name": "4-5/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("modérée", [
                    "La participation d'éléments inflammatoires n'est pas importante.",
                    "L'infiltrat inflammatoire est modéré, essentiellement fait de polynucléaires.",
                    "Il s'agit d'un infiltrat inflammatoire surtout leucocytaire d'abondance modérée.",
                    "Le contingent leucocytaire est peu abondant.",
                    "Des bandes leucocytaires de densité modérée sont présentes.",
                    "L'infiltrat inflammatoire est modéré, leucocytaire.",
                    "L'infiltrat inflammatoire se limite à quelques traînées leucocytaires.",
                    "Le contingent inflammatoire accompagnement n'est pas important.",
                    "L'infiltrat inflammatoire est d'abondance modérée.",
                    "La préparation est parcourue par de grêles traînées de polynucléaires.",
                    "Quant à la présence inflammatoire, elle se montre peu importante."
                ])
            ]
            },

            {
            "sub_name": "5-6/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("moyen abondance", [
                    "L'infiltrat inflammatoire est plutôt riche.",
                    "L'infiltrat inflammatoire est de moyenne abondance, essentiellement fait de polynucléaires.",
                    "L'infiltrat inflammatoire se montre de moyenne abondance, constitué surtout de polynucléaires.",
                    "La présence d'éléments inflammatoires est assez abondante.",
                    "Le contingent leucocytaire associé est d'abondance moyenne.",
                    "L'infiltrat inflammatoire forme quelques traînées leucocytaires.",
                    "Le contingent leucocytaire d'accompagnement est de moyenne abondance.",
                    "L'infiltrat inflammatoire est relativement abondant.",
                    "La participation d'éléments inflammatoires n'est relativement riche.",
                    "Présence d'un infiltrat moyennement abondant de polynucléaires.",
                    "Le contingent leucocytaire est assez abondant.",
                    "L'infiltrat inflammatoire est assez abondant."
                ])
            ]
            },

            {
            "sub_name": "6-7/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("importante", [
                    "Présence d'un infiltrat inflammatoire diffus, étendu à toute la préparation.",
                    "Présence de plages inflammatoires épaisses et denses.",
                    "La plupart des placards épithéliaux sont étroitement accompagnés par l'infiltrat inflammatoire.",
                    "L'infiltrat inflammatoire est retrouvé en nappes renfermant des groupements épithéliaux.",
                    "La population épithéliale est souvent escortée, parfois dissociée par l'infiltrat inflammatoire.",
                    "L'infiltrat inflammatoire est présent en traînées assez larges épaisses renfermant des amas épithéliaux.",
                    "L'infiltrat inflammatoire est important, dominé par des polynucléaires.",
                    "Présence d'un important infiltrat inflammatoire.",
                    "L'infiltrat inflammatoire est abondant."
                ])
            ]
            },

            {
            "sub_name": ">7/10",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("très importante", [
                    "La participation inflammatoire est massive.",
                    "L'infiltrat inflammatoire pénètre la desquamation épithéliale.",
                    "L'infiltrat inflammatoire va former des nappes denses, à prédominance leucocytaire.",
                    "Le contingent inflammatoire est massif, recouvrant un grand nombre de placards épithéliaux.",
                    "L'infiltrat inflammatoire prédomine très largement.",
                    "Présence d'un infiltrat inflammatoire diffus, étendu à toute la préparation.",
                    "L'infiltrat inflammatoire est très important, dominé par des polynucléaires.",
                    "L'infiltrat inflammatoire est particulièrement important, principalement leucocytaire.",
                    "L'infiltrat inflammatoire se montre très riche, constitué en majorité de leucocytes.",
                    "Présence de plages inflammatoires épaisses et denses."
                ])
            ]
            },

            {
            "sub_name": "modérée polymorphe",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("modérée polymorphe", [
                    "L'infiltrat inflammatoire est polymorphe, modéré.",
                    "L'infiltrat inflammatoire est modéré.",
                    "Présence d'un infiltrat modéré et polymorphe.",
                    "L'infiltrat inflammatoire est modéré, leuco-histiocytaire.",
                    "Des bandes leuco-histiocytaires de densité modérée sont présentes.",
                    "Quant à la présence inflammatoire, elle se montre peu importante.",
                    "L'infiltrat inflammatoire se montre d'abondance modérée.",
                    "Le contingent inflammatoire accompagnement n'est pas important, polymorphe.",
                    "L'infiltrat inflammatoire se limite à quelques traînées leuco-histiocytaires.",
                    "Quant à la participation inflammatoire, elle se montre polymorphe, modérée."
                ])
            ]
            }
            
        ]
    },

    # 3rd group
    {
        "name": "Fond",
        "bg_color": "pink",
        "buttons": [
            ("très propre", [
                "La préparation montre un fond bien propre.",
                "La préparation montre un fond d'aspect très propre.",
                "Cette préparation est de caractère particulièrement propre.",
                "La préparation montre un fond particulièrement propre.",
                "Le frottis paraît très propre.",
                "On constate qu'il s'agit d'un fond bien propre.",
                "La préparation montre un fond très propre.",
                "Le fond de la préparation est bien propre.",
                "Il s'agit d'une préparation bien propre.",
                "Le fond de la préparation est très propre.",
                "Le fond du frottis est nettement dégagé, clair."
            ]),
            ("globalement propre", [
                "On est en présence d'une préparation à fond propre.",
                "Dans l'ensemble, il s'agit d'une préparation propre.",
                "Dans l'ensemble, cette préparation est d'aspect propre.",
                "Le fond se montre généralement propre.",
                "Il s'agit d'une préparation propre.",
                "Cette préparation est de caractère propre.",
                "Le fond se montre propre.",
                "Ce frottis paraît globalement net.",
                "On constate qu'il s'agit d'un fond qui est dans l'ensemble propre.",
                "Le fond est globalement propre.",
                "Le fond du frottis est plutôt dégagé, clair.",
                "Cette préparation est de caractère propre dans l'ensemble.",
                "Le fond se montre propre.",
                "Ce frottis paraît net pour l'essentiel.",
                "Ce frottis paraît net dans l'ensemble."
            ]),
            ("à peine granuleux", [
                "La préparation paraît d'aspect discrètement granuleux.",
                "Le fond est à peine granuleux.",
                "La préparation se révèle légèrement granuleuse.",
                "Le frottis va montrer un arrière-fond de caractère à peine granuleux.",
                "Ce frottis est d'aspect discrètement granuleux.",
                "Le fond du frottis se montre à peine granuleux.",
                "Ce frottis présente un fond discrètement granuleux.",
                "Il s'agit d'une préparation légèrement granuleuse."
            ]),
            ("granuleux mais propre", [
                "Ce frottis bien que granuleux conserve un aspect généralement propre.",
                "Ce frottis légèrement granuleux reste pour l'essentiel propre.",
                "Ce frottis se montre un peu granuleux et reste plutôt propre.",
                "Granuleux par endroits, le fond de cette préparation reste généralement propre.",
                "Le fond de ce frottis est légèrement granuleux et reste dans l'ensemble propre.",
                "Cette préparation à fond un peu granuleux reste pour l'essentiel plutôt propre.",
                "Ce frottis bien que granuleux présente un aspect généralement propre.",
                "Le frottis va montrer un arrière-fond granuleux, mais globalement propre."
            ]),
            ("modérément granuleux", [
                "Le frottis va montrer un arrière-fond de caractère peu granuleux.",
                "Il s'agit d'une préparation modérément granuleuse.",
                "Ce frottis est d'aspect modérément granuleux.",
                "On est en présence d'un fond d'aspect peu granuleux.",
                "Le fond est modérément granuleux.",
                "La préparation se révèle modérément granuleuse.",
                "Le fond du frottis se montre peu granuleux.",
                "Ce frottis présente un fond modérément granuleux."
            ]),
            ("très granuleux", [
                "Ce frottis est d'aspect très granuleux.",
                "Le fond du frottis se montre très granuleux.",
                "Il s'agit d'une préparation très granuleuse.",
                "On est en présence d'un fond d'aspect très granuleux.",
                "Le frottis va montrer un arrière-fond de caractère très granuleux.",
                "Le fond est très granuleux.",
                "La préparation se révèle très granuleuse."
            ]),
            ("granuleux", [
                "Il s'agit d'une préparation granuleuse.",
                "Le fond du frottis se montre granuleux.",
                "Le fond est granuleux.",
                "La préparation paraît d'aspect granuleux.",
                "La préparation se révèle bien granuleuse.",
                "Le frottis va montrer un arrière-fond de caractère granuleux.",
                "Ce frottis est d'aspect granuleux.",
                "On est en présence d'un fond d'aspect granuleux."
            ]),
            ("sale", [
                "La préparation est sale.",
                "On retrouve un fond d'aspect bien trouble.",
                "Ce prélèvement est d'aspect sale."
            ])
        ]
    },

    # 4th group
    {
        "name": "Mucus",
        "bg_color": "yellow",
        "buttons": [
            ("mucus+++", [
                "Le mucus est abondant.",
                "Le mucus est rapporté en abondance.",
                "La glaire est épaisse.",
                "De la glaire est présente en abondance.",
                "Présence de mucus en plages étendues.",
                "Le mucus rapporté est riche.",
                "Une glaire abondante occupe le fond.",
                "Le fond est muqueux.",
                "La glaire est retrouvée en abondance.",
                "Le mucus forme des nappes.",
                "Un mucus très abondant s'observe."
            ]),
            ("trainées mucus+", [
                "Un mucus en traînées s'observe.",
                "Le mucus est rapporté en traînées.",
                "Des traînées de mucus s'observent.",
                "Le mucus forme des bandes.",
                "La glaire est en traînées.",
                "Le fond est parcouru de traînées de mucus.",
                "Présence de traînées de glaire.",
                "On retrouve de la glaire en traînées.",
                "Des traînées de glaire parcourent la préparation.",
                "Présence de traînées de mucus."
            ])
        ]
    },

    # 5th group
    {
        "name": "Mucus + sang",
        "bg_color": "ivory",
        "buttons": [
            ("mucus++ Hgie+", [
                "On retrouve de la glaire hématique en abondance.",
                "Une glaire abondante occupe le fond, accompagnée d'un peu de sang.",
                "De la glaire est présente sous la forme de traînées légèrement hématiques.",
                "Présence de mucus en plages étendues, teintées de sang.",
                "Le mucus est rapporté en abondance, à peine hématique.",
                "La glaire est retrouvée en abondance, striée de sang.",
                "Un mucus très abondant s'observe, strié de sang.",
                "Le fond est muqueux, légèrement hématique.",
                "Le mucus forme des nappes un peu hématiques.",
                "La glaire est épaisse, tatouée de sang."
            ]),
            ("mucus trainée hgie", [
                "Présence de traînées de glaire à peine hématique.",
                "Le fond est parcouru de traînées de mucus tatouées de sang.",
                "Une glaire en traînées striées de sang parcourt la préparation.",
                "Le mucus va former des traînées un peu hémorragiques.",
                "Le mucus est tatoué de sang, en traînées.",
                "De la glaire est présente en bandes tatouées de sang.",
                "On retrouve de la glaire en traînées, légèrement hématiques.",
                "Un mucus en traînées s'observe, accompagnées de filets de sang.",
                "Présence de traînées de mucus peu hématique.",
                "Le mucus rapporté se dispose en traînées striées de sang."
            ]),
            ("hémorragie", [
                "La préparation est striée de sang.",
                "Il s'agit d'un prélèvement hématique.",
                "Du sang est retrouvé.",
                "Le sang est abondant.",
                "La préparation est hémorragique."
            ])

        ]
    },

    # 6th group
    {
        "name": "floral",
        "bg_color": "lightblue",
        "buttons": [
            ("lactobacillaire+", [
                "Le fond est modérément granuleux par la présence de flore lactobacillaire.",
                "Le fond est en partie recouvert de lactobacilles.",
                "Le fond est occupé par une flore modérée de lactobacilles.",
                "Le fond est modérément lactobacillaire.",
                "Des lactobacilles sont retrouvés par endroits.",
                "Présence modérée de lactobacilles.",
                "Le frottis comporte des lactobacilles.",
                "Présence d'une flore physiologique modérée."
            ]),
            ("lactobacillaire++", [
                "Abondante présence de lactobacilles.",
                "Le fond est densément lactobacillaire.",
                "Le fond est occupé par une abondante flore de lactobacilles.",
                "Le fond du frottis est densément lactobacillaire.",
                "Le fond est recouvert de lactobacilles.",
                "Le fond est granuleux par la présence de la flore lactobacillaire.",
                "Un tapis de lactobacilles est retrouvé.",
                "La préparation est tapissée de lactobacilles.",
                "Présence d'une flore physiologique dense.",
                "Le frottis est riche en lactobacilles."
            ])
        ]
    },

    # 7th group
    {
        "name": "germes / parasites",
        "bg_color": "pink",
        "buttons": [
            ("trichomonas", [
                "On retrouve des trichomonas au sein de l'infiltrat inflammatoire.",
                "Du trichomonas est observé.",
                "Quelques trichomonas sont présents parmi les éléments inflammatoires.",
                "La présence de trichomonas est constatée.",
                "On parvient à identifier des trichomonas altérés.",
                "Des trichomonas s'observent.",
                "S'y ajoutent des trichomonas.",
                "On reconnaît des trichomonas au sein de l'infiltrat inflammatoire.",
                "La présence de trichomonas est notée."
            ]),
            ("mycose", [
                "Une mycose y est associée.",
                "On note la présence d'une mycose.",
                "Des formations mycéliennes sont rencontrées.",
                "Des structures mycéliennes sont présentes.",
                "S'y associent des filaments mycéliens.",
                "Des spores et des filaments mycéliens sont retrouvés.",
                "La présence d'une mycose est constatée.",
                "Des filaments et des spores sont présents.",
                "On note aussi la présence de formations mycéliennes.",
                "Présence de formations mycéliennes."
            ]),
            ("actinomycose", [
                "Des filaments d'actinomyces sont présents.",
                "De l'actinomycose est observée.",
                "Des formations filamenteuses d'actinomyces sont présentes.",
                "Des filaments d'actinomyces sont retrouvés.",
                "De l'actinomycose est observable.",
                "Présence d'amas filamenteux bleutés d'actinomycose.",
                "On retrouve de l'actinomycose.",
                "On retrouve des amas filamenteux d'actinomycose.",
                "On retrouve des magmas filamenteux d'actinomycose."
            ])

        ]
    },


    # 8th group
    {
        "name": "fond heterogene",
        "bg_color": "beige",
        "buttons": [
            ("muqueux++granuleux", [
                "La préparation paraît d'aspect muqueux, modérément granuleux.",
                "Ce frottis présente un fond muqueux, granuleux par endroits.",
                "Ce frottis est d'aspect muqueux, granuleux parfois.",
                "On est en présence d'un fond d'aspect muqueux, granuleux par endroits.",
                "La préparation se révèle bien riche en mucus, légèrement granuleuse.",
                "Le frottis va montrer un arrière-fond de caractère muqueux, comportant des foyers granuleux.",
                "Le fond du frottis se montre muqueux, avec foyers granuleux."
            ]),
            ("granuleux++mucus+", [
                "Il s'agit d'une préparation granuleuse, avec quelques foyers de glaire.",
                "On observe de la glaire modérée sur un fond qui est granuleux.",
                "Le frottis va montrer un arrière-fond de caractère granuleux, comportant un peu de glaire.",
                "La préparation se révèle bien granuleuse, légèrement mucoïde.",
                "Ce frottis est d'aspect granuleux, muqueux parfois.",
                "On est en présence d'un fond d'aspect granuleux, muqueux par endroits."
            ]),
            ("granuleux++mucus hémorragique", [
                "Ce frottis est d'aspect granuleux, muqueux et hématique parfois.",
                "Le frottis va montrer un arrière-fond de caractère granuleux, comportant un peu de glaire strié de sang.",
                "Le fond du frottis se montre granuleux, avec présence modérée de mucus teinté de sang.",
                "On observe de la glaire modérée, légèrement hématique, sur un fond qui est granuleux.",
                "Ce frottis présente un fond granuleux, muqueux et hématique par endroits.",
                "La préparation paraît d'aspect granuleux, modérément muco-hématique."
            ])

        ]
    },

    #9th group
    {
        "name": "Malpighien régulier",
        "bg_color": "lightblue",
        "buttons": [
            {
            "sub_name": "Hautes",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("supérieur modéré", [
                    "Peu abondant, le contingent épithélial reste morphologiquement régulier, provenant des couches supérieures.",
                    "D'abondance modérée, les groupements épithéliaux rapportés sont formés de cellules malpighiennes intermédiaires et superficielles, d'aspect préservé.",
                    "D'aspect morphologique régulier, la population épithéliale se montre peu importante. Elle consiste en cellules malpighiennes intermédiaires et superficielles.",
                    "La population épithéliale desquamée se montre peu importante et consiste en cellules malpighiennes intermédiaires et superficielles, sans anomalie.",
                    "D'aspect préservé, la desquamation épithéliale se montre peu importante. Elle est faite de cellules malpighiennes intermédiaires et superficielles.",
                    "De morphologie régulière, la population épithéliale se montre d'abondance modérée, constituée de cellules malpighiennes intermédiaires et superficielles."
                ]),
                ("supérieur moyen", [
                    "La population épithéliale desquamée se montre de moyenne abondance. Elle consiste en cellules malpighiennes intermédiaires et superficielles, sans anomalie.",
                    "De moyenne abondance, les groupements épithéliaux rapportés sont formés de cellules intermédiaires et superficielles, d'aspect conservé.",
                    "Les groupements épithéliaux rapportés assez nombreux, dispersés. Leur morphologie est régulière.",
                    "C'est une desquamation épithéliale de moyenne abondance qui est présente. Elle est constituée de cellules malpighiennes hautes, sans modification particulière.",
                    "Les groupements épithéliaux rapportés sont assez abondants. Leur morphologie est régulière.",
                    "Les cellules épithéliales desquamées, assez nombreuses, proviennent des couches supérieures du revêtement, d'aspect régulier.",
                    "Relativement abondant, le contingent épithélial conserve un aspect morphologiquement régulier, et provient des couches supérieures.",
                    "La population épithéliale est relativement abondante, formée de cellules intermédiaires et superficielles, montrant un aspect régulier.",
                    "C'est une population épithéliale de moyenne abondance qu'on retrouve, constituée de cellules malpighiennes hautes, sans modification particulière.",
                    "D'aspect préservé morphologiquement, le matériel épithélial est moyennement abondant, formé de cellules malpighiennes intermédiaires et superficielles.",
                    "D'aspect régulier morphologiquement, la desquamation épithéliale est assez abondante, formée d'éléments malpighiens superficiels et intermédiaires.",
                    "Les cellules épithéliales desquamées, assez nombreuses, proviennent des couches supérieures du revêtement, d'aspect régulier."
                ]),
                ("supérieur abondant", [
                    "D'aspect préservé morphologiquement, le matériel épithélial est important, formé d'éléments malpighiens superficiels et intermédiaires.",
                    "Abondant, le contingent épithélial conserve un aspect morphologiquement régulier, et provient des couches supérieures.",
                    "Bien nombreux, les placards épithéliaux présents sont formés de cellules malpighiennes intermédiaires et superficielles, d'aspect régulier.",
                    "La population épithéliale desquamée se montre abondante et consiste en cellules malpighiennes intermédiaires et superficielles, sans anomalie.",
                    "Les groupements épithéliaux rapportés sont de type malpighien, en grand nombre. Leur morphologie est régulière.",
                    "D'aspect préservé, la population épithéliale est de grande abondance. Elle est faite de cellules malpighiennes intermédiaires et superficielles.",
                    "La population épithéliale de grande abondance, est malpighienne appartenant aux couches supérieures et conserve un aspect régulier.",
                    "Il s'agit d'une population épithéliale de grande abondance, formée de cellules malpighiennes intermédiaires et superficielles. Elles sont d'aspect régulier.",
                    "En nombre important, les groupements épithéliaux rapportés sont formés de cellules malpighiennes intermédiaires et superficielles, d'aspect conservé.",
                    "D'abondance marquée, les placards épithéliaux se composent de cellules malpighiennes intermédiaires et superficielles, sans anomalies.",
                    "D'aspect préservé morphologiquement, le matériel épithélial est bien abondant, formé d'éléments malpighiens intermédiaires et superficiels.",
                    "D'aspect préservé morphologiquement, la population épithéliale est de grande abondance, formée d'éléments malpighiens intermédiaires et superficiels.",
                    "Relativement abondant, le contingent épithélial reste morphologiquement régulier, issu des couches supérieures.",
                    "La population épithéliale desquamée se montre abondante et consiste en cellules malpighiennes intermédiaires et superficielles, sans anomalie."
                ]),
                ("superieur tres abondant", [
                    "C'est une desquamation épithéliale très riche qu'on retrouve. Elle est constituée de cellules malpighiennes hautes, sans modification particulière.",
                    "Le matériel épithélial, important, est représenté par des cellules intermédiaires et superficielles, de morphologie conservée.",
                    "De morphologie régulière, la population épithéliale se montre très abondante. Elle consiste en cellules malpighiennes intermédiaires et superficielles.",
                    "Les cellules épithéliales desquamées, très nombreuses, proviennent des couches supérieures du revêtement, d'aspect régulier.",
                    "La population épithéliale très abondante est malpighienne appartenant aux couches supérieures et conserve un aspect régulier.",
                    "Très abondant, le contingent épithélial reste morphologiquement régulier, provient des couches supérieures.",
                    "C'est une desquamation épithéliale très riche qu'on retrouve. Elle est constituée de cellules malpighiennes hautes, sans modification particulière.",
                    "C'est une desquamation épithéliale très riche qui est présente. Elle est constituée de cellules malpighiennes hautes, sans modification particulière.",
                    "D'aspect préservé, la desquamation épithéliale est très riche. Elle est faite de cellules malpighiennes intermédiaires et superficielles.",
                    "D'aspect préservé morphologiquement, la desquamation épithéliale est très riche, formée de cellules malpighiennes intermédiaires et superficielles.",
                    "D'aspect morphologique régulier, la population épithéliale se montre très importante. Elle consiste en cellules malpighiennes intermédiaires et superficielles.",
                    "Très abondants, les groupements épithéliaux rapportés sont formés de cellules malpighiennes intermédiaires et superficielles, d'aspect préservé.",
                    "C'est une desquamation épithéliale très riche qu'on retrouve. Elle est constituée de cellules malpighiennes hautes, sans modification particulière.",
                    "De morphologie conservée, la population épithéliale se montre très importante. Elle consiste en cellules malpighiennes intermédiaires et superficielles.",
                    "C'est une desquamation épithéliale très riche qu'on retrouve, constituée de cellules malpighiennes hautes, sans modification particulière.",
                    "Très abondant, le contingent épithélial se montre morphologiquement régulier, issu des couches supérieures."
                ])
            ]
            },

            {
            "sub_name": "polymorphes majorite superieures",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("polymorphes modéré superieur+", [
                    "D'aspect préservé morphologiquement, la population épithéliale est polymorphe modérée, formée principalement d'éléments malpighiennes superficielles et intermédiaires.",
                    "La population épithéliale desquamée se montre peu importante et va consister surtout en cellules malpighiennes intermédiaires et superficielles, sans anomalie.",
                    "D'aspect préservé morphologiquement, la desquamation épithéliale est modérée, formée surtout d'éléments malpighiens intermédiaires et superficiels.",
                    "D'aspect préservé morphologiquement, la population épithéliale est polymorphe, modérée, formée surtout d'éléments malpighiennes intermédiaires et superficielles.",
                    "D'aspect morphologique régulier, la population épithéliale se montre peu importante. Elle se compose avant tout de cellules malpighiennes intermédiaires et superficielles.",
                    "De morphologie régulière, la population épithéliale se montre d'abondance modérée. Elle consiste principalement en cellules malpighiennes intermédiaires et superficielles.",
                    "La population épithéliale, plutôt modérée, se compose d'éléments malpighiens en majorité hauts, sans irrégularité observable.",
                    "Les groupements épithéliaux rapportés sont peu nombreux, polymorphes. Leur morphologie est régulière.",
                    "D'aspect régulier morphologiquement, la population épithéliale est assez modérée, polymorphe, formée d'éléments malpighiennes superficielles et intermédiaires.",
                    "D'aspect régulier, la desquamation épithéliale se montre modérée, essentiellement des éléments malpighiens superficielles et intermédiaires."
                ]),
                ("polymorphe moyen superieur+", [
                    "D'abondance moyenne, les placards épithéliaux sont polymorphes, dominés par les cellules malpighiennes intermédiaires et superficielles, d'aspect régulier.",
                    "D'aspect régulier, la desquamation épithéliale se montre moyennement abondante, essentiellement des éléments malpighiens superficielles et intermédiaires.",
                    "La population épithéliale, plutôt abondante, se compose d'éléments malpighiens en majorité hauts, sans irrégularité observable.",
                    "Il s'agit d'une population épithéliale assez abondante, composée en majorité de cellules malpighiennes intermédiaires et superficielles. Elles sont d'aspect régulier.",
                    "D'aspect conservé, les cellules appartiennent en majorité aux couches hautes et sont d'abondance moyenne.",
                    "Assez abondant, le contingent épithélial reste morphologiquement régulier, appartenant surtout aux couches supérieures.",
                    "C'est une population épithéliale moyennement abondante qu'on retrouve. Elle est constituée surtout de cellules malpighiennes hautes, sans modification particulière.",
                    "Les cellules épithéliales desquamées proviennent avant tout des couches supérieures du revêtement, d'aspect régulier.",
                    "Assez abondant, le contingent épithélial reste morphologiquement régulier, provenant principalement des couches supérieures.",
                    "De morphologie conservée, la population épithéliale se montre assez importante, polymorphe. Elle consiste surtout en cellules malpighiennes intermédiaires et superficielles.",
                    "D'aspect régulier, la desquamation épithéliale se montre de moyenne abondance, faite d'éléments malpighiens superficielles et intermédiaires, majoritairement.",
                    "La population épithéliale, d'abondance moyenne, est malpighienne, appartenant surtout aux couches supérieures et conserve un aspect régulier.",
                    "La population épithéliale est assez abondante, formée de cellules intermédiaires et superficielles majoritaires, montrant un aspect régulier.",
                    "D'aspect régulier morphologiquement, la desquamation épithéliale est assez abondante, dominée par les éléments malpighiens superficielles et intermédiaires."
                ]),
                ("polymorphe abondant superieur +", [
                    "D'aspect conservé, les cellules appartiennent en majorité aux couches hautes et sont nombreuses.",
                    "Abondant, le contingent épithélial reste morphologiquement régulier, provenant principalement des couches supérieures.",
                    "La population épithéliale est abondante, formée de cellules intermédiaires et superficielles majoritaires, montrant un aspect régulier.",
                    "D'aspect préservé morphologiquement, la desquamation épithéliale est abondante, formée de cellules malpighiennes intermédiaires et superficielles majoritairement.",
                    "Abondant, la population épithéliale reste morphologiquement régulière, issue en majorité des couches supérieures.",
                    "La population épithéliale se montre abondante et consiste en cellules malpighiennes, représentant majoritairement les couches supérieures du revêtement, et qui conservent un aspect régulier.",
                    "De morphologie régulière, la population épithéliale se montre abondante. Elle consiste principalement en cellules malpighiennes intermédiaires et superficielles.",
                    "Abondant, le matériel épithélial reste morphologiquement régulier, issu principalement des couches supérieures du revêtement.",
                    "Abondants, les groupements épithéliaux rapportés sont formés essentiellement de cellules malpighiennes intermédiaires et superficielles, d'aspect préservé.",
                    "De morphologie régulière, la population épithéliale est abondante, en majorité composée de cellules malpighiennes intermédiaires et superficielles.",
                    "D'aspect préservé morphologiquement, la desquamation épithéliale est abondante, formée de cellules malpighiennes intermédiaires et superficielles majoritairement.",
                    "La population épithéliale desquamée se montre nombreuse. Elle est composée surtout de cellules malpighiennes intermédiaires et superficielles, sans anomalie.",
                    "Abondant, le contingent épithélial se montre morphologiquement régulier, issu des couches supérieures principalement."
                ])
            ]
            },

            {
            "sub_name": "polymorphes majorite profondes",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("polymorphes modéré profondes+", [
                    "D'aspect régulier morphologiquement, la desquamation épithéliale est d'abondance modérée, dominée par les éléments malpighiens profonds.",
                    "Peu abondants, les groupements épithéliaux rapportés sont formés majoritairement de cellules malpighiennes profondes. Leur morphologie est régulière.",
                    "Peu riche, le contingent épithélial conserve un aspect morphologiquement régulier, et provient en majorité des couches basses.",
                    "Les groupements épithéliaux rapportés sont peu nombreux, dispersés, essentiellement des couches profondes, de morphologie régulière.",
                    "La population épithéliale se montre peu importante. Elle consiste principalement en cellules malpighiennes profondes, sans irrégularité observable.",
                    "D'aspect préservé morphologiquement, la population épithéliale est polymorphe d'abondance modérée, formée principalement d'éléments malpighiens profonds.",
                    "De morphologie régulière, la population épithéliale se montre modérée. Elle consiste principalement en cellules malpighiennes profondes.",
                    "D'aspect régulier, la desquamation épithéliale est d'abondance modérée, hétérogène composée surtout d'éléments malpighiens profonds.",
                    "D'aspect morphologique conservé, la population épithéliale se montre peu importante, de composition hétérogène. Elle consiste principalement en cellules malpighiennes profondes.",
                    "La population épithéliale desquamée se montre peu importante et consiste principalement en cellules malpighiennes profondes, sans anomalie.",
                    "Peu nombreux, la population épithéliale est principalement formée de cellules malpighiennes profondes. Elles sont d'aspect régulier.",
                    "D'aspect préservé, la desquamation épithéliale est d'abondance modérée, formée de cellules majoritairement profondes."
                ]),
                ("polymorphe moyen profondes+", [
                    "Les groupements épithéliaux rapportés sont issus des couches basses, assez nombreux, dispersés. Leur morphologie est régulière.",
                    "Il s'agit d'une population épithéliale de moyenne abondance, composée en majorité de cellules malpighiennes profondes. Elles sont d'aspect régulier.",
                    "Assez riche, le matériel épithélial reste morphologiquement régulier, issu principalement des couches basses du revêtement.",
                    "Assez nombreux, la population épithéliale est principalement formée de cellules malpighiennes profondes. Elles sont d'aspect régulier.",
                    "La desquamation épithéliale est de moyenne abondance, faite de cellules principalement profondes, sans modification notable.",
                    "D'aspect conservé, les cellules appartiennent en majorité aux couches profondes et sont assez nombreuses.",
                    "Les groupements épithéliaux rapportés sont polymorphes de type malpighien, assez nombreux, profonds. Leur morphologie est régulière.",
                    "De morphologie régulière, la population épithéliale se montre de moyenne abondance. Elle consiste principalement en cellules malpighiennes profondes.",
                    "D'aspect morphologique conservé, la desquamation épithéliale se montre assez importante et consiste surtout en cellules malpighiennes profondes.",
                    "La desquamation épithéliale est de moyenne abondance, faite de cellules principalement profondes, sans modification notable.",
                    "C'est une desquamation épithéliale de moyenne abondance qu'on retrouve. Elle est constituée principalement de cellules malpighiennes profondes, sans modification particulière.",
                    "La population épithéliale desquamée se montre assez importante et consiste principalement en cellules malpighiennes profondes, sans anomalie."
                ]),
                ("polymorphe abondant profondes+", [
                    "La population épithéliale est abondante, faite de cellules malpighiennes, profondes en majorité et qui conservent un aspect régulier.",
                    "De morphologie conservée, la population épithéliale se montre assez importante, polymorphe. Elle consiste surtout en cellules malpighiennes profondes.",
                    "C'est une population épithéliale abondante qu'on retrouve. Elle est constituée surtout de cellules malpighiennes profondes, sans modification particulière.",
                    "Abondante, la desquamation épithéliale se compose en majorité de cellules profondes, d'aspect régulier.",
                    "De morphologie conservée, la population épithéliale se montre polymorphe, assez importante. Elle est formée essentiellement de cellules malpighiennes profondes.",
                    "D'aspect préservé morphologiquement, la population épithéliale est abondante, en majorité des cellules malpighiennes profondes.",
                    "La population épithéliale est abondante. Elle consiste principalement en cellules malpighiennes, profondes qui conservent un aspect régulier.",
                    "Nombreux, la population épithéliale est principalement formée de cellules malpighiennes profondes. Elles sont d'aspect régulier.",
                    "D'aspect régulier, la desquamation épithéliale se montre abondante, faite d'éléments malpighiens profonds, majoritairement.",
                    "D'aspect morphologique conservé, la population épithéliale se montre assez importante, de composition hétérogène. Elle consiste principalement en cellules malpighiennes profondes.",
                    "C'est une desquamation épithéliale abondante qu'on retrouve. Elle est constituée principalement de cellules malpighiennes profondes, sans modification particulière.",
                    "La population épithéliale est abondante, faite de cellules malpighiennes, profondes en majorité et qui conservent un aspect régulier."
                ])
            ]
            },

            {
            "sub_name": "profondes",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("atrophique modéré", [
                    "Il s'agit d'une population épithéliale peu abondante, composée de cellules malpighiennes profondes. Elles sont d'aspect régulier.",
                    "D'aspect préservé, la population épithéliale est modérée. Elle est faite de cellules malpighiennes profondes.",
                    "Peu abondant, le contingent épithélial reste morphologiquement régulier, provenant des couches basses.",
                    "D'aspect morphologique régulier, la population épithéliale se montre peu importante. Elle consiste en cellules malpighiennes profondes.",
                    "D'aspect régulier, la desquamation épithéliale se montre d'abondance modérée, formée d'éléments malpighiens profonds.",
                    "D'aspect régulier, la desquamation épithéliale est assez modérée, formée d'éléments malpighiens profonds.",
                    "D'aspect morphologique conservé, la population épithéliale se montre peu importante. Elle consiste en cellules malpighiennes profondes.",
                    "Les groupements épithéliaux rapportés sont peu nombreux, atrophiques, dispersés, de morphologie régulière.",
                    "D'aspect préservé, la desquamation épithéliale est modérée, formée de cellules malpighiennes profondes.",
                    "La population épithéliale est modérée. Elle est constituée de cellules malpighiennes profondes, sans modification notable.",
                    "La population épithéliale d'abondance modérée, est malpighienne, atrophique et conserve un aspect régulier."
                ]),
                ("atrophique moyen", [
                    "La population épithéliale est de moyenne abondance, constituée de cellules malpighiennes, représentant les couches basses du revêtement, et conservant un aspect régulier.",
                    "D'aspect préservé, la population épithéliale est de moyenne abondance, formée de cellules malpighiennes profondes.",
                    "La population épithéliale est d'abondance moyenne. Elle consiste en cellules malpighiennes, profondes qui conservent un aspect régulier.",
                    "Le matériel épithélial, assez riche, est représenté par des cellules profondes, de morphologie conservée.",
                    "De moyenne abondance, les groupements épithéliaux rapportés sont formés de cellules malpighiennes profondes, d'aspect régulier.",
                    "La population épithéliale desquamée se montre assez importante et va consister en cellules malpighiennes profondes, sans anomalie.",
                    "D'aspect conservé, les cellules appartiennent aux couches profondes et sont d'abondance moyenne.",
                    "La population épithéliale desquamée se montre assez importante. Elle consiste en cellules malpighiennes profondes, sans modification anormale.",
                    "La population épithéliale est de moyenne abondance, constituée de cellules malpighiennes, représentant les couches basses du revêtement, et conservant un aspect régulier.",
                    "D'aspect préservé morphologiquement, la desquamation épithéliale est de moyenne abondance, formée de cellules malpighiennes profondes.",
                    "Assez abondant, le matériel épithélial reste morphologiquement régulier, issu des couches basses du revêtement.",
                    "C'est une desquamation épithéliale de moyenne abondance, constituée de cellules malpighiennes profondes, sans modification notable.",
                    "D'aspect morphologique conservé, la desquamation épithéliale se montre assez importante. Elle consiste en cellules malpighiennes profondes."
                ]),
                ("atrophique abondant", [
                    "D'aspect régulier morphologiquement, la population épithéliale est abondante, formée d'éléments malpighiens profondes.",
                    "D'aspect régulier morphologiquement, la desquamation épithéliale est abondante, formée d'éléments malpighiens profonds.",
                    "D'aspect préservé, la population épithéliale est abondante, formée de cellules malpighiennes profondes.",
                    "Abondant, le contingent épithélial se montre morphologiquement régulier, issu des couches basses.",
                    "Abondants, les groupements épithéliaux rapportés sont malpighiens, formés de cellules malpighiennes profondes, d'aspect régulier.",
                    "Abondants, les groupements épithéliaux sont formés de cellules malpighiennes profondes, morphologiquement régulier.",
                    "C'est une population épithéliale abondante qu'on retrouve, constituée de cellules malpighiennes profondes, sans modification particulière.",
                    "Les groupements épithéliaux rapportés sont nombreux, de caractère atrophique. Leur morphologie est régulière.",
                    "De morphologie conservée, la population épithéliale se montre importante. Elle est formée de cellules malpighiennes profondes.",
                    "D'aspect conservé, les cellules appartiennent aux couches profondes et sont abondants.",
                    "D'aspect préservé morphologiquement, la population épithéliale est abondante, formée de cellules malpighiennes profondes.",
                    "Les groupements épithéliaux rapportés, atrophiques, sont nombreux, dispersés. Leur morphologie est régulière.",
                    "D'aspect préservé morphologiquement, la desquamation épithéliale est abondante, formée d'éléments malpighiens profonds.",
                    "D'aspect régulier morphologiquement, la population épithéliale est abondante, formée d'éléments malpighiens profondes.",
                    "La population épithéliale se montre importante. Elle consiste en cellules malpighiennes profondes, sans irrégularité observable.",
                    "La population épithéliale desquamée se montre abondante. Elle consiste en cellules malpighiennes profondes, sans anomalie."
                ])
            ]
            },

            {
            "sub_name": "Hautes + cytolyse",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("supérieures modéré cytolyse+", [
                    "D'aspect conservé, les cellules appartiennent aux couches hautes et sont d'abondance modérée, un peu cytolytiques.",
                    "Les groupements épithéliaux rapportés sont peu nombreux, dispersés, parfois cytolytiques, de morphologie régulière.",
                    "De morphologie conservée, la desquamation épithéliale est d'abondance modérée. Elle se compose de cellules intermédiaires et superficielles, avec des variations cytolytiques.",
                    "D'abondance modérée, les groupements épithéliaux rapportés sont formés de cellules malpighiennes intermédiaires et superficielles, d'aspect régulier, cytolytiques par endroits.",
                    "D'aspect préservé, la population épithéliale est modérée, cytolytique, formée de cellules malpighiennes intermédiaires et superficielles.",
                    "D'aspect préservé, la desquamation épithéliale se montre peu importante. Elle est faite de cellules malpighiennes intermédiaires et superficielles, siège d'une cytolyse.",
                    "D'aspect préservé, la population épithéliale est modérée, cytolytique, formée de cellules malpighiennes intermédiaires et superficielles.",
                    "La population épithéliale desquamée se montre d'abondance modérée. Elle consiste en cellules malpighiennes intermédiaires et superficielles, présentant des remaniements cytolytiques, sans anomalie.",
                    "D'abondance modérée, les placards épithéliaux sont formés de cellules malpighiennes intermédiaires et superficielles, présentant des phénomènes de cytolyse, d'aspect régulier.",
                    "C'est une population épithéliale modérée qui est présente. Elle est constituée de cellules malpighiennes hautes, en partie cytolytiques, sans autre modification.",
                    "D'aspect régulier, la desquamation épithéliale se montre modérée, formée d'éléments malpighiens superficiels et intermédiaires, certains cytolytiques.",
                    "D'aspect préservé, la population épithéliale est modérée, cytolytique. Elle est faite de cellules malpighiennes intermédiaires et superficielles."
                ]),
                ("supérieur moyen cytolyse+", [
                    "La population épithéliale est abondante. Elle est constituée de cellules malpighiennes hautes qui sont le siège de phénomènes de cytolyse, sans atypies notables.",
                    "La desquamation épithéliale est abondante, faite de cellules hautes, sans modification notable, en dehors de la cytolyse.",
                    "D'aspect préservé, la desquamation épithéliale est moyennement abondante, formée de cellules malpighiennes intermédiaires et superficielles, avec cytolyse physiologique.",
                    "La population épithéliale est abondante. Elle consiste en cellules malpighiennes, intermédiaires et superficielles qui conservent un aspect régulier; de la cytolyse est constatée.",
                    "La population épithéliale est assez abondante, composée de cellules malpighiennes, représentant les couches supérieures du revêtement, montrant de la cytolyse, régulières.",
                    "D'aspect régulier morphologiquement, la desquamation épithéliale est assez abondante, formée d'éléments malpighiens superficiels et intermédiaires. Ils montrent de la cytolyse.",
                    "La population épithéliale abondante est malpighienne. Les cellules appartiennent aux couches supérieures, cytolytiques et conservent un aspect régulier.",
                    "D'aspect préservé, la desquamation épithéliale est assez importante. Elle est faite de cellules malpighiennes intermédiaires et superficielles plus ou moins cytolytiques.",
                    "Les groupements épithéliaux rapportés sont de type malpighien, relativement nombreux. Elles sont en partie cytolytiques, régulières.",
                    "La population épithéliale desquamée se montre assez importante. Elle consiste en cellules malpighiennes intermédiaires et superficielles, avec des éléments cytolytiques, sans modification anormale.",
                    "Abondants, les groupements épithéliaux rapportés sont formés de cellules intermédiaires et superficielles, plus ou moins cytolytiques, d'aspect conservé.",
                    "La population épithéliale est abondante, faite de cellules malpighiennes, intermédiaires et superficielles qui conservent un aspect régulier. On y observe de la cytolyse."
                ]),
                ("superieures abondant cytolyse+", ["Pas de phrase"])
            ]
            },

            {
            "sub_name": "Cylindriques",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("cylindriques rares", [
                    "Des cellules mucipares sont observées, préservées.",
                    "Présence de quelques cellules cylindriques, régulières.",
                    "Des cellules cylindriques assez rares sont présentes différenciées.",
                    "On retrouve quelques cellules endocervicales.",
                    "La population endocervicale est pauvre, sans anomalie.",
                    "La desquamation endocervicale est faible, constituée de cellules mucipares normales.",
                    "Des cellules cylindriques assez rares sont présentes différenciées.",
                    "Des cellules mucipares sont observées, préservées.",
                    "De rares cellules cylindriques sont rencontrées, conservées.",
                    "De rares cellules cylindriques sont rencontrées, conservées.",
                    "Les éléments endocervicaux sont peu nombreux, sans irrégularité.",
                    "La desquamation endocervicale est faible, constituée de cellules mucipares normales.",
                    "Des cellules mucipares sont observées, préservées."
                ]),
                ("cylindrique modérées", [
                    "La population endocervicale est modérée, sans anomalie.",
                    "Les groupements endocervicaux sont peu nombreux, sans irrégularité.",
                    "Présence de quelques placards de cellules cylindriques.",
                    "Des cellules cylindriques sont rencontrées, conservées.",
                    "On retrouve des groupements de cellules endocervicales.",
                    "La population endocervicale est modérée, sans anomalie.",
                    "La desquamation endocervicale est modérée, constituée de cellules mucipares normales.",
                    "La population endocervicale est modérée, sans anomalie.",
                    "Présence de quelques placards de cellules cylindriques.",
                    "Présence de quelques placards de cellules cylindriques.",
                    "Les groupements endocervicaux sont peu nombreux, sans irrégularité.",
                    "Des cellules mucipares sont observées, préservées.",
                    "Des cellules cylindriques sont présentes différenciées.",
                    "Des cellules mucipares sont observées, préservées.",
                    "Les groupements endocervicaux sont peu nombreux, sans irrégularité."
                ]),
                ("cylindrique abondant", [
                    "De nombreuses cellules cylindriques sont rencontrées, conservées.",
                    "Des placards de cellules mucipares sont observés, préservés.",
                    "Des placards de cellules mucipares sont observés, préservés.",
                    "Des cellules cylindriques assez nombreuses, sont présentes, différenciées.",
                    "De nombreuses cellules cylindriques sont rencontrées, conservées.",
                    "On retrouve des cellules endocervicales abondantes.",
                    "Présence de plusieurs placards de cellules cylindriques, régulières.",
                    "De nombreuses cellules cylindriques sont rencontrées, conservées.",
                    "De nombreuses cellules cylindriques sont rencontrées, conservées.",
                    "Les éléments endocervicaux sont nombreux, sans irrégularité.",
                    "On retrouve des cellules endocervicales abondantes.",
                    "On retrouve des cellules endocervicales abondantes.",
                    "La population endocervicale est riche, sans anomalie."
                ])
            ]
            },

            {
            "sub_name": "Cylindriques + Métaplasie",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("cylindrique modéré métaplasie+", [
                    "La population endocervicale est modérée, régulière, partiellement métaplasique.",
                    "La population endocervicale est modérée, régulière, partiellement métaplasique.",
                    "On retrouve des cellules endocervicales, certaines modifiées par la métaplasie.",
                    "Présence de placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "Présence de placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "La population endocervicale est modérée, régulière, partiellement métaplasique.",
                    "Présence de placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "Présence de placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "Présence de placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "La desquamation endocervicale est modérée, constituée de cellules mucipares normales, certaines métaplasiques.",
                    "Des cellules cylindriques peu nombreuses, sont présentes, différenciées ou parfois en métaplasie."
                ]),
                ("cylindrique modéré métaplasie++", [
                    "Les éléments endocervicaux sont peu nombreux, sans irrégularité, volontiers en métaplasie.",
                    "Des cellules cylindriques sont rencontrées, le plus souvent métaplasiques.",
                    "Des placards de cellules mucipares sont observés, la plupart métaplasiques.",
                    "La population endocervicale est modérée, régulière, métaplasique.",
                    "Présence de placards de cellules cylindriques, généralement transformées par la métaplasie.",
                    "Des cellules cylindriques peu nombreuses, sont présentes, métaplasiques pour la plupart.",
                    "La desquamation endocervicale est modérée, constituée de cellules mucipares normales ou plus souvent métaplasiques.",
                    "Les éléments endocervicaux sont peu nombreux, sans irrégularité, volontiers en métaplasie.",
                    "On retrouve des cellules endocervicales, plusieurs modifiées par la métaplasie.",
                    "Présence de placards de cellules cylindriques, généralement transformées par la métaplasie.",
                    "Des cellules cylindriques sont rencontrées, le plus souvent métaplasiques.",
                    "Les éléments endocervicaux sont peu nombreux, sans irrégularité, volontiers en métaplasie.",
                    "Les éléments endocervicaux sont peu nombreux, sans irrégularité, volontiers en métaplasie."
                ]),
                ("cylindrique abondant métaplasie+", [
                    "Présence de plusieurs placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "La population endocervicale est riche, régulière, partiellement métaplasique.",
                    "Présence de plusieurs placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "La population endocervicale est riche, régulière, partiellement métaplasique.",
                    "Des cellules cylindriques assez nombreuses, sont présentes, différenciées ou parfois en métaplasie.",
                    "De nombreuses cellules cylindriques sont rencontrées, conservées ou parfois métaplasiques.",
                    "La population endocervicale est riche, régulière, partiellement métaplasique.",
                    "De nombreuses cellules cylindriques sont rencontrées, conservées ou parfois métaplasiques.",
                    "Présence de plusieurs placards de cellules cylindriques, régulières ou transformées par la métaplasie.",
                    "On retrouve des cellules endocervicales abondantes, certaines modifiées par la métaplasie.",
                    "Des cellules cylindriques assez nombreuses, sont présentes, différenciées ou parfois en métaplasie.",
                    "Des cellules cylindriques assez nombreuses, sont présentes, différenciées ou parfois en métaplasie."
                ]),
                ("cylindrique abondant métaplasie++", [
                    "Présence de plusieurs placards de cellules cylindriques, généralement transformées par la métaplasie.",
                    "Des cellules cylindriques assez nombreuses, sont présentes, métaplasiques pour la plupart.",
                    "De nombreuses cellules cylindriques sont rencontrées, le plus souvent métaplasiques.",
                    "La population endocervicale est riche, régulière, métaplasique.",
                    "Des cellules cylindriques assez nombreuses, sont présentes, métaplasiques pour la plupart.",
                    "Les éléments endocervicaux sont nombreux, sans irrégularité, volontiers en métaplasie.",
                    "On retrouve des cellules endocervicales abondantes, plusieurs modifiées par la métaplasie.",
                    "La desquamation endocervicale est abondante, constituée de cellules mucipares normales ou plus souvent métaplasiques.",
                    "De nombreuses cellules cylindriques sont rencontrées, le plus souvent métaplasiques.",
                    "Les éléments endocervicaux sont nombreux, sans irrégularité, volontiers en métaplasie.",
                    "Présence de plusieurs placards de cellules cylindriques, généralement transformées par la métaplasie.",
                    "On retrouve des cellules endocervicales abondantes, plusieurs modifiées par la métaplasie.",
                    "Des cellules cylindriques assez nombreuses, sont présentes, métaplasiques pour la plupart.",
                    "La desquamation endocervicale est abondante, constituée de cellules mucipares normales ou plus souvent métaplasiques."
                ])

            ]
            },
          
            {
            "sub_name": "Cytolyse",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("cytolyse", [
                    "Des modifications cytolytiques sont observées.",
                    "Des remaniements en rapport avec la cytolyse sont constatées.",
                    "Des phénomènes de cytolyse s'observent.",
                    "Des modifications cytolytiques sont observées.",
                    "Des phénomènes de cytolyse s'observent.",
                    "Présence d'une cytolyse physiologique.",
                    "Des changements cytolytiques sont notés.",
                    "Des changements cytolytiques sont notés.",
                    "Des modifications cytolytiques sont observées.",
                    "Des modifications cytolytiques sont observées.",
                    "Des modifications cytolytiques sont observées.",
                    "Des changements cytolytiques sont notés.",
                    "On observe des remaniements cytolytiques.",
                    "Des remaniements en rapport avec la cytolyse sont constatées.",
                    "Présence d'une cytolyse physiologique.",
                    "Présence d'une cytolyse physiologique.",
                    "Des modifications cytolytiques sont observées.",
                    "Des phénomènes de cytolyse s'observent."
                ])
            ]
            },

            {
            "sub_name": "Malpighien particulier",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("clue-cells+", [
                    "Des clue-cells sont observés, au sein de la desquamation épithéliale.",
                    "On rencontre des clue-cells.",
                    "Des clue-cells sont présents parmi les cellules malpighiennes.",
                    "Des clue-cells sont observés, au sein de la desquamation épithéliale.",
                    "Des éléments à cytoplasme granulaire du type clue-cell sont présents.",
                    "Des éléments à cytoplasme granulaire du type clue-cell sont présents.",
                    "Des clue-cells sont observés.",
                    "Des éléments à cytoplasme granulaire du type clue-cell sont présents.",
                    "Des éléments à cytoplasme granulaire du type clue-cell sont présents.",
                    "Des clue-cells sont présents parmi les cellules malpighiennes.",
                    "La population épithéliale a intéressé des clue-cells.",
                    "Des clue-cells sont observés."
                ]),
                ("clue-cell++", [
                    "La population épithéliale contient un grand nombre de clue-cells.",
                    "La population épithéliale contient un grand nombre de clue-cells.",
                    "La population épithéliale contient un grand nombre de clue-cells.",
                    "La population épithéliale contient un grand nombre de clue-cells.",
                    "Plusieurs clue-cells sont présents parmi les cellules malpighiennes.",
                    "On rencontre des clue-cells en abondance.",
                    "De nombreux clue-cells sont observés.",
                    "Des altérations de type clue-cell sont constatées, nombreuses.",
                    "La population épithéliale contient un grand nombre de clue-cells.",
                    "Des altérations de type clue-cell sont constatées, nombreuses.",
                    "De nombreux éléments à cytoplasme granulaire du type clue-cell sont présents.",
                    "De nombreux éléments à cytoplasme granulaire du type clue-cell sont présents.",
                    "On retrouve en abondance des clue-cells au sein de la population malpighienne.",
                    "Plusieurs clue-cells sont présents parmi les cellules malpighiennes."
                ]),
                ("koilocytes", [
                    "Des modifications correspondant à des koïlocytes sont notées.",
                    "Des altérations cellulaires correspondant à des koïlocytes sont notées.",
                    "Des altérations cellulaires correspondant à des koïlocytes sont notées.",
                    "Présence de koïlocytes.",
                    "Des koïlocytes sont présents.",
                    "Des altérations cellulaires correspondant à des koïlocytes sont notées.",
                    "Présence de koïlocytes.",
                    "Présence de koïlocytes.",
                    "Des modifications correspondant à des koïlocytes sont notées.",
                    "Des koïlocytes sont présents.",
                    "Présence de koïlocytes.",
                    "On rencontre des cellules de type koïlocyte.",
                    "Des modifications cellulaires compatibles avec des koïlocytes sont notées.",
                    "Présence de koïlocytes.",
                    "S'y associent des éléments de type koïlocyte.",
                    "Des altérations cellulaires correspondant à des koïlocytes sont notées.",
                    "On note la présence de koïlocytes."
                ]),
                ("koilocytes et dyskératocytes", [
                    "On retrouve aussi des koïlocytes épars, à côté de dyskératocytes.",
                    "Des koïlocytes et dyskératocytes sont présents.",
                    "Des altérations cellulaires correspondant à des koïlocytes sont notées, ainsi que de la dyskératose.",
                    "Des altérations cellulaires correspondant à des koïlocytes sont notées, ainsi que de la dyskératose.",
                    "Présence de koïlocytes associés à des dyskératocytes.",
                    "Des modifications correspondant à des dyskératocytes et des koïlocytes sont notées.",
                    "Des koïlocytes et dyskératocytes sont identifiés.",
                    "Des modifications cellulaires compatibles avec des koïlocytes sont notées, escortés de dyskératocytes.",
                    "Des koïlocytes et dyskératocytes sont présents.",
                    "Des altérations cellulaires compatibles avec des koïlocytes sont notées, ainsi que des dyskératocytes.",
                    "Des koïlocytes et dyskératocytes sont identifiés.",
                    "Des koïlocytes et dyskératocytes sont identifiés.",
                    "Des modifications cellulaires compatibles avec des koïlocytes sont notées, escortés de dyskératocytes."
                ]),
                ("dyskératocytes", [
                    "Des dyskératocytes sont présents.",
                    "On retrouve des dyskératocytes.",
                    "On rencontre des cellules de type dyskératocyte.",
                    "Des altérations cellulaires dyskératosiques sont notées.",
                    "Des modifications correspondant à des dyskératocytes sont notées.",
                    "Des modifications correspondant à des dyskératocytes sont notées.",
                    "On retrouve aussi épars des dyskératocytes.",
                    "S'y associent des éléments dyskératosiques.",
                    "On retrouve des dyskératocytes.",
                    "Des modifications cellulaires dyskératosiques s'observent.",
                    "Des modifications correspondant à des dyskératocytes sont notées.",
                    "Des dyskératocytes sont présents.",
                    "On retrouve aussi des dyskératocytes.",
                    "Des modifications cellulaires dyskératosiques s'observent.",
                    "S'y associent des éléments dyskératosiques.",
                    "On retrouve aussi épars des dyskératocytes."
                ]),
                ("binuclées", ["Pas de Phrase"])

            ]
            },

            {
            "sub_name": "irritation",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("irritation +", [
                    "Des remaniements irritatifs sont aussi constatés.",
                    "On note des groupements de caractère irrité.",
                    "On note la présence de remaniements irritatifs.",
                    "On note la présence de remaniements irritatifs.",
                    "On note la présence d'altérations irritatives.",
                    "Des amas irrités sont rencontrés.",
                    "Placards malpighiens conservés et irrités se côtoient.",
                    "A noter la présence de changements irritatifs.",
                    "On rencontre des placards irrités.",
                    "On note la présence de remaniements irritatifs.",
                    "Des amas irrités sont rencontrés.",
                    "A noter la présence de changements irritatifs.",
                    "Parmi les groupements épithéliaux, sont présents des placards irrités.",
                    "Présence de groupements d'aspect irrité.",
                    "Des remaniements irritatifs sont notés."
                ]),
                ("irritation++", [
                    "On note la présence de francs remaniements irritatifs.",
                    "Des amas très irrités sont rencontrés.",
                    "On rencontre côte à côte des placards malpighiens préservés et des amas très irrités.",
                    "Placards malpighiens conservés ou bien très irrités se côtoient.",
                    "Des remaniements irritatifs, assez marqués, sont aussi constatés.",
                    "Présence de placards de caractère très irrité.",
                    "Placards malpighiens conservés ou bien très irrités se côtoient.",
                    "Des cellules modifiées, de caractère bien irrité, sont présentes.",
                    "On observe la présence de plusieurs changements irritatifs.",
                    "On rencontre des placards irrités, nombreux.",
                    "Plusieurs amas remaniés modifiés par l'irritation sont observés.",
                    "Des placards altérés, bien irrités sont observés.",
                    "Des remaniements irritatifs prononcés sont notés.",
                    "Placards malpighiens conservés ou bien très irrités se côtoient.",
                    "Des remaniements irritatifs, assez marqués, sont aussi constatés.",
                    "Des amas très irrités sont rencontrés."
                ]),
                ("irritation+++", [
                    "On rencontre des placards irrités, très nombreux.",
                    "Des signes de souffrance marquée sont observés au sein du matériel épithélial.",
                    "On note la présence de nombreuses modifications irritatives nettes.",
                    "Des cellules modifiées, très nombreuses, de caractère bien irrité, sont présentes.",
                    "On note la présence de nombreuses modifications irritatives nettes.",
                    "Des cellules modifiées, très nombreuses, de caractère bien irrité, sont présentes.",
                    "Placards malpighiens peu conservés, et groupements très irrités se côtoient.",
                    "Présence de groupements nombreux, d'aspect bien irrité.",
                    "On observe souvent la présence de plusieurs changements irritatifs.",
                    "On constate la présence de très nombreux groupements irrités.",
                    "On note la présence de nombreuses modifications irritatives nettes.",
                    "On note plusieurs groupements de caractère bien irrité.",
                    "Parmi les groupements épithéliaux, sont présents des placards nettement irrités, nombreux."
                ]),
                ("exocytose+", [
                    "Des foyers d'exocytose sont observés.",
                    "On retrouve quelques foyers d'exocytose.",
                    "La desquamation épithéliale va présenter des foyers d'exocytose modérée.",
                    "Les placards épithéliaux sont par endroits le siège d'une exocytose modérée.",
                    "La desquamation épithéliale se caractérise par une exocytose modérée.",
                    "La desquamation épithéliale est par endroits le siège d'une exocytose modérée.",
                    "La desquamation épithéliale va présenter des foyers d'exocytose modérée.",
                    "La population épithéliale est par endroits le siège d'une exocytose modérée.",
                    "La population épithéliale est par endroits le siège d'une exocytose modérée.",
                    "Quelques foyers d'exocytose sont constatés au sein des placards épithéliaux.",
                    "Une exocytose peu marquée est retrouvée.",
                    "La desquamation épithéliale est par endroits le siège d'une exocytose modérée.",
                    "Quelques foyers d'exocytose sont notés.",
                    "La population épithéliale est par endroits le siège d'une exocytose modérée.",
                    "Une exocytose modérée est constatée."
                ]),
                ("exocytose++", [
                    "La population épithéliale se caractérise par de l'exocytose.",
                    "La desquamation épithéliale se caractérise par une exocytose assez marquée.",
                    "Les placards épithéliaux sont par endroits le siège d'une exocytose.",
                    "Une exocytose est constatée.",
                    "Des foyers d'exocytose sont notés.",
                    "La desquamation épithéliale va présenter des foyers d'exocytose assez franche.",
                    "Des foyers d'exocytose sont constatés au sein des placards épithéliaux.",
                    "Des foyers d'exocytose sont notés au sein de la composante épithéliale.",
                    "La desquamation épithéliale est le siège d'une exocytose.",
                    "La desquamation épithéliale va présenter des foyers d'exocytose.",
                    "Une exocytose marquée est retrouvée.",
                    "Les placards épithéliaux sont par endroits le siège d'une exocytose."
                ]),
                ("exocytose+++", ["Pas de phrase"]),

            ]
            },

            {
            "sub_name": "Dystrophique",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("dystrophique seul+", [
                    "Des modifications sont constatées, dystrophiques.",
                    "Des changements dystrophiques sont observés.",
                    "On observe des modifications de caractère dystrophique.",
                    "On observe quelques modifications de caractère dystrophique.",
                    "On observe quelques remaniements dystrophiques.",
                    "Des remaniements dystrophiques sont constatés.",
                    "Des modifications de caractère dystrophique sont notées."
                ]),
                ("dystrophique seul++", [
                    "Des remaniements dystrophiques importants sont constatés.",
                    "Des modifications de caractère dystrophique sont constatées, importantes.",
                    "On observe des remaniements de caractère dystrophique.",
                    "Des modifications de caractère dystrophique assez marquées sont notées.",
                    "De franches modifications dystrophiques sont observées.",
                    "D'importantes modifications sont constatées, de caractère dystrophique.",
                    "Des modifications dystrophiques marquées sont constatées.",
                    "Des changements dystrophiques prononcés sont constatés.",
                    "On observe de franches modifications de caractère dystrophique."
                ]),
                ("métaplasie seule", [
                    "Parmi les groupements épithéliaux, sont présents des placards métaplasiques.",
                    "On constate la présence de groupements métaplasiques.",
                    "A noter la présence de remaniements métaplasiques.",
                    "Des amas métaplasiques sont rencontrés.",
                    "On observe la présence de remaniements métaplasiques.",
                    "On note la présence de remaniements de caractère métaplasique.",
                    "On note la présence de modifications métaplasiques.",
                    "Des cellules dystrophiques, de caractère métaplasique, sont présentes.",
                    "Placards malpighiens et métaplasiques se côtoient.",
                    "Des amas remaniés modifiés par la métaplasie sont observés."
                ]),
                ("métaplasie immature", [
                    "Des cellules dystrophiques, de caractère métaplasique, immature pour certains, sont présentes.",
                    "Placards malpighiens et métaplasiques se côtoient, quelques-uns de caractère immature.",
                    "Des remaniements métaplasiques, parfois immatures, sont observés.",
                    "Parmi les groupements épithéliaux, sont présents des placards métaplasiques, certains de caractère immature.",
                    "Des placards en métaplasie sont observés, pour certains immatures.",
                    "On note la présence de remaniements métaplasiques, partiellement immatures.",
                    "Des amas métaplasiques sont rencontrés, dont un contingent immature.",
                    "On observe la présence de remaniements métaplasiques.",
                    "Des amas de caractère métaplasique sont rencontrés, dont un contingent immature.",
                    "On note la présence de remaniements de caractère métaplasique, parfois immature.",
                    "Des remaniements métaplasiques, certains de caractère immature, sont aussi constatés."
                ]),
                ("dystrophique type métaplasique", [
                    "On observe quelques modifications de caractère dystrophique, métaplasique.",
                    "Des remaniements dystrophiques métaplasiques sont constatés.",
                    "Des modifications dystrophiques de type métaplasie sont observées.",
                    "Des remaniements dystrophiques métaplasiques s'observent.",
                    "Des modifications de caractère dystrophique, surtout métaplasiques, sont notées."
                ]),
                ("dystrophique type hyperplasie", [
                    "Des modifications de caractère dystrophique, surtout hyperplasiques, sont notées.",
                    "Des modifications dystrophiques de type hyperplasie sont observées.",
                    "Des modifications dystrophiques, hyperplasiques sont constatées.",
                    "On observe quelques modifications de caractère dystrophique, hyperplasique.",
                    "Des remaniements dystrophiques hyperplasiques sont constatés.",
                    "Des remaniements dystrophiques hyperplasiques s'observent.",
                    "Des changements dystrophiques, en particulier de l'hyperplasie, sont constatés."
                ]),
                ("dystrophique metaplasie + hyperplasie", [
                    "Des modifications de caractère dystrophique, comprenant des amas métaplasiques et hyperplasiques, sont notées.",
                    "Des modifications dystrophiques, métaplasiques et hyperplasiques sont constatées.",
                    "Des changements dystrophiques, métaplasiques et hyperplasiques, sont observés.",
                    "On observe quelques remaniements de caractère dystrophique, consistant en métaplasie et hyperplasie.",
                    "Des remaniements dystrophiques, mêlant métaplasie et hyperplasie s'observent.",
                    "Des modifications de caractère dystrophique, à la fois hyperplasiques et métaplasiques, sont constatées.",
                    "Des remaniements dystrophiques hyperplasiques et métaplasiques sont constatés.",
                    "Les changements observés sont dystrophiques, métaplasiques et hyperplasiques."
                ]),
                ("squames rares", [
                    "Des cellules squameuses sont observées, rares.",
                    "Présence de quelques squames.",
                    "De rares cellules squameuses sont rencontrées.",
                    "Des squames dispersées sont notées.",
                    "Des éléments squameux s'observent.",
                    "On retrouve quelques éléments squameux.",
                    "Des cellules squameuses assez rares sont présentes.",
                    "La desquamation comporte de rares squames."
                ]),
                ("squames++", [
                    "Des éléments squameux s'observent épars.",
                    "De nombreuses cellules squameuses sont rencontrées.",
                    "Des cellules squameuses sont observées.",
                    "Présence de plusieurs squames.",
                    "La desquamation comporte des squames.",
                    "On retrouve des éléments squameux.",
                    "Plusieurs squames dispersées sont notées."
                ]),
                ("squames anuclées + parakératosiques", [
                    "Des éléments squameux parfois parakératosiques s'observent, épars.",
                    "Présence de cellules anucléées et parakératosiques.",
                    "On retrouve des éléments squameux, parakératosiques et anucléées.",
                    "Des cellules squameuses anucléées ou parakératosiques sont observées.",
                    "Des cellules squameuses, certaines parakératosiques sont présentes.",
                    "Des cellules squameuses anucléées et parakératosiques sont rencontrées.",
                    "La desquamation comporte des squames parakératosiques et anucléées."
                ])

            ]
            }
        ]
    },

    #10TH group
    {
        "name": "Conclusion",
        "bg_color": "beige",
        "buttons": [
            {
            "sub_name": "RAS",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("OK", [
                    "Conclusion : On ne retrouve pas de lésion intra-épithéliale ou de malignité au niveau de ce col.",
                    "Conclusion : ce col ne présente pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Prélèvement sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Frottis ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Il n'y a pas de lésion intra-épithéliale, ni de malignité sur ce prélèvement.",
                    "Conclusion : On n'observe pas de lésion intra-épithéliale ou de malignité sur ce col."
                ])
            ]
            },

            {
            "sub_name": "dystrophique",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("ectropion", [
                    "Conclusion : Col siège d'un ectropion. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect en faveur d'un ectropion, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Aspect d'ectropion. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Il s'agit d'un ectropion, sans lésion intra-épithéliale ni malignité."
                ]),
                ("ectropion inflammatoire", [
                    "Conclusion : Aspect compatible avec un ectropion inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect cytologique d'ectropion inflammatoire. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence d'un ectropion inflammatoire, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Ces aspects correspondent à un ectropion inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect en faveur d'un ectropion inflammatoire, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Il s'agit d'un ectropion inflammatoire, sans lésion intra-épithéliale ni malignité."
                ]),
                ("ectropion metaplasique", [
                    "Conclusion : Il s'agit d'un ectropion en métaplasie, sans lésion intraépithéliale, ni malignité.",
                    "Conclusion : Ces aspects correspondent à un ectropion métaplasique, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect d'ectropion métaplasique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col siège d'un ectropion métaplasique, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Aspect cytologique d'ectropion métaplasique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence d'un ectropion remanié, métaplasique, ne montrant pas de lésion intra-épithéliale ou de malignité."
                ]),

                ("ectropion minime", [
                    "Conclusion : Aspect en faveur d'un ectropion minime, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Aspect compatible avec un petit ectropion, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col siège d'un ectropion minime, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Aspect cytologique d'ectropion minime. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Il s'agit d'un ectropion minime, sans lésion intraépithéliale, ni malignité."
                ]),
                ("ectropion minime inflammatoire", [
                    "Conclusion : Présence d'un ectropion minime inflammatoire, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect d'ectropion minime inflammatoire. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Ces aspects correspondent à un léger ectropion inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Il s'agit d'un petit ectropion inflammatoire, sans lésion intraépithéliale, ni malignité.",
                    "Conclusion : Col siège d'un petit ectropion inflammatoire. Absence de lésion intra-épithéliale ou de malignité."
                ]),
                ("ectropion minime métaplasique", [
                    "Conclusion : Col siège d'un petit ectropion métaplasique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence d'un ectropion minime remanié, métaplasique, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Ces aspects correspondent à un léger ectropion métaplasique, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col siège d'un ectropion minime métaplasique, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Il s'agit d'un petit ectropion en métaplasie, sans lésion intraépithéliale, ni malignité."
                ]),
                ("ectropion inflammatoire metaplasique", [
                    "Conclusion : Il s'agit d'un ectropion inflammatoire et métaplasique, sans lésion intraépithéliale, ni malignité.",
                    "Conclusion : Col siège d'un ectropion remanié inflammatoire et métaplasique, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Présence d'un ectropion inflammatoire et métaplasique, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Ces aspects correspondent à un ectropion remanié, métaplasique et inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col siège d'un ectropion inflammatoire, remanié par la métaplasie. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect compatible avec un ectropion en remaniement métaplasique et inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect cytologique d'ectropion métaplasique et inflammatoire. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect en faveur d'un ectropion inflammatoire et métaplasique, sans lésion intra-épithéliale ou malignité."
                ]),
                ("ectropion minime inflammatoire metaplasique", [
                    "Conclusion : Présence d'un ectropion minime inflammatoire et métaplasique, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col siège d'un petit ectropion inflammatoire, remanié par la métaplasie. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col siège d'un petit ectropion remanié inflammatoire et métaplasique, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Ces aspects correspondent à un ectropion minime remanié, métaplasique et inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect d'ectropion minime inflammatoire et métaplasique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Il s'agit d'un petit ectropion inflammatoire et métaplasique, sans lésion intraépithéliale, ni malignité.",
                    "Conclusion : Aspect en faveur d'un petit ectropion inflammatoire et métaplasique, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Aspect cytologique d'ectropion minime métaplasique et inflammatoire. Absence de lésion intra-épithéliale ou de malignité."
                ]),
                ("col atrophique", [
                    "Conclusion : Ces aspects sont ceux d'un frottis atrophique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Modifications de caractère atrophique, sans lésion intraépithéliale ou malignité.",
                    "Conclusion : Aspect atrophique, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Frottis atrophique, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Aspect d'atrophie. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col atrophique. Absence de lésion intra-épithéliale ou de malignité."
                ]),
                ("col dystrophique", [
                    "Conclusion : Présence de remaniements dystrophiques. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col dystrophique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence de modifications dystrophiques. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect de col dystrophique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Les modifications observées sur ce col sont de caractère dystrophique, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Frottis dystrophique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Ces aspects sont ceux d'un col dystrophique. Absence de lésion intra-épithéliale ou de malignité."
                ]),
                ("col dystrophique atrophique", [
                    "Conclusion : Frottis dystrophique de la ménopause. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Les modifications constatées sont de caractère dystrophique, observables au cours de la ménopause, sans lésion intra-épithéliale ou malignité sur ce col.",
                    "Conclusion : Col remanié, dystrophique de la ménopause. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col de caractère remanié, dystrophique de ménopause. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Les modifications observées sur ce col sont de caractère dystrophique, compatibles avec l'atrophie, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Col atrophique, de caractère dystrophique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col dystrophique de la ménopause, ne montrant pas de lésion intra-épithéliale ou de malignité."
                ])
            ]
            },

            {
            "sub_name": "specifique",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("col gardnerella", [
                    "Conclusion : Aspect de vaginose bactérienne. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect cytologique de vaginose bactérienne. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Vaginose bactérienne, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Aspect compatible avec une vaginose bactérienne, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence d'une vaginose bactérienne, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Frottis siège de gardnerella, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Frottis siège d'une vaginose bactérienne, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Il s'agit d'une vaginose bactérienne, sans lésion intraépithéliale, ni malignité."
                ]),
                ("col mycose", [
                    "Conclusion : Aspect de mycose, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Aspect cytologique de mycose. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Il s'agit d'une mycose, sans lésion intraépithéliale, ni malignité.",
                    "Conclusion : Frottis siège d'une mycose. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Ces aspects correspondent à une mycose, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Prélèvement montrant la présence de mycose. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence de mycose, sans lésion intra-épithéliale ou de malignité."
                ]),
                ("col actinomycose", [
                    "Conclusion : Présence d'une actinomycose, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Prélèvement montrant la présence d'actinomycose. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect d'actinomycose, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Aspect cytologique d'actinomycose. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Il s'agit d'une actinomycose, sans lésion intraépithéliale, ni malignité.",
                    "Conclusion : Frottis siège d'une actinomycose. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence d'actinomycose, sans lésion intra-épithéliale ou de malignité."
                ]),
                ("col trichomonas", [
                    "Conclusion : Prélèvement montrant la présence de trichomonas. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect cytologique de trichomonase. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Frottis siège de trichomonas. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect de trichomonas, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Ces aspects correspondent à du trichomonas, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence de trichomonas, sans lésion intra-épithéliale, ni malignité."
                ])
           ]
            },


            {
            "sub_name": "inflammatoire",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("col inflammatoire", [
                    "Conclusion : Remaniements de caractère inflammatoire, sans spécificité. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect inflammatoire. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Frottis inflammatoire non spécifique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Modifications de caractère inflammatoire, sans spécificité. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Modifications inflammatoires non spécifiques. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Modifications inflammatoires sans caractère spécifique. Absence de lésion intra-épithéliale ou de malignité."
                ]),

                ("col inflammatoire faible", [
                    "Conclusion : Présence de quelques signes d'inflammation banale, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Discrète inflammation banale sans lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence d'une inflammation discrète sans caractère spécifique, sans lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Ces aspects correspondent à un col de caractère peu inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect de col discrètement inflammatoire. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col présentant quelques signes inflammatoires, sans lésion intra-épithéliale, ni malignité."
                ]),
                ("col inflammatoire modéré", [
                    "Conclusion : Présence d'une inflammation banale, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence de signes d'une inflammation peu marquée, sans lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Présence de quelques signes inflammatoires. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col modérément inflammatoire, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Frottis modérément inflammatoire, sans lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col de caractère inflammatoire, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Présence d'une inflammation peu marquée sans caractère spécifique, sans lésion intra-épithéliale ou de malignité."
                ]),
                ("col très inflammatoire", [
                    "Conclusion : Inflammation banale franche, sans lésion intra-épithéliale ou malignité.",
                    "Conclusion : Ces aspects correspondent à un col de caractère très inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Aspect cytologique d'une inflammation prononcée. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col intensément inflammatoire, sans lésion intra-épithéliale, ni malignité.",
                    "Conclusion : Col siège d'une inflammation non spécifique, importante. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Frottis inflammatoire marqué. Absence de lésion intra-épithéliale ou de malignité.",
                    "Conclusion : Col de caractère inflammatoire prononcé, sans lésion intra-épithéliale ou malignité."
                ]),
                ("col très inflammatoire contrôlé", [
                    "Conclusion : Frottis inflammatoire marqué, sans lésion intraépithéliale ni malignité, à contrôler.",
                    "Conclusion : Inflammation banale franche. Absence de lésion intra-épithéliale ou de malignité, à contrôler.",
                    "Conclusion : Col de caractère inflammatoire prononcé, sans lésion intra-épithéliale ou malignité, à contrôler.",
                    "Conclusion : Col siège d'une inflammation non spécifique, importante. Absence de lésion intra-épithéliale ou de malignité. À contrôler.",
                    "Conclusion : Aspect de col remanié, inflammatoire. Absence de lésion intra-épithéliale ou de malignité, à contrôler.",
                    "Conclusion : Ces aspects correspondent à un col très inflammatoire, ne présentant pas de lésion intra-épithéliale ou de malignité, à contrôler.",
                    "Conclusion : Aspect cytologique d'une inflammation prononcée. Absence de lésion intra-épithéliale ou de malignité, à contrôler.",
                    "Conclusion : Col intensément inflammatoire, sans lésion intra-épithéliale ni malignité, à contrôler."
                ])
           ]
            },

            {
            "sub_name": "atypies",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("ASC-US*", [
                    "Conclusion : Col montrant des lésions malpighiennes atypiques de signification indéterminée de type ASC-US*.",
                    "Conclusion : Col présentant des modifications de signification indéterminée (ASC-US*).",
                    "Conclusion : Présence d'atypies malpighiennes de signification indéterminée (ASC-US*).",
                    "Conclusion : Présence d'atypies de caractère indéterminé (ASC-US*).",
                    "Conclusion : Col présentant des modifications de type ASC-US*.",
                    "Conclusion : Modifications de signification indéterminée (ASC-US*)."
                ]),
                ("ASC-H*", [
                    "Conclusion : Présence de remaniements indéterminés, ne pouvant écarter une lésion de haut grade (ASC-H*).",
                    "Conclusion : Présence de lésions épithéliales malpighiennes de type ASC-H*, ne permettant pas d'exclure une lésion de haut grade.",
                    "Conclusion : Col siège d'atypies malpighiennes de type ASC-H* qui n'élimine pas une possible lésion de haut grade.",
                    "Conclusion : Col siège d'une lésion atypique, ne pouvant éliminer une possible lésion de haut grade (ASC-H*).",
                    "Conclusion : Présence de lésions malpighiennes de type ASC-H* qui ne peuvent éliminer un haut grade."
                ]),
                ("AGC*", [
                    "Conclusion : Présence de lésion de cellules glandulaires de type AGC*.",
                    "Conclusion : Col siège de lésion d'AGC*.",
                    "Conclusion : Lésion de type AGC*."
                ]),
                ("note asc-us", [
                    "*ASC-US : Atypical Squamous Cells of Undetermined Significance.",
                    "*ASC-US = Atypical Squamous Cells of Undetermined Significance."
                ]),
                ("note asc-h", [
                    "*ASC-H : Atypical Squamous Cells cannot exclude a High intraepithelial lesion."
                ]),
                ("note AGC", [
                    "*AGC: Atypical Glandular Cells."
                ]),
                ("HPV faible", [
                    "Modifications cytologiques en rapport avec la présence d'HPV (lésion intra-épithéliale de bas grade).",
                    "Col montrant des signes d'une présence d'HPV (lésion intra-épithéliale de bas grade).",
                    "Signes cytologiques d'infestation à HPV (lésion de bas grade).",
                    "Présence de signes d'HPV (lésion intra-épithéliale de bas grade).",
                    "Présence d'HPV (lésion intra-épithéliale de bas grade)."
                ]),
                ("HPV", [
                    "Frottis montrant la présence d'HPV (lésion intra-épithéliale de bas grade).",
                    "Col présentant des signes d'infestation à HPV (lésion intra-épithéliale de bas grade).",
                    "Présence d'HPV (lésion intra-épithéliale de bas grade).",
                    "Signes cytologiques d'HPV (lésion intra-épithéliale de bas grade) sur ce col.",
                    "Signes cytologiques d'infestation à HPV (lésion de bas grade)."
                ]),
                ("HPV+ CIN1", [
                    "Présence d'une dysplasie CIN1 avec signes d'HPV (lésion intra-épithéliale de bas grade).",
                    "Lésion dysplasique CIN1 avec HPV (lésion intra-épithéliale de bas grade).",
                    "Col siège d'une CIN1 dans un contexte d'HPV (lésion intra-épithéliale de bas grade).",
                    "Aspect d'infestation à HPV avec dysplasie CIN1 (lésion intra-épithéliale de bas grade).",
                    "Aspect de condylome, associé à une dysplasie CIN1 (lésion intra-épithéliale de bas grade)."
                ]),
                ("CIN1", [
                    "Aspect d'une dysplasie CIN1 (lésion intra-épithéliale de bas grade).",
                    "Présence d'une dysplasie CIN1 (lésion intra-épithéliale de bas grade).",
                    "Lésion de CIN1 (lésion de bas grade).",
                    "Lésion dysplasique CIN1 (lésion intra-épithéliale de bas grade)."
                ]),
                ("CIN2", [
                    "Aspect cytologique en faveur d'une dysplasie CIN2 (lésion intraépithéliale de haut grade).",
                    "Lésion dysplasique CIN2 (lésion de haut grade).",
                    "Présence d'une dysplasie CIN2 (lésion de haut grade).",
                    "Il s'agit de dysplasie CIN2 (lésion intraépithéliale de haut grade)."
                ]),
                ("CIN3", [
                    "Lésion de CIN3 (haut grade).",
                    "Lésion dysplasique CIN2-CIN3 (haut grade).",
                    "Aspect en faveur d'une CIN3 (lésion de haut grade)."
                ]),
                ("suspect de malignite", [
                    "Présence de cellules atypiques, suspectes de malignité. À explorer.",
                    "Présence d'amas cellulaires suspects. À explorer."
                ])

            ]
            },

            {
            "sub_name": "Vagin",  # This is the new sub-name
            "bg_color": "lightgreen",  # You can assign a different color to the subcategory
            "buttons": [
                ("V. mycose", ["Pas de phrase"]),
                ("V. gardnerella", ["Pas de phrase"]),
                ("V. HPV", ["Pas de phrase"]),
                ("Vagin RAS", [
                    "Prélèvement sans lésion intra-épithéliale ou malignité.",
                    "Absence de lésion intraépithéliale ou de malignité à l'examen.",
                    "On n'observe pas de lésion intraépithéliale ou de malignité.",
                    "L'examen ne montre pas de lésion intraépithéliale ou de malignité.",
                    "Il n'y a pas de lésion intraépithéliale ou de malignité.",
                    "On ne retrouve pas de lésion intraépithéliale ou de malignité observable sur ce prélèvement.",
                    "Absence de lésion intraépithéliale ou de malignité à l'examen de ce prélèvement."
                ]),
                ("V. atrophique", [
                    "Modifications de caractère atrophique, sans lésion intraépithéliale ou malignité.",
                    "Aspect d'atrophie. Absence de lésion intraépithéliale ou de malignité.",
                    "Frottis atrophique. Absence de lésion intraépithéliale ou de malignité.",
                    "Frottis atrophique, sans lésion intraépithéliale ou malignité.",
                    "Il s'agit d'une atrophie. Absence de lésion intraépithéliale ou de malignité."
                ]),
                ("V. dystrophique", [
                    "Aspect dystrophique, sans lésion intra-épithéliale ou malignité.",
                    "Vagin siège de remaniements dystrophiques. Absence de lésion intra-épithéliale ou de malignité.",
                    "Frottis dystrophique, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Présence de modifications dystrophiques, sans lésion intra-épithéliale ou malignité.",
                    "Frottis dystrophique. Absence de lésion intra-épithéliale ou de malignité."
                ]),
                ("V. inflammatoire", [
                    "Remaniements de caractère inflammatoire, sans spécificité. Absence de lésion intra-épithéliale ou de malignité.",
                    "Frottis présentant des signes d'inflammation non spécifique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Présence de signes inflammatoires, sans caractère spécifique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Frottis de caractère inflammatoire, sans spécificité, ne montrant pas de lésion intra-épithéliale ou de malignité.",
                    "Modifications inflammatoires sans caractère spécifique. Absence de lésion intra-épithéliale ou de malignité.",
                    "Frottis de caractère inflammatoire banal, sans lésion intra-épithéliale ou de malignité.",
                    "Modifications inflammatoires non spécifiques. Absence de lésion intra-épithéliale ou de malignité."
                ])

            ]
            }
        ]
    }
]

# Create the main window
root = tk.Tk()
root.title("Medical Report Editor")
root.geometry("700x500")

# Define a larger font
editor_font = ("Arial", 14)  # You can change the font size as needed

# Create a frame for the text editor so it stays fixed above the scrolling area
text_frame = tk.Frame(root)
text_frame.grid(row=0, column=0, columnspan=3, pady=10, padx=10, sticky="ew")

# Create a text editor with undo functionality and a larger font
text_editor = tk.Text(text_frame, height=10, width=80, undo=True, font=editor_font)
text_editor.pack(expand=True, fill=tk.BOTH)


# if you want dark background for text editor
# text_editor = tk.Text(root, height=10, width=80, undo=True, font=("Arial", 14),bg="#2E2E2E", fg="#E0E0E0", insertbackground="white")


# Enable "Ctrl + Z" for undo action and "Ctrl + Y" for redo action
root.bind("<Control-z>", lambda event: text_editor.edit_undo())  # Undo action
root.bind("<Control-y>", lambda event: text_editor.edit_redo())  # Redo action

# Add a Save button with "Ctrl + S" for appending to Word
root.bind("<Control-s>", lambda event: append_to_word())  # Ctrl + S to append to Word
# Bind the close button to prompt the user before closing
root.protocol("WM_DELETE_WINDOW", on_close)

# Create a canvas and scrollbar for the groups
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)  # Increase width
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
max_columns = 2  # Number of columns for groups
current_row = 0
current_column = 0

for group in button_groups:
    # Create a frame for the group
    frame = tk.Frame(scrollable_frame, bg=group["bg_color"], padx=10, pady=5)
    frame.grid(row=current_row, column=current_column, padx=5, pady=5, sticky="nsew")

    # Add a label for the group
    label = tk.Label(frame, text=group["name"], bg=group["bg_color"], font=("Arial", 16, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=2, sticky="w")

    # Create buttons inside the group
    button_row = 1
    button_column = 0

    for item in group["buttons"]:
        if isinstance(item, tuple):  # Regular button (label, options)
            label, options = item
            create_button(frame, label, options, group["bg_color"], button_row, button_column)

            # Adjust column and row for the next button
            button_column += 1
            if button_column > 1:  # Max 2 columns
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

                # Adjust column and row for next button
                sub_button_column += 1
                if sub_button_column > 1:  # Max 2 columns
                    sub_button_column = 0
                    sub_button_row += 1

            # Ensure the next subgroup does not overwrite the previous one
            button_row += sub_button_row + 1  

    # Update row and column for the next group
    current_column += 1
    if current_column >= max_columns:
        current_column = 0
        current_row += 1

# Bind two-finger scrolling (for touchpad or mouse wheel)
def on_scroll(event):
    if event.delta != 0:  # Check for scroll direction
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

root.bind_all("<MouseWheel>", on_scroll)  # Bind mouse wheel (works for touchpad too)


# Run the Tkinter event loop
root.mainloop()
