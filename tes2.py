from tkinter import *
from PIL import ImageTk, Image
import pandas as pd


win=Tk()
win.title("Cinemakmur Premiere")
 


def ds_pf():
    global s_pf
    s_pf = Toplevel()
    s_pf.title('Pemilihan Film')
    s_pf.config(background="white")
    s_pf.geometry('1000x600')
    s_pf.resizable(False,False)    
    kotak=PhotoImage(file='bg1.png')
    Label(s_pf,image=kotak,background="white").place(x=0,y=0)        

    global dfdf
    film = pd.read_csv('film.csv')
    dfdf = pd.DataFrame(film)

    locjudul = (dfdf["judul"])
    daftarjudul = locjudul.tolist()
    locposter = (dfdf["poster"])
    daftarposter = locposter.tolist()
    print(daftarposter)

    Belitiket_btnimg=PhotoImage(file="Buttonbelitiket.png")
    def button_beli(x):
        belitiket_btn=Button(s_pf,image=Belitiket_btnimg, borderwidth=0,fg = "#ffffff", 
                    cursor="hand2", bd=0, font=("yu gothic ui", 8, "bold"), 
                    background="white",activebackground='#ffffff',wraplength=100,
                    text=("Beli Tiket Sekarang"),compound="center",
                    command = ds_pj)
        belitiket_btn.place(x=450,y=330)
    
        image2 = Image.open((dfdf['poster'].iloc[x]))
        
        resize_image2 = image2.resize((177,250))
        
        img2 = ImageTk.PhotoImage(resize_image2)
        
        poster_button=Button(s_pf,image=img2, borderwidth=0,fg = "#424243", 
                cursor="hand2", bd=0, font=("yu gothic ui", 8, "bold"), 
                background="white",activebackground='#ffffff',wraplength=100,
                command = ds_pj)
        poster_button.image = img2
        poster_button.place(x=220,y=130)
        global judul,sinopsis
        judul=Label(s_pf,text=dfdf['judul'].iloc[x], font=('yu gothic ui', 16, 'bold'), background="white")
        judul.place(x=450,y=130)
        sinopsis=Label(s_pf, font=('yu gothic ui', 9, 'bold'),text="%.250s" %dfdf['sinopsis'].iloc[x]+str(" ..."),
                       wraplength=200,justify="left",bg='white')
        sinopsis.place(x=450,y=165)
        global pilihanfilm
        pilihanfilm=x
    button_beli(1)
        



    def button_poster():
        Button(s_pj,image=tglback_btn, borderwidth=0, 
        cursor="hand2", bd=0, font=("arial, 16"), 
        background="white",activebackground='#ffffff',
        command=lambda:tanggal_back()
        ).place(x=570,y=138,)  
        for i in range (len(daftarposter)-2):
            image = Image.open((dfdf['poster'].iloc[i]))
            resize_image = image.resize((91,127))
            img = ImageTk.PhotoImage(resize_image)
            image2 = Image.open((dfdf['poster2'].iloc[i]))
            resize_image2 = image2.resize((91,127)) 
            img2 = ImageTk.PhotoImage(resize_image2)
            
            poster_button=Button(s_pf,image=img, borderwidth=0,fg = "#424243", 
                    cursor="hand2", bd=0, font=("yu gothic ui", 8, "bold"), 
                    background="white",activebackground='#ffffff',wraplength=100,
                    text=((dfdf['judul'].iloc[i])),compound="top",
                    command=lambda i=i:fpickposter(i))
            poster_button.image = img
            poster_button.place(x=50+(i*115),y=437)
            if pickposter[0] == i:
                poster_button.configure(image=img2,command=lambda i=i:fdelposter(i))
                poster_button.image = img2
        judul.configure(text="")
        sinopsis.configure(text="")


    def fpickposter(poster):
        if len(pickposter)>0:
            del pickposter[0]
        pickposter.append(poster)
        button_poster()
        button_beli(poster)
    def fdelposter(poster):
        pickposter.remove(poster)
        button_poster()
    global pickposter
    pickposter=[1]
    button_poster()
    judul.configure(text=dfdf['judul'].iloc[1])
    sinopsis.configure(text="%.250s" %dfdf['sinopsis'].iloc[1]+str(" ..."))


    s_pf.mainloop()


