import random, os
wordcomplete = False
word_list = ["aardvark", "baboon", "camel"]
random_word = word_list[random.randint(0,len(word_list)-1)]
user_completed_status = "_"*len(random_word)


user_input=str(input("choce one letter = "))
while (wordcomplete == False):
        if(user_input in random_word):
            for i in range(0, len(random_word)):
                if(user_input == random_word[i]):
                    user_completed_status = user_completed_status[:i] + str(user_input) + user_completed_status[i + 1:]
            if(user_completed_status == random_word):
                wordcomplete = True
            else:
                os.system('clear')
                print(user_completed_status)
                user_input=str(input("choce one letter = "))
        else:
            os.system('clear')
            print("letter dosent exist")
            print(user_completed_status)
            user_input=str(input("choce one letter = "))

os.system('clear')
print(f"world was = {random_word}")
print("you win")