import random
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os


def get_image(filename,width,height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)


#Mettre le code dans jeux
def jeux(fichier):
    print("Le jeux commence")

    jeu = Tk()

    if fichier:
        img = Image.open(fichier)
    else:
        img = Image.open("image1.jpg")

    w, h = img.size
    print(img.size)

    w_carre = 1/3*w     #coupage
    h_carre = 1/3*h


    coord_1 = list((0,0,w_carre,h_carre))
    coord_2 = list((w_carre,0,w_carre*2,h_carre))
    coord_3 = list((w_carre*2,0,w,h_carre))
    coord_4 = list((0,h_carre,w_carre,h_carre*2))
    coord_5 = list((w_carre,h_carre,w_carre*2,h_carre*2))
    coord_6 = list((w_carre*2,h_carre,w,h_carre*2))
    coord_7 = list((0,h_carre*2,w_carre,h))
    coord_8 = list((w_carre,h_carre*2,w_carre*2,h))
    coord_9 = list((w_carre*2,h_carre*2,w,h))




    morceau_1 = img.crop(coord_1)
    image1 = PhotoImage(morceau_1)
    morceau_2 = img.crop(coord_2)
    image2 = PhotoImage(morceau_2)
    morceau_3 = img.crop(coord_3)
    image3 = PhotoImage(morceau_3)
    morceau_4 = img.crop(coord_4)
    image4 = PhotoImage(morceau_4)
    morceau_5 = img.crop(coord_5)
    image5 = PhotoImage(morceau_5)
    morceau_6 = img.crop(coord_6)
    image6 = PhotoImage(morceau_6)
    morceau_7 = img.crop(coord_7)
    image7 = PhotoImage(morceau_7)
    morceau_8 = img.crop(coord_8)
    image8 = PhotoImage(morceau_8)
    morceau_9 = img.crop(coord_9)
    image9 = PhotoImage(morceau_9)


    morceau_1.save("1.jpeg")
    morceau_2.save("2.jpeg")
    morceau_3.save("3.jpeg")
    morceau_4.save("4.jpeg")
    morceau_5.save("5.jpeg")
    morceau_6.save("6.jpeg")
    morceau_7.save("7.jpeg")
    morceau_8.save("8.jpeg")
    morceau_9.save("9.jpeg")


    #dernière fenêtre
    def new():
        global second
        second=Toplevel(master=jeu)
        second.geometry('1150x700+200+60')
        second.title("FIN")
        second.config(bg='#E6F0C7')
        second.resizable(False,False)
        lbl=Label(second,text="Bien joué! Vous avez réussi !!",width=28,height=2,font=('Helvetica bold', 15),bg='#E6F0C7',compound=tkinter.CENTER)
        lbl.place(relx=0.5,rely=0.1, anchor='center')
        lbl.pack()
        image = Image.open("image1.jpg")
        photo = ImageTk.PhotoImage(image)
        quitter= Button(second, text="Fermer",font=('15'), bg='#C3CCAB', command=second.destroy)
        quitter.pack()
        quitter.place(relx=0.1,rely=0.58,anchor='center')
        can = tkinter.Canvas(second, width = 800, height = 600)
        can.create_image(0,0,anchor = tkinter.NW, image=photo)
        can.image=photo
        can.pack()




    #fonction du jeu
    def btnclick(x,y):
        global space_row
        global space_col
        if abs(x - space_row) + abs(y - space_col) == 1:
            buttons[space_row, space_col]['text'] = buttons[x,y]['text']
            buttons[x,y]['text']= ' '
            temp = buttons[x,y]['image']
            buttons[x,y]['image'] = buttons[space_row,space_col]['image']
            buttons[space_row,space_col]['image'] = temp
            space_row = x
            space_col = y
            n = 0
            for row in range(3):
                for col in range(3):
                    if buttons[row, col]['text'] != numbers[n]:
                        return
                    n +=1
            label['text'] = 'Bravo!'
            new()

            os.remove("1.jpeg")
            os.remove("2.jpeg")
            os.remove("3.jpeg")
            os.remove("4.jpeg")
            os.remove("5.jpeg")
            os.remove("6.jpeg")
            os.remove("7.jpeg")
            os.remove("8.jpeg")
            os.remove("9.jpeg")



    jeu.title('Puzzle')
    jeu.geometry('800x600+200+100')
    jeu.resizable(width=False,height=False)
    Button(jeu,text="suivant",command=new)


    #background image
    canvas_jeu = tkinter.Canvas(jeu, width= 800, height=600)
    im_jeu = get_image('beige.jpg',800,600)
    canvas_jeu.create_image(400,300,image=im_jeu)
    canvas_jeu.pack()


    im_label= get_image('beige.jpg',800,60)
    label = Label(master=jeu,text="Remettez les puzzles dans l'ordre!",fg='#8D63B3',font=("Impact","15","bold"),image=im_label,compound=tkinter.CENTER)
    label.place(relx=0,rely=0,relheight=0.1,relwidth=1)
    row_of_space=0
    space_col=0
    numbers=list('12345678 ')
    random.shuffle(numbers)
    buttons= {}
    im_button={}
    for row in range(3):
        for col in range(3):
            button = Button(jeu,command=lambda x=row,y=col : btnclick(x,y),fg='white',font=("Impact","50"),compound=tkinter.CENTER)
            buttons[row,col] = button
            index = numbers.pop()
            button['text'] = index
            if index == ' ':
                im_button[row,col] = get_image('blanc.jpg',240,180)
            else:
                im_button[row,col] = get_image(f'{index}.jpeg',240,180)
            button['image'] = im_button[row,col]
            button.place(relx=0.3*col,rely=0.1+0.3*row,relwidth=0.3,relheight=0.3)
            if button['text'] == ' ':
                space_row = row
                space_col = col
                change_var(row,col)
    numbers = list('12345678 ')
    jeu.mainloop()


