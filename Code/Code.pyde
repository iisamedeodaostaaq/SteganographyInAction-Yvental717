limg=500                                                                #DEFINIZIONE DELLA LARGHEZZA DEL DISEGNO
aimg=500                                                                #DEFINIZIONE DELL'ALTEZZA DEL DISEGNO
img=createImage(limg,aimg,RGB)                                          #CREAZIONE DELL IMAGINE
img.loadPixels()                                                        #CARICA DEI PIXEL DELL IMMAGINE VUOTA
e_l=0                                                                   #E_L(END LINE)SEGNA QUANDO LA RIGA NERA PER COMPLETARE LA FORMA è STATA CREATA
n_q=0                                                                   #N_Q(NUMERO QUADRATI)VARIABILE CHE CONTA IL NUMERO DI QUADRATI PER RIGA
 
def setup():
    size(limg,aimg)                                                     
    creaImg()                                                           
        
def creaImg():
    global p,y,x,limg,aimg,e_l,n_q,z
    input=createInput("Input")                                           #APERTURA DEL FILE NELLA DIRECTORY DATA PER RICEVERE IL TESTO DA STEGANOGRAFARE
    content=""                                       
    p=0                                                                  #POSIZIONE DEL PIXEL
    while n_q<=10:                                                       #CICLO FINCHE CI SONO PAROLE NEL FILE DI TESTO O FINCHE LA RIGA NON è FINITA 
        data1 = input.read()                                             #LETTURA PRIMO VALORE
        data2 = input.read()                                             #LETTURA SECONDO VALORE
        data3 = input.read()                                             #LETTURA TERZO VALORE
        if data2==-1:                                                    #CONTROLLO VALORE VUOTO 
            data2=255                                                    
        if data3==-1:                                                    #CONTROLLO VALORE VUOTO
            data3=255                                                    
        if data1==-1:                                                    #CONTROLLO VALORE VUOTO
            if n_q==0:
                break
            else:
                for z in range (10-n_q):
                    for x in range (50):
                        for y in range (50):
                            img.pixels[p+y+(limg*x)]=color(0,0,0)        #COLORAZIONE PIXEL NERO
                            e_l=1
        else:                                                            #CREAZIONE DEL QUADRATO COLORATO IN BASE AI 3 VALORI CATTURATI IN INPUT 
            n_q+=1
            for x in range (50):
                for y in range (50):
                    img.pixels[p+y+(limg*x)]=color(data1,data2,data3)         #COLORAZIONE PIXEL
        p=p+50                                                                #AVANZAMENTO QUADRATO
        if(p%limg==0):
            p=p+limg*49                                                       #AVANZAMENTO DI RIGA
            n_q=0                                                             #AZZERAMENTO DEL CONTATORE DI QUADRATI 
            if e_l==1:                                                        #SE LA RIGA NERA è STATA CREATA INTERROMPERE LA FUNZIONE
                break
    img.updatePixels()                                                        #AGGIORNAMENTO DEI PIXEL NELL IMMAGINE 
    image(img,0,0)                                                            #STAMPA A SCHERMO DELL IMMAGINE
    save("Mistery.tiff")                                                          #SALVATAGGIO DELL IMMAGINE
    
