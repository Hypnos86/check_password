'''Aplikacja  Check_Passsword'''
import tkinter as tk
from function.info import show_information
from function.write import Password

windows = tk.Tk()
windows.geometry('350x200')
windows.title('CheckPass')
windows.iconbitmap('ico/chain.ico')
windows.columnconfigure(1, weight=2)
windows.rowconfigure(1, weight=1)

about = tk.Button(master=windows, text='Instrukcja', command=show_information, width=20)
about.grid(column=0, row=0, pady=5, padx=10, sticky=tk.N, columnspan=2)

folder = tk.Button(master=windows, text='Plik', width=20)
folder.grid(column=0, row=1, pady=5, padx=5, sticky=tk.W)

button_folder = tk.Button(master=windows, text='Sprawdz', width=20)
button_folder.grid(column=1, row=1, pady=5, padx=5, sticky=tk.E)

folder_label = tk.Label(master=windows, text='lalal')
folder_label.grid(column=0, row=2, columnspan=2, pady=5, padx=15, sticky=tk.EW)

open_frame = Password()
button_pass = tk.Button(master=windows, text='Sprawdz hasło', command=open_frame.open_frame, width=20)
button_pass.grid(column=0, row=3, columnspan=2, pady=5, padx=10, sticky=tk.N)

# exit
close = tk.Button(master=windows, text='Zamknij', command=windows.destroy, width=20)
close.grid(column=0, columnspan=2, pady=5, padx=10, sticky=tk.S)

# footer
footer = tk.Label(master=windows, text='® 2022 Kamil Kubiak', bg='#3cb371', fg='white')
footer.grid(column=0, row=6, sticky=tk.EW, columnspan=2)

windows.mainloop()
