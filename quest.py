from base_form import BaseForm
from tkinter import Button, Label, PanedWindow

class QuestPage(BaseForm):
    def __init__(self, category, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #panelWindow = PanedWindow(self, ori)
        self.path_category = "categories/"+category+"/informasi.txt"
        with open(self.path_category) as f:
            count_questions = 0
            while line := f.readline():
                print("Line "+str(count_questions)+" : "+line.rstrip())
                count_questions+=1
            self.count_questions = count_questions
        self.current_answer = 0

        #define container bottom button answer
        container_button = Label(self)
        container_button["bg"] = "#eadebc"
        container_button.place(x=0, y=self.width*0.60, width=self.width, height=self.width-(self.width*0.60))


        start_x = 0 
        for i in range(4):
            button = Button(self)
            button.place(x=start_x+50, y=self.width*0.63, width=150, height=40)
            start_x = (150*(i+1))






