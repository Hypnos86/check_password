'''Aplikacja  Check_Passsword'''
import tkinter as tk
from Repository.info import Info
from Repository.write import Password

windows = tk.Tk()
windows.geometry('350x250')
windows.title('CheckPass')
windows.iconbitmap('ico/chain.ico')
windows.columnconfigure(1, weight=2)
windows.rowconfigure(1, weight=1)

password = Password()
info = Info()

about = tk.Button(master=windows, text='Instrukcja', command=info.show_information, width=15)
about.grid(column=0, row=0, pady=5, padx=10, sticky=tk.N, columnspan=2)

folder = tk.Button(master=windows, text='Plik', width=15)
folder.grid(column=0, row=1, pady=5, padx=5, sticky=tk.W)

button_folder = tk.Button(master=windows, text='Sprawdz', width=15)
button_folder.grid(column=1, row=1, pady=5, padx=5, sticky=tk.E)

folder_label = tk.Label(master=windows, text='---')
folder_label.grid(column=0, row=2, columnspan=2, pady=5, padx=15, sticky=tk.EW)


button_pass = tk.Button(master=windows, text='Sprawdz hasło', command=password.open_frame, width=15)
button_pass.grid(column=0, row=3, columnspan=2, pady=5, padx=10, sticky=tk.N)

# exit
close = tk.Button(master=windows, text='Zamknij', command=windows.destroy, width=15)
close.grid(column=0, columnspan=2, pady=5, padx=10, sticky=tk.S)

# footer
footer = tk.Label(master=windows, text='® 2022 Kamil Kubiak', bg='#3cb371', fg='white')
footer.grid(column=0, row=6, sticky=tk.EW, columnspan=2)

windows.mainloop()
