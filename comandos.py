from BotAmino import *


client = BotAmino()
client.prefix = "-"

@client.command()
def echo(data, t : str, nt = 100):
    for _ in range(int(nt)):
           data.subClient.send_message(data.chatId,message=t,messageType=109)

@client.command()
def coins(data, amt : int , nt = 1):
    print(data.comId)
    print(data.authorId)
    print(data.chatId)
    amt , nt = int (amt) , int(nt)
    for _ in range(nt):
           try:
           	data.subClient.send_message(chatId= data.chatId,coins=amt,transactionId="0dff83e6-dd46-4e2d-a256-8162de572231")
           except:
           	pass
@client.command()
def echo(data, t : str, nt = 100):
    for _ in range(int(nt)):
           data.subClient.send_message(data.chatId,message=t)

@client.command()
def steve(data):
    data.subClient.send_message(data.chatId,message="""🏿🏿🏿🏿🏿🏿🏿🏿\n🏿🏿🏿🏿🏿🏿🏿🏿\n🏿🏿🏽🏽🏽🏽🏿🏿\n🏽🏽🏽🏽🏽🏽🏽🏽\n🏽⬜⬛🏽🏽⬛⬜🏽\n🏽🏽🏽🏿🏿🏽🏽🏽\n🏽🏽🏿🏽🏽🏿🏽🏽\n🏽🏽🏿🏿🏿🏿🏽🏽""",messageType=109)
@client.command()
def ayuda(data):
    data.subClient.send_message(data.chatId,message='✏--------------------------------------\nHola, hola, soy una pequeña\nbot en desarrollo de\n entretenimiento y \ndiversion, usa "-entretenimiento" para ver las cosas que hago\nve mi wiki con -wihack\nUsa -echo para verlo\n-minecraft para ver los mensajes ghost que tengo <3✏---------------------------------------')
print("Comandos de ayuda listo")
@client.command()
def coins(data):
    data.subClient.get_wallet_amount()

@client.command()
def echo_help(data):
     data.subClient.send_message(data.chatId,message="[ci]Tengo dos -echo, el normal y el -echo_ghost; el segundo es un mensae fantasma")
@client.command()
def minecraft(data):
     data.subClient.send_message(data.chatId,message="""[ci]Los que tengo por ahora es:
     	 [ci]-steve""")
     data.subClient.send_message(data.chatId,message="[ci]Mi creador es esta persona <3\n[ci]http://aminoapps.com/u/Anark1")
@client.answer("Tashi prendete")
def hello (data):
    data.subClient.send_message(data.chatId,message="Ya estoy prendida 👉👈")
@client.command()
def abrazar(data):
    data.subClient.send_message(data.chatId,message="×Corresponde tu abrazo×\n\n<3")
    
@client.command() 
def programacion(data):
    data.subClient.send_message(data.chatId,message="Aprende programacion y mas cosas aqui >.<\n http://aminoapps.com/c/HackingUtils")

@client.command()
def desarrollo(data):
     data.subClient.send_message(data.chatId,message="[ci]Mi desarrollo lo puedes ver en esta comunidad <3\n\n[ci]aminoapps.com/c/Laratshu")
@client.command()
def entretenimiento (data):
	data.subClient.send_message(data.chatId,message="[ciu]comandos de entretenimiento <3\n\n[ci]-uwu -elfa\n\n[ci]-ping -nia \n\n[ci]-sempai\n\n[ci]-chistes1\2 -oniichan\n\n[ci]-ichinizan\n[ci]-pro -r34_loli\n[ci]-minita -furry\n[ci]-miku -sdlg")
	


@client.command()
def minita(data):
    data.subClient.send_message(data.chatId,message="[ci]Pasen ig de la minita >.<")
	
@client.command()
def ping(data):
    data.subClient.send_message(data.chatId, message="pong!")
    
@client.command
def wihack_shadow(data):
    data.subClient.send_message(data,chatId,message="The Shadow Brokers es un grupo de piratas informáticos que apareció por primera vez en el verano de 2016")
 
@client.command()
def voce(data):
     data.subClient.send_message(data.chatId,message="Ñao manito KKKKKKKKKKKKKKK")
