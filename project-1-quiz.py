q1="""What is the song that recently got selected for oscar ?
a.hrudayama
b.pavizha mazha
c.naatu naatu
d.srivalli"""

q2="""What aare the highlights of recently approved budget by union minister
a.ndian economy has increased in size from being 10th to 5th largest
in the world in the past nine years
b.saptarshi
c.Atmanirbhar clean plant programd
d.all of the above"""

q3="""due to which Iran women death hijab protest got started?
a.Mahsa mongoi
b.Masih Alinejad
c.Mahsa amini
d.Mina torabi"""

q4="""Who is the president of ukraine?
a.Petro Poroshenko
b.Vladimir putin
c.Volodymyr Zelenskyy
d.Vladimir Klitschko"""

q5="""What is the best scenic and nature place to visit in Andhrapradesh?
a.Araku
b.Talakona waterfalls
c.Ananthagiri hills
d.papikondalu"""


questions={q1:"c",q2:"d",q3:"c",q4:"c",q5:"a"}
name=input("Hi whats your name")
print("Hello",name,"Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this que(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter the answer")
    if ans==questions[i]:
        print("wow!you got 1 point")
        score=score+1
        print("Your score is:",score)
    else:
        print("wrong answer, u lost 1 mark")
        score=score-1
        print("ur curent score is:",score)
    flag2=input("Do you want to Quit?type(Yes/No)")
    if flag2=="yes":
        break
print("your total score is:",score)
