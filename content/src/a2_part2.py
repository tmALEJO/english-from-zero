# A2 · Parte 2 (unidades 29–34)

unit("u29-salud", "A2", "En el médico", "🩺",
     "Ya puedo explicar qué me pasa y entender consejos del médico",
     "Síntomas, el médico y la farmacia, y should para dar y recibir consejos.",
     grammar=["Should / shouldn't para consejos"],
     items="""
symptom | síntoma | 📋 | símp-tom
cough | tos / toser | 😷 | kof
sore throat | dolor de garganta | 🗣️ | sor zróut
runny nose | nariz que gotea | 🤧
toothache | dolor de muela | 🦷 | túuz-eik
earache | dolor de oído | 👂 | íer-eik
backache | dolor de espalda | 😣
dizzy | mareado | 😵 | dí-si
allergy | alergia | 🌼 | á-ler-yi
injury | lesión | 🩹 | ín-ye-ri
blood | sangre | 🩸 | blad
bone | hueso | 🦴 | bóun
skin | piel | ✋ | skin
pill | pastilla | 💊 | pil
syrup | jarabe | 🧴 | sí-rop
prescription | fórmula médica | 📝 | pres-kríp-shon
appointment | cita (médica) | 📅
emergency | emergencia | 🚨 | i-mér-yen-si
ambulance | ambulancia | 🚑 | ám-biu-lans
patient | paciente | 🛏️
pain | dolor | ⚡ | péin
hurt | doler / lastimar | 🤕 | hert
break your leg | romperse la pierna | 🦵
cut your finger | cortarse el dedo | 🔪
rest | descansar | 🛌 | rest
get better | mejorarse | 📈
take medicine | tomar medicina | 💊
twice a day | dos veces al día | 2️⃣
every eight hours | cada ocho horas | ⏰
You should rest | Deberías descansar | 🛌
You shouldn't smoke | No deberías fumar | 🚭
drink plenty of water | tomar mucha agua | 💧
healthy food | comida saludable | 🥦
exercise | hacer ejercicio | 🏋️ | ék-ser-sais
I feel sick | Me siento mal | 🤢
I need a doctor | Necesito un médico | 🧑‍⚕️
Is it serious? | ¿Es grave? | ❗
It's nothing serious | No es nada grave | 🙂
check-up | chequeo | 🩺 | chék-ap
""",
     extras=[
         D("should para consejos",
           "Así dan consejos los médicos y los amigos.",
           """
You have a fever. You should rest. || Tienes fiebre. Deberías descansar. || should
You should drink plenty of water. || Deberías tomar mucha agua. || should
You shouldn't eat fast food. || No deberías comer comida rápida. || shouldn't
He should see a doctor. || Él debería ir al médico. || should
Should I take this pill? || ¿Debería tomar esta pastilla? || Should
""",
           "Después de should, el verbo…",
           ["Lleva -s con he/she", "Va en forma normal", "Va con to"], 1,
           "should = debería. Sirve para dar consejos. Igual que can, es igual para todas las personas y el verbo siguiente va sin cambios: She should rest (no 'shoulds' ni 'rests'). Negativo: shouldn't.",
           """
You look tired. You should go to bed early. || Te ves cansado. Deberías acostarte temprano.
""",
           fills="""
You have a cough. You ___ smoke. | should / shouldn't | 1 | Tienes tos. No deberías fumar.
She should ___ a doctor. | see / sees | 0 | Ella debería ir al médico.
___ I take this medicine every day? | Should / Do should | 0 | ¿Debería tomar esta medicina todos los días?
Take one pill ___ a day. | twice / two | 0 | Tome una pastilla dos veces al día.
"""),
         dialogue("En la farmacia", "💊 Pides algo para la gripa.", """
Pharmacist: Hello. How can I help you? || Hola. ¿En qué le puedo ayudar?
You: I have a sore throat and a cough. || Tengo dolor de garganta y tos.
Pharmacist: Do you have a fever? || ¿Tiene fiebre?
You: No, I don't. || No.
Pharmacist: Take this syrup every eight hours. And you should drink plenty of water. || Tome este jarabe cada ocho horas. Y debería tomar mucha agua.
You: Should I see a doctor? || ¿Debería ir al médico?
Pharmacist: If you don't get better in three days, yes. || Si no mejora en tres días, sí.
"""),
         story("El partido del domingo", "⚽", """
On Sunday Carlos played football with his friends. || El domingo Carlos jugó fútbol con sus amigos.
In the second half he fell and hurt his ankle. The pain was terrible. || En el segundo tiempo se cayó y se lastimó el tobillo. El dolor era terrible.
His friends called an ambulance and he went to the emergency room. || Sus amigos llamaron una ambulancia y fue a urgencias.
The doctor checked his leg. "It's not broken. It's nothing serious." || El médico le revisó la pierna. "No está rota. No es nada grave."
"You should rest for two weeks and you shouldn't play football." || "Debería descansar dos semanas y no debería jugar fútbol."
Carlos was sad, but now he watches the games from the sofa. || Carlos se puso triste, pero ahora ve los partidos desde el sofá.
""", questions=[
             ("¿Qué se lastimó Carlos?", ["La muñeca", "El tobillo", "La cabeza"], 1),
             ("¿Estaba roto?", ["Sí", "No, no era grave"], 1),
             ("¿Qué le dijo el médico?", ["Que descansara dos semanas", "Que jugara mañana", "Que tomara jarabe"], 0),
         ]),
         roleplay("Consulta médica", "🩺 Vas al médico porque te duele la espalda.", """
Doctor: Good afternoon. What's the problem? || Buenas tardes. ¿Cuál es el problema?
+ My back hurts a lot. || Me duele mucho la espalda.
- My back hurt a lot tomorrow. || Me dolió mucho la espalda mañana. || Mezcla pasado con mañana.
Doctor: When did it start? || ¿Cuándo empezó?
+ Three days ago. I carried a heavy box. || Hace tres días. Cargué una caja pesada.
- In three days. || En tres días. || Eso sería en el futuro; di "three days ago".
Doctor: Take these pills twice a day, and you should rest. || Tome estas pastillas dos veces al día y debería descansar.
+ Should I go to work? || ¿Debería ir a trabajar?
- I should to rest. || Yo debería a descansar. || Después de should no va "to".
Doctor: No, you shouldn't. Rest for three days. || No, no debería. Descanse tres días.
"""),
     ],
     writes="""
Deberías descansar. | You should rest.
Me duele la garganta. | I have a sore throat. | My throat hurts.
¿Es grave? | Is it serious?
""",
     dictations="""
Take one pill every eight hours. || Tome una pastilla cada ocho horas.
You shouldn't eat so much sugar. || No deberías comer tanta azúcar.
""")

