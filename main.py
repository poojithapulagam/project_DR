import json
#import gemini 

# Load existing JSON data
with open('data.json', 'r') as file:
    data = json.load(file)
# Get dynamic input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
course = input("Enter your course: ")
is_student_input = input("Are you a student? (yes/no): ")
is_student = True if is_student_input.lower() == "yes" else False
university = input("Enter your university name: ")

# Update JSON data
data["name"] = name
data["age"] = age
data["course"] = course
data["is_student"] = is_student
data["university"] = university

# Write updated data to JSON file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Print updated data
print("\nUpdated JSON data:")
print(data)
# --- Step 2: SLM functions ---
def query_gemini(question):
    # Placeholder for Gemini API call
    return f"Answer not found locally. Querying Gemini for: '{question}'"

def answer_question(question, data):
    question_lower = question.lower()
    for key in data:
        if key.lower() in question_lower:
            return f"{key.capitalize()}: {data[key]}"
    return query_gemini(question)

# --- Step 3: Ask questions loop ---
while True:
    user_input = input("\nAsk a question (or type 'exit'): ")
    if user_input.lower() == "exit":
        print("Exiting SLM...")
        break
    print(answer_question(user_input, data))
