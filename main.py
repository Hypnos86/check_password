'''Aplikacja  Check_Passsword'''
import tkinter as tk
from function.info import show_information
from function.my_function import Password

windows = tk.Tk()
windows.geometry('400x250')
windows.title('Sprawdz swoje hasło')
windows.iconbitmap('../ico/chain.ico')
windows.columnconfigure(1, weight=3)
windows.rowconfigure(1, weight=1)

about = tk.Button(master=windows, text='Instrukcja', command=show_information)
about.grid(column=1, row=1, sticky=tk.EW)

folder = tk.Button(master=windows, text='Plik')
folder.grid(column=0, row=2, padx=5, pady=5, sticky=tk.EW)

label_folder = tk.Label(master=windows)
label_folder.grid(column=1, row=2, sticky=tk.EW)

button_folder = tk.Button(master=windows, text='Importuj i sprawdz')
button_folder.grid(column=2, row=2, sticky=tk.EW)

label_pass = tk.Label(master=windows, text='Wpisz hasło')
label_pass.grid(column=0, row=3, padx=5, pady=5, sticky=tk.EW)

enter_pass = tk.Entry(master=windows)
enter_pass.config(show='*')
enter_pass.grid(column=1, row=3)


def take_word():
    word = enter_pass.get()
    my_password = Password()
    my_password.check_password(word)


button_pass = tk.Button(master=windows, text='Sprawdz hasło', command=take_word)
button_pass.grid(column=2, row=3, padx=5, pady=5, sticky=tk.EW)

information = tk.Label(master=windows)
information.grid(column=0, row=4, columnspan=3, sticky=tk.EW)

# exit
close = tk.Button(master=windows, text='Zamknij', command=windows.destroy)
close.grid(column=0, row=5, padx=10, pady=10, columnspan=1, sticky=tk.EW)

# footer
footer = tk.Label(master=windows, text='® 2022 Kamil Kubiak', bg='#3cb371', fg='white')
footer.grid(column=0, row=6, sticky=tk.EW, columnspan=3)

windows.mainloop()