unit("u30-viaje", "A2", "De viaje", "✈️",
     "Ya puedo moverme en un aeropuerto y un hotel",
     "Aeropuerto, migración, hotel y pedir cosas con amabilidad (can / could).",
     grammar=["Could you…? para pedir con amabilidad"],
     items="""
passport | pasaporte | 🛂 | pás-port
boarding pass | pase de abordar | 🎫 | bór-ding pas
flight | vuelo | 🛫 | fláit
gate | puerta de embarque | 🚪 | guéit
luggage | equipaje | 🧳 | lá-gich
suitcase | maleta | 🧳 | súut-keis
backpack | morral | 🎒 | bák-pak
check in | registrarse (vuelo / hotel) | ✅
check out | salir del hotel / entregar la habitación | 🔚
departure | salida | 🛫 | di-pár-cher
arrival | llegada | 🛬 | a-rái-val
delayed | retrasado | ⏳ | di-léid
canceled | cancelado | ❌ | kán-seld
customs | aduana | 🛃 | kás-toms
tourist | turista | 📸 | túu-rist
abroad | en el extranjero | 🌍 | a-bród
foreign | extranjero | 🗺️ | fó-ren
reservation | reserva | 📒 | re-ser-véi-shon
single room | habitación sencilla | 🛏️
double room | habitación doble | 🛏️🛏️
reception | recepción | 🛎️ | ri-sép-shon
towel | toalla | 🧺 | táu-el
air conditioning | aire acondicionado | ❄️
elevator | ascensor | 🛗 | é-le-vei-tor
view | vista | 🏞️ | viú
map | mapa | 🗺️ | map
guide | guía | 🧑‍🏫 | gáid
souvenir | recuerdo (de viaje) | 🗿 | su-ve-níer
exchange money | cambiar dinero | 💱
How long are you staying? | ¿Cuánto tiempo se va a quedar? | 📆
I'm here on vacation | Estoy aquí de vacaciones | 🏖️
I'm here for work | Estoy aquí por trabajo | 💼
Could you help me, please? | ¿Podría ayudarme, por favor? | 🙏
Could I have a window seat? | ¿Me podría dar un puesto en la ventana? | 🪟
Is breakfast included? | ¿El desayuno está incluido? | 🥐
I have a reservation | Tengo una reserva | 📝
Where is gate twelve? | ¿Dónde está la puerta doce? | 🚪
Have a nice trip! | ¡Buen viaje! | 👋
""",
     extras=[
         D("can y could para pedir",
           "Compara estas formas de pedir algo.",
           """
Can you help me? || ¿Me puedes ayudar? || Can
Could you help me, please? || ¿Podría ayudarme, por favor? || Could
Can I have a towel? || ¿Me das una toalla? || Can
Could I have a window seat? || ¿Me podría dar un puesto en la ventana? || Could
Could you repeat that, please? || ¿Podría repetir eso, por favor? || Could
""",
           "¿Qué forma suena más amable y formal?",
           ["can", "could"], 1,
           "Can y could sirven para pedir algo. Could es más amable y formal (como 'podría'), ideal con desconocidos, en hoteles, aeropuertos o el trabajo. Después de los dos, el verbo va en forma normal.",
           """
Excuse me, could you tell me where the elevator is? || Disculpe, ¿podría decirme dónde está el ascensor?
""",
           fills="""
___ you call a taxi for me, please? | Could / Should | 0 | ¿Podría pedirme un taxi, por favor?
Could I ___ the bill, please? | have / has | 0 | ¿Me podría traer la cuenta, por favor?
My flight is ___. It leaves at ten now. | delayed / canceled | 0 | Mi vuelo está retrasado. Ahora sale a las diez.
I'd like a ___ room for two people. | double / single | 0 | Quisiera una habitación doble para dos personas.
"""),
         dialogue("En migración", "🛂 Llegas al aeropuerto de Miami.", """
Officer: Passport, please. || Pasaporte, por favor.
You: Here you are. || Aquí tiene.
Officer: What's the purpose of your visit? || ¿Cuál es el motivo de su visita?
You: I'm here on vacation. || Estoy aquí de vacaciones.
Officer: How long are you staying? || ¿Cuánto tiempo se va a quedar?
You: Two weeks. I have a hotel reservation. || Dos semanas. Tengo reserva de hotel.
Officer: OK. Enjoy your trip! || Bien. ¡Disfrute su viaje!
"""),
         story("Un vuelo retrasado", "⏳", """
Laura arrived at the airport at five in the morning. Her flight to Madrid was at seven. || Laura llegó al aeropuerto a las cinco de la mañana. Su vuelo a Madrid era a las siete.
She checked in, showed her passport and went to gate twelve. || Hizo el check-in, mostró su pasaporte y se fue a la puerta doce.
Then she saw the screen: "Flight 304: DELAYED." || Entonces vio la pantalla: "Vuelo 304: RETRASADO."
She waited for four hours. She read a book and bought a souvenir. || Esperó cuatro horas. Leyó un libro y compró un recuerdo.
On the plane she asked, "Could I have a window seat?" The attendant said yes. || En el avión preguntó: "¿Me podría dar un puesto en la ventana?" La azafata dijo que sí.
When she arrived in Madrid, the view from the window was beautiful. || Cuando llegó a Madrid, la vista desde la ventana era hermosa.
""", questions=[
             ("¿A dónde viajaba Laura?", ["A Miami", "A Madrid", "A Bogotá"], 1),
             ("¿Cuánto esperó?", ["Una hora", "Cuatro horas", "Dos días"], 1),
             ("¿Qué pidió en el avión?", ["Un puesto en la ventana", "Una toalla", "Comida"], 0),
         ]),
         roleplay("Llegada al hotel", "🛎️ Llegas a la recepción del hotel.", """
Receptionist: Good evening. Welcome to Hotel Andes. || Buenas noches. Bienvenido al Hotel Andes.
+ Good evening. I have a reservation. My name is Sam Ruiz. || Buenas noches. Tengo una reserva. Me llamo Sam Ruiz.
- Good evening. I'm a reservation. || Buenas noches. Soy una reserva. || Tú tienes una reserva: "I have a reservation".
Receptionist: Yes, a single room for three nights. || Sí, una habitación sencilla por tres noches.
+ Is breakfast included? || ¿El desayuno está incluido?
- Is breakfast delayed? || ¿El desayuno está retrasado? || "Delayed" se usa para vuelos o buses.
Receptionist: Yes, from six to ten. Here is your key. || Sí, de seis a diez. Aquí está su llave.
+ Thank you. Could you tell me where the elevator is? || Gracias. ¿Podría decirme dónde está el ascensor?
- Thank you. Could you to tell me the elevator? || Gracias. ¿Podría a decirme el ascensor? || Después de could no va "to".
"""),
     ],
     writes="""
Tengo una reserva. | I have a reservation.
¿Podría ayudarme, por favor? | Could you help me, please? | Could you help me please?
Mi vuelo está retrasado. | My flight is delayed.
""",
     dictations="""
Where is gate twelve? || ¿Dónde está la puerta doce?
Could I have a window seat, please? || ¿Me podría dar un puesto en la ventana, por favor?
""",
     speak="""
I'm here on vacation for two weeks. || Estoy aquí de vacaciones por dos semanas.
""")

