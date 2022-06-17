from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from fpdf import FPDF
import random, string
import datetime
import tkinter.messagebox as messagebox
import webbrowser

win=Tk()
win.title("Cinemakmur Premiere")

 
def login1():
    userData = pd.read_csv('databases\\userdatabase.csv')
    df = pd.DataFrame(userData)
    

    global user
    global pasw
    global nomor
    user=username_entry.get()
    pasw=password_entry.get()
 
    matching_creds = (len(df[(df.username == user) & (df.password == pasw)]) > 0)

    if matching_creds:
        print('success')
        ds_pf()
    else:
        print('\nYour account is not registered yet!')
        print('please contact admin')
        messagebox.showinfo("Ingpo", "Username atau password anda salah")
def register1():
    userData = pd.read_csv('databases\\userdatabase.csv')
    df = pd.DataFrame(userData)

    global user
    global pasw
    user=username_entry2.get()
    pasw=password_entry2.get()
    namalengkap=nama_entry2.get()

    matching_creds = (len(df[(df.username == user) ]) < 1)

    if matching_creds and user != "":
        print('success')
        newuser = {'username' : [user],
                   'password' : [pasw],
                   'namalengkap' : [namalengkap]}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('databases\\userdatabase.csv', mode='a', index=False, header=False)
        messagebox.showinfo("Ingpo", "Register berhasil")
        s_rs.destroy()
    else:
        s_rs.destroy()
        messagebox.showinfo("Ingpo", "Mohon isi data diri dengan benar")
        registerscreen()


def rekapbeli():
    global nomor
    datapembelian = pd.read_csv('databases\\datapembelian.csv')
    dfdt = pd.DataFrame(datapembelian)
    ambildatauser = pd.read_csv('databases\\userdatabase.csv',index_col = 'username')
    dfadu = pd.DataFrame(ambildatauser)
    nomor = dfadu.loc[user, 'nomor']
    namalengkap = dfadu.loc[user,'namalengkap']
    countrow = dfdt.shape[0]
    nopembelian = f"{(countrow + 1):08d}"
    waktupembelian = datetime.datetime.now()
    
    databelibaru = {'nopembelian' : [nopembelian],
                'waktupembelian' : [waktupembelian],
                'user' : [user],
                'namalengkap' : [namalengkap],
                'judul' : [dfdf['judul'].iloc[pilihanfilm]],
                'waktu' : [pickjam[0]],
                'tanggal' : [picktanggal[0]],
                'kodebayar' : [id],
                }
    inputdatapembelian = pd.DataFrame(databelibaru)
    inputdatapembelian.to_csv('databases\\datapembelian.csv', mode='a', index=False, header=False)

    print('')



