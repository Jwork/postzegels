import tkinter as tk
import tkinter.ttk as ttk


def render(p_elem:tk.Tk) -> None:
    
    #SETUP FRAMES
    input_frame = tk.Frame(master=p_elem)
    
    input_frame.pack(side="top", anchor="nw")


    #SETUP LABELS AND INPUTS
    label_jaar = ttk.Label(master = input_frame, text="Jaar van uitgifte:")
    entry_jaar = ttk.Entry(master = input_frame, width=30)

    label_catalogus_nummer  = ttk.Label(master = input_frame, text="catalogus nummer:")
    entry_catalogus_nummer = ttk.Entry(master = input_frame, width=30)
 
    label_categorie = ttk.Label(master = input_frame, text="categorie:")
    entry_categorie = ttk.Entry(master = input_frame, width=30)

    label_onderwerp = ttk.Label(master = input_frame, text="onderwerp:")
    entry_onderwerp = ttk.Entry(master = input_frame, width=30)

    label_soort_zegel = ttk.Label(master = input_frame, text="soort zegel:")
    entry_soort_zegel = ttk.Entry(master = input_frame, width=30)


    label_type_zegel = ttk.Label(master = input_frame, text="type zegel:")
    entry_type_zegel = ttk.Entry(master = input_frame, width=30)

    label_waarde_opdruk = ttk.Label(master = input_frame, text="waarde opdruk:")
    entry_waarde_opdruk = ttk.Entry(master = input_frame, width=30)

    label_afbeelding_pad = ttk.Label(master = input_frame, text="afbeelding:")
    entry_afbeelding_pad = ttk.Entry(master = input_frame, width=30)

    label_informatie = ttk.Label(master = input_frame, text="informatie:")
    entry_informatie = tk.Text(master = input_frame, width=23, height=3)

    label_zegel_conditie = ttk.Label(master = input_frame, text="conditie:")
    entry_zegel_conditie = ttk.Entry(master = input_frame, width=30)
    
    label_catalogus_prijs = ttk.Label(master = input_frame, text="catalogus prijs:")
    entry_catalogus_prijs = ttk.Entry(master = input_frame, width=30)
    
    label_mijn_prijs = ttk.Label(master = input_frame, text="mijn prijs:")
    entry_mijn_prijs = ttk.Entry(master = input_frame, width=30)

    #CONFIGURE THE GRID
    label_jaar.grid(sticky="E",row=0,column=0)
    entry_jaar.grid(sticky="W",row=0, column=1)

    label_catalogus_nummer.grid(sticky="E",row=1,column=0)
    entry_catalogus_nummer.grid(sticky="W",row=1,column=1)

    label_categorie.grid(sticky="E",row=2,column=0)
    entry_categorie.grid(sticky="W",row=2,column=1)

    label_onderwerp.grid(sticky="E",row=3,column=0)
    entry_onderwerp.grid(sticky="W",row=3,column=1)

    label_soort_zegel.grid(sticky="E",row=4,column=0)
    entry_soort_zegel.grid(sticky="W",row=4,column=1)

    label_type_zegel.grid(sticky="E",row=5,column=0)
    entry_type_zegel.grid(sticky="W",row=5,column=1)

    label_waarde_opdruk.grid(sticky="E",row=6,column=0)
    entry_waarde_opdruk.grid(sticky="W",row=6,column=1)

    label_afbeelding_pad.grid(sticky="E",row=7,column=0)
    entry_afbeelding_pad.grid(sticky="W",row=7,column=1)

    label_zegel_conditie.grid(sticky="E",row=8,column=0)
    entry_zegel_conditie.grid(sticky="E",row=8,column=1)
  
    label_catalogus_prijs.grid(sticky="E",row=9,column=0)
    entry_catalogus_prijs.grid(sticky="E",row=9,column=1)

    label_mijn_prijs.grid(sticky="E",row=10,column=0)
    entry_mijn_prijs.grid(sticky="E",row=10,column=1)
  
    label_informatie.grid(sticky="E",row=11,column=0)
    entry_informatie.grid(sticky="W",row=11,column=1)