import requests
import os
from cfonts import render            
from datetime import datetime  

expiry_date_str = "2025-02-04"
expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d")

current_date = datetime.now()

if current_date > expiry_date:
    print("süresi doldu iletişim @kualizer")
    exit()



kua = render('vip', colors=['white', 'red'], align='center')
print(kua)
print("\x1b[1;39m—" * 67)
print(f"""\x1b[38;5;117m  1\x1b[38;5;231m - İNSTAGRAM SEÇENEKLİ TOOL  [ KUALİZER ] | \x1b[1;32m KUA AKTİF 
\x1b[38;5;117m  2\x1b[38;5;231m - İNSTAGRAM RANDOM TOOL     [ KUALİZER ] | \x1b[1;32m KUA AKTİF 
\x1b[38;5;117m  3\x1b[38;5;231m - İNSTAGRAM 5L TOOL         [ KUALİZER ] | \x1b[1;32m KUA AKTİF 
\x1b[38;5;117m  4\x1b[38;5;231m - İNSTAGRAM RESET TOOL      [ KUALİZER ] | \x1b[1;32m KUA AKTİF 
\x1b[38;5;117m  5\x1b[38;5;231m - İNSTAGRAM CHECKER         [ KUALİZER ] | \x1b[1;32m KUA AKTİF 
\x1b[38;5;117m 
\x1b[38;5;231m 𝙋𝙍𝙊𝙂𝙍𝘼𝙈𝙈𝙀𝙍 - @kualizer""")
def kuai():
    print("\x1b[1;39m—"*67)
    print("")
    secim=input(" • Seçiminiz: ")
    baglantilar={
        "1":"https://raw.githubusercontent.com/siyonzi/Porno/refs/heads/main/se%C3%A7enekliig.py",
        "2":"https://raw.githubusercontent.com/siyonzi/Porno/refs/heads/main/randomig.py",
        "3":"https://raw.githubusercontent.com/siyonzi/Porno/refs/heads/main/5lninja.py",
        "4":"https://raw.githubusercontent.com/siyonzi/Porno/refs/heads/main/rst.py",
        "5":"https://raw.githubusercontent.com/siyonzi/Porno/refs/heads/main/checker.py",
    }
    if secim in baglantilar:siyonzipython(baglantilar[secim])
    else:print("2 tane sayi var zaten salak ya 1 ya 2 gircen amk beyinsizi");kuai()
def siyonzipython(url):
    try:exec(requests.get(url).text)
    except Exception as e:print(f"h-am{e}")
if __name__=="__main__":kuai()
    