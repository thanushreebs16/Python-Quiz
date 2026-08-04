import random
print("            *************")
print()
print("        Welcome to Python Quiz")
print()
print("            *************")
print()
questions=[
    {
        "question":"Who developed Python?",
        "options":["James Gosling","Guido van Rossum","Dennis Ritche","Bjarne Stroustrup"],
        "answer":2
    },
    {
        "question":"What year was Python first released?",
        "options":[1989,1995,2000,1991],
        "answer":4
    },
    {
        "question":"What symbol is used to write comments in Python?",
        "options":["//","#","/**/","--"],
        "answer":2
    },
    {
        "question":"Which function is used to display output in Python?",
        "options":["display()","show()","print()","output()"],
        "answer":3
    },
    {
        "question":"Which function is used to take input from user?",
        "options":["scan()","input()","read()","get()"],
        "answer":2
    },
    {
        "question":"Which data type is used to store decimal numbers?",
        "options":["inr","float","str","bool"],
        "answer":2
    },
    {
        "question":"Which keyword is used to define a function in Python?",
        "options":["function","define","def","func"],
        "answer":3
    },
    {
        "question":"Which loop is used to iterate over a sequence in Python?",
        "options":["for","loop","repeat","do"],
        "answer":1
    },
    {
        "question":"Which data type stores True or False values?",
        "options":["tuple","float","list","bool"],
        "answer":4
    },
    {
        "question":"Which brackets are used to create a list in Python?",
        "options":["()","{}","[]","<>"],
        "answer":3
    }

]
random.shuffle(questions)
score=0
for number,question in enumerate(questions,start=1):
    print(number,question["question"])
    print()
    for number,option in enumerate(question["options"],start=1):
        print(number,option)
    user_input=int(input("\nEnter your choice:"))
    print()
    if user_input==question["answer"]:
        print("Correct answer")
        print()
        score+=1
    else:
         answer_index=question["answer"]-1
         print(f"Wrong answer \nThe correct answer is:{question["options"][answer_index]}")
         print()
print()
x=len(questions)
print(f"Your score is:{score} out of {x}")