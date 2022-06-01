from tkinter import *
from tkinter import ttk
import datetime
import random, string
import pandas as pd
from PIL import ImageTk, Image
from tkinter.font import Font

root = Tk()
text = Text(root)
myFont = Font(family="Open Sans", size=12, weight="bold")
time_now = datetime.datetime.now()
time_nextmonth  = datetime.datetime(time_now.year, time_now.month+1, time_now.day-1)


# TICKET ORDER SECTION
def login():
    userData = pd.read_csv('userdatabase.csv')
    df = pd.DataFrame(userData)
    

    global user
    global pasw
    global nomor
    user=e1.get()
    pasw=e2.get()
 
    matching_creds = (len(df[(df.username == user) & (df.password == pasw)]) > 0)

    if matching_creds:
        print('success')
        session = 1
        clearscreen("first")
        pilihfilmscreen()
        nomor = df.df['nomor'==user]
        return session, user
    else:
        print('\nYour account is not registered yet!')
        print('please contact admin')
        session = 0
        return session
def register():
    userData = pd.read_csv('userdatabase.csv')
    df = pd.DataFrame(userData)

    global user
    global pasw
    user=e1.get()
    pasw=e2.get()
    namalengkap=e3.get()
    nomor=e4.get()

    matching_creds = (len(df[(df.username == user) ]) < 1 or len(df[(df.nomor == nomor) ]) < 1)

    if matching_creds and user != "":
        print('success')
        newuser = {'username' : [user],
                   'password' : [pasw],
                   'namalengkap' : [namalengkap],
                   'nomor' : [nomor]}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('userdatabase.csv', mode='a', index=False, header=False)
        clearscreen("first")
        pilihfilmscreen()
    else:
        print('Username or number already exist')
def indeksfilm(x):
  daftarfilm = pd.read_csv('film.csv')
  df = pd.DataFrame(daftarfilm)
  
  pilihanfilm = x
  
  matching_creds = (len(df[(df.judul == pilihanfilm)]) > 0)

  if matching_creds:
    indekss = df[df['judul']==pilihanfilm].index.item()
    return indekss
  else:
    print()
def pilihfilem(judulfilmmm):
  global filem,indeksu
  filem = judulfilmmm
  print (indeksfilm(filem))
  indeksu = (indeksfilm(filem))
  movieinfo()
  clearscreen("pickfilm")
  moviedetailscreen()
  #cariindekskursi()
  #pickseat()
  #pembayaran()
  #rekapbeli()
  #return indeksu,filem
def movieinfo():
  global fullinfo,judul,harga,durasi
  daftarfilm = pd.read_csv('film.csv')
  df = pd.DataFrame(daftarfilm)
  
  judul= (df['judul'].iloc[indeksu])
  harga = (df['harga'].iloc[indeksu])
  durasi = (df['durasi'].iloc[indeksu])
  
  fullinfo = '''
  Judul film \t\t : {0}
  Harga Tiket \t\t : {1}
  Durasi film\t\t : {2}
  '''
  print(fullinfo.format(judul,harga,durasi))
def cariindekskursi():
  global indekskursi, pilihanjam,pilihantanggal
  pilihantanggal = int(input('pilih tanggal = '))
  pilihanjam = int(input('pilihjam = '))
  datakursi2 = pd.read_csv('datakursi2.csv')
  carkur3 = pd.DataFrame(datakursi2)
  carkur2 = carkur3[carkur3['judul']==filem]
  carkur = carkur2[carkur2['tanggal']==pilihantanggal]
  indekskursi = carkur[carkur['jam']==pilihanjam].index.item()
  return indekskursi,pilihanjam,pilihantanggal
def availableseat():
    kursifilm = pd.read_csv('datakursi2.csv')
    dfkf = pd.DataFrame(kursifilm)
    locfilm = dfkf.loc[indekskursi]
    daftarkursi = locfilm.tolist()
    print()
    for a in range (7,len(daftarkursi)):
        if daftarkursi[a] == 1:
            print('%d Available'%(a-6))
        else:
            print('%d Booked' %(a-6))
    print()
def pickseat():
  availableseat()
  datakursi = pd.read_csv('datakursi2.csv', index_col='kode')
  dfdk = pd.DataFrame(datakursi)
  kursipilihan = input('pilih kursi anda = ')
  dfdk.loc[indekskursi, kursipilihan] = 0
  dfdk.to_csv("datakursi2.csv")
  return kursipilihan
  print()
