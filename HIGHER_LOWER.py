from math import acosh
import logo1_game
import random
import game_database
import os
print(logo1_game.game_logo)
score=0
def display_account_info(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name},a {description},from {country}"
def check_sum(guess,follower_count_1,follower_count_2):
    if follower_count_1<follower_count_2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
account_2=random.choice(game_database.data)
continue_flage=True
while continue_flage:
    account_1=account_2
    account_2=random.choice(game_database.data)
    while account_1== account_2:
        account_2 = random.choice(game_database.data)
    display_account_info(account_1)
    display_account_info(account_2)
    print(f"compare1:{display_account_info(account_1)}")
    print(logo1_game.vs)
    print(f"compare2:{display_account_info(account_2)}")
    guess=int(input("who has more followers Type1 or Type2 ="))
    follower_count_1=account_1["followers_count"]
    follower_count_2=account_2["followers_count"]
    is_correct=check_sum(guess,follower_count_1,follower_count_2)
    os.system('cls')
    if is_correct==True:
        score=score+1
        print(f"your are right and your score is {score} ")
    else:
        print(f"its wrong your final score is {score} ")
        continue_flage=False














