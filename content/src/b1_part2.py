# B1 · Parte 2 (unidades 47–52)

unit("u47-phrasal", "B1", "Phrasal verbs del día a día", "🧩",
     "Ya entiendo y uso los phrasal verbs más comunes",
     "Verbos de dos partes (get up, look for, turn on) que los nativos usan todo el tiempo.",
     grammar=["Phrasal verbs separables e inseparables"],
     items="""
get up | levantarse | 🛏️
get on | subirse (bus, tren) / llevarse bien | 🚌
get along with | llevarse bien con | 🤝
get back | volver / regresar | 🔙
get over | superar (algo malo) | 🌈
get rid of | deshacerse de | 🗑️
look for | buscar | 🔍
look after | cuidar | 🍼
look forward to | esperar con ganas | 🤩
look up | buscar (información) | 📖
look out! | ¡cuidado! | ⚠️
find out | averiguar / descubrir | 🕵️
figure out | entender / resolver | 🧠
turn up | subir (volumen) / aparecer | 🔊
turn down | bajar (volumen) / rechazar | 🔉
put on | ponerse (ropa) | 🧥
take off | quitarse (ropa) / despegar | ✈️
put away | guardar | 📥
throw away | botar | 🗑️
pick up | recoger / contestar el teléfono | 📞
come back | volver | ↩️
come in | entrar / pasar | 🚪
go out | salir (de rumba, a la calle) | 🌃
go on | continuar | ▶️
carry on | seguir / continuar | ⏩
run out of | quedarse sin | 🪫
set up | montar / configurar | 🛠️
fill in | llenar (formulario) | 📝
check out | revisar / mirar / salir del hotel | 👀
sort out | arreglar / resolver | 🧹
work out | hacer ejercicio / salir bien | 🏋️
hang out | pasar el rato | 🛹
hang up | colgar (teléfono) | 📵
call back | devolver la llamada | 📲
show up | aparecer / llegar | 🙋
break down | dañarse (máquina) | 🚗💥
calm down (B1) | calmarse
cheer up (B1) | animarse
grow up | crecer (una persona) | 🧒➡️🧑
bring up | criar / sacar un tema | 👪
make up | inventar / reconciliarse | 🎭
give back | devolver | 🎁
take care of | encargarse de / cuidar | 💚
wake up (B1) | despertarse
slow down | ir más despacio | 🐢
speed up | acelerar | 🏎️
hold on | esperar un momento | ✋
watch out | tener cuidado | 👀
try on | probarse (ropa) | 🪞
eat out | comer afuera | 🍽️
stay in | quedarse en casa | 🏠
end up | terminar (en un lugar/situación) | 🏁
come up with | ocurrírsele (una idea) | 💡
put off | aplazar | 📅
""",
     extras=[
         D("Qué es un phrasal verb",
           "Mira cómo una partícula cambia el significado del verbo.",
           """
Look at the photo. || Mira la foto. || Look at
I'm looking for my keys. || Estoy buscando mis llaves. || looking for
Can you look after my dog? || ¿Me cuidas el perro? || look after
I'm looking forward to the trip. || Espero con ganas el viaje. || looking forward to
Look up the word in the dictionary. || Busca la palabra en el diccionario. || Look up
""",
           "¿Qué pasa con el significado de look?",
           ["Siempre significa 'mirar'", "Cambia según la partícula (for, after, up)"], 1,
           "Un PHRASAL VERB es verbo + partícula (up, on, for…) y su significado suele ser distinto al del verbo solo. No se traducen palabra por palabra: apréndelos como vocabulario nuevo. Muchos se pueden separar con un pronombre: Turn it off (no 'turn off it').",
           """
It's cold. Put on your jacket. / Put it on. || Hace frío. Ponte la chaqueta. / Póntela.
""",
           fills="""
I need to ___ my glasses. I can't find them. | look for / look after | 0 | Necesito buscar mis gafas. No las encuentro.
Please ___ the TV. I want to sleep. | turn off / turn on | 0 | Por favor apaga el televisor. Quiero dormir.
We ran ___ milk. Can you buy some? | out of / out | 0 | Se nos acabó la leche. ¿Puedes comprar?
I get ___ well with my brother. | along / over | 0 | Me llevo bien con mi hermano.
The music is too loud. Turn it ___. | down / up | 0 | La música está muy duro. Bájale.
"""),
         dialogue("Una mañana caótica", "⏰ Hablas con tu compañero de apartamento.", """
Sam: Hurry up! We're late. Did you get up late again? || ¡Apúrate! Vamos tarde. ¿Te levantaste tarde otra vez?
Leo: Yes. And I'm looking for my phone. I can't find it. || Sí. Y estoy buscando mi celular. No lo encuentro.
Sam: Hold on, I'll call it. Listen… it's under the sofa. || Espera, lo llamo. Escucha… está debajo del sofá.
Leo: Thanks! Oh no, we've run out of coffee. || ¡Gracias! Ay no, se nos acabó el café.
Sam: We can pick some up on the way. Put on your jacket and let's go! || Podemos comprar en el camino. ¡Ponte la chaqueta y vámonos!
"""),
         story("El carro que se dañó", "🚗", """
Last Sunday Felipe and his girlfriend set off early for a trip to the coast. || El domingo pasado Felipe y su novia salieron temprano para un viaje a la costa.
They were looking forward to a relaxing weekend. || Estaban esperando con ganas un fin de semana relajante.
After two hours the car broke down in the middle of nowhere. || Después de dos horas el carro se dañó en la mitad de la nada.
Felipe tried to figure out the problem, but he couldn't. They had also run out of water. || Felipe intentó entender el problema, pero no pudo. Además se les había acabado el agua.
Finally a farmer showed up with his truck and helped them. || Por fin apareció un campesino con su camioneta y los ayudó.
They ended up spending the night at the farmer's house. It turned out to be the best part of the trip! || Terminaron pasando la noche en la casa del campesino. ¡Resultó ser la mejor parte del viaje!
""", questions=[
             ("¿Qué pasó después de dos horas?", ["Llovió", "Se dañó el carro", "Llegaron a la costa"], 1),
             ("¿De qué se habían quedado sin?", ["Gasolina", "Agua", "Dinero"], 1),
             ("¿Dónde pasaron la noche?", ["En un hotel", "En la casa del campesino", "En el carro"], 1),
         ]),
         roleplay("Cuidar la casa de un vecino", "🏡 Tu vecina se va de viaje y te pide favores.", """
Neighbor: Could you look after my cat this weekend? || ¿Me podrías cuidar el gato este fin de semana?
+ Sure, no problem. When are you coming back? || Claro, no hay problema. ¿Cuándo vuelves?
- Sure. When are you looking for back? || Claro. ¿Cuándo estás buscando atrás? || Se dice "When are you coming back?".
Neighbor: On Monday. Please pick up my mail too. || El lunes. Por favor recoge mi correo también.
+ OK. Should I turn on the lights at night? || Bueno. ¿Prendo las luces en la noche?
- OK. Should I throw away your cat? || Bueno. ¿Boto tu gato? || ¡Para nada!
Neighbor: Yes, please. And if there's a problem, call me and I'll call you back. || Sí, por favor. Y si hay algún problema, llámame y te devuelvo la llamada.
+ Don't worry. Have a great trip! || Tranquila. ¡Que tengas un muy buen viaje!
- Hang up, please. || Cuelga, por favor. || No tiene sentido aquí.
"""),
     ],
     writes="""
Estoy buscando mis llaves. | I'm looking for my keys. | I am looking for my keys.
Ponte la chaqueta. | Put on your jacket. | Put your jacket on.
Se nos acabó la leche. | We've run out of milk. | We ran out of milk. ; We have run out of milk.
""",
     dictations="""
I'm really looking forward to the weekend. || De verdad espero con ganas el fin de semana.
Can you turn the music down, please? || ¿Puedes bajarle a la música, por favor?
""")

