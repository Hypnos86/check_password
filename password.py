from requests import get
from hashlib import sha1


class Password:
    def __init__(self, file) -> None:
        self.file = file
        with open(self.file, mode='r', encoding='utf-8') as read_file:
            self.word_list = [line.strip() for line in read_file]

    def check_password(self):
        passwords = self.word_list
        for word in passwords:
            encode_password = sha1(word.encode('utf-8'))
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
                print(f'Twoje hasło było złamane i użyte {hash_dict[sufix_password]}')

                with open(f'change_passwords_with_priority.txt', mode='a', encoding='utf-8') as output_file:
                    output_file.write(
                        f'Twoje hasło "{word}" było złamane i użyte {hash_dict[sufix_password]} razy. Zmień je szybko!!! \n')

            else:
                print('Twoje hasło jest bezpieczne, tak trzymaj!')

            print(f'hasło: {word}\n hasz: {hash_password}\n prefix: {prefix_password}\n sufix: {sufix_password}\n')


password = Password('password.txt')
password.check_password()
