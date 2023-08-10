from kivy.lang import Builder
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy.uix.screenmanager import ScreenManager,Screen 
from kivy.properties import StringProperty, NumericProperty  
from kivy.uix.popup import Popup
from kivy.factory import Factory
#from kivy.uix.scatter import Scatter
#from kivy.uix.camera import Camera

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineAvatarListItem,TwoLineListItem,OneLineListItem
from kivymd.uix.pickers import MDDatePicker

from fungsi import *

Builder.load_file('myfactory.kv')
Builder.load_file('login.kv')
Builder.load_file('menu.kv')
Builder.load_file('mohon_baru.kv')
Builder.load_file('mohon_simp.kv')
Builder.load_file('mohon_simp_ubah.kv')
Builder.load_file('mohon_pinjaman.kv')
Builder.load_file('mohon_pinjaman_lunas.kv')
Builder.load_file('mohon_pinjaman_tenor.kv')

#Window.size = (600,900)
#Window.size = (400,600)

class Popup_List_One(Popup): 
    namatabel = StringProperty ("")
    namaclass = StringProperty ("")    

    def on_pre_open(self):
        self.set_list_view("", False)
    
    def set_list_view(self, textcari, search):  
        def add_list_item(key1,text1):
            self.ids.DaftarList.data.append(
                {   "viewclass": "OneLineListItem",
                    "text": text1,
                    "font_style": 'Subtitle2',
                    "secondary_font_style": 'Caption',
                    "tertiary_font_style": 'Caption',
                    "on_press": lambda xx=key1: self.hasil_itemclik(xx)
                }
            )
        
        if self.namatabel.strip()=='produk' and self.namaclass.strip()=='Mohon_Simp_Page':
            datatbl = ['Simpanan Ummah','Simpanan Haji','Simpanan Hari Raya','Simpanan Pendidikan','Simpanan Sukarela','Simpanan Berjangka']

        if self.namatabel.strip()=='produk' and self.namaclass.strip()=='Mohon_Pinjaman_Page':
            datatbl = ['Pembiayaan Murobahah','Pembiayaan Mudhorobah','Pembiayaan Al-Qord','Pembiayaan Jk.Pendek','Pembiayaan Jk.Panjang']

        if self.namatabel.strip()=='waktu' and self.namaclass.strip()=='Mohon_Simp_Page':
            datatbl = ['1 Bulan','3 Bulan','6 Bulan','12 Bulan']     

        if self.namatabel.strip()=='norek' and self.namaclass.strip()=='Mohon_Simp_Ubah_Page':
            datatbl = ['1034 Simpanan Sukarela','2056 Simpanan Ummah','5001 Simpanan Berjangka']
        
        if self.namatabel.strip()=='norek' and self.namaclass.strip()=='Mohon_Pinjaman_Lunas_Page':
            datatbl = ['3010 Pembiayaan Mudhorobah']   

        if self.namatabel.strip()=='norek' and self.namaclass.strip()=='Mohon_Pinjaman_Tenor_Page':
            datatbl = ['3010 Pembiayaan Mudhorobah']   
             
        self.ids.DaftarList.data = []
        for record in datatbl:
            xkey1 = record.strip()
            xtext1= record.strip()
            add_list_item(xkey1, xtext1)

    def hasil_itemclik(self,value1):            
        if self.namaclass.strip()=='Mohon_Simp_Page':
            Mohon_Simp_Page.hasilcaripopup1 = value1    

        if self.namaclass.strip()=='Mohon_Pinjaman_Page':
            Mohon_Pinjaman_Page.hasilcaripopup1 = value1       
        
        if self.namaclass.strip()=='Mohon_Simp_Ubah_Page':
            Mohon_Simp_Ubah_Page.hasilcaripopup1 = value1 

        if self.namaclass.strip()=='Mohon_Pinjaman_Lunas_Page':
            Mohon_Pinjaman_Lunas_Page.hasilcaripopup1 = value1 

        if self.namaclass.strip()=='Mohon_Pinjaman_Tenor_Page':
            Mohon_Pinjaman_Tenor_Page.hasilcaripopup1 = value1             

        self.dismiss()                

