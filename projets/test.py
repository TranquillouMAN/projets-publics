#ECRIRE "bonsoir paris"
# r=12000
# s=1250
# e=10
# rh=230
# assertionUn = (((365*3)/(24-(16-8)))*(rh)>r)==(e*s<r) #false
# assOne = (15740,625 > 12000) #true
# asstwo = (12500<12000) #false
# assertionUn = (15740,625 > 12000)==(12500<12000) #false    
# #assertion2 = (((365*3)/(4-(12-8)))*(rh)>r)==(e*s<r) #true
# assOne = (1095/0>12000) #False
# asstwo = (12500<12000) #false                                       


# def retournerSixPlusTrois():
#     return 6+3
# def retournerSixPlusX(x):
#     return 6 + x
# #print("Qui vole un" + retournerSixPlusTrois() + "vole un boeuf")
# print(retournerSixPlusX(3))

# def add(x;y):
#     return x+y
# def sub(x;y):
#     return x-y
# def divide(x;y):
#     return x/y
# def multiply(x;y):
#     return x*y
# def modulo(x;y):
#     return x%y
# 19.58jour ouvrée par mois
# 8h ouvrée par jour

def calculeSalaireSeconde(c,j,h,s):
    return c/(j*h*s)

print(calculeSalaireSeconde(1200,19.58,8,3600))

def calculeSalaireHeure(c,j,h):
    return c/(j*h)

print(calculeSalaireHeure(1200,19.58,8))
        

#FIN   