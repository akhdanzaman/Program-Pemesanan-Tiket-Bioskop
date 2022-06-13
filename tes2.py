from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

root = Tk()
root.title('ringkasan pembayaran')
root.config(background="white")
root.geometry('1000x600')
root.resizable(False,False)





def cariindekskursi():
    global indekskursi
    datakursi2 = pd.read_csv('datakursi2.csv')
    carkur3 = pd.DataFrame(datakursi2)
    carkur2 = carkur3[carkur3['judul']=="ARCHER"]
    carkur = carkur2[carkur2['tanggal']==22]
    indekskursi = carkur[carkur['jam']==10].index.item()

def makebutton(avaibility,seatno,col,row):
    seat_code=int(seatno-6)
    lgn_button = Image.open('E:\Files\Tugasnip\KULIAH\Prokom\Program-Pemesanan-Tiket-Bioskop\Login Page\images\\btn1 - Copy.png')
    photo = ImageTk.PhotoImage(lgn_button)
    lgn_button_label = Label(root, image=photo, bg='white')
    lgn_button_label.image = photo
    lgn_button_label.grid(column=col,row=row,padx=5,pady=5)
    login = Button(lgn_button_label, 
                    text='SEAT %d' %seat_code, font=("yu gothic ui", 13, "bold"), 
                    width=5, bd=0,
                    bg='#3047ff',
                    cursor='hand2', 
                    activebackground='#3047ff', 
                    fg='white',
                    command =lambda:store_picked_seatno(seat_code))
    login.place(x=20, y=10)
    login.grid(column=seat_code,row=0)
    if avaibility != "ava":
        login.configure(bg='grey',state=DISABLED)

    if pickedseat.count(seat_code) > 0 :
        login.configure(bg='white',command =lambda:del_picked_seatno(seat_code))
        print("ADALUR")
def availableseat():
    kursifilm = pd.read_csv('datakursi2.csv')
    dfkf = pd.DataFrame(kursifilm)
    locfilm = dfkf.loc[indekskursi]
    daftarkursi = locfilm.tolist()
    print()
    for a in range (7,len(daftarkursi)):
        row = ((a+1)//8)-1
        column = ((a+1)-(7*row))-row
        if daftarkursi[a] == 1:
            print('%d Available'%(a-6))
            makebutton("ava",a,column,row)
        else:
            print('%d Booked' %(a-6))
            makebutton("booked",a,column,row)
    print()
    lgn_button = Image.open('E:\Files\Tugasnip\KULIAH\Prokom\Program-Pemesanan-Tiket-Bioskop\Login Page\images\\btn1 - Copy.png')
    photo = ImageTk.PhotoImage(lgn_button)
    lgn_button_label = Label(root, image=photo, bg='white')
    lgn_button_label.image = photo
    lgn_button_label.grid(column=2,row=9,padx=20,pady=20)
    login = Button(lgn_button_label, 
                    text='SUBMIT', font=("yu gothic ui", 13, "bold"), 
                    width=5, bd=0,
                    bg='#3047ff',
                    cursor='hand2', 
                    activebackground='#3047ff', 
                    fg='white',
                    command =lambda:pickseat())
    login.place(x=20, y=10)
    login.grid(column=1,row=1)
def store_picked_seatno(seat_code):
    pickedseat.append(seat_code)
    print(pickedseat)
    availableseat()
def del_picked_seatno(seat_code):
    pickedseat.remove(seat_code)
    print(pickedseat)
    availableseat()
pickedseat=[]
def pickseat():
    for i in range (len(pickedseat)):
        availableseat()
        print(pickedseat)
        pickedseat.append("0")
        datakursi = pd.read_csv('datakursi2.csv', index_col='kode')
        dfdk = pd.DataFrame(datakursi)
        kursipilihan = str(pickedseat[i])
        dfdk.loc[indekskursi, kursipilihan] = 0
        dfdk.to_csv("datakursi2.csv")
        print(pickedseat[i])
    pickedseat.clear()
    availableseat()

    

#Beli_button=PhotoImage(file="E:\\Files\\Tugasnip\\KULIAH\\Prokom\\Program-Pemesanan-Tiket-Bioskop\\btn2.png")


cariindekskursi()
availableseat()
root.mainloop()