def registerscreen():
    global s_rs
    s_rs = Toplevel()
    s_rs.title('Pemilihan Film')
    s_rs.config(background="white")
    s_rs.geometry('1920x1080')
    s_rs.resizable(False,False)    
    bg_frame = Image.open('images\\M6new.png')
    photo = ImageTk.PhotoImage(bg_frame)
    bg_panel = Label(s_rs, image=photo)
    bg_panel.image = photo
    bg_panel.pack(fill='both', expand='yes')

    # ====== Login Frame =========================
    global lgn_frame
    lgn_frame = Frame(s_rs, bg='white', width=950, height=600)
    lgn_frame.place(x=300, y=100)

    # ========================================================================
    # ============ Left Side Image ================================================
    # ========================================================================
    side_image = Image.open('images\\Gnew2.png')
    photo = ImageTk.PhotoImage(side_image)
    side_image_label = Label(lgn_frame, image=photo, bg='#ffffff')
    side_image_label.image = photo
    side_image_label.place(x=0, y=30)
    

    # ========================================================================
    # ============ Sign In label =============================================
    # ========================================================================
    sign_in_label = Label(lgn_frame, text="Sign Up", bg="#ffffff", fg="navy",
                                font=("yu gothic ui", 17, "bold"))
    sign_in_label.place(x=550, y=130)

    # ========================================================================
    # ============================username====================================
    # ========================================================================
    global password_entry2, username_entry2, nama_entry2
    username_label = Label(lgn_frame, text="Username", bg="#ffffff", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    username_label.place(x=550, y=190)

    username_entry2 = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                font=("yu gothic ui ", 12, "bold"))
    username_entry2.place(x=550, y=225, width=270)

    username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    username_line.place(x=550, y=249)
    
    #====================NAMA===============
    nama_label = Label(lgn_frame, text="Nama", bg="#ffffff", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    nama_label.place(x=550, y=350)

    
    nama_entry2 = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                font=("yu gothic ui", 12, "bold"))
    nama_entry2.place(x=550, y=387, width=244)

    nama_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    nama_line.place(x=550, y=410)





    # ========================================================================
    # ============================login button================================
    # ========================================================================
    Belitiket_btnimg=PhotoImage(file="images\\btn1.png")
    belitiket_btn=Button(lgn_frame,image=Belitiket_btnimg, borderwidth=0,fg = "#ffffff", 
                    cursor="hand2", bd=0, font=("yu gothic ui", 14, "bold"), 
                    background="white",activebackground='#ffffff',wraplength=100,
                    text=("REGISTER"),compound="center",
                    command = register1)
    belitiket_btn.place(x=550, y=420)
    
    # =========== Sign Up ==================================================
    sign_button = Button(lgn_frame, text='Already Have Account', font=("yu gothic ui", 11, "bold"),
                            relief=FLAT, borderwidth=0, background="#ffffff", fg='black',command=lambda: s_rs.destroy())
    sign_button.place(x=622, y=485)




    # ========================================================================
    # ============================password====================================
    # ========================================================================
    password_label = Label(lgn_frame, text="Password", bg="#ffffff", fg="#4f4e4d",
                                font=("yu gothic ui", 13, "bold"))
    password_label.place(x=550, y=270)

    
    password_entry2 = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                font=("yu gothic ui", 12, "bold"), show="*")
    password_entry2.place(x=550, y=306, width=244)

    password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
    password_line.place(x=550, y=330)

    # ========= show/hide password ==================================================================
    show_image = ImageTk.PhotoImage \
        (file='images\\show.png')

    hide_image = ImageTk.PhotoImage \
        (file='images\\hide.png')


    def show():
        hide_button = Button(lgn_frame, image=hide_image, command=hide, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        hide_button.place(x=860, y=320)
        password_entry.config(show='')

    def hide():
        show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,
                                    activebackground="white"
                                    , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=860, y=320)
        password_entry.config(show='*')

        show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=860, y=320)
    s_rs.mainloop()


def loginbaru():
      bg_frame = Image.open('images\\M6new.png')
      photo = ImageTk.PhotoImage(bg_frame)
      bg_panel = Label(win, image=photo)
      bg_panel.image = photo
      bg_panel.pack(fill='both', expand='yes')

      # ====== Login Frame =========================
      global lgn_frame
      lgn_frame = Frame(win, bg='white', width=950, height=600)
      lgn_frame.place(x=300, y=110)





      # ========================================================================
      # ============ Left Side Image ================================================
      # ========================================================================
      side_image = Image.open('images\\Gnew2.png')
      photo = ImageTk.PhotoImage(side_image)
      side_image_label = Label(lgn_frame, image=photo, bg='#ffffff')
      side_image_label.image = photo
      side_image_label.place(x=0, y=30)
      

      # ========================================================================
      # ============ Sign In label =============================================
      # ========================================================================
      sign_in_label = Label(lgn_frame, text="Sign In", bg="#ffffff", fg="navy",
                                  font=("yu gothic ui", 17, "bold"))
      sign_in_label.place(x=550, y=140)

      # ========================================================================
      # ============================username====================================
      # ========================================================================
      global password_entry, username_entry
      username_label = Label(lgn_frame, text="Username", bg="#ffffff", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
      username_label.place(x=550, y=200)

      username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                  font=("yu gothic ui ", 12, "bold"))
      username_entry.place(x=550, y=235, width=270)

      username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
      username_line.place(x=550, y=259)
  
    

      # ========================================================================
      # ============================login button================================
      # ========================================================================
      
      lgn_button = Image.open('images\\btn1.png')
      photo = ImageTk.PhotoImage(lgn_button)
      lgn_button_label = Label(lgn_frame, image=photo, bg='#ffffff')
      lgn_button_label.image = photo
      lgn_button_label.place(x=550, y=350)
      login = Button(lgn_button_label,command=login1, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                          bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
      login.place(x=20, y=10)
      
      # =========== Sign Up ==================================================
      sign_label = Label(lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                              relief=FLAT, borderwidth=0, background="#ffffff", fg='black')
      sign_label.place(x=550, y=435)

      lgn_button2 = Image.open('images\\register.png')
      photo2 = ImageTk.PhotoImage(lgn_button2)
      lgn_button_label2 = Button(lgn_frame, image=photo2, bg='#ffffff',borderwidth=0,
                                    command=registerscreen)
      lgn_button_label2.image = photo2
      lgn_button_label2.place(x=670, y=430, width=111, height=35)


      # ========================================================================
      # ============================password====================================
      # ========================================================================
      password_label = Label(lgn_frame, text="Password", bg="#ffffff", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
      password_label.place(x=550, y=280)

      
      password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#ffffff", fg="#6b6a69",
                                  font=("yu gothic ui", 12, "bold"), show="*")
      password_entry.place(x=550, y=316, width=244)

      password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
      password_line.place(x=550, y=340)
    
      # ========= show/hide password ==================================================================
      show_image = ImageTk.PhotoImage \
          (file='images\\show.png')

      hide_image = ImageTk.PhotoImage \
          (file='images\\hide.png')

      def show():
        hide_button = Button(lgn_frame, image=hide_image, command=hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        hide_button.place(x=860, y=320)
        password_entry.config(show='')

      def hide():
        show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=860, y=320)
        password_entry.config(show='*')

      show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,
                                activebackground="white"
                                , borderwidth=0, background="white", cursor="hand2")
      show_button.place(x=860, y=320)

