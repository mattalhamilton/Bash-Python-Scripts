#Matt Hamilton
#Mod 03 Tutorial


lyrics_string=("Quisiera:Ayer:cambiarle:conocí:el:un:final"
               ":cielo:al:sin:cuento|Las:sol|Y:barras:un:y"
               ":hombre:los:sin:tragos:suelo|Un:han:santo:"
               "sido:en:testigo|De:prision|Y:el:una:dolor:"
               "canción:que:triste:me:sin:causaste:dueño|Y:"
               "y:conocí:to':tus:lo:ojos:que:negros|Y:hiciste"
               ":ahora:conmigo|Un:sí:infeliz:que:en:no:el:"
               "puedo:amor,:vivir:que:sin:aun:ellos:no:yo|"
               "Le:te:pido:supera|Que:al:ahora:cielo:camina"
               ":solo:solo:un:sin:deseo|Que:nadie:en:por:tus"
               ":todas:ojos:las:yo:aceras|Preguntándole:pueda"
               ":a:vivir|He:Dios:recorrido:si:el:en:mundo:verdad"
               ":entero|te:el:vengo:amor:a:existe|:decir|")

##This makes the list from the string
lyrics_list = lyrics_string.split(':')


song1=[]
song2=[]
song3=[]

##One loop to split this into two strings
for i in range(0,len(lyrics_list),2):
    song1.append(lyrics_list[i])
    song2.append(lyrics_list[i+1])

    
##song1
song1_print = ' '.join(song1)
song1_print = song1_print.replace('|','\n')
print(song1_print.strip())

print('\n\n')
##song2
song2_print = ' '.join(song2)
song2_print = song2_print.replace('|','\n')
print(song2_print.strip())




##song3
print('\nWords that are in both songs: ')

for i in range(len(song1)):
    try:
        if song1[i] in song2:
            if song1[i] not in song3:
                song3.append(song1[i])
    except:
        continue

for m in range(len(song3)):
    print(song3[m])
    
input()
        