unit("u48-reglas", "B1", "Reglas y obligaciones", "📋",
     "Ya puedo explicar reglas, prohibiciones y lo que está permitido",
     "must, mustn't, have to, don't have to, can, be allowed to para normas y señales.",
     grammar=["Must / mustn't", "be allowed to", "Diferencia mustn't vs don't have to"],
     items="""
must | deber (obligación fuerte) | ❗ | mast
mustn't | no deber (prohibido) | ⛔ | má-sent
be allowed to | tener permiso de / estar permitido | ✅ | a-láud
not allowed | no permitido | 🚫
permission | permiso | 📝 | per-mí-shon
forbidden | prohibido | 🚷 | for-bí-den
compulsory | obligatorio | 📌 | kom-pál-so-ri
optional | opcional | 🔘 | óp-sho-nal
law | ley | ⚖️ | lo
rule (B1) | regla
sign | señal / letrero | 🪧 | sáin
fine | multa | 💸 | fáin
ticket (fine) | multa / comparendo | 🎫
seat belt | cinturón de seguridad | 🦺
helmet | casco | ⛑️ | jél-met
speed limit | límite de velocidad | 🚸
parking | parqueadero / estacionar | 🅿️ | pár-king
no smoking | prohibido fumar | 🚭
wear a uniform | usar uniforme | 👔
keep quiet | guardar silencio | 🤫
switch off your phone | apagar el celular | 📴
show your ID | mostrar tu documento | 🪪
respect | respetar / respeto | 🙇 | ris-pékt
obey | obedecer | 👮 | o-béi
break the rules | romper las reglas | 💥
follow the rules | seguir las reglas | ✅
punish | castigar | ⚖️ | pá-nish
punishment | castigo | 🔒 | pá-nish-ment
behave | comportarse | 😇 | bi-jéiv
manners | modales | 🎩 | má-ners
polite | educado / cortés | 🙏 | po-láit
rude | grosero | 😤 | ruud
dress code (B1) | código de vestimenta
safety | seguridad | 🛡️ | séif-ti
security | seguridad (vigilancia) | 🔐 | se-kiú-ri-ti
guard | guardia / vigilante | 💂 | gard
visitor | visitante | 🧳 | ví-si-tor
entrance | entrada | 🚪 | én-trans
exit | salida | 🚪 | ék-sit
emergency exit | salida de emergencia | 🚨
no entry | no hay paso / prohibido entrar | ⛔
staff only | solo personal autorizado | 🧑‍💼
keep off the grass | no pisar el césped | 🌱
do not disturb | no molestar | 🚫
under 18 | menores de 18 | 🔞
pets | mascotas | 🐾 | pets
take photos (B1) | tomar fotos
touch | tocar | 👆 | tach
feed the animals | alimentar a los animales | 🐒
You must wear a helmet | Debes usar casco | ⛑️
You mustn't park here | No puedes estacionar aquí | 🚫
Are we allowed to take photos? | ¿Se pueden tomar fotos? | 📷
You don't have to pay | No tienes que pagar | 🆓
""",
     extras=[
         D("must, mustn't y don't have to",
           "Lee estas normas. Fíjate bien en las dos negativas.",
           """
You must wear a seat belt. || Debes usar el cinturón de seguridad. || must
Passengers must show their ID. || Los pasajeros deben mostrar su documento. || must
You mustn't smoke here. || No puedes fumar aquí (está prohibido). || mustn't
You don't have to pay. It's free. || No tienes que pagar. Es gratis. || don't have to
We're not allowed to use phones in class. || No se nos permite usar el celular en clase. || not allowed to
""",
           "¿Qué significa You mustn't touch?",
           ["No es necesario que toques", "Está prohibido tocar"], 1,
           "must = obligación fuerte (reglas, leyes). mustn't = PROHIBIDO. don't have to = NO es necesario (puedes si quieres). Son muy distintos: You mustn't come = no puedes venir; You don't have to come = no tienes que venir. be allowed to = tener permiso.",
           """
At the museum you mustn't touch the paintings, but you don't have to pay on Sundays. || En el museo no puedes tocar las pinturas, pero no tienes que pagar los domingos.
""",
           fills="""
You ___ drive faster than 60 here. It's the law. | mustn't / don't have to | 0 | No puedes manejar a más de 60 aquí. Es la ley.
You ___ bring food. Lunch is included. | don't have to / mustn't | 0 | No tienes que traer comida. El almuerzo está incluido.
All visitors ___ wear a helmet in the factory. | must / mustn't | 0 | Todos los visitantes deben usar casco en la fábrica.
Are we ___ to take photos? | allowed / allow | 0 | ¿Se nos permite tomar fotos?
"""),
         dialogue("Primer día en la fábrica", "🏭 Un supervisor te explica las reglas.", """
Supervisor: Welcome! First, the safety rules. You must wear a helmet at all times. || ¡Bienvenido! Primero, las reglas de seguridad. Debe usar casco todo el tiempo.
You: OK. Am I allowed to use my phone? || Bueno. ¿Puedo usar el celular?
Supervisor: Only during breaks. You mustn't use it near the machines. || Solo en los descansos. No puede usarlo cerca de las máquinas.
You: Do I have to wear a uniform? || ¿Tengo que usar uniforme?
Supervisor: Yes, but you don't have to buy it. The company gives it to you. || Sí, pero no tiene que comprarlo. La empresa se lo da.
You: Great. And where is the emergency exit? || Perfecto. ¿Y dónde está la salida de emergencia?
"""),
         story("Reglas en otros países", "🌐", """
When you travel, it's important to know the local rules. || Cuando viajas, es importante conocer las reglas locales.
In Singapore you mustn't chew gum on public transport. You can get a fine! || En Singapur no puedes masticar chicle en el transporte público. ¡Te pueden multar!
In Japan you must take off your shoes before you enter a house. || En Japón debes quitarte los zapatos antes de entrar a una casa.
In many European cities you don't have to tip waiters, but it's polite. || En muchas ciudades europeas no tienes que dar propina a los meseros, pero es amable.
In some countries you aren't allowed to take photos of government buildings. || En algunos países no se permite tomar fotos de edificios del gobierno.
Before your next trip, look up the rules. It will save you problems! || Antes de tu próximo viaje, busca las reglas. ¡Te ahorrará problemas!
""", questions=[
             ("¿Qué está prohibido en el transporte de Singapur?", ["Comer", "Masticar chicle", "Hablar"], 1),
             ("¿Qué debes hacer en una casa en Japón?", ["Quitarte los zapatos", "Llevar un regalo", "Hablar bajito"], 0),
             ("¿La propina es obligatoria en muchas ciudades europeas?", ["Sí", "No, pero es amable"], 1),
         ]),
         roleplay("En el museo", "🏛️ Un guardia habla contigo en la entrada.", """
Guard: Good morning. Can I see your ticket? || Buenos días. ¿Puedo ver su boleto?
+ Here you are. Are we allowed to take photos inside? || Aquí tiene. ¿Se permite tomar fotos adentro?
- Here you are. Must I to take photos? || Aquí tiene. ¿Debo a tomar fotos? || Pregunta por permiso: "Are we allowed to…?".
Guard: Yes, but you mustn't use the flash. || Sí, pero no puede usar el flash.
+ OK. Do I have to leave my backpack here? || Bueno. ¿Tengo que dejar mi morral aquí?
- OK. I mustn't leave the museum. || Bueno. No puedo salir del museo. || No tiene sentido.
Guard: Yes, please. And you mustn't touch the paintings. || Sí, por favor. Y no puede tocar las pinturas.
+ Understood. Thank you! || Entendido. ¡Gracias!
- I don't have to touch them? || ¿No tengo que tocarlas? || "Mustn't" es prohibición, no falta de necesidad.
"""),
     ],
     writes="""
Debes usar casco. | You must wear a helmet. | You have to wear a helmet.
No puedes fumar aquí. | You mustn't smoke here. | You must not smoke here. ; You can't smoke here.
No tienes que pagar. | You don't have to pay. | You do not have to pay.
""",
     dictations="""
Are we allowed to take photos? || ¿Se permite tomar fotos?
You mustn't park in front of the entrance. || No puedes estacionar frente a la entrada.
""")