@client.command()
def furry(data):
    data.subClient.send_message(data.chatId,message=" aqui tienes >.<\n https://images.app.goo.gl/iu7gQQSxDMF3DNmu5  ")
@client.command()
def miku(data):
    data.subClient.send_message(data.chatId,message="[ci]Aqui tienes <3\n[ci]nhttps://images.app.goo.gl/ssL6fncCoe8QWePC6")
@client.command()
def music_sempai(data):
    data.subClient.send_message(data.chatId,message="[ci]Aqui tienes lindura >.<\n[ci]https://youtu.be/nGeubO1-ryU")
@client.command()
def sdlg (data):
	data.subClient.send_message(data.chatId,message="[ci]calla gordo teton")
@client.command()
def estetica(data):
	data.subClient.send_message(data.chatId,message="[ci]https://aminoapps.com/u/lobito_anoimo22\n[ci] Esta persona hizo la estetica 🎀 ")
@client.command()
def pro(data):
    data.subClient.send_message(data.chatId, message="[ci]que pro ")
  #
 #wihack
 #
 
@client.command()
def wihack (data):
    data.subClient.send_message(data.chatId, message="[ci]Eh creado una wiki pero de Hacking, te muestro los que tengo por ahora \n[ci]Grupos de Hacking\n~wihack_shadow ~wihack_fancy_bear\n~wihack_lazarus_group\n~wihack_lizard_squad\n~wihack_anonymous\n~wihack_cozy_bear\n~wihack_bureau_121\n~wihack_unidad_8200\n~wihack_lulz_security\n~wihack_chaos_computer_club\n~wihack_honker_union\n~wihack_hacking_team\n~wihack_tailored_acces_operation\n~wihack_nso_group\n~wihack_ejercito_cibernetico_irani\n[ci]Sistemas operativos\n~wihack_gnu/linux\n~wihack_debian\n~wihack_ubuntu\n~wihack_arch\n~wihack_deepin\n~wihack_gentoo\n[ci]cibercrimen\n~wihack_ciberataque\n~wihack_pirateria\n~wihack_ddos\n~wihack_malware\n~wihack_pishing\n~wihack_ataque_sql")
@client.answer("~wihack_ataque_sql")
def hello(data):
    data.subClient.send_message(dats.chatId,message="Inyección SQL es un método de infiltración de código intruso que se vale de una vulnerabilidad informática presente en una aplicación en el nivel de validación de las entradas para realizar operaciones sobre una base de datos. ")
@client.answer("~wihack_pishing")
def hello(data):
    data.subClient.send_message(data.chatId,message="Phishing es el delito de engañar a las personas para que compartan información confidencial como contraseñas y números de tarjetas de crédito. Como ocurre en la pesca, existe más de una forma de atrapar a una víctima, pero hay una táctica de phishing que es la más común")
@client.answer("~wihack_malware")
def hello(data):
    data.subClient.send_message(data.chatId,message="Malware o “software malicioso” es un término amplio que describe cualquier programa o código malicioso que es dañino para los sistemas.")
@client.answer("~wihack_ddos")
def hello(data):
    data.subClient.send_message(data.chatId,message="En seguridad informática, un ataque de denegación de servicio, llamado también ataque DoS, es un ataque a un sistema de computadoras o red que causa que un servicio o recurso sea inaccesible a los usuarios legítimos")
@client.answer("~wihack_ciberataque")
def hello(data):
    data.subClient.send_message(data.chatId,message="En computadora y redes de computadoras un ataque es un intento de exponer, alterar, desestabilizar, destruir, eliminar para obtener acceso sin autorización o utilizar un activo.")
@client.answer("~wihack_gentoo")
def hello(data):
    data.subClient.send_message(data.chatId,message="Gentoo Linux es una distribución GNU/Linux basada en paquetes fuente orientada a usuarios avanzados con experiencia en sistemas operativos. Fue fundada por Daniel Robbins, basada en la inactiva distribución llamada Enoch Linux. En el año 2002, esta última pasó a denominarse Gentoo Linux. ")
@client.answer("~wihack_deepin")
def hello(data):
    data.subClient.send_message(data.chatId,message="Deepin es un sistema operativo de software libre y código abierto. Es una distribución de Linux basada en Debian. Se ejecuta en computadores personales, servidores y máquinas virtuales, en arquitecturas x86-64 y ARM")
