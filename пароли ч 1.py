def s():
    c = ['qwertyyuiop', 'asdfghjkl', "zxcvbnm", "ёйцукенгшщзхъ", "фывапролджэё", "ячсмитьбю"]
    password = input()
    if (not (not (
            len(password) < 9) and not password.islower() and not password.isupper() and not password.isalpha() and
             not password.isdigit() and any(
                i in '0123456789' for i in password))):
        raise ValueError("error")
    password = password.lower()
    for i in c:
        for j in range(len(password) - 2):
            if password[j:j + 3] in i:
                # print(password[j:j+3])
                raise ValueError("error")
    print("ok")


try:
    s()
except ValueError as e:
    print(e)