unit("u49-ambiente", "B1", "El medio ambiente", "🌎",
     "Ya puedo hablar de problemas ambientales y soluciones",
     "Contaminación, reciclaje, energía y el cambio climático, con verbos para proponer soluciones.",
     grammar=["Cuantificadores: too much / too many / not enough", "Pasiva sencilla de presente"],
     items="""
environment | medio ambiente | 🌍 | en-vái-ron-ment
climate change | cambio climático | 🌡️
global warming | calentamiento global | 🔥
pollution | contaminación | 🏭 | po-lú-shon
pollute | contaminar | 🛢️ | po-lúut
air pollution | contaminación del aire | 💨
plastic | plástico | 🧴 | plás-tik
garbage | basura | 🗑️ | gár-bich
waste | desperdicio / desperdiciar | 🚮 | uéist
recycle | reciclar | ♻️ | ri-sái-kol
reuse | reutilizar | 🔁 | ri-iús
reduce | reducir | ⬇️ | ri-diús
save energy | ahorrar energía | 💡
renewable energy | energía renovable | 🔋
solar panel | panel solar | ☀️
wind turbine | turbina eólica | 🌬️
fossil fuels | combustibles fósiles | ⛽
oil (fuel) | petróleo | 🛢️
coal | carbón | ⚫ | kóul
gas | gas | 🔥
carbon dioxide | dióxido de carbono | 💨
greenhouse effect | efecto invernadero | 🏠
temperature | temperatura | 🌡️ | tém-pe-ra-cher
drought | sequía | 🏜️ | dráut
flood | inundación | 🌊 | flad
wildfire | incendio forestal | 🔥 | uáild-faier
deforestation | deforestación | 🪓 | di-fo-res-téi-shon
cut down trees | talar árboles | 🌳
species | especies | 🐾 | spíi-shiis
extinct | extinto | 🦣 | eks-tínkt
protect | proteger | 🛡️ | pro-tékt
nature reserve | reserva natural | 🏞️
natural resources | recursos naturales | 💧
damage | daño / dañar | 💥 | dá-mich
destroy | destruir | 🏚️ | dis-trói
harm | dañar / daño | ⚠️ | jarm
harmful | dañino | ☠️ | járm-ful
eco-friendly | ecológico | 🌿 | íi-kou-frend-li
organic | orgánico | 🥬 | or-gá-nik
public transport | transporte público | 🚌
carpool | compartir carro | 🚗👥
reusable bag | bolsa reutilizable | 🛍️
single-use | de un solo uso | 🥤
compost | compost / abono | 🪱 | kóm-post
volunteer | voluntario | 🙋 | vo-lun-tíer
campaign | campaña | 📣 | kam-péin | La g no suena.
government | gobierno | 🏛️ | gá-vern-ment
take action | actuar / tomar medidas | ✊
make a difference | marcar la diferencia | ✨
too much plastic | demasiado plástico | 🧴
too many cars | demasiados carros | 🚗🚗
not enough trees | no hay suficientes árboles | 🌳
""",
     extras=[
         D("too much, too many, not enough",
           "Mira qué palabra va con cosas que se cuentan y cuáles no.",
           """
There's too much pollution in big cities. || Hay demasiada contaminación en las ciudades grandes. || too much
We use too much plastic. || Usamos demasiado plástico. || too much
There are too many cars on the roads. || Hay demasiados carros en las calles. || too many
There aren't enough trees in my neighborhood. || No hay suficientes árboles en mi barrio. || enough
We don't recycle enough. || No reciclamos lo suficiente. || enough
""",
           "¿Cuál va con sustantivos contables (cars, bottles)?",
           ["too much", "too many"], 1,
           "too much + incontable (pollution, plastic, water). too many + contable plural (cars, bottles, people). not enough = no suficiente, con los dos. Y para procesos y hechos se usa mucho la voz pasiva: Plastic is recycled (el plástico se recicla).",
           """
Millions of trees are cut down every year. || Se talan millones de árboles cada año.
""",
           fills="""
There's ___ garbage on the beach. | too much / too many | 0 | Hay demasiada basura en la playa.
There are ___ plastic bottles in the ocean. | too many / too much | 0 | Hay demasiadas botellas plásticas en el océano.
We don't have ___ clean water. | enough / too | 0 | No tenemos suficiente agua limpia.
Paper ___ recycled in this factory. | is / does | 0 | El papel se recicla en esta fábrica.
"""),
         dialogue("Una campaña en la universidad", "♻️ Dos estudiantes organizan una campaña.", """
Ana: We should do something. There's too much plastic in the cafeteria. || Deberíamos hacer algo. Hay demasiado plástico en la cafetería.
Leo: I agree. Most of it is single-use. || De acuerdo. La mayoría es de un solo uso.
Ana: What if we start a campaign? We could ask students to bring reusable cups. || ¿Y si empezamos una campaña? Podríamos pedirles a los estudiantes que traigan vasos reutilizables.
Leo: Great idea. And we can put recycling bins in every building. || Excelente idea. Y podemos poner canecas de reciclaje en cada edificio.
Ana: We'll need volunteers. || Vamos a necesitar voluntarios.
Leo: Let's make posters this weekend. Small actions can make a difference! || Hagamos carteles este fin de semana. ¡Las pequeñas acciones pueden marcar la diferencia!
"""),
         story("El páramo que nos da agua", "💧", """
Near many Colombian cities there are páramos, unique high mountain ecosystems. || Cerca de muchas ciudades colombianas hay páramos, ecosistemas únicos de alta montaña.
They work like sponges: they collect water from the clouds and release it slowly. || Funcionan como esponjas: recogen el agua de las nubes y la sueltan despacio.
Millions of people drink water that comes from páramos. || Millones de personas toman agua que viene de los páramos.
However, they are in danger because of mining, farming and climate change. || Sin embargo, están en peligro por la minería, la agricultura y el cambio climático.
If we destroy them, many cities will suffer droughts in the future. || Si los destruimos, muchas ciudades sufrirán sequías en el futuro.
That's why some páramos are now protected as nature reserves. || Por eso algunos páramos ahora están protegidos como reservas naturales.
""", questions=[
             ("¿Cómo funcionan los páramos?", ["Como esponjas que guardan agua", "Como volcanes", "Como desiertos"], 0),
             ("¿Por qué están en peligro?", ["Por la minería, la agricultura y el cambio climático", "Por el turismo", "Por los animales"], 0),
             ("¿Qué pasará si los destruimos?", ["Habrá más lluvia", "Muchas ciudades sufrirán sequías", "Nada"], 1),
         ]),
         roleplay("Convencer a un amigo", "🚗 Tu amigo va al trabajo solo en carro todos los días.", """
Friend: I drive to work every day. It's faster. || Manejo al trabajo todos los días. Es más rápido.
+ But there are too many cars, and they cause a lot of pollution. || Pero hay demasiados carros, y causan mucha contaminación.
- But there is too much cars. || Pero hay demasiado carros. || Con "cars" (contable) es "too many".
Friend: Maybe, but the bus takes too long. || Tal vez, pero el bus se demora demasiado.
+ What about carpooling with your colleagues? You'll save money too. || ¿Y si compartes carro con tus colegas? También ahorrarás plata.
- You should cut down trees. || Deberías talar árboles. || Es lo contrario de cuidar el ambiente.
Friend: That's not a bad idea. || No es mala idea.
+ Small changes can make a big difference! || ¡Los pequeños cambios pueden marcar una gran diferencia!
- Small changes are harmful. || Los pequeños cambios son dañinos. || No tiene sentido.
"""),
     ],
     writes="""
Hay demasiada contaminación. | There's too much pollution. | There is too much pollution.
Deberíamos reciclar más. | We should recycle more.
No hay suficientes árboles. | There aren't enough trees. | There are not enough trees.
""",
     dictations="""
Climate change is a global problem. || El cambio climático es un problema global.
We use too much single-use plastic. || Usamos demasiado plástico de un solo uso.
""",
     speak="""
In my opinion, we should use more renewable energy. || En mi opinión, deberíamos usar más energía renovable.
""")

