import random

choices = ['가위', '바위', '보']
user = input("가위, 바위, 보 중 하나를 골라주세요: ")

if user not in choices:
    print("잘못된 입력입니다.")
else:
    computer = random.choice(choices)
    print(f"당신: {user}")
    print(f"컴퓨터: {computer}")

    if user == computer:
        print("비겼습니다.")
    elif (user == '가위' and computer == '보') or (user == '바위' and computer == '가위') or (user == '보' and computer == '바위'):
        print("이겼습니다.")
    else:
        print("졌습니다.")
