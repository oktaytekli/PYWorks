#Question

class Question:
    def __init__(self, text, chocices, answer):
        self.text = text
        self.chocies = chocices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer



# print(q1.checkAnswer('Python'))
# print(q2.checkAnswer('JavaScript'))
# print(q2.checkAnswer('C#'))


#Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.quesIndex = 0

    def getQuestion(self):
        return quiz.questions[self.quesIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru : {self.quesIndex + 1}: {question.text}')

        for q in question.chocies:
            print('-'+ q)
        
        answer = input('Cevabınız: ')
        print(question.checkAnswer(answer))
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.quesIndex += 1
        

    def loadQuestion(self):
        if len(self.questions) == self.quesIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Skorunuz:', self.score)
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.quesIndex +1

        if questionNumber > totalQuestion:
            print('Quiz Bitti.')
        else:
            print(f'Soru {questionNumber} of {totalQuestion}'.center(100,'*'))

    
        

q1 = Question('En iyi programlama dili hangisidir?', ['C#', 'Java', 'JavaScript', 'Python'], 'Python')
q2 = Question('En popüler programlama dili hangisidir?', ['C#', 'Java', 'JavaScript', 'Python'], 'C#')
q3 = Question('En çok kazandıran programlama dili hangisidir?', ['C#', 'Java', 'JavaScript', 'Python'], 'JavaScript')
question = [q1,q2,q3]

quiz=Quiz(question)
quiz.loadQuestion()
# question = quiz.getQuestion()
# #question = quiz.questions[quiz.quesIndex] # gelen questions objelerinden quiz in içerisinde ki questionindx ini almış oalcağız.
# print(question.text)