unit("u50-estilo-vida", "B1", "Salud y estilo de vida", "🥗",
     "Ya puedo hablar de hábitos saludables y dar consejos detallados",
     "Hábitos, alimentación, ejercicio y bienestar; el gerundio como sujeto y consejos con should / ought to.",
     grammar=["Gerundio como sujeto: Eating well is important", "It's important to…"],
     items="""
lifestyle | estilo de vida | 🧘
habit | hábito | 🔁 | já-bit
healthy habits | hábitos saludables | 🥦
unhealthy | poco saludable | 🍟 | an-jél-zi
diet | dieta / alimentación | 🥗 | dái-et
balanced diet | alimentación balanceada | ⚖️
junk food | comida chatarra | 🍔
fast food (B1) | comida rápida
vegetables | verduras | 🥕 | véch-ta-bols
fruit | fruta | 🍎 | fruut
protein | proteína | 🍗 | próu-tiin
vitamins | vitaminas | 💊 | vái-ta-mins
calories | calorías | 🔢 | ká-lo-ris
fat | grasa / gordo | 🧈 | fat
sugar (B1) | azúcar
portion | porción | 🍽️ | pór-shon
skip meals | saltarse comidas | ⏭️
snack | onces / algo de picar | 🍪 | snak
hydrated | hidratado | 💧 | jái-drei-ted
work out (gym) | entrenar en el gimnasio | 🏋️
gym | gimnasio | 🏟️ | yim
stretch | estirar | 🤸 | strech
muscle | músculo | 💪 | má-sol | La c no suena.
fitness | estado físico | 🏃 | fít-nes
get in shape | ponerse en forma | 🎯
stay fit | mantenerse en forma | ✨
weight | peso | ⚖️ | uéit
lose weight (B1) | bajar de peso
sleep well | dormir bien | 😴
get enough sleep | dormir lo suficiente | 🛌
stress (B1) | estrés | 😫
mental health | salud mental | 🧠
well-being | bienestar | 🌈 | uel-bíi-ing
meditate | meditar | 🧘 | mé-di-teit
breathe | respirar | 🌬️ | bríid
smoke | fumar | 🚬 | smóuk
quit smoking | dejar de fumar | 🚭
alcohol | alcohol | 🍷 | ál-ko-jol
addicted to | adicto a | 🔗 | a-dík-ted
screen time | tiempo frente a pantallas | 📱
sedentary | sedentario | 🛋️ | sé-den-te-ri
active | activo | ⚡ | ák-tiv
energy | energía | 🔋 | é-ner-yi
routine | rutina | 🔁 | ru-tíin
balance | equilibrio | ⚖️ | bá-lans
benefit | beneficio | ✅ | bé-ne-fit
improve your health | mejorar tu salud | 📈
reduce stress | reducir el estrés | 🧘
take the stairs | subir por las escaleras | 🪜
ought to | debería (consejo) | 🫵 | ót tu
It's important to sleep well | Es importante dormir bien | 😴
Eating well is the key | Comer bien es la clave | 🔑
""",
     extras=[
         D("El gerundio como sujeto",
           "Mira cómo empiezan estas frases. En español usamos el infinitivo.",
           """
Eating vegetables is good for you. || Comer verduras es bueno para ti. || Eating
Sleeping eight hours is important. || Dormir ocho horas es importante. || Sleeping
Smoking is very harmful. || Fumar es muy dañino. || Smoking
Walking every day reduces stress. || Caminar todos los días reduce el estrés. || Walking
It's important to drink water. || Es importante tomar agua. || It's important to
""",
           "Cuando una acción es el sujeto de la frase, en inglés se usa…",
           ["El verbo con -ing", "El verbo con to al principio siempre", "El verbo solo"], 0,
           "Cuando una actividad es el sujeto, se usa el GERUNDIO (-ing): Swimming is fun (nadar es divertido). Otra forma muy común: It's + adjetivo + to + verbo: It's important to sleep well. ought to = should (un poco más formal).",
           """
Doing exercise improves your mood. It's a good idea to start slowly. || Hacer ejercicio mejora tu ánimo. Es buena idea empezar despacio.
""",
           fills="""
___ too much sugar is bad for your teeth. | Eating / Eat | 0 | Comer demasiado azúcar es malo para los dientes.
It's important ___ enough sleep. | to get / getting to | 0 | Es importante dormir lo suficiente.
___ is the best way to reduce stress for me. | Running / Run | 0 | Correr es la mejor forma de reducir el estrés para mí.
You ___ to drink more water. | ought / should | 0 | Deberías tomar más agua. | "ought" siempre va con to.
"""),
         dialogue("Con el entrenador", "🏋️ Tu primer día en el gimnasio.", """
Trainer: So, what's your goal? || Entonces, ¿cuál es tu meta?
You: I want to get in shape and have more energy. I'm very sedentary. || Quiero ponerme en forma y tener más energía. Soy muy sedentario.
Trainer: OK. Exercising three times a week is a good start. || Bueno. Hacer ejercicio tres veces por semana es un buen comienzo.
You: What about my diet? || ¿Y mi alimentación?
Trainer: Eating more vegetables and protein will help. And you ought to reduce junk food. || Comer más verduras y proteína ayudará. Y deberías reducir la comida chatarra.
You: That's going to be hard! || ¡Eso va a ser difícil!
Trainer: Don't worry. Changing habits takes time. || Tranquilo. Cambiar hábitos toma tiempo.
"""),
         story("Treinta días sin celular en la noche", "📵", """
Last month Sebastián did an experiment: no screens after nine p.m. for thirty days. || El mes pasado Sebastián hizo un experimento: nada de pantallas después de las nueve de la noche durante treinta días.
He was addicted to his phone. He usually checked social media until one in the morning. || Era adicto al celular. Normalmente revisaba redes sociales hasta la una de la mañana.
The first week was very difficult. He felt bored and anxious. || La primera semana fue muy difícil. Se sentía aburrido y ansioso.
Then he started reading books and meditating before bed. || Luego empezó a leer libros y a meditar antes de dormir.
After two weeks he was sleeping better and he had more energy in the morning. || Después de dos semanas dormía mejor y tenía más energía en la mañana.
"Reducing screen time changed my life," he says. "My mental health is much better." || "Reducir el tiempo de pantalla me cambió la vida", dice. "Mi salud mental está mucho mejor."
""", questions=[
             ("¿Cuál fue el experimento?", ["No comer azúcar", "No usar pantallas después de las 9 p. m.", "Correr todos los días"], 1),
             ("¿Cómo fue la primera semana?", ["Fácil", "Muy difícil", "Aburrida pero fácil"], 1),
             ("¿Qué mejoró?", ["Su sueño y su energía", "Su salario", "Su inglés"], 0),
         ]),
         roleplay("Aconsejar a tu hermano", "😩 Tu hermano siempre está cansado.", """
Brother: I'm always tired. I don't know why. || Siempre estoy cansado. No sé por qué.
+ How many hours do you sleep? || ¿Cuántas horas duermes?
- How many hours do you sleeping? || ¿Cuántas horas tú durmiendo? || Se dice "do you sleep".
Brother: About five. I play video games until late. || Como cinco. Juego videojuegos hasta tarde.
+ That's not enough. Getting eight hours of sleep is really important. || No es suficiente. Dormir ocho horas es muy importante.
- Get eight hours is important. || Dormir ocho horas es importante. || Como sujeto va el gerundio: "Getting".
Brother: And I skip breakfast. || Y me salto el desayuno.
+ You ought to eat breakfast. It gives you energy for the day. || Deberías desayunar. Te da energía para el día.
- You ought eat junk food. || Deberías comer comida chatarra. || Mal consejo y falta "to".
"""),
     ],
     writes="""
Comer verduras es bueno para la salud. | Eating vegetables is good for your health. | Eating vegetables is good for you. ; Eating vegetables is healthy.
Es importante dormir bien. | It's important to sleep well. | It is important to sleep well.
Quiero ponerme en forma. | I want to get in shape. | I want to get fit.
""",
     dictations="""
Smoking is very harmful to your health. || Fumar es muy dañino para la salud.
You ought to reduce your screen time. || Deberías reducir tu tiempo frente a pantallas.
""")

