EP_04 = "luke_skywalker,leia,han_solo,darth_vader,obi-wan_kenobi,c-3po,r2-d2"
EP_05 = "yoda,lando_calrissian,boba_fett,palpatine"
EP_06 = "jabba_the_hutt"
EP_01 = "qui-gon_jinn,padme_amidala,anakin_skywalker,mace_windu,darth_maul"
EP_02 = "count_dooku,jango_fett"
EP_03 = "general_grievous"

episodio_validar = 0

episodio, personagem = input().split(" ")

if EP_01.find(personagem.lower()) >= 0:
    episodio_validar = 1
elif EP_02.find(personagem.lower()) >= 0:
    episodio_validar = 1
elif EP_03.find(personagem.lower()) >= 0:
    episodio_validar = 3
elif EP_04.find(personagem.lower()) >= 0:
    episodio_validar = 4
elif EP_05.find(personagem.lower()) >= 0:
    episodio_validar = 5
elif EP_06.find(personagem.lower()) >= 0:
    episodio_validar = 6

if episodio_validar < int(episodio):
    print("APARECEU_ANTES=SIM")
else:
    print("APARECEU_ANTES=NAO")