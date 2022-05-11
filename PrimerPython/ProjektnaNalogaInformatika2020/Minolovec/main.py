import pygame as py
import random
import time

py.init()

#lastnosti polja(osnovni parametri)
sirinaMinPolja = 40 #min = 9(v originalu)
visinaMinPolja = 30 #min = 9(v originalu)
steviloMin = 20 #min = 10(v originalu)

#preverjanje pravilnosti osnovnih parametrov
if steviloMin >= sirinaMinPolja * visinaMinPolja:
    exit()

#grafika
pokrivalo = py.image.load('Grafika/pokrivalo.png')
vprasaj = py.image.load('Grafika/vprasaj.png')
zastavica = py.image.load('Grafika/zastavica.png')
nula = py.image.load('Grafika/nula.png')
nicka = py.image.load('Grafika/0.png')
enka = py.image.load('Grafika/1.png')
dvojka = py.image.load('Grafika/2.png')
trojka = py.image.load('Grafika/3.png')
stirka = py.image.load('Grafika/4.png')
petka = py.image.load('Grafika/5.png')
sestka = py.image.load('Grafika/6.png')
sedmka = py.image.load('Grafika/7.png')
osmka = py.image.load('Grafika/8.png')
devetka = py.image.load('Grafika/9.png')
minaN = py.image.load('Grafika/minaN.png')
minaR = py.image.load('Grafika/minaR.png')
minaZ = py.image.load('Grafika/minaZ.png')
smajliN = py.image.load('Grafika/smajliN.png')
smajliZ = py.image.load('Grafika/smajliZ.png')
smajliX = py.image.load('Grafika/smajliX.png')
smajliO = py.image.load('Grafika/smajliO.png')
ikona = py.image.load('Grafika/ikona.png')

#lastnosti okna
spodnjiM = 20
leviIdesni = 20
zgornjiM = 25
srednjiM = 25
visinaStevcev = 25
sirinaOkna = 2 * leviIdesni + sirinaMinPolja * 25
visinaOkna = visinaStevcev + spodnjiM + zgornjiM + srednjiM + visinaMinPolja * 25
okno = py.display.set_mode((sirinaOkna,visinaOkna))

#naslov okna
py.display.set_caption('Minolovec')
py.display.set_icon(ikona)

#ustvarjanje slovarja polj
minPolje = dict()
for i in range(1, sirinaMinPolja + 1):
    for j in range(1, visinaMinPolja + 1):
        minPolje[(i, j)] = ['neodkrito', -3, 0]



