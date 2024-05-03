

# 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]

list1=[]
for i in range(1,6):
    list1.append(input("{}-ci ededi daxil edin : ".format(i)))
list1.sort()    
print(list1)


# 2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü.

list = input("Cümləni daxil edin : ").split()
soz=''
for i in list:
    list2=sorted(i)
    for j in list2:
        soz+=j
    soz+=" "
print (soz) 

3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
ilk input== 4   
ikinci input == 7
ucuncu input == 2
dorduncu input == 13

təbriklər . 4 cehdde 13 reqemeni tapdiz


say=1
while True:
    eded=int(input('əded daxil edin : '))
    if eded==20:
        print("Tebrikler {} cəhddə tapdiz".format(say))
        break
    say+=1



4). 1 ile 100 arasinda sade ededleri print edin. (for loops)


sadələr = []
def sade(eded):
    for j in range(2, eded):
        if eded % j == 0:
            return False
    return True

for i in range(2, 100):
    if sade(i):
        sadələr.append(i)
print(sadələr)