def change_var(row,col):
    global space_row
    space_row = row
    global space_col
    space_col = col



def custom():
    Page_Custom = Tk()
    Page_Custom.geometry('1000x600')

    label = Label(Page_Custom, text ="Mettez votre image dans le fichier 'sources' et entrez le nom du fichier\n(ATTENTION : Mettez votre image au nom 'image1.jpeg')", font=('Helvetica bold', 18))  #
    label.pack()
    label.place(relx=0.5, rely=0.33, anchor='center')

    InputBox = Text(Page_Custom, height = 1.5, width = 52)
    InputBox.pack()
    InputBox.place(relx=0.5, rely=0.5, anchor='center')

    def verification():
        photo = InputBox.get("1.0",'end-1c')
        if Image.open(photo):
            Page_Custom.destroy()
            jeux(photo)


    button_commencer1 = Button(Page_Custom, text ="Commencer", font=('Helvetica bold', 15), command= verification)
    button_commencer1.pack()
    button_commencer1.place(relx=0.5, rely=0.67, anchor='center')


    Page_Custom.mainloop()





#Page d'accueil

Page_Acceuil = Tk()
Page_Acceuil.geometry('1100x700')
Page_Acceuil.title("Accueuil")

#background image
canvas_pa = tkinter.Canvas(Page_Acceuil, width= 1100, height=700)
im_pa = get_image('beige.jpg',1500,1100)
canvas_pa.create_image(400,300,image=im_pa)
canvas_pa.pack()

img_text=get_image('beige.jpg',500,80)
textprincipale = Label(Page_Acceuil,text='Puzzle coulissant', font=('Helvetica bold', 30) , image=img_text,compound=tkinter.CENTER)
textprincipale.pack()
textprincipale.place(relx=0.5, rely=0.33, anchor='center')

button_commencer = Button(Page_Acceuil,text='Commencer',font=('Helvetica bold', 20), command=lambda: [Page_Acceuil.destroy(), jeux(None)])
button_commencer.pack()
button_commencer.place(relx=0.5, rely=0.5, anchor='center')
button_commencer.config(border="2")


button_custom = Button(Page_Acceuil,text='Custom', font=('Helvetica bold', 15), command=lambda: [Page_Acceuil.destroy(), custom()])
button_custom.pack()
button_custom.place(relx=0.5, rely=0.65, anchor='center')
button_custom.config(border="2")


Page_Acceuil.mainloop()