def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))
def pembayaran():
  datapembelian = pd.read_csv('datapembelian.csv')
  dfdp = pd.DataFrame(datapembelian)
  while True:
    id_generator()
    if (len(dfdp.loc[dfdp['kodebayar'] == id_generator])) < 1:
        global id
        id = id_generator()
        print(id)
        break
        
  return id
def rekapbeli():
    global nomor
    datapembelian = pd.read_csv('datapembelian.csv')
    dfdt = pd.DataFrame(datapembelian)
    ambildatauser = pd.read_csv('userdatabase.csv',index_col = 'username')
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
                'nomor' : [nomor],
                'judul' : [filem],
                'waktu' : [pilihanjam],
                'tanggal' : [pilihantanggal],
                'kodebayar' : [id],
                }
    inputdatapembelian = pd.DataFrame(databelibaru)
    inputdatapembelian.to_csv('datapembelian.csv', mode='a', index=False, header=False)

    print('')

# TKINTER SECTION
def clearscreen(screen):
  if screen=="first":
    e1.grid_forget()
    e2.grid_forget()
    e3.grid_forget()
    e4.grid_forget()
    mylabel1.grid_forget()
    mylabel2.grid_forget()
    mylabel3.grid_forget()
    mylabel4.grid_forget()
    mybutton1.grid_forget()
    mybutton2.grid_forget()
  elif screen == "pickfilm":
    wrapper1.pack_forget()
    wrapper2.pack_forget()
def logininstead():
    mybutton1.config(text='Login',
                    command = login)
    mybutton2.config(text='Register instead',
                    command=registerinstead)
    e3.grid_forget()
    e4.grid_forget()
    mylabel3.grid_forget()
    mylabel4.grid_forget()
def registerinstead():
    mybutton1.config(text='Register',
                    command = register)
    mybutton2.config(text='Login instead',
                    command=logininstead)
    mylabel3.grid(row=2,column=0)
    mylabel4.grid(row=3,column=0)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)
def firstscreen():
  global e1,e2,e3,e4,e4,mylabel1,mylabel2,mylabel3,mylabel4,mybutton1,mybutton2
  e1=Entry(root)
  e1.grid(row=0,column=1)
  e2=Entry(root)
  e2.grid(row=1,column=1)
  e3=Entry(root)
  e3.grid(row=2,column=1)
  e4=Entry(root)
  e4.grid(row=3,column=1)

  mylabel1 = Label(root, text='Username')
  mylabel1.grid(row=0,column=0)
  mylabel2 = Label(root, text='Password')
  mylabel2.grid(row=1,column=0)
  mylabel3 = Label(root, text='Nama')
  mylabel3.grid(row=2,column=0)
  mylabel4 = Label(root, text='Nomor Hp')
  mylabel4.grid(row=3,column=0)

  mybutton1 = Button(root, 
                  text='Register',
                  borderwidth=0,
                  command=register,
                  bg = '#296d98',
                  fg = 'white'  )
  mybutton1.grid(row=4,column=1)

  mybutton2 = Button(root,
                  text='Login instead',
                  borderwidth = 0,
                  command = logininstead)
  mybutton2.grid(row=5,column=1)
def pilihfilmscreen():
    global wrapper1,wrapper2
    wrapper1 = LabelFrame(root,borderwidth = 2)
    wrapper2 = LabelFrame(root,borderwidth = 2)
    mycanvas = Canvas(wrapper2)
    mycanvas.pack(side=LEFT, fill="both",expand="y")

    yscrollbar = ttk.Scrollbar(wrapper2, orient="vertical", command=mycanvas.yview)
    yscrollbar.pack(side=RIGHT, fill="y")

    mycanvas.configure(yscrollcommand=yscrollbar.set)

    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    myframe = Frame(mycanvas)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")

    wrapper1.pack(fill="x", padx=10, pady=10)
    wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

    datafilem = pd.read_csv('film.csv')
    dfdf = pd.DataFrame(datafilem)
    locfilm = dfdf['judul'].tolist()
    for i in range (len(locfilm)):

        image = Image.open((dfdf['poster'].iloc[i]))
        
        resize_image = image.resize((140,196))
        
        img = ImageTk.PhotoImage(resize_image)
        
        btnfilm = Button(myframe,image=img, 
                        command=lambda i=i: pilihfilem(str(dfdf['judul'].iloc[i])),
                        borderwidth = 0)
        btnfilm.image = img
        btnfilm.grid(column=0,row=0+i)
        wrapper3 = LabelFrame(myframe,borderwidth = 0)
        mylabel1 = Label(wrapper3,text=dfdf['judul'].iloc[i],font = myFont)
        mylabel1.grid(column=0,row=1)
        mylabel2 = Label(wrapper3,text="%.250s" %dfdf['sinopsis'].iloc[i]+str(" ..."),font = myFont.configure(size=14),wraplength=200,justify="left")
        mylabel2.grid(column=0,row=2)
        btn_order = Button(wrapper3,
                          command=lambda i=i: pilihfilem(str(dfdf['judul'].iloc[i])),
                          text = "Order Ticket")
        btn_order.grid(column=0,row=3)
        wrapper3.grid(column=1,row=0+i)
    mylabel3 = Label(wrapper1,text="Pesan Tiket Onlen",font = myFont)
    mylabel3.pack()