unit("u51-cultura", "B1", "Viajes y cultura", "🗺️",
     "Ya puedo hablar de viajes, costumbres y diferencias culturales",
     "Experiencias de viaje, costumbres de otros países y comparar culturas con respeto.",
     grammar=["used to (introducción)", "Comparar culturas: similar to, different from"],
     items="""
culture | cultura | 🎎 | kál-cher
custom | costumbre | 🪅 | kás-tom
tradition (B1) | tradición
belief | creencia | 🙏 | bi-líif
religion | religión | ⛪ | ri-lí-yon
language | idioma | 🗣️ | lán-güich
accent | acento | 👄 | ák-sent
local | local / del lugar | 📍 | lóu-kal
foreigner | extranjero (persona) | 🧳 | fó-re-ner
destination | destino | 📌 | des-ti-néi-shon
sightseeing | turismo (ver lugares) | 🏛️ | sáit-sii-ing
landmark | lugar emblemático | 🗽 | lánd-mark
monument | monumento | 🗿 | mó-niu-ment
cathedral | catedral | ⛪ | ka-zíi-dral
castle | castillo | 🏰 | ká-sol | La t no suena.
ruins | ruinas | 🏛️ | rú-ins
old town | centro histórico | 🏘️
market (B1) | mercado
street food | comida callejera | 🌮
dish | plato (comida) | 🍛 | dish
cuisine | cocina (gastronomía) | 🍽️ | kui-síin
spicy (B1) | picante
backpacking | viajar de mochilero | 🎒 | bák-pa-king
hostel | hostal | 🛏️ | jós-tel
guided tour | visita guiada | 🧑‍🏫
travel agency | agencia de viajes | 🏢
itinerary | itinerario | 🗒️ | ai-tí-ne-ra-ri
jet lag | desfase horario | 😵 | yet lag
culture shock | choque cultural | 😳
get used to (B1) | acostumbrarse a
respect (B1) | respetar
tip (money) | propina | 💵
greet | saludar | 👋 | gríit
bow | hacer una reverencia | 🙇 | báu
shake hands | darse la mano | 🤝
kiss on the cheek | beso en la mejilla | 😘
punctual | puntual | ⏱️ | pánk-chual
crowded (B1) | lleno de gente
welcoming | acogedor / hospitalario | 🤗 | uél-ka-ming
souvenir (B1) | recuerdo
similar to | parecido a | 🟰
different from | diferente de | ≠
the same as | igual que | ⚖️
in common | en común | 🤝
abroad (B1) | en el extranjero
passport control | control de pasaportes | 🛂
visa | visa | 📄 | víi-sa
currency | moneda (de un país) | 💱 | ká-ren-si
exchange rate | tasa de cambio | 📉
it's worth visiting | vale la pena visitarlo | 💯
off the beaten track | fuera de lo turístico | 🛤️
""",
     extras=[
         D("Comparar culturas",
           "Fíjate en la preposición que va con cada expresión.",
           """
Colombian food is different from Mexican food. || La comida colombiana es diferente de la mexicana. || different from
Spanish is similar to Italian. || El español es parecido al italiano. || similar to
The weather in Pasto is the same as in Quito. || El clima de Pasto es igual que el de Quito. || the same as
We have a lot in common. || Tenemos mucho en común. || in common
In Colombia people used to write letters. Now they text. || En Colombia la gente antes escribía cartas. Ahora escribe mensajes. || used to
""",
           "¿Qué preposición va con similar?",
           ["similar to", "similar of", "similar than"], 0,
           "different FROM, similar TO, the same AS, have something IN common. Y used to + verbo = 'antes solía' (algo que ya no pasa): I used to live in Cali. Lo vas a practicar más a fondo en una próxima unidad.",
           """
Is Japanese culture very different from ours? In some ways, yes. || ¿La cultura japonesa es muy diferente de la nuestra? En algunos aspectos, sí.
""",
           fills="""
British English is a little different ___ American English. | from / of | 0 | El inglés británico es un poco diferente del americano.
Portuguese is similar ___ Spanish. | to / as | 0 | El portugués es parecido al español.
My accent is the same ___ my mother's. | as / like to | 0 | Mi acento es igual al de mi mamá.
We don't have anything ___ common. | in / on | 0 | No tenemos nada en común.
"""),
         dialogue("Choque cultural", "🌏 Una amiga volvió de vivir en Japón.", """
You: How was Japan? Did you experience culture shock? || ¿Qué tal Japón? ¿Tuviste choque cultural?
Mia: At first, yes! People are very punctual and quiet on the trains. || ¡Al principio sí! La gente es muy puntual y callada en los trenes.
You: Is the food very different from ours? || ¿La comida es muy diferente de la nuestra?
Mia: Totally. But I got used to it. Now I miss the street food! || Totalmente. Pero me acostumbré. ¡Ahora extraño la comida callejera!
You: Did people greet you with a bow? || ¿La gente te saludaba con una reverencia?
Mia: Yes. They don't usually kiss on the cheek like we do. || Sí. Normalmente no dan beso en la mejilla como nosotros.
"""),
         story("Mochilero por Suramérica", "🎒", """
After finishing university, Tomás went backpacking for six months. || Después de terminar la universidad, Tomás se fue de mochilero seis meses.
He visited ruins in Peru, glaciers in Argentina and markets in Bolivia. || Visitó ruinas en Perú, glaciares en Argentina y mercados en Bolivia.
He stayed in cheap hostels and met travelers from all over the world. || Se quedó en hostales baratos y conoció viajeros de todo el mundo.
His favorite places were off the beaten track: small villages with very welcoming people. || Sus lugares favoritos estaban fuera de lo turístico: pueblos pequeños con gente muy acogedora.
He learned that every country has its own customs, but people everywhere have a lot in common. || Aprendió que cada país tiene sus costumbres, pero la gente en todas partes tiene mucho en común.
"Traveling taught me more than university," he says with a smile. || "Viajar me enseñó más que la universidad", dice con una sonrisa.
""", questions=[
             ("¿Cuánto tiempo viajó Tomás?", ["Un mes", "Seis meses", "Un año"], 1),
             ("¿Dónde se quedaba?", ["En hoteles de lujo", "En hostales baratos", "En casas de familia"], 1),
             ("¿Qué aprendió?", ["Que la gente en todas partes tiene mucho en común", "Que viajar es aburrido", "Que no le gustan los pueblos"], 0),
         ]),
         roleplay("Recomendar Colombia", "🇨🇴 Un turista te pide consejos en un hostal.", """
Tourist: It's my first time in Colombia. What's worth visiting? || Es mi primera vez en Colombia. ¿Qué vale la pena visitar?
+ The old town in Cartagena is beautiful, and the coffee region is amazing. || El centro histórico de Cartagena es hermoso, y el Eje Cafetero es increíble.
- The coffee is worth visiting a castle. || El café vale visitar un castillo. || Frase sin sentido.
Tourist: Is the food spicy? || ¿La comida es picante?
+ Not really. It's different from Mexican food. It isn't very spicy. || No mucho. Es diferente de la mexicana. No es muy picante.
- Yes, it's different of Mexican. || Sí, es diferente de la mexicana. || Se dice "different from".
Tourist: Should I tip in restaurants? || ¿Debo dejar propina en los restaurantes?
+ Usually there's a ten percent tip on the bill, but it's optional. || Normalmente viene un diez por ciento de propina en la cuenta, pero es opcional.
- You mustn't eat in restaurants. || No puede comer en restaurantes. || No tiene sentido.
"""),
     ],
     writes="""
El español es parecido al italiano. | Spanish is similar to Italian.
Vale la pena visitar Cartagena. | Cartagena is worth visiting. | It's worth visiting Cartagena.
Me acostumbré a la comida. | I got used to the food.
""",
     dictations="""
Every country has its own customs. || Cada país tiene sus propias costumbres.
I experienced culture shock at first. || Al principio tuve choque cultural.
""")