@client.answer("~wihack_arch")
def hello(data):
    data.subClient.send_mesaage(data.chatId,message="Arch Linux ​ es una distribución Linux para computadoras x86-64​, arquitecturas ARM y I686 orientada a usuarios avanzados. Se compone en su mayor parte de software libre y de código abierto​ y apoya la participación comunitaria.")
@client.answer("~wihack_ububtu")
def hello(data):
    data.subClient.send_message(data.chatId,message="Ubuntu es un sistema operativo de software libre y código abierto. Es una distribución de Linux basada en Debian. Puede correr en computadores de escritorio y servidores. Está orientado al usuario promedio, con un fuerte enfoque en la facilidad de uso y en mejorar la experiencia del usuario.")
@client.answer("~wihack_debian")
def hello(data):
    data.subClient.send_message(data.chatId,message="Debian GNU/Linux es un sistema operativo libre, desarrollado por miles de voluntarios de todo el mundo, que colaboran a través de Internet")
@client.answer("~wihack_gnu/linux")
def hello(data):
    data.subClient.send_message(data.chatId,message="Linux es el nombre que reciben una serie de sistemas operativos de tipo Unix bajo la licencia GNU GPL (General Public License o Licencia Pública General de GNU) que son su mayoría gratuitos y con todo lo necesario para hacer funcionar un PC, con la peculiaridad de que podemos instalar un sistema muy ligero ")
@client.answer("~wihack_pirateria")
def hello(data):
    data.subClient.send_message(data.chatId,message="El término hacker, ​ hispanizado como jáquer, ​ tiene diferentes significados.​ Según el diccionario los hackers, ​ «es todo individuo que se dedica a programar de forma entusiasta, o sea un experto entusiasta de cualquier tipo», ​ que considera que poner la información al alcance de todos constituye un extraordinario")
@client.answer("~wihack_ejercito_cibernetico_irani")
def hello(data):
    data.subClient.send_message(data.chatId,message="El Ejército Cibernético Iraní es un grupo de hackers informáticos iraníes. Se cree que está conectado al gobierno iraní, aunque no está oficialmente reconocido como una entidad por el gobierno.​ Ha prometido lealtad al Líder Supremo de Irán")
@client.answer("~wihack_nso_group")
def hello(data):
    data.subClient.send_message(data.chatId,message="NSO Group Technologies es una empresa tecnológica israelí dedicada a la creación de software de intrusión y vigilancia fundada en 2010 por Niv Carmi, Omri Lavie y Shalev Hulio.")
@client.answer("~wihack_tailored_acces_operation")
def hello(data):
    data.subClient.send_message(data.chatId,message="La Oficina de Tailored Access Operations es un centro de recopilación de información, relacionada con la ciberguerra, de la Agencia de Seguridad Nacional. Ha estado en funcionamiento aproximadamente desde el año 1998.​​")
@client.answer("~wihack_hacking_team")
def hello(data):
    data.subClient.send_message(data.chatId,message="Hacking Team es una compañía de tecnología de la información italiana, ubicada en Milán, que vende herramientas de vigilancia e intrusión ofensiva a gobiernos, agencias de aplicación de la ley y empresas.​")
@client.answer("~wihack_honker_union")
def hello(data):
    data.subClient.send_message(data.chatId,message='Honker o hacker rojo es un grupo conocido por el hacktivismo, principalmente presente en China. Literalmente, el nombre significa "Invitado rojo", en comparación con la transliteración china habitual de piratas informáticos')
@client.answer("~wihack_chaos_computer_club")
def hello (data):
    data.subClient.send_message(data.chatId,message="El Club de Computación Caos es la mayor asociación de hackers de Europa.​ El CCC tiene su sede en Alemania y otros países de habla alemana. Los distintos temas de interés del Club de Computación Caos según su página web son: Hacking Ciencia Sociología Cultura Comunidad")
@client.answer("~wihack_lulz_security")
def hello(data):
    data.subClient.send_message(data.chatId,message=' Lulz Security fue un grupo hacker black hat.​ Su lema es Laughing at your security since 2011!. Algunos alegan, que los fundadores fueron Lauren Ludosky y Emmanuel Lzodkasky. Por eso "Lulz"')
