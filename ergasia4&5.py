

word=input("write here:")

tab=list(word)
elegxos=False
print(tab)
s=" "
i=0
c=0

for i in range(0,100):
  
 try:   
  if(tab[i]=="o"and tab[i+1]=="n"and tab[i+2]=="e"):
   if(elegxos==False):
    a=1
    elegxos=True
   else:
       b=1
  if(tab[i]=="t"and tab[i+1]=="w"and tab[i+2]=="o"):
   if(elegxos==False):
    a=2
    elegxos=True
   else:
       b=2
  if(tab[i]=="t"and tab[i+1]=="h"and tab[i+2]=="r"and tab[i+3]=="e"and tab[i+4]=="e"):
   if(elegxos==False):
    a=3
    elegxos=True
   else:
    b=3
  if(tab[i]=="f"and tab[i+1]=="o"and tab[i+2]=="u"and tab[i+3]=="r"):
    if(elegxos==False):
     a=4
     elegxos=True
    else:
       b=4
  if(tab[i]=="f"and tab[i+1]=="i"and tab[i+2]=="v"and tab[i+3]=="e"):
    if(elegxos==False):
     a=5
     elegxos=True
    else:
       b=5
  if(tab[i]=="s"and tab[i+1]=="i"and tab[i+2]=="x"):
    if(elegxos==False):
     a=6
     elegxos=True
    else:
       b=6
  if(tab[i]=="s"and tab[i+1]=="e"and tab[i+2]=="v"and tab[i+3]=="e"and tab[i+4]=="n"):
    if(elegxos==False):
     a=7
     elegxos=True
    else:
       b=7    
  if(tab[i]=="e"and tab[i+1]=="i"and tab[i+2]=="g"and tab[i+3]=="h"and tab[i+4]=="t"):
     if(elegxos==False):
      a=8
      elegxos=True
     else:
      b=8
  if(tab[i]=="n"and tab[i+1]=="i"and tab[i+2]=="n"and tab[i+3]=="e"):
     if(elegxos==False):
      a=9
      elegxos=True
     else:
       b=9
  if(tab[i]=="z"and tab[i+1]=="e"and tab[i+2]=="r"and tab[i+3]=="o"):
     if(elegxos==False):
      a=0
      elegxos=True
     else:
       b=0
   
 except IndexError:
      gotdata = 'null'

 try:
     if(tab[i]=="p"and tab[i+1]=="l"and tab[i+2]=="u"and tab[i+3]=="s"):
      s="+"
     if(tab[i]=="m"and tab[i+1]=="i"and tab[i+2]=="n"and tab[i+3]=="u"and tab[i+4]=="s"):
      s="-"
     if(tab[i]=="t"and tab[i+1]=="i"and tab[i+2]=="m"and tab[i+3]=="e"and tab[i+4]=="s"):
      s="*"
     if(tab[i]=="d" and tab[i+1]=="i" and tab[i+2]=="v"):
      s="//"
 except IndexError:
     gotdata = 'null'
      
if(a==0 or b==0 and s=="//"):
         print("ΣΦΑΛΜΑ(ΕΓΙΝΕ ΔΙΑΙΡΕΣΗ ΜΕ ΜΗΔΕΝ)!!!")
else:
 if(s=="+"):
  c=a+b
 if(s=="-"):
  c=a-b
 if(s=="*"):
  c=a*b
 if(s=="//"):
  c=a//b
 print("ο πρώτος αριθμός είναι:",repr(a))
 print("ο δεύτερος αριθμός είναι:",repr(b))
 print("η πράξη είναι: ",s)
 print("το αποτέλεσμα είναι:",repr(c))