#funkcija za barvo odzadja
def odzadje():
    okno.fill((250,250,250))
    okno.blit(smajliN,(int((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2), 25))
    py.display.update()

#začetni parametri
prviKlik = 0
zadnjiKlik = ()
prvaMina = False
zmagovalec = False
zacetekIgranja = 0

#funkcija za risanje polja
def polje():
    for i in minPolje:

        #risanje znakov desnega klika
        if minPolje[i][0] == 'neodkrito':
            if minPolje[i][1] == -3:
                okno.blit(pokrivalo, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][1] == -2:
                okno.blit(vprasaj, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][1] == -1:
                okno.blit(zastavica, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))

        #risanje številk
        else:
            if minPolje[i][2] == 0:
                okno.blit(nicka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
                #odkrivanje okoliškoh ničel
                # možni premiki
                levo = False
                desno = False
                gor = False
                dol = False
                if i[0] - 1 >= 1:
                    levo = True
                if i[0] + 1 <= sirinaMinPolja:
                    desno = True
                if i[1] - 1 >= 1:
                    gor = True
                if i[1] + 1 <= visinaMinPolja:
                    dol = True
                if levo and gor:
                    minPolje[i[0] - 1, i[1] - 1][0] = 'odkrito'
                if gor:
                    minPolje[i[0], i[1] - 1][0] = 'odkrito'
                if desno and gor:
                    minPolje[i[0] + 1, i[1] - 1][0] = 'odkrito'
                if levo:
                    minPolje[i[0] - 1, i[1]][0] = 'odkrito'
                if desno:
                    minPolje[i[0] + 1, i[1]][0] = 'odkrito'
                if levo and dol:
                    minPolje[i[0] - 1, i[1] + 1][0] = 'odkrito'
                if dol:
                    minPolje[i[0], i[1] + 1][0] = 'odkrito'
                if desno and dol:
                    minPolje[i[0] + 1, i[1] + 1][0] = 'odkrito'

            if minPolje[i][2] == 1:
                okno.blit(enka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][2] == 2:
                okno.blit(dvojka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][2] == 3:
                okno.blit(trojka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][2] == 4:
                okno.blit(stirka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][2] == 5:
                okno.blit(petka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][2] == 6:
                okno.blit(sestka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][2] == 7:
                okno.blit(sedmka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            if minPolje[i][2] == 8:
                okno.blit(osmka, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))

        #risanje min
        if prvaMina:
            if i == zadnjiKlik and minPolje[i][2] == 9 and zmagovalec != True:
                okno.blit(minaR, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
            elif minPolje[i][2] == 9:
                if minPolje[i][1] == -1:
                    okno.blit(minaZ, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
                else:
                    okno.blit(minaN, (leviIdesni + (i[0] - 1) * 25, zgornjiM + srednjiM + visinaStevcev + (i[1] - 1) * 25))
    py.display.update()

#risanje točk(štetje ugibanih min)
def stevec():
    stetje = steviloMin

    for i in minPolje:
        if minPolje[i][1] == -1:
            stetje -= 1

    if stetje <= 0:
        okno.blit(nula, (leviIdesni + 25 * 2, zgornjiM))

    else:
        if len(str(stetje)) == 1:
            stevilka = '0' + '0' + str(stetje)

        elif len(str(stetje)) == 2:
            stevilka = '0' + str(stetje)

        elif len(str(stetje)) == 3:
            stevilka = str(stetje)

        for j in range(len(stevilka)):
            if int(stevilka[j]) == 0:
                okno.blit(nula, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 1:
                okno.blit(enka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 2:
                okno.blit(dvojka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 3:
                okno.blit(trojka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 4:
                okno.blit(stirka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 5:
                okno.blit(petka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 6:
                okno.blit(sestka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 7:
                okno.blit(sedmka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 8:
                okno.blit(osmka, (leviIdesni + 25 * j, zgornjiM))
            if int(stevilka[j]) == 9:
                okno.blit(devetka, (leviIdesni + 25 * j, zgornjiM))

#funkcija za uro
def ura(prvaMina):
    cas = time.time() - zacetekIgranja
    if prviKlik == 0 or cas <= 0:
        okno.blit(nula, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3), zgornjiM))
        okno.blit(nula, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * 1, zgornjiM))
        okno.blit(nula, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * 2, zgornjiM))

    elif prvaMina or zmagovalec:
        pass

    elif len(str(int(cas))) > 3:
        okno.blit(devetka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3), zgornjiM))
        okno.blit(devetka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * 1, zgornjiM))
        okno.blit(devetka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * 2, zgornjiM))

    else:
        if len(str(int(cas))) == 1:
            sekunde = '0' + '0' + str(int(cas))

        elif len(str(int(cas))) == 2:
            sekunde = '0' + str(int(cas))

        elif len(str(int(cas))) == 3:
            sekunde = str(int(cas))

        for j in range(len(sekunde)):
            if int(sekunde[j]) == 0:
                okno.blit(nula, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 1:
                okno.blit(enka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 2:
                okno.blit(dvojka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 3:
                okno.blit(trojka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 4:
                okno.blit(stirka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 5:
                okno.blit(petka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 6:
                okno.blit(sestka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 7:
                okno.blit(sedmka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 8:
                okno.blit(osmka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))
            if int(sekunde[j]) == 9:
                okno.blit(devetka, ((leviIdesni + sirinaMinPolja * 25 - 25 * 3) + 25 * j, zgornjiM))

#zanka za izvajanje
odzadje()

izvaja = True
while izvaja:

    #klic funkcij
    polje()
    ura(prvaMina)
    stevec()

    for dogodek in py.event.get():

        #izhod
        if dogodek.type == py.QUIT:
            izvaja = False

        #gumb za resetiranje oz. smajli
        #resetiranje
        if dogodek.type == py.MOUSEBUTTONDOWN and dogodek.button == 1 and int((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2) <= py.mouse.get_pos()[0] <= int(((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2) + 25) and 25 <= py.mouse.get_pos()[1] <= 50:
            okno.blit(smajliN, (int((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2), 25))
            for i in range(1, sirinaMinPolja + 1):
                for j in range(1, visinaMinPolja + 1):
                    minPolje[(i, j)] = ['neodkrito', -3, 0]
            prvaMina = False
            prviKlik = 0
            zmagovalec = False

        #risanje O smajlija
        if dogodek.type == py.MOUSEBUTTONDOWN and dogodek.button == 1 and prvaMina == False:
            okno.blit(smajliO, (int((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2), 25))

        # risanje X smajlija
        if prvaMina and not zmagovalec:
            okno.blit(smajliX, (int((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2), 25))

        # risanje Z smajlija in zmaga
        if prvaMina == False:
            zmaga = True
            for i in minPolje:
                if minPolje[i][0] == 'neodkrito' and minPolje[i][2] != 9:
                    zmaga = False
            if zmaga:
                for i in minPolje:
                    if minPolje[i][2] == 9:
                        minPolje[i][1] = -1
                okno.blit(smajliZ, (int((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2), 25))
                prvaMina = True
                zmaga = True
                zmagovalec = True

        # risanje N smajlija
        if dogodek.type == py.MOUSEBUTTONUP and dogodek.button == 1 and prvaMina == False:
            okno.blit(smajliN, (int((2 * leviIdesni + sirinaMinPolja * 25) / 2 - 25 / 2), 25))

        #zaznavanje klikov
        if py.mouse.get_pos()[0] < leviIdesni or py.mouse.get_pos()[0] > leviIdesni + sirinaMinPolja * 25 or py.mouse.get_pos()[1] < zgornjiM + srednjiM + visinaStevcev or py.mouse.get_pos()[1] > visinaStevcev + zgornjiM + srednjiM + visinaMinPolja * 25:
            continue
        else:

            # zaznavanje prvega pritisnjenega polja in generiranje polja
            #prvo pritisnjeno polje
            if dogodek.type == py.MOUSEBUTTONDOWN and dogodek.button == 1 and prviKlik == 0:
                while prviKlik < 1:
                    if py.mouse.get_pos()[0] < leviIdesni or py.mouse.get_pos()[0] > leviIdesni + sirinaMinPolja * 25 or \
                            py.mouse.get_pos()[1] < zgornjiM + srednjiM + visinaStevcev or py.mouse.get_pos()[
                        1] > visinaStevcev + zgornjiM + srednjiM + visinaMinPolja * 25:
                        continue
                    else:
                        koordinate = py.mouse.get_pos()
                        koordinataX = koordinate[0]
                        koordinataY = koordinate[1]
                        koordinataX = (koordinataX - leviIdesni) // 25 + 1
                        koordinataY = (koordinataY - (zgornjiM + srednjiM + visinaStevcev)) // 25 + 1
                        minPolje[(koordinataX, koordinataY)][0] = 'odkrito'
                        prvoPolje = (koordinataX, koordinataY)
                        prviKlik += 1
                        zacetekIgranja = time.time()

                #generiranje polja
                #postavljanje min
                postavljeneMine = []
                while steviloMin > len(postavljeneMine):
                    potencialnaMina = (random.randint(1,sirinaMinPolja), random.randint(1, visinaMinPolja))
                    if potencialnaMina not in postavljeneMine and potencialnaMina != prvoPolje:
                        postavljeneMine.append(potencialnaMina)
                        minPolje[(potencialnaMina[0], potencialnaMina[1])][2] = 9

                #postavljanje števil
                for i in minPolje:
                    if minPolje[i][2] != 9:
                        steviloOkoliskihMin = 0

                        #možni premiki
                        levo = False
                        desno = False
                        gor= False
                        dol = False
                        if i[0] - 1 >= 1:
                            levo = True
                        if i[0] + 1 <= sirinaMinPolja:
                            desno = True
                        if i[1] - 1 >= 1:
                            gor = True
                        if i[1] + 1 <= visinaMinPolja:
                            dol = True

                        #dejansko štetje
                        if levo and gor:
                            if minPolje[i[0] - 1, i[1] - 1][2] == 9:
                                steviloOkoliskihMin += 1
                        if gor:
                            if minPolje[i[0], i[1] - 1][2] == 9:
                                steviloOkoliskihMin += 1
                        if desno and gor:
                            if minPolje[i[0] + 1, i[1] - 1][2] == 9:
                                steviloOkoliskihMin += 1
                        if levo:
                            if minPolje[i[0] - 1, i[1]][2] == 9:
                                steviloOkoliskihMin += 1
                        if desno:
                            if minPolje[i[0] + 1, i[1]][2] == 9:
                                steviloOkoliskihMin += 1
                        if levo and dol:
                            if minPolje[i[0] - 1, i[1] + 1][2] == 9:
                                steviloOkoliskihMin += 1
                        if dol:
                            if minPolje[i[0], i[1] + 1][2] == 9:
                                steviloOkoliskihMin += 1
                        if desno and dol:
                            if minPolje[i[0] + 1, i[1] + 1][2] == 9:
                                steviloOkoliskihMin += 1
                        minPolje[i][2] = steviloOkoliskihMin

            #zaznavanje desnih in levih klikov na polja
            if prvaMina == False:

                #levi klik miške
                if dogodek.type == py.MOUSEBUTTONDOWN and dogodek.button == 1:
                    koordinate = py.mouse.get_pos()
                    koordinataX = koordinate[0]
                    koordinataY = koordinate[1]
                    koordinataX = (koordinataX - leviIdesni) // 25 + 1
                    koordinataY = (koordinataY - (zgornjiM + srednjiM + visinaStevcev)) // 25 + 1
                    minPolje[(koordinataX, koordinataY)][0] = 'odkrito'
                    if minPolje[(koordinataX, koordinataY)][2] == 9:
                        prvaMina = True
                        zadnjiKlik = (koordinataX, koordinataY)

                #desni klik miške
                elif dogodek.type == py.MOUSEBUTTONDOWN and dogodek.button == 3:
                    koordinate = py.mouse.get_pos()
                    koordinataX = koordinate[0]
                    koordinataY = koordinate[1]
                    koordinataX = (koordinataX - leviIdesni) // 25 + 1
                    koordinataY = (koordinataY - (zgornjiM + srednjiM + visinaStevcev)) // 25 + 1
                    if minPolje[(koordinataX, koordinataY)][1] == -3 and minPolje[(koordinataX, koordinataY)][0] != 'odkrito':
                        minPolje[(koordinataX, koordinataY)][1] = -1
                    elif minPolje[(koordinataX, koordinataY)][1] == -2 and minPolje[(koordinataX, koordinataY)][0] != 'odkrito':
                        minPolje[(koordinataX, koordinataY)][1] = -3
                    elif minPolje[(koordinataX, koordinataY)][1] == -1 and minPolje[(koordinataX, koordinataY)][0] != 'odkrito':
                        minPolje[(koordinataX, koordinataY)][1] = -2