class Login_Page(Screen):
    def masukprogram(self):
        user = self.ids.userid.text.strip()    
        pswd = self.ids.pswdid.text.strip()  

        if user=='demo' and pswd=='demo':
            self.ids.userid.text = ''
            self.ids.pswdid.text = ''
            self.manager.transition.direction= 'left'
            self.manager.current = 'Menu_Page' 
        else:
            tombol_canc = MDFlatButton(text="OK", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Gagal..",
                text='Maaf user id belum tardaftar atau pasword salah ',
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

    def dialog_canc(self,obj):
        self.dialog.dismiss()   
        
class Menu_Page(Screen):
    def laporan(self):        
        tombol_canc = MDFlatButton(text="OK", on_release=self.dialog_canc)
        self.dialog = MDDialog(title="Info",
            text='... Under Contruction ...',                 
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()
            
    def dialog_canc(self,obj):
        self.dialog.dismiss()
        pass

    def dialog_ok(self,obj):
        self.dialog.dismiss() 
        tombol_canc = MDFlatButton(text="OK", on_release=self.closing)
        self.dialog = MDDialog(
            text='TERIMA KASIH ... ',
            size_hint=(.5,.2),      
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()

class Mohon_Baru_Page(Screen):

    def on_pre_enter(self):
        syarat = 'Dengan ini pemohon menyatakan dan bersedia memenuhi kewajiban keanggotaan '\
            'yang disyaratkan sebagai berikut :\n'\
            'a. Membayar simpanan pokok sebesar : Rp. 200.000,- \n'\
            '   (dua ratus ribu rupiah) hanya 1 (satu) kali \n'\
            'b. Membayar simpanan wajib sebesar : Rp. 25.000,- \n'\
            '   (dua puluh lima ribu rupiah) setiap bulan \n'\
            'Demikian permohonan ini dibuat dan diisi dengan sebenarnya untuk dapat dipergunakan sebagaimana mestinya'
        self.ids.txtsyarat.text = syarat
        
    def date_lahir(self, value):
        text_tgl = tanggal_value(value)
        if text_tgl==None: date_dialog = MDDatePicker()
        else: date_dialog = MDDatePicker(year=text_tgl.year, month=text_tgl.month,day=text_tgl.day) 
        date_dialog.bind(on_save=self.get_date_lahir)
        date_dialog.open()
    
    def get_date_lahir(self, instance, value,date_range):
        text_date = tanggal_text(value)
        self.ids.tgl_lhr.text = text_date

    def add_gambar(self, value):
        pass 

    def simpan(self):
        tombol_ok = MDFlatButton(text="OK", on_release=self.dialog_ok)
        tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
        self.dialog = MDDialog(title="Konfirm..",
            text='Apakah anda yakin data yang diisikan sudah benar dan siap diupload ',                 
            radius=[20, 7, 20, 7],
            buttons=[tombol_ok,tombol_canc]) 
        self.dialog.open()
    
    def dialog_canc(self,obj):
        self.dialog.dismiss()
        pass

    def dialog_ok(self,obj):
        self.dialog.dismiss() 
        tombol_canc = MDFlatButton(text="OK", on_release=self.closing)
        self.dialog = MDDialog(
            text='TERIMA KASIH ... ',
            size_hint=(.5,.2),      
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()

    def closing(self,obj):
        self.dialog.dismiss()
        self.manager.transition.direction= 'left'
        self.manager.current = 'Login_Page' 

class Mohon_Simp_Page(Screen):     
    hasilcaripopup1 = StringProperty('')  
    hasilcaripopup1 = " "

    def on_pre_enter(self):
        syarat = 'Catatan:\nBila tidak potong gaji maka pembayaran/setoran melalui '\
            'transfer ke rekening BCA sentra xxxx nomor: 01010101'
        self.ids.tranfer.text = syarat    

    def add_gambar(self, value):
        pass 

    def cari_produk(self):        
        popup2 = Popup_List_One()    
        popup2.namatabel = "produk" 
        popup2.namaclass = "Mohon_Simp_Page"
        popup2.bind(on_dismiss=self.cari_produk_ok)
        popup2.open()   

    def cari_produk_ok(self, obj):        
        if Mohon_Simp_Page.hasilcaripopup1.strip()!='':
            self.ids.produk.text=Mohon_Simp_Page.hasilcaripopup1.strip()

        if Mohon_Simp_Page.hasilcaripopup1.strip()=='Simpanan Berjangka':
            self.ids.setoranlbl.text='Nilai Simpanan'
            self.ids.waktu.disabled = False
            self.ids.waktucmd.disabled = False
            self.ids.waktu.opacity = 1
            self.ids.waktucmd.opacity = 1
            self.ids.waktulbl.opacity = 1            
        else:
            self.ids.setoranlbl.text='Setoran/ Bulan'
            self.ids.waktu.text=''
            self.ids.waktu.disabled = True
            self.ids.waktucmd.disabled = True
            self.ids.waktu.opacity = 0
            self.ids.waktucmd.opacity = 0           
            self.ids.waktulbl.opacity = 0     

    def cari_waktu(self):        
        popup2 = Popup_List_One()    
        popup2.namatabel = "waktu" 
        popup2.namaclass = "Mohon_Simp_Page"
        popup2.bind(on_dismiss=self.cari_waktu_ok)
        popup2.open()   

    def cari_waktu_ok(self, obj):        
        if Mohon_Simp_Page.hasilcaripopup1.strip()!='':
            self.ids.waktu.text=Mohon_Simp_Page.hasilcaripopup1.strip()

    def simpan(self):
        xproduk = self.ids.produk.text.strip()
        xwaktu = self.ids.waktu.text.strip()
        xsetoran = self.ids.setoran.text.strip()
        xlanjut = 1
        
        if xlanjut == 1 and xproduk=='':
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf produk simpanan harus dipilih...',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1 and xproduk=='Simpanan Berjangka':
            if xwaktu=='' or xsetoran==0 :
                xlanjut = 0
                tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
                self.dialog = MDDialog(title="Cek Lagi..",
                    text='Maaf nilai dan jangka waktu harus diisikan',                 
                    radius=[20, 7, 20, 7],
                    buttons=[tombol_canc]) 
                self.dialog.open()

        if xlanjut == 1: 
            tombol_ok = MDFlatButton(text="OK", on_release=self.dialog_ok)
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Konfirm..",
                text='Apakah anda yakin data yang diisikan sudah benar dan siap diupload ',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_ok,tombol_canc]) 
            self.dialog.open()
    
    def dialog_canc(self,obj):
        self.dialog.dismiss()
        pass

    def dialog_ok(self,obj):
        self.dialog.dismiss() 
        tombol_canc = MDFlatButton(text="OK", on_release=self.closing)
        self.dialog = MDDialog(
            text='TERIMA KASIH ... ',
            size_hint=(.5,.2),      
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()

    def closing(self,obj):
        self.dialog.dismiss()
        self.manager.transition.direction= 'left'
        self.manager.current = 'Menu_Page' 

class Mohon_Pinjaman_Page(Screen):
    hasilcaripopup1 = StringProperty('')  
    hasilcaripopup1 = " "

    def cari_produk(self):        
        popup2 = Popup_List_One()    
        popup2.namatabel = "produk" 
        popup2.namaclass = "Mohon_Pinjaman_Page"
        popup2.bind(on_dismiss=self.cari_produk_ok)
        popup2.open()   

    def cari_produk_ok(self, obj):        
        if Mohon_Pinjaman_Page.hasilcaripopup1.strip()!='':
            self.ids.produk.text=Mohon_Pinjaman_Page.hasilcaripopup1.strip()

    def add_gambar(self, value):
        pass 

    def simpan(self):
        xproduk = self.ids.produk.text.strip()
        xwaktu = self.ids.waktu.text.strip()
        xnilai = self.ids.nilai.text.strip()
        xlanjut = 1
        
        if xlanjut == 1 and xproduk=='':
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf produk pinjaman harus dipilih...',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1 and (xwaktu=='' or xnilai==0) :
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi..",
                text='Maaf nilai pinjaman dan jangka waktu harus diisikan',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1: 
            tombol_ok = MDFlatButton(text="OK", on_release=self.dialog_ok)
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Konfirm..",
                text='Apakah anda yakin data yang diisikan sudah benar dan siap diupload serta, '\
                    'memberikan mandat kepada pengurus untuk dievaluasi dan nilai pengajuan akan dilihat dengan '\
                    'cashflow dari keseluruhan limit yang tersisa setiap periodenya.',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_ok,tombol_canc]) 
            self.dialog.open()
    
    def dialog_canc(self,obj):
        self.dialog.dismiss()
        pass

    def dialog_ok(self,obj):
        self.dialog.dismiss() 
        tombol_canc = MDFlatButton(text="OK", on_release=self.closing)
        self.dialog = MDDialog(
            text='TERIMA KASIH ... ',
            size_hint=(.5,.2),      
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()

    def closing(self,obj):
        self.dialog.dismiss()
        self.manager.transition.direction= 'left'
        self.manager.current = 'Menu_Page' 

class Mohon_Simp_Ubah_Page(Screen):
    hasilcaripopup1 = StringProperty('')  
    hasilcaripopup1 = " "

    def pilih_jenis(self, checkbox, value):
        if self.ids.jenis01.active==True:
            self.ids.lblubah01.text='Setoran Lama'
            self.ids.lblubah01.opacity= 1            
            self.ids.ubah01.disabled= True
            self.ids.ubah01.text='10000' if self.ids.norek.text.strip()=='1034' else ''
            self.ids.ubah01.opacity= 1            
            self.ids.txtubah01.opacity= 1

            self.ids.lblubah02.text=''
            self.ids.lblubah02.opacity= 0
            self.ids.ubah02.disabled= True
            self.ids.ubah02.opacity= 0
            self.ids.cmdubah02.disabled= True
            self.ids.cmdubah02.opacity= 0
            
            self.ids.setoran.disabled= False
            self.ids.setoran.opacity= 1
            self.ids.setoranlbl.opacity= 1
            self.ids.potong.disabled= False
            self.ids.potong.opacity= 1
            self.ids.potonglbl.opacity= 1

        if self.ids.jenis02.active==True:
            self.ids.lblubah01.text='Jml Penarikan'
            self.ids.lblubah01.opacity= 1
            self.ids.ubah01.disabled= False
            self.ids.ubah01.opacity= 1
            self.ids.ubah01.text=''
            self.ids.txtubah01.opacity= 1

            self.ids.lblubah02.text='Tgl'
            self.ids.lblubah02.opacity= 1
            self.ids.ubah02.disabled= True
            self.ids.ubah02.opacity= 1
            self.ids.cmdubah02.disabled= False
            self.ids.cmdubah02.opacity= 1
            
            self.ids.setoran.disabled= True
            self.ids.setoran.opacity= 0
            self.ids.setoranlbl.opacity= 0
            self.ids.potong.disabled= True
            self.ids.potong.opacity= 0
            self.ids.potonglbl.opacity= 0

        if self.ids.jenis03.active==True:
            self.ids.lblubah01.text=''
            self.ids.lblubah01.opacity= 0
            self.ids.ubah01.disabled= True
            self.ids.ubah01.opacity= 0
            self.ids.ubah01.text=''
            self.ids.txtubah01.opacity= 1

            self.ids.lblubah02.text='Tgl'
            self.ids.lblubah02.opacity= 1
            self.ids.ubah02.disabled= True
            self.ids.ubah02.opacity= 1
            self.ids.cmdubah02.disabled= False
            self.ids.cmdubah02.opacity= 1
            
            self.ids.setoran.disabled= True
            self.ids.setoran.opacity= 0
            self.ids.setoranlbl.opacity= 0
            self.ids.potong.disabled= True
            self.ids.potong.opacity= 0
            self.ids.potonglbl.opacity= 0

    def cari_norek(self):        
        popup2 = Popup_List_One()    
        popup2.namatabel = "norek" 
        popup2.namaclass = "Mohon_Simp_Ubah_Page"
        popup2.bind(on_dismiss=self.cari_norek_ok)
        popup2.open()   

    def cari_norek_ok(self, obj):        
        if Mohon_Simp_Ubah_Page.hasilcaripopup1.strip()!='':
            noreknya = Mohon_Simp_Ubah_Page.hasilcaripopup1.strip()
            self.ids.norek.text= noreknya[0:5]
            self.ids.noreknm.text= noreknya[5:30]            
            if noreknya[0:4]=='1034': 
                self.ids.atasnama.text='Wibowo Demo Saja'
                self.ids.saldo.text= '750,000'
                self.ids.saldonilai.text= '750000'
                self.ids.ubah01.text='10000' if self.ids.jenis01.active==True else ''
            if noreknya[0:4]=='2056': 
                self.ids.atasnama.text='Wibowo Demo Saja'
                self.ids.saldo.text= '14,575,250'
                self.ids.saldonilai.text= '14575250'
                self.ids.ubah01.text=''
            if noreknya[0:4]=='5001': 
                self.ids.atasnama.text= 'Siti Fatiham Anjani' 
                self.ids.saldo.text= '25,000,000'
                self.ids.saldonilai.text= '25000000'
                self.ids.ubah01.text=''

    def date_ubah02(self, value):
        text_tgl = tanggal_value(value)
        if text_tgl==None: date_dialog = MDDatePicker()
        else: date_dialog = MDDatePicker(year=text_tgl.year, month=text_tgl.month,day=text_tgl.day) 
        date_dialog.bind(on_save=self.get_date_ubah02)
        date_dialog.open()
    
    def get_date_ubah02(self, instance, value,date_range):
        text_date = tanggal_text(value)
        self.ids.ubah02.text = text_date

    def simpan(self):        
        xxjenis = 0
        xxjenis = 1 if self.ids.jenis01.active==True else xxjenis
        xxjenis = 2 if self.ids.jenis02.active==True else xxjenis
        xxjenis = 3 if self.ids.jenis03.active==True else xxjenis
        xxnorek = self.ids.norek.text.strip()
        xxsaldo = int(self.ids.saldonilai.text) if self.ids.saldonilai.text.strip()!='' else 0
        xxtarik = int(self.ids.ubah01.text) if self.ids.ubah01.text.strip()!='' else 0
        xxsetoran= int(self.ids.setoran.text) if self.ids.setoran.text.strip()!='' else 0
        xxpotong= 1 if self.ids.potong.active==True else 0
        xxtgl = self.ids.ubah02.text.strip()
        xlanjut = 1
        
        if xlanjut == 1 and xxnorek=='':
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf no.rekening simpanan harus dipilih...',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1 and xxjenis==0:
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf jenis transaksi harus dipilih...',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1 and xxnorek=='5001' and xxjenis!=3: 
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf simpanan berjangka hanya bisa transaksi penutupan',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1 and xxjenis==1 and xxpotong==1 and xxsetoran==0:
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi..",
                text='Maaf nilai setoran potong gaji harus diisikan',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()
        
        if xlanjut == 1 and xxjenis==2 and xxtarik<5000000 :
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi..",
                text='Maaf nilai permohonan penarikan minimal 5 juta',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1 and xxjenis==2 and xxtarik>xxsaldo:
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi..",
                text='Maaf penarikan melebihi saldo rekening',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1 and xxjenis>=2 and xxtgl=='':
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi..",
                text='Maaf rencana tanggal transaksi harus diisikan',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1: 
            tombol_ok = MDFlatButton(text="OK", on_release=self.dialog_ok)
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Konfirm..",
                text='Apakah anda yakin data yang diisikan sudah benar dan siap diupload ',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_ok,tombol_canc]) 
            self.dialog.open()
    
    def dialog_canc(self,obj):
        self.dialog.dismiss()
        pass

    def dialog_ok(self,obj):
        self.dialog.dismiss() 
        tombol_canc = MDFlatButton(text="OK", on_release=self.closing)
        self.dialog = MDDialog(
            text='TERIMA KASIH ... ',
            size_hint=(.5,.2),      
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()

    def closing(self,obj):
        self.dialog.dismiss()
        self.manager.transition.direction= 'left'
        self.manager.current = 'Menu_Page' 

class Mohon_Pinjaman_Lunas_Page(Screen):
    hasilcaripopup1 = StringProperty('')  
    hasilcaripopup1 = " "

    def cari_norek(self):        
        popup2 = Popup_List_One()    
        popup2.namatabel = "norek" 
        popup2.namaclass = "Mohon_Pinjaman_Lunas_Page"
        popup2.bind(on_dismiss=self.cari_norek_ok)
        popup2.open()   

    def cari_norek_ok(self, obj):        
        if Mohon_Pinjaman_Lunas_Page.hasilcaripopup1.strip()!='':
            noreknya = Mohon_Pinjaman_Lunas_Page.hasilcaripopup1.strip()
            self.ids.norek.text= noreknya[0:5]
            self.ids.noreknm.text= noreknya[5:30]            
            self.ids.atasnama.text='Wibowo Demo Saja'
            self.ids.saldo.text= '8,765,350'

    def simpan(self):        
        xxnorek = self.ids.norek.text.strip()
        xlanjut = 1
        
        if xlanjut == 1 and xxnorek=='':
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf nomor pembiayaan harus dipilih...',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()
        
        if xlanjut == 1: 
            tombol_ok = MDFlatButton(text="OK", on_release=self.dialog_ok)
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Konfirm..",
                text='Apakah anda yakin data yang diisikan sudah benar dan siap diupload ',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_ok,tombol_canc]) 
            self.dialog.open()
    
    def dialog_canc(self,obj):
        self.dialog.dismiss()
        pass

    def dialog_ok(self,obj):
        self.dialog.dismiss() 
        tombol_canc = MDFlatButton(text="OK", on_release=self.closing)
        self.dialog = MDDialog(
            text='TERIMA KASIH ... ',
            size_hint=(.5,.2),      
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()

    def closing(self,obj):
        self.dialog.dismiss()
        self.manager.transition.direction= 'left'
        self.manager.current = 'Menu_Page' 

class Mohon_Pinjaman_Tenor_Page(Screen):
    hasilcaripopup1 = StringProperty('')  
    hasilcaripopup1 = " "

    def cari_norek(self):        
        popup2 = Popup_List_One()    
        popup2.namatabel = "norek" 
        popup2.namaclass = "Mohon_Pinjaman_Tenor_Page"
        popup2.bind(on_dismiss=self.cari_norek_ok)
        popup2.open()   

    def cari_norek_ok(self, obj):        
        if Mohon_Pinjaman_Tenor_Page.hasilcaripopup1.strip()!='':
            noreknya = Mohon_Pinjaman_Tenor_Page.hasilcaripopup1.strip()
            self.ids.norek.text= noreknya[0:5]
            self.ids.noreknm.text= noreknya[5:30]            
            self.ids.atasnama.text='Wibowo Demo Saja'
            self.ids.saldo.text= '8,765,350'
            self.ids.angsuran01.text= '876.535'
            self.ids.tenor01.text= '10 Bulan'

    def ubah_tenor(self, value):
        xsisa = 8765350
        xvalue= 0 if value.strip()=='' else int(value)
        xangs = 0 if xvalue==0 else int(xsisa/xvalue)
        self.ids.angsuran02.text=f"{int(xangs):,}"

    def simpan(self):        
        xxnorek = self.ids.norek.text.strip()
        xtenor = 0 if self.ids.tenor02.text.strip()=='' else int(self.ids.tenor02.text)
        xlanjut = 1
        
        if xlanjut == 1 and xxnorek=='':
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf nomor pembiayaan harus dipilih...',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()
        
        if xlanjut == 1 and xtenor==0:
            xlanjut = 0
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Cek Lagi",
                text='Maaf perubahan tenor harus diisikan...',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_canc]) 
            self.dialog.open()

        if xlanjut == 1: 
            tombol_ok = MDFlatButton(text="OK", on_release=self.dialog_ok)
            tombol_canc = MDFlatButton(text="Batal", on_release=self.dialog_canc)
            self.dialog = MDDialog(title="Konfirm..",
                text='Apakah anda yakin data yang diisikan sudah benar dan siap diupload ',                 
                radius=[20, 7, 20, 7],
                buttons=[tombol_ok,tombol_canc]) 
            self.dialog.open()
    
    def dialog_canc(self,obj):
        self.dialog.dismiss()
        pass

    def dialog_ok(self,obj):
        self.dialog.dismiss() 
        tombol_canc = MDFlatButton(text="OK", on_release=self.closing)
        self.dialog = MDDialog(
            text='TERIMA KASIH ... ',
            size_hint=(.5,.2),      
            radius=[20, 7, 20, 7],
            buttons=[tombol_canc]) 
        self.dialog.open()

    def closing(self,obj):
        self.dialog.dismiss()
        self.manager.transition.direction= 'left'
        self.manager.current = 'Menu_Page' 

