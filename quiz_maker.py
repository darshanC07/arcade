import random

def option(list1,i):
  random_set = set()
  random_set.add(i)
  while len(random_set)!=4:
    num = random.randint(0,len(list1)-1)
    random_set.add(num)
  temp_list = list(random_set)
  for n in range(0,len(random_set)):
    # print(temp_list[n])
    print(n+1,list1[temp_list[n]])
  return temp_list.index(i)+1

def input():
  while True:
    input_ = input("Enter 1 to start Quiz: ")
    if input_.isdigit():
      input_ = int(input_)
      if input_==1:
        return input_
      else:
        print("Enter valid input.")
    else:
      print("Enter valid input.")

def answer_of_user():
  while True:
    input_ = input("Enter correct answer number : ")
    if input_.isdigit():
      input_ = int(input_)
      if input_==1:
        return input_
      else:
        print("Enter valid input.")
    else:
      print("Enter valid input.")


que = ["current prime minister of india","sun rises in ______","what do we inhale","current home minister of india","current cm of maharastra"]
# print(len(que))
ans = ["narendra modi","east","oxygen","amit shah","eknath shinde"]
# print(len(ans))
option_list = ["narendra modi","east","oxygen","amit shah","eknath shinde","north","south","west","darshan choudhary","ms dhoni","devendra fadnavis","CO2","nitrogen"]
name = input("Enter your name : ")
print("hello",name)
input_ = input()
done_que = []
if(input_==1):
  points = 0
  i = 0
  while i<len(que):
    print("question",i+1)
    random_ = 0
    while((random_ in done_que)==True):
      random_ = random.randint(0,len(que)-1)
    done_que.append(random_)
    print("Q.",que[random_],"\n\tCurrent Points = ",points)
    correct_ans = option(option_list,random_)
    user_ans = answer_of_user()
    if user_ans==correct_ans:
      print("You are right.\n+500 points")
      points+=500
    else:
      print("Wrong Answer. Better luck Next Time.\nYour Points : ",points)
      break
    print("-------------------------------")
    i+=1