@client.answer("~wihack_unidad_8200")
def hello(data):
    data.subClient.send_message(data.chatId,message="La Unidad 8200 es una unidad perteneciente a los Cuerpos de Inteligencia de las Fuerzas de Defensa de Israel cuya misión es la captación de señales de inteligencia y descifrado de códigos")
@client.answer("~wihack_bureau_121")
def hello(data):
    data.subClient.send_message(data.chatId,message="  Bureau 121 es una agencia de guerra cibernética de Corea del Norte, que forma parte de la Oficina General de Reconocimiento de las fuerzas armadas de Corea del Norte.\n\nSegún las autoridades estadounidenses, el RGB gestiona operaciones clandestinas y tiene seis oficinas\n\nSe cree que las operaciones cibernéticas son rentables forma de que Corea del Norte mantenga una opción militar asimétrica, así como un medio para reunir inteligencia; sus principales objetivos de inteligencia son Corea del Sur, Japón y Estados Unidos. Bureau 121 fue creado en 1998")
@client.answer("~wihack_cozy_bear")
def hello(data):
    data.subClient.send_message(data.chatId,message="Cozy Bear, es un grupo de hackers rusos que se cree asociado con la inteligencia rusa, en especial con el Servicio de Inteligencia Exterior y/o con el Servicio Federal de Seguridad.​​ Su presentación al público fue realizada por FireEye")
@client.answer("~wihack_anonymous")
def hello(data):
    data.subClient.send_message(data.chatId,message=" Anonymous es un pseudonimo utilizado mundialmente por diferentes grupos e individuos para realizar en su nombre —poniéndose de acuerdo con otros— acciones o publicaciones individuales o concertadas. Surgidos del imageboard 4chan y del foro Hackers; en un comienzo como un movimiento por diversión")
@client.answer("~wihack_lizard_squad")
def hello(data):
    data.subClient.send_message(data.chatId,message="  Lizard Squad, en español Escuadrón Lagarto, es un grupo de unos 25 hackers que captó la atención internacionalmente por una serie de ataques a distintas grandes empresas como Sony, Microsoft y a regímenes como Corea del Norte.​​Considerados black fedora crackers")
@client.answer("~wihack_fancy_bear")
def hello(data):
    data.subClient.send_message(data.chatId,message="Fancy Bear, es un grupo de hackers vinculados a Rusia.​ Se cree que está asociado con la inteligencia rusa, en especial con el GRU")
@client.answer("~wihack_shadow_brokers")
def hello(data):
     data.subClient.send_message(data.chatId,message="The Shadow Brokers es un grupo de piratas informáticos que apareció por primera vez en el verano de 2016")

@client.answer("~wihack_lazarus_group")
def hello (data):
     data.subClient.send_message(data.chatId,message="[ci]Lazarus Group es un grupo de ciberdelincuentes compuesto por un número desconocido de individuos. Aunque no se sabe mucho sobre el grupo, los investigadores les han atribuido muchos ciberataques durante la última década.")
 	

    
@client.answer("sexo")
def hello(data):
    data.subClient.send_message(data.chatId, message="sexo?, oh sexo gay, eh tenido tanto sexo gay >.<")
     
 	
@client.answer("Tashi que eres?")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Soy una chica soy un chico, nadie lo sabe, mi unico deber es confundir a las personas sexualemente <3")

@client.answer("¿Tashi?")
def hello(data):
    data.subClient.send_message(data.chatId, message='[ci]Aqui estoy!\n\npon "-ayuda" para usarme 🎀')
  
@client.answer("Tashi zorra")
def hello(data):
    data.subClient.send_message(data.chatId, message="Obvio que lo soy mi amor >.<")
    
@client.answer("Bot inutil")
def hello(data):
    data.subClient.send_message(data.chatId, message="Inutil tu puta madre >:c")
    




