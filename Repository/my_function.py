from requests import get
from hashlib import sha1
import tkinter as tk


class Password:

    # def take_word(self):
    #     haslo = enter_pass.get()
    #     print(haslo)
    #     my_password = Password()
    #     my_password.check_password(haslo)

    def check_password(self, password):
        encode_password = sha1(password.encode('utf-8'))
        hash_password = encode_password.hexdigest()
        prefix_password = hash_password[:5]
        url = 'https://api.pwnedpasswords.com/range/' + prefix_password
        response = get(url)
        response_lis = response.text.splitlines()

        hash_list = [hash_list[0:35] for hash_list in response_lis]
        hash_count = [hash_list[36:] for hash_list in response_lis]
        hash_dict = dict(zip(hash_list, hash_count))
        sufix_password = hash_password[5:40].upper()

        if sufix_password in hash_dict.keys():
            text = f'Twoje hasło "{password}" było złamane i użyte {hash_dict[sufix_password]} razy. \n Zmień je jak najszybciej!!'

        else:
            text = f'Twoje hasło jest bezpieczne, tak trzymaj! \n hasło: {password} \n hasz: {hash_password} \n prefix: {prefix_password} \n sufix: {sufix_password}'

        frame = tk.Toplevel()
        frame.geometry('380x100')
        frame.title('Analiza hasła')
        frame = tk.Label(master=frame, text=text)
        frame.pack(fill='both', expand=True, side=tk.TOP)
