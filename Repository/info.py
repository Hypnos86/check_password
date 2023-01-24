import tkinter as tk


class Info:
    def show_information(self):
        frame = tk.Toplevel()
        frame.geometry('700x110')
        frame.title('Informacje o aplikacji')
        message = f'Sprawdzić hasła można na dwa sposoby.\n ' \
                  f'Metoda 1 - Przygotuj plik txt i wpisz tam hasła jedno pod drugim, które chcesz sparawdzić. \n Następnie klikni "Importuj i sprawdz". \n' \
                  f'Metoda 2 - Wpisz swoje hasło i klikni "Spwardz hasło" '

        frame = tk.Label(master=frame, text=message)
        frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
