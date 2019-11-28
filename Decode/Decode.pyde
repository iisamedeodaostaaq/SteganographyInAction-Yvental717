char1='a'                                          #DEFINIZIONE DI UNA VARIABILE DI TIPO CHAR PER LA TRASPOSIZIONE DA ASCII A CARATTERE
char2='a'                                          #DEFINIZIONE DI UNA VARIABILE DI TIPO CHAR PER LA TRASPOSIZIONE DA ASCII A CARATTERE
char3='a'                                          #DEFINIZIONE DI UNA VARIABILE DI TIPO CHAR PER LA TRASPOSIZIONE DA ASCII A CARATTERE
x=0                                                
p=0                                                #DEFINIZIONE DI UNA VARIABILE P UTILIZZATA PER INDICARE IL PIXEL CON IL QUALE STIAMO LAVORANDO
testo=""
n_r=0                                              #NUMERO DI RIGHE 
def setup():
    global img
    img=loadImage("Mistery.tiff")                      #IMPORTO L'IMMAGINE
    img.loadPixels()                               #IMPORTO I PIXELS
    deco()                                         #FUNZIONE PER RICAVARE IL MESSAGGIO DALL IMMAGINE
    
def deco():
    global x,y,char1,char2,char3,img,testo,p
    data1=red(img.pixels[p])
    data2=green(img.pixels[p])
    data3=blue(img.pixels[p])  
    while data1 != 0.0 or data2 != 0.0 or data3 != 0.0:
        for x in range (10):                       #RIPETIZIONE DELLE ISTRUZIONE PER 10 QUADRATI
            data1=red(img.pixels[p])               #CATTURA DEL VALORE NUMERICO RED NELL IMMAGINE
            data2=green(img.pixels[p])             #CATTURA DEL VALORE NUMERICO GREEN NELL IMMAGINE
            data3=blue(img.pixels[p])              #CATTURA DEL VALORE NUMERICO BLUE NELL IMMAGINE
            if data3 >128.0:                       #CONTROLLO VALORE 255 AGGIUNTO
                data3=0
            if data2>128.0:                        #CONTROLLO VALORE 255 AGGIUNTO
                data2=0
            if data1 == 0.0 and data2 == 0.0 and data3 == 0.0 : #CONTROLLO FINE DEL TESTO
                break                    
            data1_i = int(data1)                   #CAMBIO DEL PRIMO VALORE RED DA FLOAT A INT
            data2_i = int(data2)                   #CAMBIO DEL SECONDO VALORE DA FLOAT A INT
            data3_i = int(data3)                   #CAMBIO DEL TERZO VALORE DA FLOAT A INT               
            char1=chr(data1_i)                     #ASSEGNAZIONE DEL PRIMO VALORE ASCII DA INT A CHAR
            char2=chr(data2_i)                     #ASSEGNAZIONE DEL SECONDO VALORE ASCII DA INT A CHAR
            char3=chr(data3_i)                     #ASSEGNAZIONE DEL TERZO VALORE ASCII DA INT A CHAR
            testo+=char1                           #AGGIUNTA DEL PRIMO CARATTERE AL TESTO
            testo+=char2                           #AGGIUNTA DEL SECONDO CARATTERE AL TESTO
            testo+=char3                           #AGGIUNTA DEL TERZO CARATTERE AL TESTO
            p+=50                                  #VALORE AGGIUNTO A P PER SPOSTARSI DI RIQUADRO                             
        p+=500*49                                  #VALORE AGGIUNTO A P PER SPOSTARSI DI RIGA
    print(testo)                                   #STAMPA DEL TESTO FINALE
    
