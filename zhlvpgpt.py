
from tkinter import *
import openai
openai.api_key = "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" #api key 

prompt = "display the symptoms of a random mental disorder without showing the name of disorder, and let me enter the name of disorder and treatment, Check my anwser and determine if it is correct or not, and repeat it until I stop"
## "content" is the prompt of initial conversation but it oftenly display the symptoms of major depressive disorder"
#message_history = [{"role":"user", "content": prompt}]

#don't show the first item in the list message_history
message_history = [{"role":"user", "content": prompt}]
def inticaht():
    completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = message_history
        )
    
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": reply_content})
    print(message_history)
    return reply_content


def caht(msg, role="user"): #function to start communication
    message_history.append({"role":role, "content": msg})

    
    while True:
        
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = message_history
        )

        reply_content = completion.choices[0].message.content
        
        print(reply_content)
        
        message_history.append({"role": "assistant", "content": reply_content})
        ##inp = input(">: ")
                

        return reply_content



first_reply= inticaht()




BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window=Tk()
        self._setup_main_window()
    def run(self):
        self.window.mainloop()


    def _setup_main_window(self):
        self.window.title("VP")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, text=first_reply, font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)


        line=Label(self.window, width=450, bg=BG_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        bottom_label=Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        self.msg_entry=Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.0011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)


        send_button = Button(bottom_label, text="Enter", font=FONT_BOLD, width=20, bg=BG_GRAY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "you")
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}:{msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"patient:{caht(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)










        self.text_widget.see(END)



if __name__=="__main__":
    app=ChatApplication()
    app.run()