unit("u31-tareas", "A2", "La casa y las obligaciones", "🧹",
     "Ya puedo hablar de las tareas de la casa y de lo que tengo que hacer",
     "Oficios de la casa y have to / don't have to para obligaciones.",
     grammar=["Have to / don't have to"],
     items="""
do the dishes | lavar los platos | 🍽️
do the laundry | lavar la ropa | 🧺 | du de lón-dri
make the bed | tender la cama | 🛏️
take out the trash | sacar la basura | 🗑️
sweep the floor | barrer el piso | 🧹
mop the floor | trapear el piso | 🫧
vacuum | aspirar | 🌀 | vá-kium
iron | planchar | 👔 | ái-ron
dust | sacudir el polvo | 🪶 | dast
water the plants | regar las plantas | 🪴
feed the dog | darle comida al perro | 🐕
walk the dog | sacar a pasear al perro | 🦮
set the table | poner la mesa | 🍴
tidy up | ordenar | 🧸 | tái-di ap
wash | lavar | 🫧 | uosh
fold | doblar | 👕 | fóuld
fix | arreglar | 🔧 | fiks
paint the walls | pintar las paredes | 🎨
grocery shopping | hacer mercado | 🛒 | gróu-se-ri
chores | oficios / quehaceres | 📋 | chors
messy | desordenado | 🌪️ | mé-si
tidy | ordenado | ✨ | tái-di
dishwasher | lavaplatos (máquina) | 🍽️
washing machine | lavadora | 🧺
broom | escoba | 🧹 | brum
bucket | balde | 🪣 | bá-ket
soap | jabón | 🧼 | sóup
sponge | esponja | 🧽 | spanch
trash can | caneca de basura | 🗑️
I have to work | Tengo que trabajar | 💼
She has to study | Ella tiene que estudiar | 📚
You don't have to come | No tienes que venir | 🙅
Do I have to pay? | ¿Tengo que pagar? | 💵
It's your turn | Es tu turno | 🔄
share | compartir | 🤝
help out | echar una mano | 🖐️
roommate | compañero de apartamento | 🏠 | rúum-meit
landlord | arrendador / dueño | 🔑 | lánd-lord
rent | arriendo | 💲 | rent
bills | cuentas / facturas | 🧾 | bils
""",
     extras=[
         D("have to / don't have to",
           "Lee lo que estas personas deben y no deben hacer.",
           """
I have to do the dishes every night. || Tengo que lavar los platos todas las noches. || have to
She has to take out the trash. || Ella tiene que sacar la basura. || has to
We don't have to cook today. || Hoy no tenemos que cocinar. || don't have to
He doesn't have to work on Sundays. || Él no tiene que trabajar los domingos. || doesn't have to
Do you have to pay rent? || ¿Tienes que pagar arriendo? || have to
""",
           "¿Qué significa don't have to?",
           ["Está prohibido", "No es necesario", "Lo hice ayer"], 1,
           "have to = tener que (obligación). Con he/she/it: has to. Ojo: don't have to NO significa 'prohibido', significa 'no es necesario': You don't have to come = no tienes que venir (si quieres, vienes).",
           """
I have to clean my room, but I don't have to do it today. || Tengo que limpiar mi cuarto, pero no tengo que hacerlo hoy.
""",
           fills="""
My brother ___ to walk the dog. | have / has | 1 | Mi hermano tiene que sacar al perro.
You ___ have to come. It's optional. | don't / doesn't | 0 | No tienes que venir. Es opcional.
___ we have to pay for the water? | Do / Does | 0 | ¿Tenemos que pagar el agua?
She doesn't have ___ iron her clothes. | to / — | 0 | Ella no tiene que planchar su ropa.
"""),
         dialogue("Repartiendo los oficios", "🏠 Nuevos compañeros de apartamento.", """
Lia: OK, let's share the chores. || Bueno, repartamos los oficios.
Sam: I can do the dishes and take out the trash. || Yo puedo lavar los platos y sacar la basura.
Lia: Great. I'm going to do the laundry and water the plants. || Genial. Yo voy a lavar la ropa y regar las plantas.
Sam: Who has to clean the bathroom? || ¿Quién tiene que limpiar el baño?
Lia: We can take turns. This week it's your turn! || Podemos turnarnos. ¡Esta semana es tu turno!
Sam: Oh no! || ¡Ay no!
"""),
         story("Un sábado de oficios", "🧽", """
Every Saturday the Rojas family cleans the house together. || Todos los sábados la familia Rojas limpia la casa junta.
Mom does the laundry and Dad vacuums the living room. || Mamá lava la ropa y papá aspira la sala.
Ana has to make her bed and tidy up her room. It's always messy! || Ana tiene que tender su cama y ordenar su cuarto. ¡Siempre está desordenado!
Little Pedro doesn't have to clean, but he likes to feed the dog. || El pequeño Pedro no tiene que limpiar, pero le gusta darle comida al perro.
At noon the house is clean and tidy. || Al mediodía la casa está limpia y ordenada.
Then they do something fun: they go out for lunch! || Luego hacen algo divertido: ¡salen a almorzar!
""", questions=[
             ("¿Qué hace papá?", ["Lava la ropa", "Aspira la sala", "Riega las plantas"], 1),
             ("¿Cómo está siempre el cuarto de Ana?", ["Ordenado", "Desordenado", "Vacío"], 1),
             ("¿Qué hacen al final?", ["Duermen", "Salen a almorzar", "Ven televisión"], 1),
         ]),
         roleplay("Hablar con el arrendador", "🔑 Vas a arrendar un apartamento y tienes preguntas.", """
Landlord: The rent is six hundred thousand pesos. || El arriendo es de seiscientos mil pesos.
+ Do I have to pay the bills too? || ¿También tengo que pagar los servicios?
- Do I has to pay the bills? || ¿Yo tiene que pagar los servicios? || Con I es "have to".
Landlord: Yes, you have to pay water and electricity. || Sí, tiene que pagar agua y luz.
+ OK. Do I have to clean the stairs? || Bueno. ¿Tengo que limpiar las escaleras?
- OK. I don't have to rent. || Bueno. No tengo que arriendo. || No tiene sentido.
Landlord: No, you don't have to. A cleaner comes every Friday. || No, no tiene que hacerlo. Una señora del aseo viene todos los viernes.
+ Perfect. I'll take it. || Perfecto. Lo tomo.
- Perfect. You have to take it. || Perfecto. Usted tiene que tomarlo. || El que lo arrienda eres tú.
"""),
     ],
     writes="""
Tengo que lavar los platos. | I have to do the dishes. | I have to wash the dishes.
Ella no tiene que trabajar mañana. | She doesn't have to work tomorrow. | She does not have to work tomorrow.
Es tu turno. | It's your turn. | It is your turn.
""",
     dictations="""
Do I have to pay the rent today? || ¿Tengo que pagar el arriendo hoy?
He has to take out the trash every night. || Él tiene que sacar la basura todas las noches.
""")

