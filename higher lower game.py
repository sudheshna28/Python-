import random
import dataset
##print("HIGHIER LOWER GAME")
def display_account_info(account):
    name=account['name']
    proffession=account['proffession']
    place=account['place']
    return f"{name}, a {proffession} !! from {place}"
account1=random.choice(dataset.data)
account2=random.choice(dataset.data)
print(f"Compare 1: {display_account_info(account1)}")
print(f"Compare 2: {display_account_info(account2)}")
##guess=int(input("who has more followers?? type 1 or 2: "))
followers_count_1=account1["followers"]
followers_count_2=account2["followers"]
print(followers_count_1)
print(followers_count_2)
