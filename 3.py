a=input()
vowel=["a","A","e","E","i","I","o","O","u","U"]
consonant=["b","B","c","C","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","p","P","q","Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
if (a in vowel):
    print("Vowel")
elif (a in consonant):
    print("Consonant")
else:
    print("invalid")
    