unit("u32-naturaleza", "A2", "Animales y naturaleza", "🦜",
     "Ya puedo hablar de animales, paisajes y la naturaleza",
     "Animales, paisajes y vocabulario de la naturaleza de Colombia y el mundo.",
     grammar=["There was / there were", "Adjetivos para describir lugares"],
     items="""
dog | perro | 🐕
horse | caballo | 🐴 | jors
cow | vaca | 🐄 | káu
pig | cerdo | 🐖 | pig
chicken (animal) | gallina | 🐔
duck | pato | 🦆 | dak
rabbit | conejo | 🐇 | rá-bit
mouse (animal) | ratón | 🐁
bird | pájaro | 🐦 | berd
parrot | loro | 🦜 | pá-rot
snake | serpiente | 🐍 | snéik
frog | rana | 🐸 | frog
turtle | tortuga | 🐢 | tér-tol
butterfly | mariposa | 🦋 | bá-ter-flai
bee | abeja | 🐝 | bíi
spider | araña | 🕷️ | spái-der
monkey | mono | 🐒 | mán-ki
bear | oso | 🐻 | ber
lion | león | 🦁 | lái-on
tiger | tigre | 🐯 | tái-ger
elephant | elefante | 🐘 | é-le-fant
whale | ballena | 🐋 | uéil
shark | tiburón | 🦈 | shark
river | río | 🏞️ | rí-ver
lake | lago | 🛶 | léik
sea | mar | 🌊 | síi
ocean | océano | 🌏 | óu-shan
forest | bosque | 🌲 | fó-rest
jungle | selva | 🌴 | yán-gol
desert | desierto | 🏜️ | dé-sert
volcano | volcán | 🌋 | vol-kéi-nou
island | isla | 🏝️ | ái-land | La s no suena.
waterfall | cascada | 💦 | uó-ter-fol
hill | loma / colina | ⛰️ | jil
sky | cielo | 🌌 | skái
moon | luna | 🌙 | muun
flower | flor | 🌺 | fláu-er
grass | pasto / césped | 🌱 | gras
leaf | hoja (de árbol) | 🍃 | líif
wild | salvaje | 🐾 | uáild
endangered | en peligro de extinción | ⚠️ | en-déin-yerd
""",
     extras=[
         D("There was / there were",
           "Es el pasado de there is / there are. Mira la cantidad.",
           """
There was a big snake in the garden. || Había una serpiente grande en el jardín. || There was
There was a waterfall near the hotel. || Había una cascada cerca del hotel. || There was
There were many birds in the forest. || Había muchos pájaros en el bosque. || There were
There weren't any people on the beach. || No había nadie en la playa. || There weren't
Was there a lake? Yes, there was. || ¿Había un lago? Sí. || Was there
""",
           "¿Qué forma va con varias cosas?",
           ["There was", "There were"], 1,
           "There was = había (una cosa). There were = había (varias cosas). Es el mismo cambio de is → was y are → were.",
           """
When I was a child, there were horses and cows on my grandfather's farm. || Cuando era niño, había caballos y vacas en la finca de mi abuelo.
""",
           fills="""
___ a monkey in the tree! | There was / There were | 0 | ¡Había un mono en el árbol!
___ three turtles on the beach. | There was / There were | 1 | Había tres tortugas en la playa.
___ there any whales? | Were / Was | 0 | ¿Había ballenas?
There ___ any fish in the river. | wasn't / weren't | 1 | No había peces en el río.
"""),
         tip("🇨🇴", "Colombia en inglés", "Colombia es uno de los países con más especies de aves del mundo: 'Colombia has more bird species than any other country.' Muchas guías de turismo en inglés usan este vocabulario."),
         dialogue("En el zoológico", "🦁 Visitas el zoológico con tu sobrina.", """
Niece: Look! What's that animal? || ¡Mira! ¿Qué animal es ese?
You: It's a tiger. It's very dangerous. || Es un tigre. Es muy peligroso.
Niece: Is it bigger than a lion? || ¿Es más grande que un león?
You: Yes, tigers are the biggest cats in the world. || Sí, los tigres son los felinos más grandes del mundo.
Niece: Are there any elephants? || ¿Hay elefantes?
You: Yes, there are two. Let's go! || Sí, hay dos. ¡Vamos!
"""),
         story("Viaje al Amazonas", "🌴", """
Last year Diego traveled to the Amazon jungle with a group of tourists. || El año pasado Diego viajó a la selva del Amazonas con un grupo de turistas.
They took a small boat on the river. The water was brown and very wide. || Tomaron una lancha pequeña en el río. El agua era café y muy ancha.
There were monkeys in the trees and hundreds of colorful birds. || Había monos en los árboles y cientos de pájaros de colores.
One night there was a big frog in Diego's room! He screamed. || ¡Una noche había una rana grande en el cuarto de Diego! Gritó.
The guide explained that many animals there are endangered. || El guía explicó que muchos animales de allá están en peligro de extinción.
Diego came back home with a new dream: to protect the jungle. || Diego volvió a casa con un sueño nuevo: proteger la selva.
""", questions=[
             ("¿Cómo viajaron por el río?", ["En una lancha pequeña", "En avión", "En caballo"], 0),
             ("¿Qué había en el cuarto de Diego?", ["Una serpiente", "Una rana grande", "Un mono"], 1),
             ("¿Qué sueño tiene ahora Diego?", ["Ser guía", "Proteger la selva", "Vivir en el río"], 1),
         ]),
         roleplay("Planear una excursión", "🗺️ Un amigo extranjero te pide ideas para visitar Nariño.", """
Mark: I want to see nature. What do you recommend? || Quiero ver naturaleza. ¿Qué me recomiendas?
+ You should visit La Cocha lake. It's beautiful. || Deberías visitar la Laguna de la Cocha. Es hermosa.
- You should visit the elevator. || Deberías visitar el ascensor. || No es naturaleza.
Mark: Is it far from Pasto? || ¿Queda lejos de Pasto?
+ No, it takes about forty minutes by car. || No, se demora unos cuarenta minutos en carro.
- No, it takes forty years. || No, se demora cuarenta años. || Exagerado; di un tiempo real.
Mark: Are there any volcanoes near Pasto? || ¿Hay volcanes cerca de Pasto?
+ Yes, there is the Galeras volcano. || Sí, está el volcán Galeras.
- Yes, there were a volcano. || Sí, habían un volcán. || Con uno: "there is" (presente).
"""),
     ],
     writes="""
Había muchos pájaros en el bosque. | There were many birds in the forest. | There were a lot of birds in the forest.
El elefante es más grande que el caballo. | The elephant is bigger than the horse.
Hay una cascada cerca del río. | There is a waterfall near the river. | There's a waterfall near the river.
""",
     dictations="""
There was a monkey in the tree. || Había un mono en el árbol.
Many animals in the jungle are endangered. || Muchos animales de la selva están en peligro de extinción.
""")