loginbaru()

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))
def pembayaran():
  datapembelian = pd.read_csv('databases\\datapembelian.csv')
  dfdp = pd.DataFrame(datapembelian)
  while True:
    id_generator()
    if (len(dfdp.loc[dfdp['kodebayar'] == id_generator])) < 1:
        global id
        id = id_generator()
        print(id)
        break

def ds_pf():
    global s_pf
    s_pf = Toplevel()
    s_pf.title('Pemilihan Film')
    s_pf.config(background="white")
    s_pf.geometry('1000x600')
    s_pf.resizable(False,False)    
    kotak=PhotoImage(file='images\\bg1.png')
    Label(s_pf,image=kotak,background="white").place(x=0,y=0)        

    global dfdf
    film = pd.read_csv('databases\\film.csv')
    dfdf = pd.DataFrame(film)

    locjudul = (dfdf["judul"])
    daftarjudul = locjudul.tolist()
    locposter = (dfdf["poster"])
    daftarposter = locposter.tolist()
    print(daftarposter)

    Belitiket_btnimg=PhotoImage(file="images\\Buttonbelitiket.png")
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
        sinopsis=Label(s_pf, font=('yu gothic ui', 9, 'bold'),text="%.250s" %dfdf['sinopsis'].iloc[x],
                       wraplength=200,justify="left",bg='white')
        sinopsis.place(x=450,y=165)
        global pilihanfilm
        pilihanfilm=x
    button_beli(1)

    def button_poster():
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
    sinopsis.configure(text="%.250s" %dfdf['sinopsis'].iloc[1])


    s_pf.mainloop()

def balikpf():
    s_pj.destroy()
    ds_pf()
    
