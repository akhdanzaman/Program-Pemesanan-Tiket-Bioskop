from tkinter import *

root = Tk()
root.title('ringkasan pembayaran')
root.config(background="white")
root.geometry('1000x600')
root.resizable(False,False)

heading=Label(root,text='Konfirmasi Pembayaran', font=('arial', 15, 'bold'), background="white")
heading.place(x=50,y=50)

kotak=PhotoImage(file='C:\\Bioskop\\kotak.png')
Label(root,image=kotak,background="white").place(x=570,y=50)

poster=PhotoImage(file='C:\\Bioskop\\wi.png')
Label(root,image=poster).place(x=50,y=100)

jdwl=Label(root,text='Detail Jadwal', font=('arial', 11, 'bold'), background="white")
jdwl.place(x=250,y=120)

jdl=Label(root,text='Judul Film', font=('arial', 10), background="white")
jdl.place(x=250,y=170)

film=Label(root,text='SPIDERMAN NO WAY HOME', font=('arial', 10, 'bold'), background="white")
film.place(x=250,y=200)

tgl=Label(root,text='Tanggal', font=('arial', 10), background="white")
tgl.place(x=250,y=230)

tbt=Label(root,text='SELASA, 17 AGUSTUS 2021', font=('arial', 10, 'bold'), background="white")
tbt.place(x=250,y=260)

kls=Label(root,text='Kelas', font=('arial', 10), background="white")
kls.place(x=50,y=340)

film=Label(root,text='GOLD CLASS 2D', font=('arial', 10, 'bold'), background="white")
film.place(x=50,y=370)

tic=Label(root,text='Tiket', font=('arial', 10), background="white")
tic.place(x=50,y=410)

seat=Label(root,text='C8, C9, C10', font=('arial', 10, 'bold'), background="white")
seat.place(x=50,y=440)

jam=Label(root,text='Jam', font=('arial', 10), background="white")
jam.place(x=200,y=340)

pkl=Label(root,text='14:40', font=('arial', 10, 'bold'), background="white")
pkl.place(x=200,y=370)

ro=Label(root,text='Ringkasan Order', font=('arial', 11, 'bold'), background="white")
ro.place(x=600,y=120)

dt=Label(root,text='Detail Transaksi', font=('arial', 9, 'bold'), background="white")
dt.place(x=600,y=160)

rs=Label(root,text='REGULAR SEAT', font=('arial', 9), background="white")
rs.place(x=600,y=190)

by=Label(root,text='BIAYA LAYANAN', font=('arial', 9), background="white")
by.place(x=600,y=220)

bates=Label(root,text='__________________________________________________________', background="white")
bates.place(x=600,y=250)

tb=Label(root,text='Total Bayar', font=('arial', 9, 'bold'), background="white")
tb.place(x=600,y=280)

bates=Label(root,text='__________________________________________________________', background="white")
bates.place(x=600,y=310)

sk=Label(root,text='* Pembelian tidak bisa dibatalkan', font=('arial', 7), background="white", fg='#f00')
sk.place(x=600,y=340)

Beli_button=PhotoImage(file="C:\\Bioskop\\Button.png")
beli=Button(image=Beli_button, borderwidth=0, cursor="hand2", bd=0, font=("arial, 16"), background="white")
beli.place(x=680,y=400)

root.mainloop()