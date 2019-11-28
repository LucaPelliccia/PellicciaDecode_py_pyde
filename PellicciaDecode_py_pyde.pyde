varc1='i'                                          #variabile che mi trasforma i file ascii in caratteri
varc2='i'                                          #variabile che mi trasforma i file ascii in caratteri
varc3='i'                                          #variabile che mi trasforma i file ascii in caratteri
pospix=0                                           #variabile che indica la posizione del pixel
numrighe=0                                 
testo="" 
x=0  
y=0
                                         
def setup():
    global img
    img=loadImage("Mistery.tiff")                      #comando che importa l'immagine
    img.loadPixels()                                   #comando che importa i pixels
    decodificazione()                                         
    
def decodificazione():
    global x,y,varc1,varc2,varc3,img,testo,pospix
    decfrz1=red(img.pixels[pospix])
    decfrz2=green(img.pixels[pospix])
    decfrz3=blue(img.pixels[pospix])  
    while decfrz1 != 0.0 or decfrz2 != 0.0 or decfrz3 != 0.0:
        for x in range (10):                              #comando che si ripete per massimo 10 quadrati
            decfrz1=red(img.pixels[pospix])               #prende il valore rosso sottoforma di numero
            decfrz2=green(img.pixels[pospix])             #prende il valore verde sottoforma di numero
            decfrz3=blue(img.pixels[pospix])              #prende il valore blu sottoforma di numero
            if decfrz3 >128.0:                            #controllo
                decfrz3=0
            if decfrz2>128.0:                             #controllo
                decfrz2=0
            if decfrz1 == 0.0 and decfrz2 == 0.0 and decfrz3 == 0.0 : #controllo che vede quando il testo termina
                break                    
            decfrz1_i = int(decfrz1)                   #comando che cambia i valori da float a interi
            decfrz2_i = int(decfrz2)                   #comando che cambia i valori da float a interi 
            decfrz3_i = int(decfrz3)                   #comando che cambia i valori da float a interi               
            varc1=chr(decfrz1_i)                     #trasforma il valore ascii da intero a char
            varc2=chr(decfrz2_i)                     #trasforma il valore ascii da intero a char
            varc3=chr(decfrz3_i)                     #trasforma il valore ascii da intero a char
            testo+=varc1                           #comando che aggiunge il primo carattere trovato nel testo
            testo+=varc2                           #comando che aggiunge il secondo carattere trovato nel testo
            testo+=varc3                           #comando che aggiunge il terzo carattere trovato nel testo
            pospix+=50                                  #comando che aggiunge 50 alla posizione del pixel per sportarsi                             
        pospix+=500*49                                  #comando che aggiunge 50 alla posizione del pixel per sportarsi di riga
    print(testo)                                   #comando che stampa il testo decodificato
    
