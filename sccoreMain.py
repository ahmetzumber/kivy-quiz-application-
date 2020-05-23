
import kivy
from kivy.uix.popup import Popup
from datas import QuestionList,selectQuestion
from random import randint
from kivy.uix.label import Label

kivy.require('1.0.6')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

class MainWindow(Screen):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def quit(self):
        exit()

    def passScreen(self):
        manager.current = 'category'

class CategoryWindow(Screen):

    def __init__(self,name):
        super().__init__()
        self.name = name
        self.id = ""

    def passScreenScience(self):
        levelW = manager.get_screen('level')
        levelW.category = 'science'
        manager.current = 'level'

    def passScreenSports(self):
        levelW = manager.get_screen('level')
        levelW.category = 'sports'
        manager.current = 'level'

    def passScreenHistory(self):
        levelW = manager.get_screen('level')
        levelW.category = 'history'
        manager.current = 'level'

class LevelWindow(Screen):

    def __init__(self,name):
        super().__init__()
        self.category = ''
        self.name = name

    def passScreenEasy(self):
        questionW = manager.get_screen('question')
        questionW.category = self.category
        questionW.level = 'easy'
        questionW.question = selectQuestion(questionW.list, questionW.level)
        print('Correct answer : ',questionW.question.correct_answer)
        questionW.button_action()
        manager.current = 'question'

    def passScreenMedium(self):
        questionW = manager.get_screen('question')
        questionW.category = self.category
        questionW.level = 'medium'
        questionW.question = selectQuestion(questionW.list, questionW.level)
        print('Correct answer : ', questionW.question.correct_answer)
        questionW.button_action()
        manager.current = 'question'

    def passScreenHard(self):
        questionW = manager.get_screen('question')
        questionW.category = self.category
        questionW.level = 'hard'
        questionW.question = selectQuestion(questionW.list, questionW.level)
        print('Correct answer : ', questionW.question.correct_answer)
        questionW.button_action()
        manager.current = 'question'

class QuestionWindow(Screen):

    def __init__(self,name,category=None,level=None):
        super().__init__()
        self.name = name
        self.category = category
        self.level = level
        self.list = QuestionList(self.category)
        self.question = selectQuestion(self.list,self.level)


    def if_question_incorrect(self):
        popup = Popup(title='Information',content=Label(text=f'You are wrong :(\n\n   sccorre  :  {self.sccoreLabel.text}'),
                      size_hint=(None,None),
                      size=(500,500),
                      pos_hint={'x': 550.0 / self.width,
                                'y': 300.0 / self.height},
                      )
        popup.open()
        manager.current = 'main'

    def if_question_correct(self):
        popup = Popup(title='Information', content=Label(text='You are going well :)'),
                      size_hint=(None, None),
                      size=(500, 500),
                      pos_hint={'x': 550.0 / self.width,
                                'y': 300.0 / self.height},
                      )
        popup.open()
        self.button1.text = ''
        self.button2.text = ''
        self.button3.text = ''
        self.button4.text = ''
        self.questionLabel.text = ''
        self.sccoreLabel.text = str(int(self.sccoreLabel.text) + 10)
        self.question.isAsk = True
        self.question = selectQuestion(self.list, self.level)
        print('Correct answer : ',self.question.correct_answer)
        self.button_action()


    def button1_action(self):
        if self.button1.text is self.question.correct_answer:
            self.if_question_correct()
        else:
            self.if_question_incorrect()

    def button2_action(self):
        if self.button2.text is self.question.correct_answer:
            self.if_question_correct()
        else:
            self.if_question_incorrect()

    def button3_action(self):
        if self.button3.text is self.question.correct_answer:
            self.if_question_correct()
        else:
            self.if_question_incorrect()

    def button4_action(self):
        if self.button4.text is self.question.correct_answer:
            self.if_question_correct()
        else:
            self.if_question_incorrect()


    def button_action(self):

        correct = randint(1,4)
        self.questionLabel.text = self.question.question

        if correct == 1:
            self.button1.text = self.question.correct_answer
        elif correct == 2:
            self.button2.text = self.question.correct_answer
        elif correct == 3:
            self.button3.text = self.question.correct_answer
        elif correct == 4:
            self.button4.text = self.question.correct_answer

        for incorrect in self.question.incorrect_answer:
            if self.button1.text is '':
                self.button1.text = incorrect
            elif self.button2.text is '':
                self.button2.text = incorrect
            elif self.button3.text is '':
                self.button3.text = incorrect
            elif self.button4.text is '':
                self.button4.text = incorrect

kv = Builder.load_file("sccoreUI.kv")

manager = ScreenManager()

screens = [MainWindow(name="main"), CategoryWindow(name="category"),LevelWindow(name="level"), QuestionWindow(name="question")]

class MyApp(App):
    def build(self):
        for i in screens:
            manager.add_widget(i)

        return manager


if __name__ == '__main__':
    MyApp().run()


