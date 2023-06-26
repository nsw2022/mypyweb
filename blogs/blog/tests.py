from django.test import TestCase

# Create your tests here.
# 무주택 기간 산정
home_score = 0
home = int(input("무주택 기간을 입력해 주세요. : "))
if home < 0:
    print("음수 입력하면 대머리")
else:
    for i in (1, home):
        home_score = 2 * home + 2
        if home > 15:
            home_score = 32

    #print(home_score)


    # 부양가족 수
    family_score = 0
    family = int(input("부양가족 수를 입력해 주세요. : "))

    for i in (1, family):
        family_score = 5 * (family+1)
        if family > 6:
            family_score = 35

    #print(family_score)

    # 청약통장 가입기간
    bankbook_score = 0
    bankbook = float(input("청약통장 가입기간을 입력해 주세요. : "))

    for i in (0.5, bankbook):
        bankbook_score = bankbook + 2
        if bankbook < 0.5:
            bankbook_score = 1
        elif bankbook >= 0.5 and bankbook < 1:
            bankbook_score = 2
        elif bankbook > 15:
            bankbook_score = 17

    #print(int(bankbook_score))


    print(home_score + family_score + int(bankbook_score))