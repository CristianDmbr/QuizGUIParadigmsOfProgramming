#import tkinter with the name tk
import tkinter as tk
#import font for fonts(text)
import tkinter.font as font
#this import everything from tkinter
from tkinter import * 
# and import messagebox as mb from tkinter
from tkinter import messagebox as mb
#import json to use json file for data
import json


#data for 1st quiz
with open('Data1.json') as f:
    data = json.load(f)
 
# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])


#data for 2nd quiz
with open('Data2.json') as f:
    data1 = json.load(f)
 
# set the question, options, and answer
question1 = (data1['question1'])
options1 = (data1['options1'])
answer1 = (data1[ 'answer1'])


#data for 3rd quiz
with open('Data3.json') as f:
    data2 = json.load(f)
 
# set the question, options, and answer
question2 = (data2['question2'])
options2 = (data2['options2'])
answer2 = (data2[ 'answer2'])


#data for 4th quiz
with open('Data4.json') as f:
    data3 = json.load(f)
 
# set the question, options, and answer
question3 = (data3['question3'])
options3 = (data3['options3'])
answer3 = (data3[ 'answer3'])

#create the frame page which will serve for all pages
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


#the frame for the page1
class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
 
            
#the frame for the page2
class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Topics", font=('Georgia', 18))
       label.pack(side="top",padx=5, pady=1)

class Page2_1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Search for a topic:", font=('Georgia', 18))
       label.pack(side="top",padx=5, pady=1)
   
 #the frame for the page3  
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Do you want to start?", font=('Georgia', 30))
       label.pack(padx=5, pady=2)

#the frame for the page4
class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Do you want to start?", font=('Georgia', 30))
       label.pack(padx=5, pady=2)

#the frame for the page5
class Page5(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Do you want to start?", font=('Georgia', 30))
       label.pack(padx=5, pady=2)

#the frame for the page6
class Page6(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Do you want to start?", font=('Georgia', 30))
       label.pack(padx=5, pady=2)

#the frame for the quiz(structure)
class Quiz(Page):
       
   
    def __init__(self,*args, **kwargs):
        Page.__init__(self, *args, **kwargs)
         
        #set the questions number to 0(start)
        self.q_no=0   
        self.display_title()
        self.display_question()  
        #opt_selected holds an integer value which is used for selected option in a question.
        self.opt_selected=IntVar()     
         #displaying radio button for the current question and used to display options for the current question
        self.opts=self.radio_buttons()   
        #this is to display options for the current question
        self.display_options()    
         #this is to display the button for next and exit in the actual quiz
        self.buttons() 
        self.data_size=len(question)
        #set the correct answered questions to 0
        self.correct=0
 
 

    def display_result(self):
         
        
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
        #this shows in a separate window the results from the quiz
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
 
 
  
    def check_ans(self, q_no):
         
        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[q_no]:
            # if the option is correct it return the value true
            return True
 
    
    def next_btn(self):
         
        # Check if the answer is correct
        if self.check_ans(self.q_no):
             
            # if the answer is correct it increments the correct by 1
            self.correct += 1
         
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
         
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the GUI
            self.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()

    def back_btn(self):
        # Check if the answer is correct
        if self.check_ans(self.q_no):
             
            # if the answer is correct it increments the correct by 1
            self.correct -= 1
         
        # back to the Question  
        self.q_no -= 1
      
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            self.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()
 
 
    def buttons(self):
         
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self, text="Next",command=self.next_btn,
        width=10,font=("Georgia",16,"bold"))
         
        # palcing the button  on the screen
      
        back_button=Button(self, text="Back", command=self.back_btn,
        width=10,bg="blue",font=("Georgia",16,"bold"))
        next_button.place(x=400,y=380)
        back_button.place(x=270,y=380)
         
        # This is the second button which is used to Quit the GUI
        # quit_button = Button(self, text="Quit", command=self.destroy,
        # width=5,bg="black", fg="white",font=("ariel",16," bold"))
         
        # placing the Quit button on the screen
        # quit_button.place(x=700,y=50)
 
 

    def display_options(self):
        val=0
         
        # deselecting the options
        self.opt_selected.set(0)
         
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
    
    
 
    # This method shows the current Question on the screen
    def display_question(self):
         
        # setting the Question properties
        q_no = Label(self, text=question[self.q_no], width=60,
        font=( 'Georgia' ,16, 'bold' ), anchor= 'w' )
         
        #placing the option on the screen
        q_no.place(x=210, y=100)
 
 
    # This method is used to Display Title
    def display_title(self):
         
        # The title to be shown
        title = Label(self, text="QUIZ 1",
        width=50, font=("Georgia", 20, "bold"))
         
        # place of the title
        title.place(x=20, y=1)
 
    
    def radio_buttons(self):
         
        # initialize the list with an empty list of options
        q_list = []
         
        # position of the first option
        y_pos = 150
         
        # adding the options to the list
        while len(q_list) < 4:
             
            # setting the radio button properties
            radio_btn = Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("Georgia",14))
             
            # adding the button to the list
            q_list.append(radio_btn)
             
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
             
            # incrementing the y-axis position by 40
            y_pos += 40
         
        # return the radio buttons
        return q_list