def ds_pj():
    global s_pj
    s_pf.destroy()
    s_pj = Toplevel()
    s_pj.title('Pemilihan Jadwal')
    s_pj.config(background="white")
    s_pj.geometry('1000x600')
    s_pj.resizable(False,False)

    back_btn=PhotoImage(file="images\\Buttonback.png")
    Button(s_pj,image=back_btn, borderwidth=0, 
            cursor="hand2", bd=0, font=("arial, 16"), 
            background="white",activebackground='#ffffff',
            command=lambda:balikpf()
            ).place(x=10,y=10,)  


    heading=Label(s_pj,text='Pilih Kursi Anda', font=('arial', 15, 'bold'), background="white")
    heading.place(x=50,y=50)

    kotak=PhotoImage(file='images\\kotak4.png')
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

    Beli_button=PhotoImage(file="images\\Button3.png")
    beli2=Button(s_pj,image=Beli_button, borderwidth=0, 
                cursor="hand2", bd=0, font=("arial, 16"), 
                background="white",
                command=lambda:[ds_pk()])
    beli2.place(x=670,y=440)


    tglback_btn=PhotoImage(file="images\\Buttonback.png")
    tglforward_btn=PhotoImage(file="images\\Buttonforward.png")
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

    tanggal_tersedia = pd.read_csv('databases\\datakursi2.csv')
    dftt = pd.DataFrame(tanggal_tersedia)

    locfilm = (dftt["tanggal"])
    daftartanggal = locfilm.tolist()
    daftartanggal_clear=(list(dict.fromkeys(daftartanggal)))
    jadwal_btnp=PhotoImage(file="images\\Buttontglpasif.png")
    jadwal_btna=PhotoImage(file="images\\Buttontglaktif.png")
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

    jam_tersedia = pd.read_csv('databases\\datakursi2.csv')
    dfjt = pd.DataFrame(jam_tersedia)

    locfilm = (dfjt["jam"])
    daftarjam = locfilm.tolist()
    daftarjam_clear=(list(dict.fromkeys(daftarjam)))
    jam_btnp=PhotoImage(file="images\\Buttonjampasif.png")
    jam_btna=PhotoImage(file="images\\Buttonjamaktif.png")
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

def balikpj():
    s_pk.destroy()
    ds_pj()

