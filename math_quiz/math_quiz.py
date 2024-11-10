import random

def get_random_int(min_val, max_val):
    #Return a random integer between min_val and max_val
    return random.randint(min_val, max_val)

def get_random_operator():
    #Return a random operator from '+', '-', or '*'
    return random.choice(['+', '-', '*'])

def generate_problem(num1, num2, operator):
    #Return a math problem string and its answer based on the operator
    problem = f"{num1} {operator} {num2}"
    answer = eval(problem)  # Calculate answer safely given controlled input
    return problem, answer

def math_quiz():
    #Run a math quiz where the user answers randomly generated math problems
    score = 0
    num_questions = 3

    print("Welcome to the Math Quiz! Answer the math problems presented.")
    
    for _ in range(num_questions):
        num1, num2 = get_random_int(1, 10), get_random_int(1, 5)
        operator = get_random_operator()
        problem, correct_answer = generate_problem(num1, num2, operator)
        
        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! +1 point.")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame over! Your score: {score}/{num_questions}")

if __name__ == "__main__":
    math_quiz()