class Quiz2(Page):
       
   
    def __init__(self,*args, **kwargs):
        Page.__init__(self, *args, **kwargs)
         

        self.q_no=0
         
        self.display_title()
        self.display_question()                
        self.opt_selected=IntVar()         
        self.opts=self.radio_buttons()         
        self.display_options()         
        self.buttons()              
        self.data_size=len(question1)      
        self.correct=0
 
 

    def display_result(self):
         
     
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
      
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
 
 
  
    def check_ans(self, q_no):
         
        
        if self.opt_selected.get() == answer1[q_no]:
          
            return True
 
    
    def next_btn(self):
         
        
        if self.check_ans(self.q_no):
             
          
            self.correct += 1
         
       
        self.q_no += 1
         
        if self.q_no==self.data_size:
             
            self.display_result()
             
            self.destroy()
        else:
            self.display_question()
            self.display_options()
    
    def back_btn(self):
        if self.check_ans(self.q_no):
             
            self.correct -= 1
         
        self.q_no -= 1
      
        if self.q_no==self.data_size:
             
            self.display_result()
             
            self.destroy()
        else:
            self.display_question()
            self.display_options()
 
 
    def buttons(self):
         
     
        next_button = Button(self, text="Next",command=self.next_btn,
        width=10,font=("Georgia",16,"bold"))
         
        
        back_button=Button(self, text="Back", command=self.back_btn,
        width=10,bg="blue",font=("Georgia",16,"bold"))
        next_button.place(x=400,y=380)
        back_button.place(x=270,y=380)
 
 

    def display_options(self):
        val=0
         
        self.opt_selected.set(0)
         
       
        for option in options1[self.q_no]:
            self.opts[val]['text']=option
            val+=1
    
    
 
    def display_question(self):
         
        q_no = Label(self, text=question1[self.q_no], width=60,
        font=( 'Georgia' ,16, 'bold' ), anchor= 'w' )
         
        q_no.place(x=210, y=100)
 
 
    def display_title(self):
         
        title = Label(self, text="QUIZ 2",
        width=50, font=("Georgia", 20, "bold"))
         
        title.place(x=20, y=1)
 
    
    def radio_buttons(self):
         
        q_list = []
         
        y_pos = 150
         
        while len(q_list) < 4:
             
            radio_btn = Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("Georgia",14))
             
            q_list.append(radio_btn)
             
            radio_btn.place(x = 100, y = y_pos)
             
            y_pos += 40
         
        return q_list

