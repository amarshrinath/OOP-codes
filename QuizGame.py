#data collected from trivia.com we can use different topics for question data.

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
             " you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


#creating class for question:

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# for quiz functionality create class Quizbrain:

class QuizzBrain:
    
    def __init__(self, q_list):
        self.question_number= 0
        self.question_list = q_list
        self.score =0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True

    def next_question(self):
        current_question= self.question_list[self.question_number]
        self.question_number += 1
        user_answer= input(f"Q.{self.question_number}: {current_question.text}. (True/False)? :")
        self.check_answer(user_answer, current_question.answer)




    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()== correct_answer.lower():
            self.score += 1
            print("You Got it right")

        else:
            print("you was wrong")
        print(f"your current score : {self.score}/{self.question_number}")
        print("\n")
        
        
 #main program for executing all class modules.:

#1st we get the data from privided module.
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#starts quiz functions:
quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("Quiz is over")
print(f"your total score is : {quiz.score}/{len(question_bank)}")
        
 #------------------------------the end---------------------------------------------------------------------------------------    