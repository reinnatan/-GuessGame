from base_form import BaseForm
from tkinter import Button, Label, PanedWindow
from PIL import Image, ImageTk

class QuestPage(BaseForm):
    def __init__(self, category, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #panelWindow = PanedWindow(self, ori)
        self.path_category_questions = "categories/"+category+"/informasi.txt"
        self.path_category = "categories/"+category+"/"
        
        self.questions = []
        with open(self.path_category_questions, mode='r', encoding="utf-8-sig") as f:
            count_questions = 0
            while line := f.readline():
                splite_word = line.rstrip().split(";")
                question = {}
                answ_btn = [] 
                
                question["img_question"] = splite_word[0]
                question["desc_question"] = splite_word[1]
                answ_btn.append(splite_word[2])
                answ_btn.append(splite_word[3])
                answ_btn.append(splite_word[4])
                answ_btn.append(splite_word[5])
                answ_btn.append(splite_word[6])
                question["answer_option"] = answ_btn
                
                self.questions.append(question)
                #print("Line "+str(count_questions)+" : "+line.rstrip())
                count_questions+=1
            self.count_questions = count_questions
        self.current_answer = 0

        #define image for question
        image_question = Label(self)
        image_question.place(x=0.20*self.width, y=0.20*self.height, width=400, height=250)
        image = Image.open(self.path_category+self.questions[0]["img_question"]+".png")
        resized_image = image.resize((400, 250), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized_image)
        image_question.configure(image=tk_image)
        image_question.image = tk_image

        #define desc for question
        desc_question = Label(self)
        desc_question.place(x=0.20*self.width, y=(0.20*self.height)+250, width=400, height=50)
        desc_question.configure(text=self.questions[0]["desc_question"])

        #define container bottom button answer
        container_button = Label(self)
        container_button["bg"] = "#eadebc"
        container_button.place(x=0, y=self.width*0.60, width=self.width, height=self.width-(self.width*0.60))


        #setup button position of answer user
        start_x = 0 
        for i in range(5):
            button = Button(self)
            button.configure(text=self.questions[0]["answer_option"][i])
            button.place(x=start_x+15, y=self.width*0.63, width=130, height=40)
            start_x = (130*(i+1)) +((i+1)*5)