def moviedetailscreen():
    global wrapper1,wrapper2,wrapper3,wrapper4,wrapper5,wrapper6,wrapper7
    datafilem = pd.read_csv('film.csv')
    dfdf = pd.DataFrame(datafilem)
    wrapper1 = LabelFrame(root,borderwidth = 2,height = 140)
    #wrapper2 = LabelFrame(root,borderwidth = 2,height = 60)
    wrapper3 = LabelFrame(root,borderwidth = 2,height = 50)
    wrapper4 = LabelFrame(root,borderwidth = 2,height = 75)
    wrapper5 = LabelFrame(root,borderwidth = 2,height = 360)
    wrapper6 = LabelFrame(root,borderwidth = 2,height = 40)
    wrapper7 = LabelFrame(wrapper1,borderwidth = 0)

    #==== wrapper 1 ===
    wrapper1.pack(fill='x',expand=None, padx=10, pady=2)
    wrapper1.pack_propagate(0)
    wrapper7.grid(column=1,row=0)

    Label(wrapper7,text=(dfdf['judul'].iloc[indeksu]), font=myFont).grid(column=0,row=0,sticky="NW")
    Label(wrapper7,text='Genre \t\t: %s'%(dfdf['genre'].iloc[indeksu]), font=myFont.configure(size=14)).grid(column=0,row=1,sticky="W")
    Label(wrapper7,text='Durasi \t\t: %s' %(dfdf['durasi'].iloc[indeksu]), font=myFont.configure(size=14)).grid(column=0,row=2,sticky="W")
    Label(wrapper7,text='Sutradara \t: %s'%(dfdf['sutradara'].iloc[indeksu]), font=myFont.configure(size=14)).grid(column=0,row=3,sticky="W")
    Label(wrapper7,text='Rating \t\t: %s'%(dfdf['rating'].iloc[indeksu]), font=myFont.configure(size=14)).grid(column=0,row=4,sticky="W")

    image = Image.open((dfdf['poster'].iloc[indeksu]))
    resize_image = image.resize((100,140))
    img = ImageTk.PhotoImage(resize_image)
    poster=Label(wrapper1,image=img)
    poster.image = img
    poster.grid(column=0,row=0,sticky = "NW")

    #==== wrapper 2 ====
    #wrapper2.pack(fill='x',expand=None,padx=10,pady=2)
    #wrapper2.pack_propagate(0)

    #==== wrapper 3 ====
    wrapper3.pack(fill='x',expand=None,padx=10,pady=2)
    wrapper3.pack_propagate(0)
    frame3=Frame(wrapper3,width=500)
    frame3.grid(row=0, column=0, sticky="NW")
    synopsis_btn=Button(frame3,text="Sinopsis",width=25,borderwidth=0)
    synopsis_btn.grid(column=0,row=0,padx=25)
    order_btn=Button(frame3,text="Jadwal",width=25,borderwidth=0)
    order_btn.grid(column=1,row=0,padx=25)

    #==== wrapper 4 ====
    delta = time_nextmonth-time_now
    wrapper4.pack()
    h_s = Scrollbar(wrapper4,orient='horizontal')
    h_s.pack(side=BOTTOM,fill=X)
    h_s.config(command = myframe2.xview)

    myframe2 = Frame(wrapper4, width = 25, height = 15,
                xscrollcommand = h_s.set)
    myframe2.pack()
    
    for i in range (20):
        Button(myframe2,text=i).pack()

    

   
    
    

    #==== wrapper 5 ====
    wrapper5.pack(fill='x',expand=None,padx=10,pady=2)
    wrapper5.pack_propagate(0)

    #==== wrapper 6 ====
    wrapper6.pack(fill='x',expand=None,padx=10,pady=2)
    wrapper6.pack_propagate(0)



pilihfilmscreen()
root.geometry("500x700")

root.mainloop()