questions = [
    ("Which planet is known as the Red Planet?", 
     ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"], 
     "B", 1000),

    ("Who is known as the Father of the Nation in India?", 
     ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Sardar Patel", "D. B. R. Ambedkar"], 
     "B", 2000),

    ("Which is the largest ocean on Earth?", 
     ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"], 
     "C", 5000),

    ("What is the capital of Australia?", 
     ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"], 
     "C", 10000)
]

total_amount = 0

print(" Welcome to Kaun Banega Crorepati! \n")
print("Answer by typing A, B, C, or D.\n")

for question, options, correct_answer, prize in questions:
    print(question)
    for option in options:
        print(option)
    
    answer = input("Your answer: ").strip().upper()

    if answer == correct_answer:
        print("✅ Correct!")
        total_amount += prize
        print(f"You won ₹{prize} for this question!\n")
    else:
        print("❌ Wrong answer!")
        print(f"The correct answer was: {correct_answer}")
        break  # End the game if wrong answer

print(f" Game Over! You are taking home ₹{total_amount}")