unit("u33-servicios", "A2", "Servicios de la ciudad", "🏦",
     "Ya puedo hacer trámites en el banco, el correo y otros servicios",
     "Banco, correo, peluquería, taller y cómo hacer y responder solicitudes.",
     grammar=["I'd like to + verbo", "Preguntas indirectas sencillas"],
     items="""
open an account | abrir una cuenta | 🏦
withdraw money | sacar plata | 🏧 | uiz-dró
deposit | consignar / depósito | 💵 | di-pó-sit
transfer | transferencia / transferir | 🔁 | tráns-fer
ATM | cajero automático | 🏧 | éi-ti-em
PIN number | clave (de la tarjeta) | 🔢
receipt | recibo | 🧾 | ri-síit | La p no suena.
coin | moneda | 🪙 | kóin
bill (money) | billete | 💵
fill out a form | llenar un formulario | 📝
sign | firmar | ✍️ | sáin
signature | firma | 🖊️ | síg-na-cher
ID card | cédula / documento de identidad | 🪪
address | dirección | 🏠 | á-dres
zip code | código postal | 📮
package | paquete | 📦 | pá-kich
letter | carta | ✉️ | lé-ter
stamp | estampilla | 📯 | stamp
line | fila | 🧍🧍 | láin
wait in line | hacer fila | ⏳
hairdresser | peluquería / peluquero | 💇 | jér-dre-ser
haircut | corte de pelo | ✂️ | jér-kat
repair shop | taller de reparación | 🔧
gas station | estación de gasolina / bomba | ⛽
laundry service | lavandería | 👕
dry cleaner | tintorería | 🧥
police station | estación de policía | 🚓
city hall | alcaldía | 🏛️
open | abierto | 🟢
closed | cerrado | 🔴
opening hours | horario de atención | 🕘
I'd like to send a package | Quisiera enviar un paquete | 📦
I'd like to open an account | Quisiera abrir una cuenta | 🏦
How long will it take? | ¿Cuánto se va a demorar? | ⌛
Here's my ID | Aquí está mi cédula | 🪪
Sign here, please | Firme aquí, por favor | ✍️
Next, please! | ¡Siguiente, por favor! | ➡️
What time do you close? | ¿A qué hora cierran? | 🕖
""",
     extras=[
         D("I'd like to + verbo",
           "Ya conoces I'd like + cosa. Mira qué pasa con una acción.",
           """
I'd like a coffee. || Quisiera un café. || I'd like
I'd like to send a package. || Quisiera enviar un paquete. || I'd like to
I'd like to open an account. || Quisiera abrir una cuenta. || I'd like to
She'd like to change her address. || Ella quisiera cambiar su dirección. || 'd like to
Would you like to sign here? || ¿Le gustaría firmar aquí? || Would you like to
""",
           "Cuando lo que quieres es una ACCIÓN, después de I'd like va…",
           ["to + verbo", "verbo con -ing", "nada"], 0,
           "I'd like (I would like) es la forma amable de 'quisiera'. Con una cosa: I'd like a receipt. Con una acción: I'd like TO + verbo: I'd like to withdraw money. Para ofrecer: Would you like…?",
           """
I'd like to withdraw two hundred thousand pesos, please. || Quisiera sacar doscientos mil pesos, por favor.
""",
           fills="""
I'd like ___ send this letter to Spain. | to / — | 0 | Quisiera enviar esta carta a España.
I'd like ___ receipt, please. | a / to | 0 | Quisiera un recibo, por favor.
___ you like to open an account? | Would / Do | 0 | ¿Le gustaría abrir una cuenta?
Please ___ the form and sign here. | fill out / fill in out | 0 | Por favor llene el formulario y firme aquí.
"""),
         dialogue("En el banco", "🏦 Haces fila en el banco.", """
Clerk: Next, please! Good morning. || ¡Siguiente, por favor! Buenos días.
You: Good morning. I'd like to open a savings account. || Buenos días. Quisiera abrir una cuenta de ahorros.
Clerk: Of course. Can I see your ID? || Claro. ¿Puedo ver su cédula?
You: Here's my ID. || Aquí está mi cédula.
Clerk: Thank you. Please fill out this form and sign here. || Gracias. Por favor llene este formulario y firme aquí.
You: How long will it take? || ¿Cuánto se va a demorar?
Clerk: About fifteen minutes. || Unos quince minutos.
"""),
         story("Una mañana de trámites", "📝", """
Sofía had a lot to do on Monday morning. || Sofía tenía mucho que hacer el lunes por la mañana.
First she went to the post office to send a package to her sister in Chile. || Primero fue al correo a enviar un paquete a su hermana en Chile.
She waited in line for twenty minutes and paid with coins. || Hizo fila veinte minutos y pagó con monedas.
Then she went to the ATM, but she forgot her PIN number! || Luego fue al cajero, ¡pero se le olvidó la clave!
She went inside the bank and withdrew money with her ID card. || Entró al banco y sacó plata con su cédula.
Finally she got a haircut. "Now I'm ready for the week," she said. || Al final se cortó el pelo. "Ahora estoy lista para la semana", dijo.
""", questions=[
             ("¿A dónde envió el paquete?", ["A Chile", "A España", "A Perú"], 0),
             ("¿Qué olvidó en el cajero?", ["Su tarjeta", "Su clave", "Su cédula"], 1),
             ("¿Qué hizo al final?", ["Se cortó el pelo", "Fue a la alcaldía", "Abrió una cuenta"], 0),
         ]),
         roleplay("En el correo", "📮 Quieres enviar un paquete a Estados Unidos.", """
Clerk: Hello. How can I help you? || Hola. ¿En qué le puedo ayudar?
+ Hi. I'd like to send this package to the United States. || Hola. Quisiera enviar este paquete a Estados Unidos.
- Hi. I'd like send a package. || Hola. Quisiera enviar un paquete. || Falta "to": I'd like TO send.
Clerk: Sure. What's inside? || Claro. ¿Qué tiene adentro?
+ Some clothes and a book. || Algo de ropa y un libro.
- My PIN number. || Mi clave. || Nunca compartas tu clave, y no responde la pregunta.
Clerk: OK. Please write the address and the zip code here. || Bien. Por favor escriba la dirección y el código postal aquí.
+ No problem. How long will it take? || No hay problema. ¿Cuánto se va a demorar?
- No problem. What time do you open yesterday? || No hay problema. ¿A qué hora abren ayer? || Mezcla tiempos.
"""),
     ],
     writes="""
Quisiera abrir una cuenta. | I'd like to open an account. | I would like to open an account.
¿A qué hora cierran? | What time do you close?
Aquí está mi cédula. | Here's my ID. | Here is my ID. ; Here's my ID card.
""",
     dictations="""
I'd like to send this letter, please. || Quisiera enviar esta carta, por favor.
Please fill out the form and sign here. || Por favor llene el formulario y firme aquí.
""")

