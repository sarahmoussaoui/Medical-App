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
        "bg_color": "beige",
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
    label = tk.Label(frame, text=group["name"], bg=group["bg_color"], font=("Arial", 12, "bold"))
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
