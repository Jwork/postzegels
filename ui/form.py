import tkinter as tk
import tkinter.ttk as ttk


def renderForm() -> None:
    label_jaar = tk.Label(text="Jaar van uitgifte:").grid(row=0, column=0)
    entry_jaar = tk.Entry().grid(row=0, column=1)
    #BLANK
    filler = tk.Label().grid(row=1)
    #ADDRESS
    label_catalogus_nummer  = tk.Label(text="catalogus nummer:").grid(row=2, column=0)
    entry_catalogus_nummer = tk.Entry().grid(row=2, column=1)

    label_categorie = tk.Label(text="categorie:").grid(row=3, column=0)
    entry_categorie = tk.Entry().grid(row=3, column=1)

    label_onderwerp = tk.Label(text="onderwerp:").grid(row=4, column=0)
    entry_onderwerp = tk.Entry().grid(row=4, column=1)

    label_soort_zegel = tk.Label(text="soort zegel:").grid(row=5, column=0)
    entry_soort_zegel = tk.Entry().grid(row=5, column=1)
    #BLANK
    # filler = tk.Label().grid(row=6)

    label_type_zegel = tk.Label(text="type zegel:").grid(row=7, column=0)
    entry_type_zegel = tk.Entry().grid(row=7, column=1)

    label_waarde_opdruk = tk.Label(text="waarde opdruk:").grid(row=8, column=0)
    entry_waarde_opdruk = tk.Entry().grid(row=8, column=1)

    label_afbeelding_pad = tk.Label(text="afbeelding:").grid(row=9, column=0)
    entry_afbeelding_pad = tk.Entry().grid(row=9, column=1)

    label_informatie = tk.Label(text="informatie:").grid(row=10, column=0)
    entry_informatie = tk.Text().grid(row=10, column=1)

    label_zegel_conditie = tk.Label(text="conditie:").grid(row=11, column=0)
    entry_zegel_conditie = tk.Entry().grid(row=11, column=1)
    
    label_catalogus_prijs = tk.Label(text="catalogus prijs:").grid(row=11, column=0)
    entry_catalogus_prijs = tk.Entry().grid(row=11, column=1)
    
    label_mijn_prijs = tk.Label(text="mijn prijs:").grid(row=11, column=0)
    entry_mijn_prijs = tk.Entry().grid(row=11, column=1)




