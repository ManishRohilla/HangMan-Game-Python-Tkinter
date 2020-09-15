from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


window = Tk()
window.title("4 chances to save the innocent life")
window.geometry("1920x1020")
Label(window,text="Select Level:",font=('Helvetica','20')).grid(row=2,column=3)



chances=4;

image_paths=['5.png','4.png','3.png','2.png','1.png']
img = Image.open(image_paths[chances])
img = img.resize((650,550), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(columnspan=11,rowspan=11,sticky=W+E+N+S,padx=20,pady=10,column=6, row=2)
answer_arr=[]
def easy():
    btn001["text"]= "RESET"
    btn002["text"]= "MEDIUM"
    btn003["text"]= "HARD"
    label01=Label(window,text="HINT:Highlevel Interpreted Programming Language",font=('Helvetica','20'))
    label01.grid(row=17,column=12)
    
    def clicked(alphabet):
        global chances;
        answer= "JAVASCRIPT";
        if alphabet in answer: 
            if alphabet=="J":
                bt01["text"]= "J"
                bt01["bg"]='yellow'
                bt01.grid(column=20, row=2)
            elif alphabet=="V":
                bt03["text"]= "V"
                bt03["bg"]='yellow'
                bt03.grid(column=22, row=2)
            elif alphabet=="S":
                bt05["text"]= "S"
                bt05["bg"]='yellow'
                bt05.grid(column=24, row=2)
            elif alphabet=="C":
                bt06["text"]= "C"
                bt06["bg"]='yellow'
                bt06.grid(column=25, row=2)
            elif alphabet=="I":
                bt08["text"]= "I"
                bt08["bg"]='yellow'
                bt08.grid(column=27, row=2)
            elif alphabet=="P":
                bt09["text"]= "P"
                bt09["bg"]='yellow'
                bt09.grid(column=28, row=2)
        else:
            chances = chances - 1;
            txt="Chances remaining "+str(chances);
            
            label1.configure(text=txt)
            image = Image.open(image_paths[chances])
            image = image.resize((650,550), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.grid(columnspan=11,rowspan=11,sticky=W+E+N+S,padx=20,pady=5,column=6, row=2)
            panel.image = imgnew
            
            if chances==0:
                txt="Chances remaining "+str(chances);
            
                label1.configure(text=txt)
                messagebox.showinfo("LOOSE","Hanged!!!!!")
               
                window.destroy()
        if  bt01["text"]=="J" and bt03["text"]=="V" and bt05["text"]=="S" and bt06["text"]=="C" and bt08["text"]=="I" and bt09["text"]=="P" :
            messagebox.showinfo("You saved me ","You Win")
            
            window.destroy()
        print(chances)




    bt01 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt01.grid(column=20, row=2)
    bt02 = Button(window, text="A",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt02.grid(column=21, row=2)
    bt03 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt03.grid(column=22, row=2)
    bt04 = Button(window, text="A",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt04.grid(column=23, row=2)
    bt05 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt05.grid(column=24, row=2)
    bt06 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt06.grid(column=25, row=2)
    bt07 = Button(window, text="R",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt07.grid(column=26, row=2)
    bt08 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt08.grid(column=27, row=2)
    bt09 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt09.grid(column=28, row=2)
    bt10 = Button(window, text="T",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt10.grid(column=29, row=2)


    btn1 = Button(window, text="A",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
    btn1.grid(column=20, row=4)
    btn2 = Button(window, text="B",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
    btn2.grid(column=21, row=4)
    btn3 = Button(window, text="C",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
    btn3.grid(column=22, row=4)
    btn4 = Button(window, text="D",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
    btn4.grid(column=23, row=4)
    btn5 = Button(window, text="E",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
    btn5.grid(column=24, row=4)
    btn6 = Button(window, text="F",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
    btn6.grid(column=25, row=4)
    btn7 = Button(window, text="G",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
    btn7.grid(column=26, row=4)
    btn8 = Button(window, text="H",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
    btn8.grid(column=27, row=4)
    btn9 = Button(window, text="I",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
    btn9.grid(column=28, row=4)
    btn10 = Button(window, text="J",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
    btn10.grid(column=29, row=4)
    
    btn11= Button(window, text="K",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
    btn11.grid(column=20, row=5)
    btn12 = Button(window, text="L",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
    btn12.grid(column=21, row=5)
    btn13 = Button(window, text="M",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
    btn13.grid(column=22, row=5)
    btn14 = Button(window, text="N",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
    btn14.grid(column=23, row=5)
    btn15= Button(window, text="O",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
    btn15.grid(column=24, row=5)
    btn16 = Button(window, text="P",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
    btn16.grid(column=25, row=5)
    btn17 = Button(window, text="Q",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
    btn17.grid(column=26, row=5)
    btn18 = Button(window, text="R",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
    btn18.grid(column=27, row=5)
    btn19 = Button(window, text="S",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
    btn19.grid(column=28, row=5)
    btn20 = Button(window, text="T",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
    btn20.grid(column=29, row=5)
    
    btn21 = Button(window, text="U",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
    btn21.grid(column=22, row=6)
    btn22 = Button(window, text="V",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
    btn22.grid(column=23, row=6)
    btn23 = Button(window, text="W",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
    btn23.grid(column=24, row=6)
    btn24 = Button(window, text="X",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
    btn24.grid(column=25, row=6)
    btn25 = Button(window, text="Y",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
    btn25.grid(column=26, row=6)
    btn26 = Button(window, text="Z",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
    btn26.grid(column=27, row=6)


def medium():
    btn002["text"]= "RESET"
    btn001["text"]= "EASY"
    btn003["text"]= "HARD"
    label01=Label(window,text="HINT:German multinational automotive manufacturer",font=('Helvetica','20'))
    label01.grid(row=17,column=12)
    
    
    def clicked(alphabet):
        global chances
        answer= "VOLKSWAGEN";
        
        if alphabet in answer: 
            if alphabet=="V":
                bt01["text"]="V"
                bt01["bg"]='yellow'
                bt01.grid(column=20, row=2)
            elif alphabet=="L":
                bt03["text"]= "L"
                bt03["bg"]='yellow'
                bt03.grid(column=22, row=2)
            elif alphabet=="K":
                bt04["text"]= "K"
                bt04["bg"]='yellow'
                bt04.grid(column=23, row=2)
            elif alphabet=="W":
                bt06["text"]= "W"
                bt06["bg"]='yellow'
                bt06.grid(column=25, row=2)
            elif alphabet=="A":
                bt07["text"]= "A"
                bt07["bg"]='yellow'
                bt07.grid(column=26, row=2)
            elif alphabet=="E":
                bt09["text"]= "E"
                bt09["bg"]='yellow'
                bt09.grid(column=28, row=2)
            
        else:
            chances = chances - 1;
            txt="Chances remaining "+str(chances);
            
            label1.configure(text=txt)
            image = Image.open(image_paths[chances])
            image = image.resize((650,550), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.grid(columnspan=11,rowspan=11,sticky=W+E+N+S,padx=20,pady=5,column=6, row=2)
            panel.image = imgnew
            
            if chances==0:
                txt="Chances remaining "+str(chances);
            
                label1.configure(text=txt)
                messagebox.showinfo("Loose to guess","Hanged!!!!!")
               
                window.destroy()
        if  bt01["text"]=="V" and bt03["text"]=="L" and bt04["text"]=="K" and bt06["text"]=="W" and bt07["text"]=="A" and bt09["text"]=="E" :
            messagebox.showinfo("You saved me ","You Win")
            
            window.destroy()
        print(chances)




    bt01 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt01.grid(column=20, row=2)
    bt02 = Button(window, text="O",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt02.grid(column=21, row=2)
    bt03 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt03.grid(column=22, row=2)
    bt04 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt04.grid(column=23, row=2)
    bt05 = Button(window, text="S",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt05.grid(column=24, row=2)
    bt06 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt06.grid(column=25, row=2)
    bt07 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt07.grid(column=26, row=2)
    bt08 = Button(window, text="G",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt08.grid(column=27, row=2)
    bt09 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt09.grid(column=28, row=2)
    bt10 = Button(window, text="N",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt10.grid(column=29, row=2)

    btn1 = Button(window, text="A",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
    btn1.grid(column=20, row=4)
    btn2 = Button(window, text="B",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
    btn2.grid(column=21, row=4)
    btn3 = Button(window, text="C",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
    btn3.grid(column=22, row=4)
    btn4 = Button(window, text="D",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
    btn4.grid(column=23, row=4)
    btn5 = Button(window, text="E",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
    btn5.grid(column=24, row=4)
    btn6 = Button(window, text="F",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
    btn6.grid(column=25, row=4)
    btn7 = Button(window, text="G",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
    btn7.grid(column=26, row=4)
    btn8 = Button(window, text="H",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
    btn8.grid(column=27, row=4)
    btn9 = Button(window, text="I",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
    btn9.grid(column=28, row=4)
    btn10 = Button(window, text="J",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
    btn10.grid(column=29, row=4)
    
    btn11= Button(window, text="K",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
    btn11.grid(column=20, row=5)
    btn12 = Button(window, text="L",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
    btn12.grid(column=21, row=5)
    btn13 = Button(window, text="M",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
    btn13.grid(column=22, row=5)
    btn14 = Button(window, text="N",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
    btn14.grid(column=23, row=5)
    btn15= Button(window, text="O",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
    btn15.grid(column=24, row=5)
    btn16 = Button(window, text="P",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
    btn16.grid(column=25, row=5)
    btn17 = Button(window, text="Q",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
    btn17.grid(column=26, row=5)
    btn18 = Button(window, text="R",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
    btn18.grid(column=27, row=5)
    btn19 = Button(window, text="S",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
    btn19.grid(column=28, row=5)
    btn20 = Button(window, text="T",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
    btn20.grid(column=29, row=5)
    
    btn21 = Button(window, text="U",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
    btn21.grid(column=22, row=6)
    btn22 = Button(window, text="V",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
    btn22.grid(column=23, row=6)
    btn23 = Button(window, text="W",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
    btn23.grid(column=24, row=6)
    btn24 = Button(window, text="X",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
    btn24.grid(column=25, row=6)
    btn25 = Button(window, text="Y",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
    btn25.grid(column=26, row=6)
    btn26 = Button(window, text="Z",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
    btn26.grid(column=27, row=6)


def hard():
    btn002["text"]= "MEDIUM"
    btn001["text"]= "EASY"
    btn003["text"]= "RESET"
    label01=Label(window,text="HINT:Who develops Computer Software and codes?",font=('Helvetica','20'))
    label01.grid(row=17,column=12)
    def clicked(alphabet):
        global chances
        answer= "PROGRAMMER";
        
        if alphabet in answer: 
            if alphabet=="P":
                bt01["text"]="P"
                bt01["bg"]='yellow'
                bt01.grid(column=20, row=2)
            elif alphabet=="O":
                bt03["text"]= "O"
                bt03["bg"]='yellow'
                bt03.grid(column=22, row=2)
            elif alphabet=="G":
                bt04["text"]= "G"
                bt04["bg"]='yellow'
                bt04.grid(column=23, row=2)
            elif alphabet=="A":
                bt06["text"]= "A"
                bt06["bg"]='yellow'
                bt06.grid(column=25, row=2)
            elif alphabet=="M":
                bt07["text"]= "M"
                bt07["bg"]='yellow'
                bt07.grid(column=26, row=2)
                bt08["text"]= "M"
                bt08["bg"]='yellow'
                bt08.grid(column=27, row=2)
            elif alphabet=="E":
                bt09["text"]= "E"
                bt09["bg"]='yellow'
                bt09.grid(column=28, row=2)
            
        else:
            chances = chances - 1;
            txt="Chances remaining "+str(chances);
            
            label1.configure(text=txt)
            image = Image.open(image_paths[chances])
            image = image.resize((650,550), Image.ANTIALIAS)
            imgnew = ImageTk.PhotoImage(image)
            panel.configure(image=imgnew)
            panel.grid(columnspan=11,rowspan=11,sticky=W+E+N+S,padx=20,pady=5,column=6, row=0)
            panel.image = imgnew
            
            if chances==0:
                txt="Chances remaining "+str(chances);
            
                label1.configure(text=txt)
                messagebox.showinfo("Loose to guess","Hanged!!!!!")
               
                window.destroy()
        if  bt01["text"]=="P" and bt03["text"]=="O" and bt04["text"]=="G" and bt06["text"]=="A" and bt07["text"]=="M" and bt08["text"]=="M" and bt09["text"]=="E" :
            messagebox.showinfo("You saved me ","You Win")
            
            window.destroy()
        print(chances)




    bt01 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt01.grid(column=20, row=2)
    bt02 = Button(window, text="R",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt02.grid(column=21, row=2)
    bt03 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt03.grid(column=22, row=2)
    bt04 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt04.grid(column=23, row=2)
    bt05 = Button(window, text="R",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt05.grid(column=24, row=2)
    bt06 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt06.grid(column=25, row=2)
    bt07 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt07.grid(column=26, row=2)
    bt08 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt08.grid(column=27, row=2)
    bt09 = Button(window, text=" ",bg="red", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt09.grid(column=28, row=2)
    bt10 = Button(window, text="R",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'))
    bt10.grid(column=29, row=2)
    
    btn1 = Button(window, text="A",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
    btn1.grid(column=20, row=4)
    btn2 = Button(window, text="B",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
    btn2.grid(column=21, row=4)
    btn3 = Button(window, text="C",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
    btn3.grid(column=22, row=4)
    btn4 = Button(window, text="D",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
    btn4.grid(column=23, row=4)
    btn5 = Button(window, text="E",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
    btn5.grid(column=24, row=4)
    btn6 = Button(window, text="F",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
    btn6.grid(column=25, row=4)
    btn7 = Button(window, text="G",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
    btn7.grid(column=26, row=4)
    btn8 = Button(window, text="H",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
    btn8.grid(column=27, row=4)
    btn9 = Button(window, text="I",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
    btn9.grid(column=28, row=4)
    btn10 = Button(window, text="J",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
    btn10.grid(column=29, row=4)
    
    btn11= Button(window, text="K",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
    btn11.grid(column=20, row=5)
    btn12 = Button(window, text="L",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
    btn12.grid(column=21, row=5)
    btn13 = Button(window, text="M",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
    btn13.grid(column=22, row=5)
    btn14 = Button(window, text="N",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
    btn14.grid(column=23, row=5)
    btn15= Button(window, text="O",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
    btn15.grid(column=24, row=5)
    btn16 = Button(window, text="P",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
    btn16.grid(column=25, row=5)
    btn17 = Button(window, text="Q",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
    btn17.grid(column=26, row=5)
    btn18 = Button(window, text="R",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
    btn18.grid(column=27, row=5)
    btn19 = Button(window, text="S",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
    btn19.grid(column=28, row=5)
    btn20 = Button(window, text="T",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
    btn20.grid(column=29, row=5)
    
    btn21 = Button(window, text="U",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
    btn21.grid(column=22, row=6)
    btn22 = Button(window, text="V",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
    btn22.grid(column=23, row=6)
    btn23 = Button(window, text="W",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
    btn23.grid(column=24, row=6)
    btn24 = Button(window, text="X",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
    btn24.grid(column=25, row=6)
    btn25 = Button(window, text="Y",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
    btn25.grid(column=26, row=6)
    btn26 = Button(window, text="Z",bg="black", fg="white",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
    btn26.grid(column=27, row=6)

btn001=Button(window,text="EASY",command=easy,bg="yellow", fg="Black",width=10,height=2,font=('Helvetica','20'))
btn001.grid(row=3,column=3,padx=5,pady=5)
btn002=Button(window,text="Medium",command=medium,bg="green", fg="Black",width=10,height=2,font=('Helvetica','20'))
btn002.grid(row=4,column=3,padx=5,pady=5)
btn003=Button(window,text="HARD",command=hard,bg="red", fg="Black",width=10,height=2,font=('Helvetica','20'))
btn003.grid(row=5,column=3,padx=5,pady=5)
label1=Label(window,text="Total Chances are : 4",font=('Helvetica','20'))
label1.grid(row=16,column=12)
window.mainloop()
