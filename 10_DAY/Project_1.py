print("🎉 Welcome to Kon Banega Karodpati 🎉")

questions = [
    ("What is the capital of France?", ("1. Delhi", "2. Mumbai", "3. Paris", "4. Kolkata"), 3),
    ("Who is the CEO of Tesla?", ("1. Elon Musk", "2. Guido van Rossum", "3. Bill Gates", "4. Steve Jobs"), 1),
    ("What is the largest mammal?", ("1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Hippopotamus"), 2),
    ("Which planet is known as the Red Planet?", ("1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"), 2),
    ("What is the chemical symbol for water?", ("1. H2O", "2. CO2", "3. NaCl", "4. O2"), 1),
]

prize_levels = [1000, 5000, 10000, 20000, 50000]
safe_level = 10000

while True:
    total_money = 0

    for i in range(len(questions)):
        q, options, correct = questions[i]

        print(f"\nQuestion {i+1} for ₹{prize_levels[i]}")
        print(q)

        for opt in options:
            print(opt)

        try:
            ans = int(input("Enter option (1-4): "))
        except:
            print("Invalid input! Game Over ❌")
            break

        if ans == correct:
            print("✅ Correct!")
            total_money = prize_levels[i]
        else:
            print("❌ Wrong Answer!")
            if total_money < safe_level:
                total_money = 0
            else:
                total_money = safe_level
            break

    print(f"\n🏆 You won ₹{total_money}")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break