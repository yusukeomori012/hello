class validate():
    if hand > 2 or hand < 0:
        return False
    else:
        return True

def print_hand(hand, name="ゲスト"):
    hands = ["グー", "チョキ", "パー"]
    print(name + "は" + hands[hand] + "を出しました")

def judge(player, computer):
    if p;ayer == computer:
        print("引き分け")
    elif player == 0 and computer == 1:
        print("勝ち")
    elif player == 1 and computer == 2:
        print("勝ち")
    elif player == 2 and computer == 0:
        print("勝ち")
    else:
        print("負け")