def ds_pj():
    global s_pj
    s_pf.destroy()
    s_pj = Toplevel()
    s_pj.title('Pemilihan Jadwal')
    s_pj.config(background="white")
    s_pj.geometry('1000x600')
    s_pj.resizable(False,False)





    heading=Label(s_pj,text='Pilih Kursi Anda', font=('arial', 15, 'bold'), background="white")
    heading.place(x=50,y=50)

    kotak=PhotoImage(file='kotak4.png')
    Label(s_pj,image=kotak,background="white").place(x=530,y=50)


    image2 = Image.open((dfdf['poster'].iloc[pilihanfilm]))
    resize_image2 = image2.resize((182,254)) 
    img2 = ImageTk.PhotoImage(resize_image2)
    poster=Label(s_pj,image=img2)
    poster.image=(dfdf['poster'].iloc[pilihanfilm])
    poster.place(x=50,y=100)

    genre=Label(s_pj,text='Genre', font=('arial', 8), background="white")
    genre.place(x=250,y=100)

    genre2=Label(s_pj,text=(dfdf['genre'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    genre2.place(x=250,y=115)

    durasi=Label(s_pj,text='Durasi', font=('arial', 8), background="white")
    durasi.place(x=250,y=150)

    durasi2=Label(s_pj,text=(dfdf['durasi'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    durasi2.place(x=250,y=165)

    sut=Label(s_pj,text='Sutradara', font=('arial', 8), background="white")
    sut.place(x=250,y=200)

    sut2=Label(s_pj,text=(dfdf['sutradara'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    sut2.place(x=250,y=215)

    rat=Label(s_pj,text='Rating', font=('arial', 8), background="white")
    rat.place(x=250,y=250)

    rat2=Label(s_pj,text=(dfdf['rating'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    rat2.place(x=250,y=265)

    judul=Label(s_pj,text=dfdf['judul'].iloc[pilihanfilm], font=('arial', 16, 'bold'), background="white")
    judul.place(x=50,y=367)

    sinop=Label(s_pj,text='Sinopsis', font=('arial', 8), background="white")
    sinop.place(x=50,y=405)

    sinop2=Label(s_pj,font=('yu gothic ui', 9, 'bold'),text=dfdf['sinopsis'].iloc[pilihanfilm],
                       wraplength=400,justify="left",bg='white')
    sinop2.place(x=50,y=425)

    Beli_button=PhotoImage(file="Button3.png")
    beli2=Button(s_pj,image=Beli_button, borderwidth=0, 
                cursor="hand2", bd=0, font=("arial, 16"), 
                background="white",
                command=ds_pk)
    beli2.place(x=670,y=440)

    tglback_btn=PhotoImage(file="Buttonback.png")
    tglforward_btn=PhotoImage(file="Buttonforward.png")
    Button(s_pj,image=tglback_btn, borderwidth=0, 
            cursor="hand2", bd=0, font=("arial, 16"), 
            background="white",activebackground='#ffffff',
            command=lambda:tanggal_back()
            ).place(x=570,y=138,)   
    Button(s_pj,image=tglforward_btn, borderwidth=0, 
            cursor="hand2", bd=0, font=("arial, 16"), 
            background="white",activebackground='#ffffff',
            command=lambda:tanggal_forward()
            ).place(x=890,y=138,)   



    tanggal_tersedia = pd.read_csv('datakursi2.csv')
    dftt = pd.DataFrame(tanggal_tersedia)

    locfilm = (dftt["tanggal"])
    daftartanggal = locfilm.tolist()
    daftartanggal_clear=(list(dict.fromkeys(daftartanggal)))
    jadwal_btnp=PhotoImage(file="Buttontglpasif.png")
    jadwal_btna=PhotoImage(file="Buttontglaktif.png")
    global displaytanggal
    displaytanggal=[daftartanggal_clear[0],daftartanggal_clear[1],daftartanggal_clear[2]]

    def tanggal_back():
        global displaytanggal
        if displaytanggal[0] != daftartanggal_clear[1]:
            print(displaytanggal)
            print(daftartanggal_clear)
            terakhir = displaytanggal[2]
            displaytanggal=[]
            indeksterakhir = daftartanggal_clear.index(terakhir)
            displaytanggal.append(daftartanggal_clear[indeksterakhir-3])
            displaytanggal.append(daftartanggal_clear[indeksterakhir-2])
            displaytanggal.append(daftartanggal_clear[indeksterakhir-1])
            print(displaytanggal)
            button_tanggal()   
    def tanggal_forward():
        global displaytanggal
        if displaytanggal[2] != daftartanggal_clear[-1]:
            print(displaytanggal)
            print(daftartanggal_clear)
            terakhir = displaytanggal[0]
            displaytanggal=[]
            indeksterakhir = daftartanggal_clear.index(terakhir)
            displaytanggal.append(daftartanggal_clear[indeksterakhir+1])
            displaytanggal.append(daftartanggal_clear[indeksterakhir+2])
            displaytanggal.append(daftartanggal_clear[indeksterakhir+3])
            print(displaytanggal)
            button_tanggal()
    bulan=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    print(displaytanggal)

    def button_tanggal():
        for i in range (len(displaytanggal)):
            tgl_button=Button(s_pj,image=jadwal_btnp, borderwidth=0,fg = "#424243", 
                    cursor="hand2", bd=0, font=("yu gothic ui", 14, "bold"), 
                    background="white",activebackground='#ffffff',
                    text="%d %s"%(displaytanggal[i],bulan[6]),compound="center",
                    command=lambda i=i:fpicktanggal(displaytanggal[i]))
            tgl_button.place(x=595+(i*100),y=133)
            print(picktanggal.count(displaytanggal[i])>0)
            if picktanggal.count(displaytanggal[i])>0:
                tgl_button.configure(image=jadwal_btna,fg = "#ffffff",
                                    command=lambda i=i:fdeltanggal(displaytanggal[i]))
    def fpicktanggal(tanggal):
        if len(picktanggal)>0:
            del picktanggal[0]
        picktanggal.append(tanggal)
        button_tanggal()
    def fdeltanggal(tanggal):
        picktanggal.remove(tanggal)
        button_tanggal()
    global picktanggal,pickjam
    picktanggal=[]
    button_tanggal()

#==================================

    jam_tersedia = pd.read_csv('datakursi2.csv')
    dfjt = pd.DataFrame(jam_tersedia)

    locfilm = (dfjt["jam"])
    daftarjam = locfilm.tolist()
    daftarjam_clear=(list(dict.fromkeys(daftarjam)))
    jam_btnp=PhotoImage(file="Buttonjampasif.png")
    jam_btna=PhotoImage(file="Buttonjamaktif.png")
    global displayjam
    displayjam=[daftarjam_clear[0],daftarjam_clear[1],daftarjam_clear[2]]

    def button_jam():
        for i in range (len(displayjam)):
            jam_button=Button(s_pj,image=jam_btnp, borderwidth=0,fg = "#424243", 
                    cursor="hand2", bd=0, font=("yu gothic ui", 12, "bold"), 
                    background="white",activebackground='#ffffff',
                    text="%d:00"%(displayjam[i]),compound="center",
                    command=lambda i=i:fpickjam(displayjam[i]))
            jam_button.place(x=670+(i*85),y=213)
            print(pickjam.count(displayjam[i])>0)
            if pickjam.count(displayjam[i])>0:
                jam_button.configure(image=jam_btna,fg = "#ffffff",
                                    command=lambda i=i:fdeljam(displayjam[i]))
    def fpickjam(jam):
        if len(pickjam)>0:
            del pickjam[0]
        pickjam.append(jam)
        button_jam()
    def fdeljam(jam):
        pickjam.remove(jam)
        button_jam()
    global pickjam
    pickjam=[]
    button_jam()

    s_pj.mainloop()


def ds_pk():
    global root
    s_pj.destroy()
    root = Toplevel()
    root.title('Pemilihan Kursi')
    root.config(background="white")
    root.geometry('1000x600')
    root.resizable(False,False)

    heading=Label(root,text='Pilih Kursi Anda', font=('arial', 15, 'bold'), background="white")
    heading.place(x=50,y=50)

    kotak=PhotoImage(file='kotak3.png')
    Label(root,image=kotak,background="white").place(x=530,y=50)

    image2 = Image.open((dfdf['poster'].iloc[pilihanfilm]))
    resize_image2 = image2.resize((182,254)) 
    img2 = ImageTk.PhotoImage(resize_image2)
    poster=Label(root,image=img2)
    poster.image=(dfdf['poster'].iloc[pilihanfilm])
    poster.place(x=50,y=100)

    genre=Label(root,text='Genre', font=('arial', 8), background="white")
    genre.place(x=250,y=100)

    genre2=Label(root,text=(dfdf['genre'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    genre2.place(x=250,y=115)

    durasi=Label(root,text='Durasi', font=('arial', 8), background="white")
    durasi.place(x=250,y=150)

    durasi2=Label(root,text=(dfdf['durasi'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    durasi2.place(x=250,y=165)

    sut=Label(root,text='Sutradara', font=('arial', 8), background="white")
    sut.place(x=250,y=200)

    sut2=Label(root,text=(dfdf['sutradara'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    sut2.place(x=250,y=215)

    rat=Label(root,text='Rating', font=('arial', 8), background="white")
    rat.place(x=250,y=250)

    rat2=Label(root,text=(dfdf['rating'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
    rat2.place(x=250,y=265)

    judul=Label(root,text=dfdf['judul'].iloc[pilihanfilm], font=('arial', 16, 'bold'), background="white")
    judul.place(x=50,y=367)

    sinop=Label(root,text='Sinopsis', font=('arial', 8), background="white")
    sinop.place(x=50,y=405)

    sinop2=Label(root,font=('yu gothic ui', 9, 'bold'),text=dfdf['sinopsis'].iloc[pilihanfilm],
                       wraplength=400,justify="left",bg='white')
    sinop2.place(x=50,y=425)

    Beli_button=PhotoImage(file="Button2.png")
    beli=Button(root,image=Beli_button, borderwidth=0, 
                cursor="hand2", bd=0, font=("arial, 16"), 
                command =ds_rp,background="white")
    beli.place(x=670,y=440)



    def cariindekskursi():
        global indekskursi
        datakursi2 = pd.read_csv('datakursi2.csv')
        carkur3 = pd.DataFrame(datakursi2)
        carkur2 = carkur3[carkur3['judul']=="ARCHER"]
        carkur = carkur2[carkur2['tanggal']==picktanggal[0]]
        indekskursi = carkur[carkur['jam']==pickjam[0]].index.item()

    def makebutton(avaibility,seatno,col,row):

        bariskursi=['A','B','C',"D","E","F","G"]
        seat_code=int(seatno-6)
        lgn_button = Image.open('Button.png')
        photo = ImageTk.PhotoImage(lgn_button)

        lgn_button_label = Label(root, bg='white')
        lgn_button_label.image = photo
        lgn_button_label.place(x=513+(col*47),y=150+(row*25))
        login = Button(lgn_button_label, 
                        text='%s%d' %(bariskursi[row],col), font=("yu gothic ui", 9, "bold"), 
                        width=5, bd=0,
                        bg='#152238',
                        cursor='hand2', 
                        activebackground='#3047ff', 
                        fg='white',
                        command =lambda:store_picked_seatno(seat_code),
                        borderwidth=0)
        login.place(x=20, y=10)
        login.pack()
        if avaibility != "ava":
            login.configure(bg='grey',state=DISABLED)

        if pickedseat.count(seat_code) > 0 :
            login.configure(bg='#3047ff',command =lambda:del_picked_seatno(seat_code))
            print("ADALUR")


    def availableseat():
        kursifilm = pd.read_csv('datakursi2.csv')
        dfkf = pd.DataFrame(kursifilm)
        locfilm = dfkf.loc[indekskursi]
        daftarkursi = locfilm.tolist()
        print()
        for a in range (7,len(daftarkursi)):
            row = ((a+1)//8)-1
            column = ((a+1)-(7*row))-row-7
            if daftarkursi[a] == 1:
                print('%d Available'%(a-6))
                makebutton("ava",a,column,row)
            else:
                print('%d Booked' %(a-6))
                makebutton("booked",a,column,row)
        print()
        lgn_button = Image.open('Button.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(root, image=photo, bg='white')
        lgn_button_label.image = photo
        lgn_button_label.grid(column=2,row=9,padx=1,pady=1)
        login = Button(lgn_button_label, 
                        text='SUBMIT', font=("yu gothic ui", 5, "bold"), 
                        width=3, bd=0,
                        bg='#3047ff',
                        cursor='hand2', 
                        activebackground='#3047ff', 
                        fg='white',
                        command =lambda:pickseat())
        login.place(x=20, y=10)
        login.grid(column=1,row=1)
    def store_picked_seatno(seat_code):
        pickedseat.append(seat_code)
        availableseat()
        row = ((seat_code-1)//8)
        column = ((seat_code)-(7*row))-row
        bariskursi=['A','B','C',"D","E","F","G"]
        pickedseat_code.append('%s%d' %(bariskursi[row],column))
        seatframe=Label(root,width=100,expand=None,borderwidth=0)
        seatframe.place(x=570,y=385)
        seat=Label(seatframe,text=pickedseat_code,wraplength=100,width=15,borderwidth=0, font=('arial', 11, 'bold'), background="white",justify=CENTER)
        seat.pack()
        hargaframe=Label(root,width=100,expand=None,borderwidth=0)
        hargaframe.place(x=780,y=385)
        harga=Label(hargaframe,text='Rp %d'%(len(pickedseat*45000)),wraplength=100,width=15,borderwidth=0, font=('arial', 11, 'bold'), background="white",justify=CENTER)
        harga.pack()
        print(pickedseat_code)
    def del_picked_seatno(seat_code):
        global seatharga
        pickedseat.remove(seat_code)
        availableseat()
        row = ((seat_code-1)//8)
        column = ((seat_code)-(7*row))-row
        bariskursi=['A','B','C',"D","E","F","G"]
        pickedseat_code.remove('%s%d' %(bariskursi[row],column))
        seatframe=Label(root,width=100,expand=None,borderwidth=0)
        seatframe.place(x=570,y=385)
        seat=Label(seatframe,text=pickedseat_code,wraplength=100,width=15,borderwidth=0, font=('arial', 11, 'bold'), background="white",justify=CENTER)
        seat.pack()
        hargaframe=Label(root,width=100,expand=None,borderwidth=0)
        hargaframe.place(x=780,y=385)
        seatharga=str('Rp%d'%(len(pickedseat)*45000))
        harga=Label(hargaframe,text=seatharga,wraplength=100,width=15,borderwidth=0, font=('arial', 11, 'bold'), background="white",justify=CENTER)
        harga.pack()
        print(pickedseat_code)
    global pickedseat,pickedseat_code
    
    pickedseat=[]
    pickedseat_code=[]

    cariindekskursi()
    availableseat()
    root.mainloop()

def ds_rp():
    root.destroy()
    s_rp= Toplevel()
    s_rp.title('ringkasan pembayaran')
    s_rp.config(background="white")
    s_rp.geometry('1000x600')
    s_rp.resizable(False,False)

    heading2=Label(s_rp,text='Konfirmasi Pembayaran', font=('arial', 15, 'bold'), background="white")
    heading2.place(x=50,y=50)

    kotak2=PhotoImage(file='kotak.png')
    Label(s_rp,image=kotak2,background="white").place(x=570,y=50)


    image2 = Image.open((dfdf['poster'].iloc[pilihanfilm]))
    resize_image2 = image2.resize((182,254)) 
    img2 = ImageTk.PhotoImage(resize_image2)
    poster=Label(s_rp,image=img2)
    poster.image=(dfdf['poster'].iloc[pilihanfilm])
    poster.place(x=50,y=100)


    jdwl2=Label(s_rp,text='Detail Jadwal', font=('arial', 11, 'bold'), background="white")
    jdwl2.place(x=250,y=100)

    jdl2=Label(s_rp,text='Judul Film', font=('arial', 10), background="white")
    jdl2.place(x=250,y=140)


    film2=Label(s_rp,text=dfdf['judul'].iloc[pilihanfilm], font=('arial', 10, 'bold'), background="white")
    film2.place(x=250,y=160)

    tgl2=Label(s_rp,text='Tanggal', font=('arial', 10), background="white")
    tgl2.place(x=250,y=200)

    tbt2=Label(s_rp,text="%s Juli 2022"%picktanggal[0], font=('arial', 10, 'bold'), background="white")
    tbt2.place(x=250,y=220)

    kodebayar=Label(s_rp,text='Kode Bayar', font=('arial', 10), background="white")
    kodebayar.place(x=250,y=260)

    kodebayar2=Label(s_rp,text="%s Juli 2022"%picktanggal[0], font=('arial', 10, 'bold'), background="white")
    kodebayar2.place(x=250,y=280)

    kls2=Label(s_rp,text='Studio', font=('arial', 10), background="white")
    kls2.place(x=50,y=370)

    film2=Label(s_rp,text='Teater 1', font=('arial', 10, 'bold'), background="white")
    film2.place(x=50,y=390)

    tic2=Label(s_rp,text='Tiket', font=('arial', 10), background="white")
    tic2.place(x=50,y=430)

    seat2=Label(s_rp,text=pickedseat_code, font=('arial', 10, 'bold'), background="white")
    seat2.place(x=50,y=450)

    jam2=Label(s_rp,text='Jam', font=('arial', 10), background="white")
    jam2.place(x=200,y=370)

    pkl2=Label(s_rp,text="%d:00"%pickjam[0], font=('arial', 10, 'bold'), background="white")
    pkl2.place(x=200,y=390) 

    ro2=Label(s_rp,text='Ringkasan Order', font=('arial', 11, 'bold'), background="white")
    ro2.place(x=600,y=120)

    dt2=Label(s_rp,text='Detail Transaksi', font=('arial', 9, 'bold'), background="white")
    dt2.place(x=600,y=160)

    rs2=Label(s_rp,text='REGULAR SEAT', font=('arial', 9), background="white")
    rs2.place(x=600,y=190)

    by2=Label(s_rp,text='BIAYA LAYANAN', font=('arial', 9), background="white")
    by2.place(x=600,y=220)

    h1=Label(s_rp,text=('Rp%d'%(len(pickedseat)*45000)), font=('arial', 9), background="white")
    h1.place(x=800,y=190)

    h2=Label(s_rp,text="Rp4.000", font=('arial', 9), background="white")
    h2.place(x=800,y=220)

    bates2=Label(s_rp,text='__________________________________________________________', background="white")
    bates2.place(x=600,y=250)

    tb2=Label(s_rp,text='Total Bayar', font=('arial', 9, 'bold'), background="white")
    tb2.place(x=600,y=280)

    tb2=Label(s_rp,text=('Rp%d'%((len(pickedseat)*45000)+4000)), font=('arial', 9, 'bold'), background="white")
    tb2.place(x=800,y=280)

    bates2=Label(s_rp,text='__________________________________________________________', background="white")
    bates2.place(x=600,y=310)

    sk2=Label(s_rp,text='* Pembelian tidak bisa dibatalkan', font=('arial', 7), background="white", fg='#f00')
    sk2.place(x=600,y=340)
    global pickseat
    def pickseat():
        for i in range (len(pickedseat)):
            pickedseat.append("0")
            datakursi = pd.read_csv('datakursi2.csv', index_col='kode')
            dfdk = pd.DataFrame(datakursi)
            kursipilihan = str(pickedseat[i])
            dfdk.loc[indekskursi, kursipilihan] = 0
            dfdk.to_csv("datakursi2.csv")
            print(pickedseat[i])
        pickedseat.clear()
    Beli_button2=PhotoImage(file="Button.png")
    beli2=Button(s_rp,image=Beli_button2, borderwidth=0, cursor="hand2", bd=0, font=("arial, 16"), background="white",command=pickseat)
    beli2.place(x=680,y=400)

    s_rp.mainloop()


ds_pf()
mainloop()