class MainApp(MDApp):
    para_simpan = StringProperty("xxxx")
    def build(self):   
        sm = ScreenManager()        
        sm.add_widget(Login_Page(name='Login_Page'))  
        sm.add_widget(Menu_Page(name='Menu_Page')) 
        sm.add_widget(Mohon_Baru_Page(name='Mohon_Baru_Page')) 
        sm.add_widget(Mohon_Simp_Page(name='Mohon_Simp_Page')) 
        sm.add_widget(Mohon_Pinjaman_Page(name='Mohon_Pinjaman_Page'))
        sm.add_widget(Mohon_Simp_Ubah_Page(name='Mohon_Simp_Ubah_Page'))
        sm.add_widget(Mohon_Pinjaman_Lunas_Page(name='Mohon_Pinjaman_Lunas_Page'))
        sm.add_widget(Mohon_Pinjaman_Tenor_Page(name='Mohon_Pinjaman_Tenor_Page'))
        return sm     
    
    def on_start(self):        
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            if self.root.current == 'Menu_Page':
                self.root.current = 'Login_Page'
            elif self.root.current == 'Mohon_Baru_Page':
                self.root.current = 'Login_Page'
            elif self.root.current == 'Login_Page':
                self.get_running_app().stop()
            else:
                self.root.current = 'Menu_Page'                 
        return True 
    
    def pindah_ke(self, ygke, gerak):
        if gerak==1:
            self.root.transition.direction = 'right'
        else:
            self.root.transition.direction = 'left'

        if ygke==0: self.root.current = 'Menu_Page' 
        if ygke==1: self.root.current = 'Mohon_Baru_Page'
        if ygke==2: self.root.current = 'Mohon_Simp_Page'
        if ygke==3: self.root.current = 'Mohon_Simp_Ubah_Page'

        if ygke==5: self.root.current = 'Mohon_Pinjaman_Page'
        if ygke==6: self.root.current = 'Mohon_Pinjaman_Lunas_Page'
        if ygke==7: self.root.current = 'Mohon_Pinjaman_Tenor_Page'
    
    def format_angka(self,value):
        if type(value)==int or type(value)==float: fmbalik = f"{int(value):,}"
        elif type(value)== None: fmbalik =""        
        elif type(value)==str:
            if value.strip()=='': fmbalik =""
            else:
                fmbalik = f"{int(value):,}"
        else: fmbalik =""

        return fmbalik                

if __name__=="__main__":
    MainApp().run()