@client.answer("Hola Tashi")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Holi <3")

    
@client.answer("Como estas Tashi?")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Bien y tu? 🎀")
   
   
@client.on_member_join_chat() 
def say_hello(data): 
    data.subClient.send_message(data.chatId, f"[ci]✴✴✴✴✴✴✴✴✴✴✴✴✴\n[ci]Bienvenido \n[ci]nuevo usuario\n[ci]lee las reglas <3\n[ci]✴✴✴✴✴✴✴✴✴✴✴✴✴\n[ci]㊗{data.author}㊗")
    
@client.on_member_leave_chat()
def despedida(data):
    data.subClient.send_message(data.chatId,message="[ci]Oh, ojala se vaya bien en tu camino y esperamos volverte a ver <3..")
 
def test(data):
    return data.authorId == ["your_user_id"]

       
@client.answer("Mal Tashi")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Oww, toma este video de un gatito para alegrarte <3\n[ci]https://youtu.be/SZ58jz6m3KU")
    
@client.answer("Bien Tashi")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Me alegro <3")    
    

@client.answer("Bien Tashi")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Me alegro <3")    
    
@client.answer("zzz")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Callate, ya no me digan zzz yo solo queria ser como mi idiolo el pana cebolleta 😿")      
    
@client.answer("Te amo Tashi")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Oww, que tiern@; pero lo siento no me gustan los virgos :c")    
    

@client.answer("Puta Tashi")
def hello(data):
    data.subClient.send_message(data.chatId, message="[ci]Si soy puta, gracias por decirlo 😽💅")    
    


@client.command()
def nia(data):
    data.subClient.send_message(data.chatId, message="[ci]Nya 👉👈")
	
@client.command()
def uwu(data):
	data.subClient.send_message(data.chatId,message="[ci]Vuelves a decir UwU y te cojo 😾")
	
@client.command()
def chiste1 (data):
	data.subClient.send_message(data.chatId, message="[ci]Suena el telefonillo de una casa:- ¿Quién es?- ¿Puede bajar Juanito a jugar al baloncesto?- Pero que crueles sois, sabéis que no tiene ni brazos ni piernas.- Si, pero bota muy bien.")
	
@client.command()
def chiste2(data):
	data.subClient.send_message(data.chatId,message= "[ci]-¿Qué haces con gorra, camiseta de los Lakers y collares de oro? ¡Es el velatorio de tu madre!  \n[ci]-¿No había que venir de negro? ")

@client.command()
def chiste3 (data):
    data.subClient.send_message(data.chatId,message="Un negro en la nieve es el blanco perfecto")
@client.command()
def chiste4(data):
    data.subClient.send_message(data.chatId,message="\n-Papa papa, que es el humor negro?\n-Ves ese chico sin piernas ni brazos?\n-Pero papa soy ciego\nExacto...")

@client.command()
def chiste5(data):
    data.subClient.send_message(data.chatId,message="\n-comunista: joder el puto comunista de mierda no saca su cabeza para volarsela \n-Francés: si el hombre estaba descubriendo la leche que cojones estaba haciendole a la vaca")
    
@client.command()
def chiste6 (data):
    data.subClient.send_message(data.chatId,message=" ¿Cuál es la parte más blanca de un negro?\nSu dueño")
@client.command()
def user(data):
    data.subClient.get_user_id(name_or_id)

print = ("Comandos de comunidad listos")        
@client.command()
def join(data):
    data.subClient.join_all_chat()



@client.command()
def irse(data):
    data.subClient.leave_all_chats()
    
@client.command()
def elfa (data):
	data.subClient.send_message(data.chatId,message="[ci]🚨Atencion, Atencion, Grasoso detectado, repito Grasoso detectado🚨")
@client.command()
def ichinizan(data):
	data.subClient.send_message(data.chatId,message= " [ci]Nya Ichi ni san nya arigato 😼")
@client.command()
def oniichan(data):
	data.subClient.send_message(data.chatId,message=" [ci]Onii Chan! 👉👈")

@client.command()
def sempai(data):
	data.subClient.send_message(data.chatId,message="[ci]Sempai! 🎀")
	
@client.command()
def inutil(data):
	data.subClient.send_message(data.chatId,message="Dejame, hago lo que puedo :c")	
		
@client.command()
def angry(data):
	data.subClient.send_message(data.chatId,message="[ci] (╯°□°)╯︵ ┻━┻")

client.launch()
