import requests
from tkinter import *
data_new=""
count=0
respond = requests.get(url="https://api.kanye.rest/")
data = respond.json()["quote"]

for word in data:
    if word==" ":
        data_new+=word
        count+=1
    else:
        data_new+=word
    if count>=4:
        data_new+="\n"
        count=0


def create_quote():
    data_new = ""
    count = 0
    respond = requests.get(url="https://api.kanye.rest/")
    data = respond.json()["quote"]
    for word in data:
        if word == " ":
            data_new += word
            count += 1
        else:
            data_new += word
        if count >= 4:
            data_new += "\n\n"
            count = 0
    canvas.itemconfig(quote,text=data_new)




window = Tk()
window.config(pady=50,padx=50)
window.title("Kanye Quotes")
canvas=Canvas(width=350,height=450)



#------background_photo------#
background_png_img=PhotoImage(file="background.png")
canvas.create_image(200,250,image=background_png_img)
quote=canvas.create_text(200,250,text=data_new,fill="black",font=('Helvetica 15 bold'))

canvas.grid()

#--------button--------#
kanye_image=PhotoImage(file="kanye.png")
kanye_button=Button(image=kanye_image,highlightthickness=0,command=create_quote)
kanye_button.grid(row=6,column=0)





#-----text-----#







window.mainloop()