class Quiz3(Page):
       
   
    def __init__(self,*args, **kwargs):
        Page.__init__(self, *args, **kwargs)
         

        self.q_no=0         
        self.display_title()
        self.display_question()        
        self.opt_selected=IntVar()         
        self.opts=self.radio_buttons()         
        self.display_options()         
        self.buttons()
        self.data_size=len(question2)      
        self.correct=0
 
 

    def display_result(self):
         
     
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
      
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
 
 
  
    def check_ans(self, q_no):
         
        if self.opt_selected.get() == answer2[q_no]:
            return True
 
    
    def next_btn(self):
         
        if self.check_ans(self.q_no):
             
            self.correct += 1
         
        self.q_no += 1
         
        if self.q_no==self.data_size:
             
            self.display_result()
             
            self.destroy()
        else:
            self.display_question()
            self.display_options()
    def back_btn(self):

        if self.check_ans(self.q_no):
             
            self.correct -= 1
         
        self.q_no -= 1
      
        if self.q_no==self.data_size:
             
            self.display_result()
             
            self.destroy()
        else:
            self.display_question()
            self.display_options()
 
 
    def buttons(self):
         
        
        next_button = Button(self, text="Next",command=self.next_btn,
        width=10,font=("Georgia",16,"bold"))
         
        
        back_button=Button(self, text="Back", command=self.back_btn,
        width=10,bg="blue",font=("Georgia",16,"bold"))
        next_button.place(x=400,y=380)
        back_button.place(x=270,y=380)
 
 

    def display_options(self):
        val=0
         
        self.opt_selected.set(0)
         
        
        for option in options2[self.q_no]:
            self.opts[val]['text']=option
            val+=1
    
    
 
    def display_question(self):
         
        q_no = Label(self, text=question2[self.q_no], width=60,
        font=( 'Georgia' ,16, 'bold' ), anchor= 'w' )
         
        q_no.place(x=210, y=100)
 
 
    def display_title(self):
         
        title = Label(self, text="QUIZ 3",
        width=50, font=("Georgia", 20, "bold"))
         
        title.place(x=20, y=1)
 
    
    def radio_buttons(self):
         
        q_list = []
         
        y_pos = 150
         
        while len(q_list) < 4:
             
            radio_btn = Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("Georgia",14))
             
            q_list.append(radio_btn)
             
            radio_btn.place(x = 100, y = y_pos)
             
            y_pos += 40
         
        return q_list


class Quiz4(Page):
       
   
    def __init__(self,*args, **kwargs):
        Page.__init__(self, *args, **kwargs)
         

        self.q_no=0         
        self.display_title()
        self.display_question()        
        self.opt_selected=IntVar()        
        self.opts=self.radio_buttons()         
        self.display_options()         
        self.buttons()      
        self.data_size=len(question3)      
        self.correct=0
 
 

    def display_result(self):
         
     
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
         
      
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
 
 
  
    def check_ans(self, q_no):
         
        if self.opt_selected.get() == answer3[q_no]:
            return True
 
    
    def next_btn(self):
         
        if self.check_ans(self.q_no):
             
            self.correct += 1
         
        self.q_no += 1
         
        if self.q_no==self.data_size:
             
            self.display_result()
             
            self.destroy()
        else:
            self.display_question()
            self.display_options()

    def back_btn(self):
        if self.check_ans(self.q_no):
             
            self.correct -= 1
         
        self.q_no -= 1
      
        if self.q_no==self.data_size:
             
            self.display_result()
             
            self.destroy()
        else:
            self.display_question()
            self.display_options()
 
 
    def buttons(self):
         
        
        next_button = Button(self, text="Next",command=self.next_btn,
        width=10,font=("Georgia",16,"bold"))
         
        
        back_button=Button(self, text="Back", command=self.back_btn,
        width=10,bg="blue",font=("Georgia",16,"bold"))
        next_button.place(x=400,y=380)
        back_button.place(x=270,y=380)
 
 

    def display_options(self):
        val=0
         
        self.opt_selected.set(0)
         
        
        for option in options3[self.q_no]:
            self.opts[val]['text']=option
            val+=1
    
    
 
    def display_question(self):
         
        q_no = Label(self, text=question3[self.q_no], width=60,
        font=( 'Georgia' ,16, 'bold' ), anchor= 'w' )
         
        q_no.place(x=210, y=100)
 
 
    def display_title(self):
         
        title = Label(self, text="QUIZ 4",
        width=50, font=("Georgia", 20, "bold"))
         
        title.place(x=20, y=1)
 
    
    def radio_buttons(self):
         
        q_list = []
         
        y_pos = 150
         
        while len(q_list) < 4:
             
            radio_btn = Radiobutton(self,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("Georgia",14))
             
            q_list.append(radio_btn)
             
            radio_btn.place(x = 100, y = y_pos)
             
            y_pos += 40
         
        return q_list

