from requests import get
from hashlib import sha1
import tkinter as tk


class Password:
    INPUT = None
    TEXT_INFO = None

    def open_frame(self):
        frame = tk.Toplevel()
        frame.geometry('250x150')
        frame.title('Sprawdz swoje chasło')
        frame.columnconfigure(1, weight=2)
        frame.rowconfigure(1, weight=1)

        label_pass = tk.Label(master=frame, text='Wpisz hasło', width=15)
        label_pass.grid(column=0, row=0, columnspan=2, sticky=tk.EW)

        enter_pass = tk.Entry(master=frame, width=30)
        enter_pass.config(show='*')
        enter_pass.grid(column=0, row=1, columnspan=2, sticky=tk.N)

        self.INPUT = enter_pass
        self.TEXT_INFO = tk.StringVar()
        self.TEXT_INFO.set('*** tu znajdzie się analiza hasła ***')

        analys_pass = tk.Label(master=frame, font=('Comic sans MS', 10), textvariable=self.TEXT_INFO)
        analys_pass.grid(column=0, row=2, columnspan=2, sticky=tk.W)

        self.result_label = analys_pass

        close = tk.Button(master=frame, text='Zamknij', width=10, command=frame.destroy)
        close.grid(column=0, row=3, pady=5, padx=10, sticky=tk.W)

        check = tk.Button(master=frame, text='Sprawdz', width=10, command=self.check_password_from_input)
        check.grid(column=1, row=3, pady=5, padx=10, sticky=tk.E)

    def get_password_string_from_input(self):
        return self.INPUT.get()

    def check_password(self, password_string):
        encoded_password = sha1(password_string.encode('utf-8'))
        hashed_password = encoded_password.hexdigest()
        prefix_password = hashed_password[:5]
        url = 'https://api.pwnedpasswords.com/range/' + prefix_password
        response = get(url)
        response_lis = response.text.splitlines()

        hash_list = [hash_list[0:35] for hash_list in response_lis]
        hash_count = [hash_list[36:] for hash_list in response_lis]
        hash_dict = dict(zip(hash_list, hash_count))
        sufix_password = hashed_password[5:40].upper()

        if sufix_password in hash_dict.keys():
            text = f'Twoje hasło "{password_string}" było złamane i użyte {hash_dict[sufix_password]} razy. \n Zmień je jak najszybciej!!'

        else:
            text = f'Twoje hasło jest bezpieczne, tak trzymaj! \n hasło: {password_string} \n hasz: {hashed_password} \n prefix: {prefix_password} \n sufix: {sufix_password}'

        return text

    def check_password_from_input(self):
        password_string = self.get_password_string_from_input()
        result = self.check_password(password_string)
        self.show_result(result)
        print(result)
        return result

    def show_result(self, result):
        self.TEXT_INFO.set(result)

# passwordValidator = Password()
# passwordValidator.open_frame()
