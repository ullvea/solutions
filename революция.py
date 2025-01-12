def s():
    number = input()
    ans = ''
    num = [str(i) for i in range(910, 920)] + [str(i) for i in range(980, 990)] + [str(i) for i in range(920, 940)]
    num = num + [str(i) for i in range(902, 907)] + [str(i) for i in range(960, 970)]
    flag1 = True
    count_l, count_r = 0, 0
    flag = False
    for i in range(len(number)):
        if number[i].isdigit() or (ans == '' and number[i] == "+"):
            ans += number[i]
        elif number[i] == "(":
            count_l += 1
        elif number[i] == ')':
            count_r += 1
        if count_r > count_l:
            flag = True
    if ans[0] == '8':
        ans = '+7' + ans[1:]
    elif number.startswith("+") and not (ans[:2] in ["+7", "+1"] or ans[:3] == "+55" or ans[:4] == "+359"):
        flag1 = False
        raise ValueError("не определяется код страны")
    if flag1:
        if flag:
            raise ValueError("неверный формат")
        elif number.find("--") != -1:
            raise ValueError("неверный формат")
        elif "(" in number or ")" in number:
            if number.count("(") != number.count(")") or number.count(")") != 1:
                raise ValueError("неверный формат")
            else:
                print(ans)
        elif number.startswith("-") or number.endswith("-") or not ans.startswith("+"):
            raise ValueError("неверный формат")
        elif len(ans) != 12:
            raise ValueError("неверное количество цифр")
        elif ans[2:5] not in num and ans[:2] == "+7":
            raise ValueError("не определяется оператор сотовой связи")
        else:
            print(ans)
    else:
        print(ans)


try:
    s()
except ValueError as e:
    print(e)