#this is the main frame, where all the pages, buttons, and other functions will be displayed
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #we note every page with a new name to work easily with them
        p1 = Page1(self)
        p2 = Page2(self)
        p2_1 = Page2_1(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)
        p7 = Quiz(self)
        p8 = Quiz2(self)
        p9 = Quiz3(self)
        p10 = Quiz4(self)

        #this will be the frame for the buttons from the pages
        buttonframe = tk.Frame(self)
        #this is where the pages are stored
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        #here, every page is placed in the container, in thier own space
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2_1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p9.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p10.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    #page1
        #we created a label in the first page and organised it with "pack"
        label = tk.Label(p1, text="Main Menu", font=('Georgia', 30))
        label.pack(pady=10)

        #this is an additional feature, where users can write thier names, and the system will greet them
        e = tk.Entry(p1, width=50)
        e.insert(0, "")

        def myCLick(a):
            hello = "Hello " + e.get() + "!"
            mylabel = tk.Label(p1, text=hello, font="Georgia" ,)
            mylabel.pack()
        #this is an additional button for entering the name
        # myButton = tk.Button(p1, text="Enter", command=myCLick)
        # myButton.pack()
        tk.Label(p1, text="Enter your name:", font="Georgia" ).pack()
        e.pack()
        root.bind('<Return>', myCLick)
        #the next butt which move to the next page
        b1 = tk.Button(p1, text="Next",font="Georgia" , command=lambda: p2.show()) 
        b1.pack()
        p1.show()
        

    #page2
        #the exit button will stay in the whole time on the window. We can quit the page whenever we want
        button_exit = tk.Button(root, text="exit program", font="Georgia" ,command=root.quit)

        #every topic we have is a button, and when is clicked it opens a new page
        b3=tk.Button(p2,text="Mathematics", font="Georgia" ,command=lambda:p3.show())
        b4=tk.Button(p2,text="Computer Sience",font="Georgia" , command=lambda:p4.show())
        b5=tk.Button(p2,text="Software Engineering",font="Georgia" , command=lambda:p5.show())
        b6=tk.Button(p2,text="History",font="Georgia" , command=lambda:p6.show())
        b7=tk.Button(p2,text="Additional page",font="Georgia" , command=lambda:p2_1.show())
 
        #this is how we pack the buttons      
        b3.pack(side="top",fill="x")
        b4.pack(side="top",fill="x")
        b5.pack(side="top",fill="x")
        b6.pack(side="top",fill="x")
        b7.pack(side="top",fill="x")

        #this button will switch pages
        b0=tk.Button(p2, text='Go back!', font=('Georgia', 15),fg='red',command=lambda:p1.show())
        b0.pack(pady=10)

       


        #page2_1  
        #this additional page offers the opportunity to check whether a topic exists or not
        s = tk.Entry(p2_1, width=30)
        
        s.insert(0,"")
        first="Mathematics"
        second="Computer Sience"
        third="Software Engineering"
        forth="History"
        b=[first, second,third, forth]

        def myt():
            if s.get() in b:
                text1 =  s.get() + " already exists!"
                newlabel = tk.Label(p2_1, text=text1, font="Georgia" )
                newlabel.pack()
            else:
                label2=tk.Label(p2_1, text="No such topic!", font="Georgia" )
                label2.pack()
        s.pack()
        enter1=tk.Button(p2_1, text="enter",font="Georgia" , command=myt)  
        enter1.pack()
        #this are the buttons if someone wants to add, edit, or delete a topic
        add1=tk.Button(p2_1, text="Add a new topic",font="Georgia" )
        add1.pack()

        edit1=tk.Button(p2_1, text="Edit a  topic",font="Georgia" )
        edit1.pack()

        delete1=tk.Button(p2_1, text="Delete a topic",font="Georgia" )
        delete1.pack()
        
        #this button allows the user to go back to the previous page
        b2=tk.Button(p2_1, text='Go back!', font=('Georgia', 15),fg='red',command=lambda:p2.show())
        b2.pack(pady=10)

 #page3
        #the buttons will repeat for all the pages
        b3_2=tk.Button(p3, text="Start the quiz!", font="Georgia" ,command=lambda:p7.show())
        b3_2.pack(side='top', pady=20)
      
       
        add_b= tk.Button(p3, text="Add a new question",font="Georgia" )
        add_b.pack()

        edit_b= tk.Button(p3, text="Edit a question",font="Georgia" )
        edit_b.pack()

        delete_b=tk.Button(p3, text="Detele a question",font="Georgia" )
        delete_b.pack()

        b3_1=tk.Button(p3,text="Back",font="Georgia" , command=lambda:p2.show())
        b3_1.pack(side="top", pady=10)

 #page4
        b3_2_a=tk.Button(p4, text="Start the quiz!", font="Georgia" ,command=lambda:p8.show())
        b3_2_a.pack(side='top', pady=20)
      
       
        add_b4= tk.Button(p4, text="Add a new question",font="Georgia" )
        add_b4.pack()

        edit_b4= tk.Button(p4, text="Edit a question",font="Georgia" )
        edit_b4.pack()

        delete_b4=tk.Button(p4, text="Detele a question",font="Georgia" )
        delete_b4.pack()

        b3_1a=tk.Button(p4,text="Back",font="Georgia" , command=lambda:p2.show())
        b3_1a.pack(side="top", pady=10)

 #page5
        b3_2b=tk.Button(p5, text="Start the quiz!",font="Georgia" , command=lambda:p9.show())
        b3_2b.pack(side='top', pady=20)
      
       
        add_b5= tk.Button(p5, text="Add a new question",font="Georgia" )
        add_b5.pack()

        edit_b5= tk.Button(p5, text="Edit a question",font="Georgia" )
        edit_b5.pack()

        delete_b5=tk.Button(p5, text="Detele a question",font="Georgia" )
        delete_b5.pack()

        b3_1b=tk.Button(p5,text="Back",font="Georgia" , command=lambda:p2.show())
        b3_1b.pack(side="top", pady=10)

 #page6
        b3_2c=tk.Button(p6, text="Start the quiz!",font="Georgia" , command=lambda:p10.show())
        b3_2c.pack(side='top', pady=20)
      
       
        add_b6= tk.Button(p6, text="Add a new question",font="Georgia" )
        add_b6.pack()

        edit_b6= tk.Button(p6, text="Edit a question",font="Georgia" )
        edit_b6.pack()

        delete_b6=tk.Button(p6, text="Detele a question",font="Georgia" )
        delete_b6.pack()

        b3_1c=tk.Button(p6,text="Back",font="Georgia" , command=lambda:p2.show())
        b3_1c.pack(side="top", pady=10)

    
        button_exit.pack(side="bottom",fill="x")

      


#this is how we form the window in tkinter, how we call the class, and set the title
root = tk.Tk()
main = MainView(root)
root.title("Quiz Generator")
    
main.pack(side="top", fill="both", expand=True)
#here we set the size of the page
root.wm_geometry("800x450")
root.mainloop()
 # END OF THE PROGRAM