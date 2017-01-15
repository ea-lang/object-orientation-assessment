"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
	
	Encapsulation: data lives close to its functionality; neatly packaged and organized; everything kept together
	Abstraction: don't need to know the information a method uses internally; can hide unnecessary details
	Polymorphism: easy to make many different, interchangeable types of items 
	
2. What is a class?

	A user-defined type. 
	Just as strings and lists are classes in python, 
	the user can also define custom classes with their own methods

3. What is an instance attribute?

	An attribute that is specific to an instance, 
	not shared by all instances of the class

4. What is a method?

	A function that is defined within a class

5. What is an instance in object orientation?

	A specific realization of an object

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

	A class attribute is shared by all instances of the class, 
	whereas an instance attribute is specific to that instance.
	ex. If you have an Animal class, you could give it a class attribute that all animals share (e.g. hunger)
		If you have an instance of the Animal class, such as a dog, you could give it a instance attribute
		that is specific to dogs (e.g. whether it needs to be walked)

"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
	def __init__(self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address

class Question(object):
	def __init__(self, question, correct_answer):
		self.question = question
		self.correct_answer = correct_answer

	def ask_and_evaluate(self):
		user_answer = raw_input(self.question + " > ")
		if user_answer == self.correct_answer:
			return True
		return False

class Exam(object):
	def __init__(self, name):
		self.name = name
		self.questions = []

	def add_question(self, question, correct_answer):
		self.questions.append({'question': question, 'correct_answer': correct_answer})

	def administer(self):
		score = 0
		for question in self.questions:
			question = Question(question['question'], question['correct_answer'])
			if question.ask_and_evaluate():
				score += 1
		return float(score)/(len(self.questions))


def take_test(exam, student):
	score = exam.administer()
	student.score = score
	print "%s %s, your score is %.2f!" %(student.first_name, student.last_name, score)

def example():
	sample_exam = Exam('Sample exam')
	sample_exam.add_question("What is the capital of France?", "Paris")
	sample_exam.add_question("What is the capital of Greece?", "Athens")

	sample_student = Student("John", "Smith", "123 Pine St.")
	take_test(sample_exam, sample_student)


class Quiz(Exam):
	def administer(self):
		score = super(Quiz, self).administer()
		if score >= 0.50:
			return True
		return False