unit("u52-medios", "B1", "Medios y redes sociales", "📱",
     "Ya puedo hablar de redes sociales, noticias y entretenimiento digital",
     "Redes sociales, noticias, privacidad y desinformación; verbos para contar lo que viste en internet.",
     grammar=["Estilo indirecto básico: She said that…", "Adverbios de opinión: apparently, obviously"],
     items="""
social media | redes sociales | 📲
post | publicación / publicar | 📝 | póust
share (B1) | compartir
comment | comentario / comentar | 💬 | kó-ment
like (social) | me gusta (dar like) | 👍
follower | seguidor | 👥 | fó-lou-er
follow | seguir | ➡️ | fó-lou
unfollow | dejar de seguir | 🚫
profile | perfil | 🪪 | próu-fail
account (B1) | cuenta
influencer | influenciador | 🤳 | ín-flu-en-ser
content creator | creador de contenido | 🎥
go viral | volverse viral | 🚀
trending | tendencia | 📈 | trén-ding
hashtag | etiqueta / hashtag | #️⃣
selfie | selfi | 🤳
stream | transmitir en vivo | 📡 | stríim
podcast | podcast | 🎙️ | pód-kast
subscribe | suscribirse | 🔔 | sabs-kráib
notification | notificación | 🔔 | nou-ti-fi-kéi-shon
scroll | desplazarse / scroll | 📜 | skról
headline | titular | 📰 | jéd-lain
article | artículo | 📄 | ár-ti-kol
journalist | periodista | 🧑‍💼 | yér-na-list
reporter | reportero | 🎤 | ri-pór-ter
newspaper | periódico | 🗞️ | niús-pei-per
magazine | revista | 📖 | ma-ga-síin
TV channel | canal de televisión | 📺
advertisement | publicidad / anuncio | 📢 | ad-ver-táis-ment
ad | anuncio | 🪧 | ad
fake news | noticias falsas | 🤥
misinformation | desinformación | ⚠️ | mis-in-for-méi-shon
source | fuente | 🔎 | sors
reliable source | fuente confiable | ✅
check the facts | verificar los datos | 🔍
privacy | privacidad | 🔒 | prái-va-si
personal data | datos personales | 🗂️
hacker | hacker / pirata informático | 🧑‍💻 | já-ker
scam | estafa | 🎣 | skam
password (B1) | contraseña
block | bloquear | ⛔ | blok
report | reportar / denunciar | 🚩 | ri-pórt
cyberbullying | ciberacoso | 😢 | sái-ber-bu-li-ing
online | en línea | 🌐
offline | sin conexión | 📴
apparently | al parecer | 🤔 | a-pé-rent-li
According to… | Según… | 📚
I saw it on… | Lo vi en… | 👀
She said that… | Ella dijo que… | 💬
He told me that… | Él me dijo que… | 🗣️
""",
     extras=[
         D("Contar lo que alguien dijo",
           "Compara lo que la persona dijo con cómo se cuenta después.",
           """
"I'm tired." → She said that she was tired. || "Estoy cansada." → Dijo que estaba cansada. || was
"I love this video." → He said he loved the video. || "Me encanta este video." → Dijo que le encantaba el video. || loved
"The news is fake." → They told me that the news was fake. || "La noticia es falsa." → Me dijeron que la noticia era falsa. || was
"I will post it tomorrow." → She said she would post it the next day. || "Lo publico mañana." → Dijo que lo publicaría al día siguiente. || would
""",
           "Al contar lo que alguien dijo, el verbo normalmente…",
           ["Se queda igual", "Se mueve un paso hacia el pasado (is → was)"], 1,
           "Esto se llama ESTILO INDIRECTO. Al contar lo que alguien dijo, el verbo suele ir un paso hacia atrás: am/is → was, love → loved, will → would. say no lleva persona (She said that…); tell sí (She told ME that…). En una unidad de B2 lo verás completo.",
           """
According to the article, the video went viral in one day. || Según el artículo, el video se volvió viral en un día.
""",
           fills="""
She ___ me that she had a new account. | told / said | 0 | Me dijo que tenía una cuenta nueva.
He ___ that the photo was fake. | said / told | 0 | Dijo que la foto era falsa.
"I am busy." → She said she ___ busy. | was / is will | 0 | "Estoy ocupada." → Dijo que estaba ocupada.
Always check the ___ before you share news. | source / sauce | 0 | Revisa siempre la fuente antes de compartir noticias.
"""),
         tip("🕵️", "Antes de compartir", "Para frenar las fake news, pregúntate: Who wrote it? (¿quién lo escribió?), Is the source reliable? (¿la fuente es confiable?), Do other sites say the same? (¿otros sitios dicen lo mismo?)."),
         dialogue("¿Viste ese video?", "📱 En la universidad, entre clases.", """
Sara: Did you see the video about the bear in Bogotá? It went viral! || ¿Viste el video del oso en Bogotá? ¡Se volvió viral!
Juan: Yes, but apparently it's fake. || Sí, pero al parecer es falso.
Sara: Really? My cousin shared it. She said it was real. || ¿En serio? Mi prima lo compartió. Dijo que era real.
Juan: According to a reliable news site, it was made with artificial intelligence. || Según un sitio de noticias confiable, lo hicieron con inteligencia artificial.
Sara: Wow. I need to check the facts before I share things. || Uy. Tengo que verificar los datos antes de compartir cosas.
Juan: We all do! || ¡Todos!
"""),
         story("La estafa del sorteo", "🎣", """
One morning Patricia got a message on social media: "Congratulations! You won a new phone!" || Una mañana Patricia recibió un mensaje en redes sociales: "¡Felicitaciones! ¡Ganaste un celular nuevo!"
The message said she only had to pay for the shipping and give her personal data. || El mensaje decía que solo tenía que pagar el envío y dar sus datos personales.
She was excited, but something felt strange. The profile had no photos and few followers. || Estaba emocionada, pero algo le pareció raro. El perfil no tenía fotos y tenía pocos seguidores.
She asked her nephew, who works in cybersecurity. He told her it was a scam. || Le preguntó a su sobrino, que trabaja en ciberseguridad. Él le dijo que era una estafa.
"Never give your password or bank details online," he said. || "Nunca des tu contraseña ni tus datos bancarios en línea", le dijo.
Patricia blocked the account and reported it. Then she warned all her friends. || Patricia bloqueó la cuenta y la reportó. Luego les advirtió a todos sus amigos.
""", questions=[
             ("¿Qué decía el mensaje?", ["Que había ganado un celular", "Que tenía una deuda", "Que su cuenta estaba bloqueada"], 0),
             ("¿Qué le pareció raro del perfil?", ["Que no tenía fotos y pocos seguidores", "Que era de una empresa famosa", "Que estaba en inglés"], 0),
             ("¿Qué hizo Patricia al final?", ["Pagó el envío", "Bloqueó y reportó la cuenta", "Compartió el mensaje"], 1),
         ]),
         roleplay("Ayudar a tu mamá con un mensaje raro", "📩 Tu mamá recibe un mensaje sospechoso.", """
Mom: The bank sent me a message. They want my password. || El banco me mandó un mensaje. Quieren mi contraseña.
+ Don't send it! Banks never ask for your password. It's a scam. || ¡No la mandes! Los bancos nunca piden tu contraseña. Es una estafa.
- Send it quickly! || ¡Mándala rápido! || Nunca se comparte la contraseña.
Mom: But the message says my account will be blocked. || Pero el mensaje dice que me van a bloquear la cuenta.
+ That's what scammers say. Let's call the bank and check. || Eso es lo que dicen los estafadores. Llamemos al banco y verifiquemos.
- That's true. Banks always say that. || Es cierto. Los bancos siempre dicen eso. || Justo lo contrario.
Mom: OK. What should I do with the message? || Bueno. ¿Qué hago con el mensaje?
+ Report it and block the number. || Repórtalo y bloquea el número.
- Share it with all your followers. || Compártelo con todos tus seguidores. || Sería esparcir la estafa.
"""),
     ],
     writes="""
Ella me dijo que estaba cansada. | She told me that she was tired. | She told me she was tired.
Al parecer, la noticia es falsa. | Apparently, the news is fake. | Apparently the news is fake.
Nunca compartas tu contraseña. | Never share your password. | Don't share your password.
""",
     dictations="""
The video went viral in one day. || El video se volvió viral en un día.
According to the article, it was a scam. || Según el artículo, era una estafa.
""")
