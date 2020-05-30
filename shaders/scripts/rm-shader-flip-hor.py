import re

#righe del file
rows = []
#path dello shader
shaderPath = "shaders_glsl/misc/flip-horizontal.glsl\n"
#flag per la rmozione delle righe appartenenti allo  shader da rimuovere
rm = False
#contatore per le righe da eliminare
rmCount = 0
#apertura file e successiva lettura
with open("./shaders/retroarch.glslp", 'r') as fp:
   #ciclo for che scorre l'array delle righe del file
   for row in fp:
      #se identifico il path dello shader da rimuovere
      if(shaderPath in row) :
         #pongo il flag a true che eviterà successivamente di entrare nel'if di inserimento delle righe
         rm = True
      if(rm) :
         #se il contatore delle righe da eliminare è arrivato a 7, cambio il valore del flag rm che conferma la possibilità di aggiungere le restanti righe
         if(rmCount == 5) :
            rm = False
            rmCount = 0
         else :
            rmCount += 1
      else :
         #inserimento righe in un array
         rows.append(row)

#ottenimento del numero di shader attivi
nShaders = int(re.search('shaders = "(.*)"', rows[0]).group(1))
#decremento e reinserimento degli shader attivi
rows[0] = 'shaders = "' + str(nShaders - 1) + '"\n'
#contatore per identificare il numero dello shader
countShader = 0
#for che scorre tutte le righe del file nell'apposito array e se incontra uno shader con numero non sequenziale, in accordo con il countShader, lo sistema
for x in range(len(rows)-2):
   if('shader' in rows[x+2]):
      firstSRow = re.split(r'\s', rows[x+2])
      #print(firstSRow)
      nshader = int(re.split(r'shader', firstSRow[0])[1])
      if(nshader == countShader):
         countShader +=1
      else:
         countShader += 1
         nshader = nshader - 1
         rows[x+2] = 'shader' + str(nshader) + ' = ' + firstSRow[2] + '\n'
      #print(nshader)

#a partire dall'array delle righe del file creiamo il file in una stringa
separator = ""
retroarchGlslp = separator.join(rows)
#print(retroarchGlslp)
#chiudiamo il file in lettura
fp.close()

#apriamo il file in scrittura
file = open("./shaders/retroarch.glslp", 'w')
#scriviamo sul file
file.write(retroarchGlslp)
#chiudiamo il file in scrittura
file.close() 