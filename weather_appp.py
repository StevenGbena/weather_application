
from tkinter import*
import requests
import json


root=Tk()
root.title('THE WEATHER APP')
root.geometry('400x600')





mylabel=Label(root,text='THE WEATHER APP', borderwidth=10,bg='black',fg='red')
mylabel.pack(pady=40,padx=20)


mycity=Label(root,text='Enter city below ↓',borderwidth=10,fg='red')
mycity.pack(pady=10)


myentry=Entry(root)
myentry.pack()



def enter_word():
    current=myentry.get()
    myentry.delete(0,END)
    myentry.insert(0,current)



def click():   
    if mybutton!=enter_word:
        current=myentry.get()
        api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(current)
        response = requests.get(api_url, headers={'X-Api-Key': '9ZAxyrOegSgnYcGz+ZGZCg==jUc2wr6SUutx1S8O'}) 
        
    
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:",'City not found', response.status_code, response.text,)




mybutton=Button(root,text='check status',command=click)
mybutton.pack()

display=Label(root,)





root.mainloop()