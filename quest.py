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
                question["answer_option"] = answ_btn
                question["correct_answer"] =  splite_word[6]
                
                self.questions.append(question)
                #print("Line "+str(count_questions)+" : "+line.rstrip())
                count_questions+=1
            self.count_questions = count_questions
        self.total_correct_answer = 0
        self.total_wrong_answer = 0

        #define image for question
        image_question = Label(self)
        image_question.place(x=0.10*self.width, y=0.20*self.height, width=600, height=300)
        image = Image.open(self.path_category+self.questions[0]["img_question"]+".png")
        resized_image = image.resize((600, 300), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(resized_image)
        image_question.configure(image=tk_image)
        image_question.image = tk_image
        self.image_question = image_question

        #define desc for question
        desc_question = Label(self)
        desc_question.place(x=0.10*self.width, y=(0.20*self.height)+250, width=600, height=50)
        desc_question.configure(text=self.questions[0]["desc_question"])
        self.desc_question = desc_question

        #define container bottom button answer
        container_button = Label(self)
        container_button["bg"] = "#eadebc"
        container_button.place(x=0, y=self.width*0.60, width=self.width, height=self.width-(self.width*0.60))


        #setup button position of answer user
        start_x = 0 
        list_button_answer = []
        self.current_answer = 0
        for i in range(4):
            button_answer  = Button(self)
            button_answer.configure(text=self.questions[0]["answer_option"][i])
            button_answer.place(x=start_x+20, y=self.width*0.63, width=160, height=40)
            start_x = (160*(i+1)) +((i+1)*5)
            button_answer["command"] = lambda selected_button = button_answer : self.answer_question(selected_button)
            list_button_answer.append(button_answer)

        self.list_button_answer = list_button_answer

    def answer_question(self, button_selected):
        #print("answer question is "+self.list_button_answer[self.current_answer].cget('text'))
        self.check_answer(button_selected)
        self.current_answer=self.current_answer+1
        self.next_question()

    def check_answer(self, button_answer):
        answer_player = button_answer.cget('text')
        correct_answer = self.questions[self.current_answer]["correct_answer"]
        print("answer user "+ answer_player)
        print("correct answer "+correct_answer)

        if answer_player == correct_answer:
            self.total_correct_answer += 1
            print("Correct....")
        else:
            self.total_wrong_answer +=1
            print("Wrong.....")
    
    def next_question(self):
        if self.current_answer<self.count_questions:
            idx_question = self.current_answer
            self.desc_question.configure(text=self.questions[idx_question]["desc_question"])
            
            image = Image.open(self.path_category+self.questions[idx_question]["img_question"]+".png")
            resized_image = image.resize((600, 300), Image.ANTIALIAS)
            tk_image = ImageTk.PhotoImage(resized_image)
            self.image_question.configure(image=tk_image)
            self.image_question.image = tk_image

            for i in range(4):
                self.list_button_answer[i].configure(text=self.questions[idx_question]["answer_option"][i])            


