from datetime import date,datetime, timedelta

def tanggal_text(fvalue):    
    if type(fvalue)==date or type(fvalue)==datetime:       
        ftext_month= '00'+str(fvalue.month)
        ftext_day  = '00'+str(fvalue.day)
        ftext_date = ftext_day[-2:]+'-'+ftext_month[-2:]+'-'+str(fvalue.year)
    else:
        ftext_date=""
    return ftext_date

def tanggal_value(gvalue):    
    vdate_value = None
    if type(gvalue)==str:
        if gvalue !='':
            # cek jika tgl formatnay yyyy-mm-dd
            gcek = gvalue[:4].strip()
            if gcek.isnumeric()==True :
                vtext_thn = gvalue[:4].strip()
                vtext_bln = gvalue[5:7].strip()
                vtext_day = gvalue[-2:].strip()
            else:
                vtext_day = gvalue[:2].strip()
                vtext_bln = gvalue[3:5].strip()
                vtext_thn = gvalue[-4:].strip()
                        
            if vtext_day.isnumeric()==True and vtext_bln.isnumeric()==True and vtext_thn.isnumeric()==True:
                int_day = int(vtext_day)
                int_bln = int(vtext_bln)
                int_thn = int(vtext_thn)                
                vdate_value= date(int_thn,int_bln, int_day)
    return vdate_value

def jatuhtempo_bulan(dari_tgl, bulan_plus):
    new_tgl_tempo= ""
    if type(dari_tgl)==date or type(dari_tgl)==datetime: ceking_salah = 0
    else:
        ceking_salah = 1
        if type(dari_tgl)==None: ceking_salah = 1    
        if type(dari_tgl)==str:
            if ceking_salah==0 and dari_tgl.strip()=='': ceking_salah = 1
            else: 
                dari_tgl = tanggal_value(dari_tgl)
                ceking_salah = 0

    if ceking_salah== 0:
        if ceking_salah== 0 and (type(bulan_plus)==int or type(bulan_plus)==float): ceking_salah = 0
        else:
            ceking_salah = 1
            if type(bulan_plus)==None: ceking_salah = 1
            if type(bulan_plus)==str:
                if ceking_salah==0 and bulan_plus.strip()=='': ceking_salah = 1
                else: 
                    bulan_plus = int(bulan_plus)
                    ceking_salah = 0
    
    if ceking_salah==0:
        xc_bln = dari_tgl.month
        xc_thn = dari_tgl.year
        xc_day = dari_tgl.day
        xc_bln_plus = xc_bln + bulan_plus
        if xc_bln_plus>12:
            xc_bln = xc_bln_plus-12
            xc_thn = xc_thn + 1
        else: xc_bln = xc_bln + bulan_plus
        if xc_thn%4== 0:
            xc_hari = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            xc_hari = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        xc_day_cek = xc_hari[xc_bln-1]
        if xc_day>xc_day_cek: xc_day = xc_day_cek
        new_tgl_tempo=date(xc_thn,xc_bln,xc_day)

    return new_tgl_tempo

def jatuhtempo_hari(dari_tgl, hari_plus):    
    new_tgl_tempo= ""
    if type(dari_tgl)==date or type(dari_tgl)==datetime: ceking_salah = 0
    else:
        ceking_salah = 1
        if type(dari_tgl)==None: ceking_salah = 1    
        if type(dari_tgl)==str:
            if ceking_salah==0 and dari_tgl.strip()=='': ceking_salah = 1
            else: 
                dari_tgl = tanggal_value(dari_tgl)
                ceking_salah = 0

    if ceking_salah== 0:
        if ceking_salah== 0 and (type(hari_plus)==int or type(hari_plus)==float): ceking_salah = 0
        else:
            ceking_salah = 1
            if type(hari_plus)==None: ceking_salah = 1
            if type(hari_plus)==str:
                if ceking_salah==0 and hari_plus.strip()=='': ceking_salah = 1
                else: 
                    bulan_plus = int(hari_plus)
                    ceking_salah = 0
    
    if ceking_salah==0: new_tgl_tempo= dari_tgl + timedelta(days=hari_plus)
    return new_tgl_tempo

def tanggal_awal(ftoday):
    fbalik = None
    if type(ftoday)==date or type(ftoday)==datetime:       
        ftext_month= '00'+str(ftoday.month)
        ftext_day  = '00'+str(ftoday.day)
        ftext_date = '01-'+ftext_month[-2:]+'-'+str(ftoday.year)
        fbalik = tanggal_value(ftext_date)

    if type(ftoday)==str:        
        xdt = tanggal_value(ftoday)
        if type(xdt)==date or type(xdt)==datetime:       
            ftext_month= '00'+str(xdt.month)
            ftext_day  = '00'+str(xdt.day)
            ftext_date = '01-'+ftext_month[-2:]+'-'+str(xdt.year)
            fbalik = tanggal_value(ftext_date)

    return fbalik    

def terbilang_cari(value):
    num = 0
    if type(value)==int: num = value
    if type(value)==float: num = int(value)
    if type(value)==str:
        if value.isnumeric(): num = int(value)

def Terbilang(value):
    bil= 0
    if type(value)==int: bil = value
    if type(value)==float: bil = int(value)
    if type(value)==str:
        if value.isnumeric(): bil = int(value)

    angka = ["","Satu","Dua","Tiga","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "

    n = int(bil)
    if n>= 0 and n <= 11: Hasil = angka[n]
    elif n <20: Hasil = Terbilang (n-10) + " Belas "
    elif n <100: Hasil = Terbilang (n/10) + " Puluh " + Terbilang (n%10)
    elif n <200: Hasil = " Seratus " + Terbilang (n-100)
    elif n <1000: Hasil = Terbilang (n/100) + " Ratus " + Terbilang (n%100)
    elif n <2000: Hasil = " Seribu " + Terbilang (n-1000)
    elif n <1000000: Hasil = Terbilang (n/1000) + " Ribu " + Terbilang (n%1000)
    elif n <1000000000: Hasil = Terbilang (n/1000000) + " Juta " + Terbilang (n%1000000)
    elif n <1000000000000: Hasil = Terbilang (n/1000000000) + " Milyar " + Terbilang (n%1000000000)
    elif n <1000000000000000: Hasil = Terbilang (n/1000000000000) + " Triliyun " + Terbilang (n%1000000000000)
    elif n == 1000000000000000: Hasil = "Satu Kuadriliun"
    else:
        Hasil = "Angka Hanya Sampai Satu Kuadriliun"

    return Hasil