def ds_pk():
    if len(pickjam)>0 and len(picktanggal)>0:
        global s_pk
        print(pickjam)
        print(picktanggal)
        print(pilihanfilm)
        s_pj.destroy()
        s_pk = Toplevel()
        s_pk.title('Pemilihan Kursi')
        s_pk.config(background="white")
        s_pk.geometry('1000x600')
        s_pk.resizable(False,False)

        back_btn=PhotoImage(file="images\\Buttonback.png")
        Button(s_pk,image=back_btn, borderwidth=0, 
                cursor="hand2", bd=0, font=("arial, 16"), 
                background="white",activebackground='#ffffff',
                command=lambda:balikpj()
                ).place(x=10,y=10,)  

        heading=Label(s_pk,text='Pilih Kursi Anda', font=('arial', 15, 'bold'), background="white")
        heading.place(x=50,y=50)

        kotak=PhotoImage(file='images\\kotak3.png')
        Label(s_pk,image=kotak,background="white").place(x=530,y=50)

        image2 = Image.open((dfdf['poster'].iloc[pilihanfilm]))
        resize_image2 = image2.resize((182,254)) 
        img2 = ImageTk.PhotoImage(resize_image2)
        poster=Label(s_pk,image=img2)
        poster.image=(dfdf['poster'].iloc[pilihanfilm])
        poster.place(x=50,y=100)

        genre=Label(s_pk,text='Genre', font=('arial', 8), background="white")
        genre.place(x=250,y=100)

        genre2=Label(s_pk,text=(dfdf['genre'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
        genre2.place(x=250,y=115)

        durasi=Label(s_pk,text='Durasi', font=('arial', 8), background="white")
        durasi.place(x=250,y=150)

        durasi2=Label(s_pk,text=(dfdf['durasi'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
        durasi2.place(x=250,y=165)

        sut=Label(s_pk,text='Sutradara', font=('arial', 8), background="white")
        sut.place(x=250,y=200)

        sut2=Label(s_pk,text=(dfdf['sutradara'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
        sut2.place(x=250,y=215)

        rat=Label(s_pk,text='Rating', font=('arial', 8), background="white")
        rat.place(x=250,y=250)

        rat2=Label(s_pk,text=(dfdf['rating'].iloc[pilihanfilm]), font=('arial', 8, 'bold'), background="white")
        rat2.place(x=250,y=265)

        judul=Label(s_pk,text=dfdf['judul'].iloc[pilihanfilm], font=('arial', 16, 'bold'), background="white")
        judul.place(x=50,y=367)

        sinop=Label(s_pk,text='Sinopsis', font=('arial', 8), background="white")
        sinop.place(x=50,y=405)

        sinop2=Label(s_pk,font=('yu gothic ui', 9, 'bold'),text=dfdf['sinopsis'].iloc[pilihanfilm],
                            wraplength=400,justify="left",bg='white')
        sinop2.place(x=50,y=425)

        Beli_button=PhotoImage(file="images\\Button2.png")
        beli=Button(s_pk,image=Beli_button, borderwidth=0, 
                    cursor="hand2", bd=0, font=("arial, 16"), 
                    command =lambda:[ds_rp()],background="white")
        beli.place(x=670,y=440)

        def cariindekskursi():
            global indekskursi
            datakursi2 = pd.read_csv('databases\\datakursi2.csv')
            carkur3 = pd.DataFrame(datakursi2)
            carkur2 = carkur3[carkur3['judul']==dfdf['judul'].iloc[pilihanfilm]]
            carkur = carkur2[carkur2['tanggal']==picktanggal[0]]
            indekskursi = carkur[carkur['jam']==pickjam[0]].index.item()

        def makebutton(avaibility,seatno,col,row):

            bariskursi=['A','B','C',"D","E","F","G"]
            seat_code=int(seatno-6)
            lgn_button = Image.open('images\\Button.png')
            photo = ImageTk.PhotoImage(lgn_button)

            lgn_button_label = Label(s_pk, bg='white')
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
            kursifilm = pd.read_csv('databases\\datakursi2.csv')
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

        def store_picked_seatno(seat_code):
            pickedseat.append(seat_code)
            availableseat()
            row = ((seat_code-1)//8)
            column = ((seat_code)-(7*row))-row
            bariskursi=['A','B','C',"D","E","F","G"]
            pickedseat_code.append('%s%d' %(bariskursi[row],column))
            seatframe=Label(s_pk,width=100,expand=None,borderwidth=0)
            seatframe.place(x=570,y=385)
            seat=Label(seatframe,text=pickedseat_code,wraplength=100,width=15,borderwidth=0, font=('arial', 11, 'bold'), background="white",justify=CENTER)
            seat.pack()
            hargaframe=Label(s_pk,width=100,expand=None,borderwidth=0)
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
            seatframe=Label(s_pk,width=100,expand=None,borderwidth=0)
            seatframe.place(x=570,y=385)
            seat=Label(seatframe,text=pickedseat_code,wraplength=100,width=15,borderwidth=0, font=('arial', 11, 'bold'), background="white",justify=CENTER)
            seat.pack()
            hargaframe=Label(s_pk,width=100,expand=None,borderwidth=0)
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
        s_pk.mainloop()
    else:
        messagebox.showinfo( "Ingpo", "Mohon pilih jadwal anda",parent=s_pj)

def ds_rp():
    if len(pickedseat)!= 0:
        global s_rp
        s_pk.destroy()
        s_rp= Toplevel()
        s_rp.title('ringkasan pembayaran')
        s_rp.config(background="white")
        s_rp.geometry('1000x600')
        s_rp.resizable(False,False)

        heading2=Label(s_rp,text='Konfirmasi Pembayaran', font=('arial', 15, 'bold'), background="white")
        heading2.place(x=50,y=50)

        back_btn=PhotoImage(file="images\\Buttonback.png")
        Button(s_rp,image=back_btn, borderwidth=0, 
                cursor="hand2", bd=0, font=("arial, 16"), 
                background="white",activebackground='#ffffff',
                command=lambda:balikpk()
                ).place(x=10,y=10,)  


        kotak2=PhotoImage(file='images\\kotak.png')
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

        bates2=Label(s_rp,text='____________________', background="white")
        bates2.place(x=600,y=250)

        tb2=Label(s_rp,text='Total Bayar', font=('arial', 9, 'bold'), background="white")
        tb2.place(x=600,y=280)

        tb2=Label(s_rp,text=('Rp%d'%((len(pickedseat)*45000)+4000)), font=('arial', 9, 'bold'), background="white")
        tb2.place(x=800,y=280)

        bates2=Label(s_rp,text='____________________', background="white")
        bates2.place(x=600,y=310)

        sk2=Label(s_rp,text='* Pembelian tidak bisa dibatalkan', font=('arial', 7), background="white", fg='#f00')
        sk2.place(x=600,y=340)
        global pickseat
        def pickseat():
            for i in range (len(pickedseat)):
                pickedseat.append("0")
                datakursi = pd.read_csv('databases\\datakursi2.csv', index_col='kode')
                dfdk = pd.DataFrame(datakursi)
                kursipilihan = str(pickedseat[i])
                dfdk.loc[indekskursi, kursipilihan] = 0
                dfdk.to_csv("databases\\datakursi2.csv")
                print(pickedseat[i])
            pickedseat.clear()
        Beli_button2=PhotoImage(file="images\\Button.png")
        beli2=Button(s_rp,image=Beli_button2, borderwidth=0, cursor="hand2", bd=0, font=("arial, 16"), background="white",command=lambda:[pickseat(),ds_kb()])
        beli2.place(x=680,y=400)

        s_rp.mainloop()
    else:

        messagebox.showinfo( "Ingpo", "Mohon pilih kursi anda",parent=s_pk,)


def balikpk():
    s_rp.destroy()
    ds_pk()

def ds_kb():
    
    global s_kb
    s_rp.destroy()
    s_kb = Toplevel()
    s_kb.title('Pemilihan Jadwal')
    s_kb.config(background="white")
    s_kb.geometry('1000x600')
    s_kb.resizable(False,False)

    def printt():
        class PDF(FPDF):
            def header(self):
                # Logo
                self.image('images\\background2.jpeg', 60, 40, 80)
                self.image(dfdf['poster'].iloc[pilihanfilm], 135, 28, 45)
                #font
                self.set_font('helvetica', 'B', 20)
                # Arial bold 15
                self.set_font('helvetica', 'B', 20)
                # Title
                self.cell(0, 0, '_____________________________', border=False, ln=1, align ='C')
                self.cell(0, 0, 'THE CINEMAKMUR PREMIERE', border=False, ln=1, align ='C')
                # Line break
                self.ln(0)

        pdf = PDF('P','mm', (200, 110))
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.cell(5, 20, ' ', 0, 1)
        pdf.set_font('Arial', 'bu', 14)
        pdf.cell(103, 7, dfdf['judul'].iloc[pilihanfilm], border=False, ln=1)
        pdf.set_font('Arial', 'b', 10)
        pdf.cell(5, 5, ' ', 0, 1)
        pdf.cell(5, 7, 'Date    : %s Juli 2022'%picktanggal[0], 0, 1)
        pdf.cell(5, 7, 'Time    : %d:00'%pickjam[0], 0, 1)
        pdf.cell(5, 7, 'Seat    : %s'%pickedseat_code, 0, 1)
        pdf.cell(5, 7, 'Price   : %s' %('Rp%d'%((len(pickedseat_code)*45000)+4000)), 0, 1)
        pdf.cell(5, 7, ' ', 0, 1)
        pdf.set_font('Arial', 'b', 12)
        pdf.cell(70, 10, 'KODE BOOKING : %s'%id, 1, 1, 'C')
        pdf.output('Tiket\\Tiket %s.pdf'%id, 'F')
        
        webbrowser.open(r'Tiket\\Tiket %s.pdf'%id)

    kotak=PhotoImage(file='images\\screen book.png')
    Label(s_kb,image=kotak,background="white").place(x=0,y=0)

    exit_button2=PhotoImage(file="images\\exit button.png")
    print_button2=PhotoImage(file="images\\print button 2.png")
    hs_button2=PhotoImage(file="images\\home button.png")      
    exittt=Button(s_kb,image=exit_button2, borderwidth=0, cursor="hand2", 
    bd=0, font=("arial, 16"), background="white",command=exit)
    exittt.place(x=330,y=430)
    printtt=Button(s_kb,image=print_button2, borderwidth=0, cursor="hand2", 
    bd=0, font=("arial, 16"), background="#141945",command=printt,activebackground="#141945")
    printtt.place(x=650,y=323)
    hs=Button(s_kb,image=hs_button2, borderwidth=0, cursor="hand2", 
    bd=0, font=("arial, 16"), background="white",command=balikhs)
    hs.place(x=500,y=430)


    pembayaran()
    print(id)
    kode_booking=Label(s_kb,text=id, font=('arial', 25), background="#141945",fg="white")
    kode_booking.place(x=385,y=320)
    rekapbeli()

    s_kb.mainloop()    

def balikrp():
    s_kb.destroy()
    ds_rp()

def balikhs():
    s_kb.destroy()
    ds_pf()


mainloop()