unit("u34-dinero", "A2", "Dinero y compras", "💳",
     "Ya puedo manejar precios, pagos, devoluciones y descuentos",
     "Dinero, formas de pago, descuentos, devoluciones y quejas sencillas en una tienda.",
     grammar=["Too / enough", "Números grandes y precios"],
     items="""
price | precio | 🏷️ | práis
discount | descuento | 🔻 | dís-kaunt
sale | rebajas / oferta | 🛍️ | séil
on sale | en oferta | 📉
free shipping | envío gratis | 🚚
change (money) | cambio / vueltas | 🪙 | chéinch
pay | pagar | 💳 | péi
spend | gastar | 💸 | spend
save | ahorrar | 🐷
earn | ganar (dinero trabajando) | 💰 | ern
borrow | pedir prestado | 🤲 | bó-rou
lend | prestar | 🫴 | lend
owe | deber (dinero) | 🧾 | óu
cost | costar | 💲 | kost
afford | poder pagar / costear | 💵 | a-fórd
refund | reembolso | ↩️ | ríi-fand
return | devolver | 🔙 | ri-térn
exchange | cambiar (un producto) | 🔄 | eks-chéinch
receipt (store) | tiquete / factura | 🧾
customer | cliente | 🧑 | kás-to-mer
cashier | cajero | 🧑‍💼 | ka-shíer
online shopping | compras por internet | 🌐
order | pedido / pedir | 📦 | ór-der
deliver | entregar / domicilio | 🛵 | di-lí-ver
brand | marca | ™️ | brand
quality | calidad | ⭐ | kuó-li-ti
broken | dañado / roto | 💔 | bróu-ken
too expensive | demasiado caro | 😬
cheap enough | suficientemente barato | 👌
enough money | suficiente dinero | 💰
half price | a mitad de precio | ½
a thousand | mil | 💯 | a záu-sand
a million | un millón | 💎 | a mí-lion
Can I pay by card? | ¿Puedo pagar con tarjeta? | 💳
Keep the change | Quédese con el cambio | 🪙
I'd like to return this | Quisiera devolver esto | 🔙
It doesn't work | No funciona | ⚠️
Can I get a refund? | ¿Me pueden devolver el dinero? | 💸
That's a good deal | Es buen negocio / buena oferta | 🤝
""",
     extras=[
         D("too y enough",
           "Mira dónde va too y dónde va enough.",
           """
This jacket is too expensive. || Esta chaqueta es demasiado cara. || too
These shoes are too small. || Estos zapatos son demasiado pequeños. || too
I don't have enough money. || No tengo suficiente dinero. || enough
The shirt isn't big enough. || La camisa no es lo suficientemente grande. || enough
It's cheap enough. I'll buy it. || Está suficientemente barato. Lo compro. || enough
""",
           "¿Dónde va enough con un adjetivo (big, cheap)?",
           ["Antes del adjetivo", "Después del adjetivo"], 1,
           "too + adjetivo = demasiado (y es un problema): too expensive. enough = suficiente. Con un sustantivo va antes: enough money. Con un adjetivo va DESPUÉS: big enough, cheap enough.",
           """
I want this phone, but it's too expensive. I don't have enough money. || Quiero este celular, pero es demasiado caro. No tengo suficiente plata.
""",
           fills="""
I can't buy it. It's ___ expensive. | too / enough | 0 | No lo puedo comprar. Es demasiado caro.
Do you have ___ money for the tickets? | enough / too | 0 | ¿Tienes suficiente dinero para los boletos?
This bag isn't big ___. | enough / too | 0 | Este bolso no es lo suficientemente grande.
Can I ___ your pen? | borrow / lend | 0 | ¿Me prestas tu esfero? (pedir prestado)
"""),
         tip("💡", "borrow vs lend", "borrow = pedir prestado (tú recibes): Can I borrow your pen? lend = prestar (tú das): Can you lend me your pen? Los dos se traducen 'prestar', pero miran desde lados distintos."),
         dialogue("Devolver un producto", "🔙 Compraste unos audífonos que no funcionan.", """
You: Hi. I'd like to return these headphones. || Hola. Quisiera devolver estos audífonos.
Clerk: What's the problem? || ¿Cuál es el problema?
You: They don't work. I bought them yesterday. Here's the receipt. || No funcionan. Los compré ayer. Aquí está la factura.
Clerk: Would you like to exchange them or get a refund? || ¿Los quiere cambiar o que le devolvamos el dinero?
You: Can I get a refund, please? || ¿Me pueden devolver el dinero, por favor?
Clerk: Of course. I'll refund the money to your card. || Claro. Le devuelvo el dinero a su tarjeta.
"""),
         story("Ahorrar para un sueño", "🐷", """
Daniel wanted a new laptop for his programming classes. || Daniel quería un portátil nuevo para sus clases de programación.
The one he liked cost three million pesos. It was too expensive for him. || El que le gustaba costaba tres millones de pesos. Era demasiado caro para él.
So he decided to save money. He spent less on fast food and taxis. || Así que decidió ahorrar. Gastó menos en comida rápida y taxis.
He also earned extra money fixing computers for his neighbors. || También ganó plata extra arreglando computadores a sus vecinos.
After six months he had enough money, and the laptop was on sale! || Después de seis meses tenía suficiente dinero, ¡y el portátil estaba en oferta!
He paid half price. "That's a good deal," he said with a big smile. || Pagó la mitad. "Qué buen negocio", dijo con una gran sonrisa.
""", questions=[
             ("¿Para qué quería el portátil?", ["Para jugar", "Para sus clases de programación", "Para su papá"], 1),
             ("¿Cómo ganó plata extra?", ["Arreglando computadores", "Vendiendo comida", "Manejando taxi"], 0),
             ("¿Cuánto pagó al final?", ["El precio completo", "La mitad", "Nada"], 1),
         ]),
         roleplay("En la caja", "🛒 Pagas tus compras en el supermercado.", """
Cashier: That's forty-five thousand pesos. || Son cuarenta y cinco mil pesos.
+ Can I pay by card? || ¿Puedo pagar con tarjeta?
- Can I lend by card? || ¿Puedo prestar con tarjeta? || Se dice "pay by card".
Cashier: Sorry, the card machine doesn't work today. || Lo siento, el datáfono no funciona hoy.
+ No problem. Here's fifty thousand in cash. || No hay problema. Aquí tiene cincuenta mil en efectivo.
- No problem. I don't have enough card. || No hay problema. No tengo suficiente tarjeta. || No tiene sentido.
Cashier: Here's your change, five thousand. || Aquí está su cambio, cinco mil.
+ Thank you. Have a nice day! || Gracias. ¡Que tenga un buen día!
- Keep the receipt of the change. || Guarde el recibo del cambio. || No es una respuesta natural.
"""),
     ],
     writes="""
Es demasiado caro. | It's too expensive. | It is too expensive.
¿Puedo pagar con tarjeta? | Can I pay by card? | Can I pay with a card? ; Could I pay by card?
No tengo suficiente dinero. | I don't have enough money. | I do not have enough money.
""",
     dictations="""
I'd like to return this, it doesn't work. || Quisiera devolver esto, no funciona.
Everything is on sale this weekend. || Todo está en oferta este fin de semana.
""")
