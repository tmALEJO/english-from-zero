# A1 · Parte 1 (unidades 8–14)
# Formato de cada palabra:  inglés | español | emoji | suena como | consejo
# Frases de diálogos/historias:  inglés || español

unit("u08-preguntas", "A1", "Haciendo preguntas", "❓",
     "Ya puedo hacer preguntas sobre la rutina de otros",
     "Preguntar con do y does, responder con sí o no, y decir lo que NO haces.",
     grammar=["Do / Does", "Negativo: don't / doesn't"],
     items="""
Do you work? | ¿Trabajas? | 💼 | du iu uérk
Does she study? | ¿Ella estudia? | 📚 | das shi stádi
Yes, I do | Sí (respuesta a do) | 👍
No, I don't | No (respuesta a do) | 👎 | nóu, ai dóunt
Yes, she does | Sí, ella sí | 🙆‍♀️
No, he doesn't | No, él no | 🙅‍♂️ | nóu, ji dásent
I don't know | No sé | 🤷 | ai dóunt nóu
What do you do? | ¿A qué te dedicas? | 🧑‍🔧 | uát du iu dú
Where do you live? | ¿Dónde vives? | 🏘️
I live in Pasto | Vivo en Pasto | 📍 | ai liv in pasto
live | vivir | 🏡 | liv
read | leer | 📖 | riid
write | escribir | ✍️ | ráit
cook | cocinar | 👩‍🍳 | kuk
play | jugar / tocar (música) | 🎮 | pléi
listen to music | escuchar música | 🎧 | lísen tu miúsik
walk | caminar | 🚶‍♀️ | uók
run | correr | 🏃 | ran
drive | manejar | 🚙 | dráiv
take the bus | tomar el bus | 🚌
do homework | hacer la tarea | 📝
always | siempre | 🔁 | ól-ueis
usually | normalmente | 🗓️ | iú-shua-li
sometimes | a veces | 🎲 | sám-taims
never | nunca | 🚫 | né-ver
on weekends | los fines de semana | 🛋️
after work | después del trabajo | 🌇
before breakfast | antes del desayuno | 🥣
""",
     extras=[
         D("Preguntas con do / does",
           "Mira cómo se pregunta en inglés. Fíjate en la primera palabra.",
           """
Do you work? || ¿Trabajas? || Do
Do they live here? || ¿Ellos viven aquí? || Do
Does she cook? || ¿Ella cocina? || Does
Does he play football? || ¿Él juega fútbol? || Does
Do we study today? || ¿Estudiamos hoy? || Do
Does it work? || ¿Funciona? || Does
""",
           "¿Cuándo se usa does?",
           ["Con he, she, it", "Con I y you", "En el pasado"], 0,
           "Para preguntar en presente simple se pone do o does al principio. Does va con he, she, it; do con I, you, we, they. Ojo: con does el verbo pierde la -s: Does she cook? (no cooks).",
           """
Do you read? Yes, I do. || ¿Lees? Sí.
Does she drive? No, she doesn't. || ¿Ella maneja? No.
""",
           fills="""
___ you live in Pasto? | Do / Does | 0 | ¿Vives en Pasto?
___ he work on weekends? | Do / Does | 1 | ¿Él trabaja los fines de semana?
Does she ___ coffee? | like / likes | 0 | ¿A ella le gusta el café? | Con does el verbo va sin -s.
___ they play football? | Do / Does | 0 | ¿Ellos juegan fútbol?
"""),
         D("Negativo: don't / doesn't",
           "Ahora mira cómo se dice lo que NO se hace.",
           """
I don't drive. || No manejo. || don't
You don't cook. || Tú no cocinas. || don't
She doesn't drink coffee. || Ella no toma café. || doesn't
He doesn't work on weekends. || Él no trabaja los fines de semana. || doesn't
We don't watch TV. || No vemos televisión. || don't
""",
           "¿Qué pasa con el verbo después de doesn't?",
           ["Lleva -s", "Queda sin -s", "Cambia a pasado"], 1,
           "Para negar se usa don't (do not) o doesn't (does not) antes del verbo. Después de doesn't el verbo queda en su forma simple: She doesn't drink (no drinks).",
           """
I don't know. || No sé.
He doesn't live here. || Él no vive aquí.
""",
           fills="""
She ___ drive. | don't / doesn't | 1 | Ella no maneja.
I ___ cook on Mondays. | don't / doesn't | 0 | No cocino los lunes.
He doesn't ___ TV. | watch / watches | 0 | Él no ve televisión.
They ___ live in Bogotá. | don't / doesn't | 0 | Ellos no viven en Bogotá.
"""),
         tip("🔁", "¿Con qué frecuencia?", "always, usually, sometimes y never van ANTES del verbo: I always walk to work. Pero después de am/is/are: She is never tired."),
         dialogue("Conociendo a un compañero", "☕ En la cafetería del trabajo.", """
Ana: What do you do, Leo? || ¿A qué te dedicas, Leo?
Leo: I'm a student. I study English. || Soy estudiante. Estudio inglés.
Ana: Do you work too? || ¿También trabajas?
Leo: Yes, I do. I work on weekends. || Sí. Trabajo los fines de semana.
Ana: Where do you live? || ¿Dónde vives?
Leo: I live in Pasto. And you? || Vivo en Pasto. ¿Y tú?
"""),
         story("Dos hermanos muy diferentes", "👬", """
Tom and Ben are brothers, but they are very different. || Tom y Ben son hermanos, pero son muy diferentes.
Tom always wakes up early. He runs before breakfast. || Tom siempre se despierta temprano. Corre antes del desayuno.
Ben never runs. He usually sleeps until ten. || Ben nunca corre. Normalmente duerme hasta las diez.
Tom doesn't watch TV. He reads books after work. || Tom no ve televisión. Lee libros después del trabajo.
Ben doesn't read. He plays video games and listens to music. || Ben no lee. Juega videojuegos y escucha música.
Do they like the same food? Yes, they do. They both love pizza! || ¿Les gusta la misma comida? Sí. ¡A los dos les encanta la pizza!
""", questions=[
             ("¿Quién corre antes del desayuno?", ["Tom", "Ben", "Los dos"], 0),
             ("¿Qué hace Ben después del trabajo?", ["Lee libros", "Juega videojuegos y escucha música", "Corre"], 1),
             ("¿Qué comida les gusta a los dos?", ["Pizza", "Sopa", "Arroz"], 0),
         ]),
         roleplay("Una entrevista corta", "🎤 Una compañera te hace preguntas para una encuesta.", """
Mia: Hi! Can I ask you some questions? || ¡Hola! ¿Te puedo hacer unas preguntas?
+ Sure! || ¡Claro!
- I don't know. || No sé. || No tiene sentido como respuesta a "¿puedo preguntarte?".
Mia: Do you work or study? || ¿Trabajas o estudias?
+ I study. I'm a student. || Estudio. Soy estudiante.
- Yes, she does. || Sí, ella sí. || La pregunta es sobre ti, no sobre ella.
Mia: Do you cook at home? || ¿Cocinas en casa?
+ Yes, I do. I cook every day. || Sí. Cocino todos los días.
- Yes, I cook every day yesterday. || Sí, cocino todos los días ayer. || "yesterday" (ayer) no va con una rutina.
Mia: Thank you! Have a nice day. || ¡Gracias! Que tengas un buen día.
+ You too! Bye! || ¡Igualmente! ¡Chao!
- You're welcome tomorrow. || De nada mañana. || No tiene sentido aquí.
"""),
     ],
     writes="""
¿Trabajas los fines de semana? | Do you work on weekends?
Ella no maneja. | She doesn't drive. | She does not drive.
Nunca veo televisión. | I never watch TV.
""",
     dictations="""
Where do you live? || ¿Dónde vives?
He doesn't work on weekends. || Él no trabaja los fines de semana.
""",
     speak="""
I live in Pasto. I usually walk to work. || Vivo en Pasto. Normalmente camino al trabajo.
""")

unit("u09-hora", "A1", "La hora y los días", "🗓️",
     "Ya puedo decir la hora y acordar una cita",
     "Días, meses, la hora y las preposiciones at, on, in para decir cuándo pasa algo.",
     grammar=["Preposiciones de tiempo: at / on / in"],
     items="""
What time is it? | ¿Qué hora es? | ⌚ | uát táim is it
It's three o'clock | Son las tres en punto | 🕒 | its zrí o-klók
It's half past four | Son las cuatro y media | 🕟
It's a quarter to six | Son las seis menos cuarto | 🕠
in the afternoon | por la tarde | 🌤️
at night | en la noche | 🌃
today | hoy | 📍 | tu-déi
tomorrow | mañana (el día siguiente) | ➡️ | tu-mó-rou
yesterday | ayer | ⬅️ | iés-ter-dei
week | semana | 📅 | uíik
month | mes | 🗓️ | manz
year | año | 🎆 | íer
Monday | lunes | 1️⃣ | mán-dei
Tuesday | martes | 2️⃣ | tiús-dei
Wednesday | miércoles | 3️⃣ | uéns-dei | La primera d no suena.
Thursday | jueves | 4️⃣ | zérs-dei
Friday | viernes | 5️⃣ | frái-dei
Saturday | sábado | 6️⃣ | sá-ter-dei
Sunday | domingo | ☀️ | sán-dei
January | enero | ❄️ | yá-niu-e-ri
April | abril | 🌷
July | julio | 🏖️ | yu-lái
December | diciembre | 🎄 | di-sém-ber
birthday | cumpleaños | 🎂 | bérz-dei
early | temprano | 🐓 | ér-li
late | tarde (con retraso) | 🐢 | léit
See you on Monday | Nos vemos el lunes | 👋
What day is it today? | ¿Qué día es hoy? | 📆
appointment | cita | 🩺 | a-póint-ment
""",
     extras=[
         D("at, on, in para el tiempo",
           "Fíjate qué palabra va antes de horas, días y meses.",
           """
at seven o'clock || a las siete || at
at night || en la noche || at
on Monday || el lunes || on
on my birthday || en mi cumpleaños || on
in July || en julio || in
in the morning || por la mañana || in
""",
           "¿Qué va antes de un día de la semana?",
           ["at", "on", "in"], 1,
           "at → horas exactas y at night. on → días y fechas (on Monday, on my birthday). in → meses, años y partes del día (in July, in the morning). Y los días y meses siempre se escriben con mayúscula.",
           """
I work on Monday at eight in the morning. || Trabajo el lunes a las ocho de la mañana.
""",
           fills="""
The class is ___ nine o'clock. | at / on / in | 0 | La clase es a las nueve.
My birthday is ___ April. | at / on / in | 2 | Mi cumpleaños es en abril.
See you ___ Friday! | at / on / in | 1 | ¡Nos vemos el viernes!
I sleep ___ night. | at / on / in | 0 | Duermo en la noche.
"""),
         tip("🕰️", "Leer la hora", "o'clock = en punto. half past = y media. quarter past = y cuarto. quarter to = menos cuarto. También se dice fácil: It's four thirty (4:30)."),
         dialogue("Pidiendo una cita", "📞 Llamas al consultorio.", """
Receptionist: Good morning, City Clinic. || Buenos días, Clínica City.
You: Hi. I'd like an appointment, please. || Hola. Quisiera una cita, por favor.
Receptionist: Is Tuesday OK? || ¿Le sirve el martes?
You: Tuesday is good. What time? || El martes está bien. ¿A qué hora?
Receptionist: At half past ten in the morning. || A las diez y media de la mañana.
You: Perfect. Thank you! || Perfecto. ¡Gracias!
"""),
         story("La semana de Eva", "📅", """
Eva is very busy. On Monday she works from eight to five. || Eva está muy ocupada. El lunes trabaja de ocho a cinco.
On Tuesday and Thursday she studies English at night. || El martes y el jueves estudia inglés en la noche.
On Wednesday she cooks for her family. || El miércoles cocina para su familia.
On Friday she goes to the cinema with friends. || El viernes va al cine con amigos.
On Saturday she sleeps late. On Sunday she visits her grandmother. || El sábado duerme hasta tarde. El domingo visita a su abuela.
Her birthday is in December. She is very happy in December! || Su cumpleaños es en diciembre. ¡Está muy feliz en diciembre!
""", questions=[
             ("¿Cuándo estudia inglés Eva?", ["Lunes y miércoles", "Martes y jueves en la noche", "Los domingos"], 1),
             ("¿Qué hace el domingo?", ["Duerme tarde", "Va al cine", "Visita a su abuela"], 2),
             ("¿En qué mes es su cumpleaños?", ["Diciembre", "Abril", "Julio"], 0),
         ]),
         roleplay("¿Nos vemos?", "📱 Un amigo te escribe para verse.", """
Sam: Hey! Are you free tomorrow? || ¡Hola! ¿Estás libre mañana?
+ Yes! What time? || ¡Sí! ¿A qué hora?
- Yes, yesterday. || Sí, ayer. || "Ayer" no responde a "¿estás libre mañana?".
Sam: At six in the evening? || ¿A las seis de la tarde?
+ Six is late for me. Is five OK? || Las seis es tarde para mí. ¿Te sirve a las cinco?
- It's half past January. || Son enero y media. || Mezcla la hora con un mes.
Sam: Five is perfect. See you tomorrow! || Las cinco es perfecto. ¡Nos vemos mañana!
+ See you tomorrow! || ¡Nos vemos mañana!
- See you on yesterday! || ¡Nos vemos el ayer! || Se dice "See you tomorrow".
"""),
     ],
     writes="""
¿Qué hora es? | What time is it?
Mi cumpleaños es en julio. | My birthday is in July.
Nos vemos el lunes. | See you on Monday.
""",
     dictations="""
It's half past four. || Son las cuatro y media.
I have an appointment on Tuesday. || Tengo una cita el martes.
""")

unit("u10-casa", "A1", "Mi casa", "🏠",
     "Ya puedo describir dónde vivo",
     "Las partes de la casa, los muebles y cómo decir qué hay (there is / there are).",
     grammar=["There is / there are", "Preposiciones de lugar: in, on, under, next to"],
     items="""
kitchen | cocina | 🍳 | kí-chen
bedroom | habitación / cuarto | 🛏️ | béd-rum
bathroom | baño | 🛁 | báz-rum
living room | sala | 🛋️ | lí-ving rum
garden | jardín | 🌻 | gár-den
door | puerta | 🚪 | dór
window | ventana | 🪟 | uín-dou
table | mesa | 🪑 | téi-bol
chair | silla | 💺 | chér
bed | cama | 🛌 | bed
sofa | sofá | 🛋️ | sóu-fa
lamp | lámpara | 💡 | lamp
fridge | nevera | 🧊 | frich
shower | ducha | 🚿 | sháu-er
mirror | espejo | 🪞 | mí-ror
key | llave | 🔑 | kíi
stairs | escaleras | 🪜 | stérs
floor | piso / suelo | 🟫 | flór
wall | pared | 🧱 | uól
apartment | apartamento | 🏢 | a-párt-ment
There is a sofa | Hay un sofá | 🛋️ | dér is a sóu-fa
There are two beds | Hay dos camas | 🛏️
Is there a garden? | ¿Hay jardín? | 🌻
in | dentro de / en | 📥
on | sobre / encima de | 🔝
under | debajo de | ⬇️ | án-der
next to | al lado de | ↔️ | nekst tu
between | entre | 🔀 | bi-tuíin
big | grande | 🐘 | big
small | pequeño | 🐭 | smól
""",
     extras=[
         D("There is / there are",
           "Mira cómo se dice 'hay' en inglés.",
           """
There is a sofa in the living room. || Hay un sofá en la sala. || There is
There is a lamp on the table. || Hay una lámpara sobre la mesa. || There is
There are two bedrooms. || Hay dos habitaciones. || There are
There are three chairs in the kitchen. || Hay tres sillas en la cocina. || There are
Is there a garden? || ¿Hay jardín? || Is there
""",
           "¿Cuándo se usa there are?",
           ["Con una sola cosa", "Con varias cosas (plural)", "Para preguntar siempre"], 1,
           "En inglés 'hay' cambia según la cantidad: there is + una cosa (there is a bed), there are + varias (there are two beds). Para preguntar se invierte: Is there…? Are there…?",
           """
There's a key on the table. || Hay una llave sobre la mesa.
Are there stairs? || ¿Hay escaleras?
""",
           fills="""
___ a fridge in the kitchen. | There is / There are | 0 | Hay una nevera en la cocina.
___ four windows in my bedroom. | There is / There are | 1 | Hay cuatro ventanas en mi cuarto.
___ there a shower? | Is / Are | 0 | ¿Hay ducha?
The cat is ___ the bed. | under / between | 0 | El gato está debajo de la cama.
"""),
         dialogue("Buscando apartamento", "🏢 Visitas un apartamento para arrendar.", """
Owner: Welcome! This is the living room. || ¡Bienvenido! Esta es la sala.
You: It's big! How many bedrooms are there? || ¡Es grande! ¿Cuántas habitaciones hay?
Owner: There are two bedrooms and one bathroom. || Hay dos habitaciones y un baño.
You: Is there a garden? || ¿Hay jardín?
Owner: No, there isn't. But there is a big window. || No, no hay. Pero hay una ventana grande.
You: I like it! || ¡Me gusta!
"""),
         story("¿Dónde están mis llaves?", "🔑", """
Leo is late for work. Where are his keys? || Leo va tarde al trabajo. ¿Dónde están sus llaves?
He looks in the kitchen. The keys are not on the table. || Busca en la cocina. Las llaves no están sobre la mesa.
He looks in the bedroom. There are books on the bed, but no keys. || Busca en la habitación. Hay libros sobre la cama, pero no hay llaves.
He looks in the bathroom, next to the mirror. Nothing! || Busca en el baño, al lado del espejo. ¡Nada!
Then he sees his cat under the sofa. The cat is playing with the keys! || Entonces ve a su gato debajo del sofá. ¡El gato está jugando con las llaves!
""", questions=[
             ("¿Qué busca Leo?", ["Su celular", "Sus llaves", "Su gato"], 1),
             ("¿Qué hay sobre la cama?", ["Libros", "Llaves", "Una lámpara"], 0),
             ("¿Dónde están las llaves al final?", ["En la cocina", "Con el gato, debajo del sofá", "Al lado del espejo"], 1),
         ]),
         roleplay("Describe tu casa", "🏠 Un amigo nuevo te pregunta por tu casa.", """
Jake: Do you live in a house or an apartment? || ¿Vives en una casa o en un apartamento?
+ I live in an apartment. || Vivo en un apartamento.
- I live in a kitchen. || Vivo en una cocina. || Una cocina es una parte de la casa.
Jake: Is it big? || ¿Es grande?
+ No, it's small, but there is a nice window. || No, es pequeño, pero hay una ventana bonita.
- Yes, there are a window. || Sí, hay una ventana. || Con una sola cosa es "there is".
Jake: Cool! How many bedrooms are there? || ¡Genial! ¿Cuántas habitaciones hay?
+ There are two bedrooms. || Hay dos habitaciones.
- There is two bedrooms. || Hay dos habitaciones. || Con plural es "there are".
"""),
     ],
     writes="""
Hay una lámpara sobre la mesa. | There is a lamp on the table. | There's a lamp on the table.
Hay dos baños. | There are two bathrooms.
¿Hay jardín? | Is there a garden?
""",
     dictations="""
The keys are next to the door. || Las llaves están al lado de la puerta.
There are three chairs in the kitchen. || Hay tres sillas en la cocina.
""")

unit("u11-ropa", "A1", "Ropa y compras", "🛍️",
     "Ya puedo comprar ropa y pedir otra talla",
     "La ropa, las tallas, cómo pedir probarte algo y señalar con this, that, these, those.",
     grammar=["This / that / these / those"],
     items="""
shirt | camisa | 👔 | shert
T-shirt | camiseta | 👕 | tíi-shert
pants | pantalón | 👖 | pants
jeans | jeans / bluyín | 👖 | yíins
dress | vestido | 👗 | dres
skirt | falda | 👗 | skert
shoes | zapatos | 👞 | shúus
sneakers | tenis | 👟 | sníi-kers
jacket | chaqueta | 🧥 | yá-ket
hat | sombrero / gorra | 👒 | jat
socks | medias | 🧦 | soks
bag | bolso | 👜 | bag
size | talla | 📏 | sáis
small | pequeño (talla S) | 🔹
medium | mediano (talla M) | 🔷 | mí-di-um
large | grande (talla L) | 🔶 | larch
Can I try it on? | ¿Me lo puedo probar? | 🪞 | kan ai trái it on
Do you have a smaller size? | ¿Tiene una talla más pequeña? | ⬇️
Do you have it in black? | ¿Lo tiene en negro? | ⚫
It's too big | Me queda muy grande | 🎈
It's too small | Me queda muy pequeño | 🤏
It fits well | Me queda bien | ✅
I'll take it | Me lo llevo | 🛒 | ail téik it
How much are these? | ¿Cuánto cuestan estos? | 🏷️
this | este / esta (cerca, uno) | 👇 | dis
that | ese / aquel (lejos, uno) | 👉 | dat
these | estos / estas (cerca, varios) | 👇👇 | díis
those | esos / aquellos (lejos, varios) | 👉👉 | dóus
cash | efectivo | 💵 | cash
credit card | tarjeta de crédito | 💳
""",
     extras=[
         D("this, that, these, those",
           "Mira la distancia y la cantidad en cada frase.",
           """
This shirt is nice. (en mi mano) || Esta camisa es bonita. || This
That jacket is expensive. (allá) || Esa chaqueta es cara. || That
These shoes are small. (aquí, varios) || Estos zapatos son pequeños. || These
Those socks are cheap. (allá, varios) || Esas medias son baratas. || Those
""",
           "¿Cuál usas para varias cosas que están lejos?",
           ["this", "these", "those"], 2,
           "this = una cosa cerca; that = una cosa lejos; these = varias cerca; those = varias lejos. En inglés no cambian por masculino o femenino: this shirt, this dress.",
           """
I like this hat, but I don't like those shoes. || Me gusta este sombrero, pero no me gustan esos zapatos.
""",
           fills="""
How much is ___ dress? (en tu mano) | this / these | 0 | ¿Cuánto cuesta este vestido?
___ sneakers are great! (aquí, varios) | This / These | 1 | ¡Estos tenis son geniales!
Can I see ___ jacket over there? | that / those | 0 | ¿Puedo ver esa chaqueta de allá?
___ socks are too big. (allá) | That / Those | 1 | Esas medias son muy grandes.
"""),
         dialogue("En la tienda de ropa", "🛍️ Quieres comprar una chaqueta.", """
Clerk: Hi! Can I help you? || ¡Hola! ¿Le puedo ayudar?
You: Yes, please. How much is this jacket? || Sí, por favor. ¿Cuánto cuesta esta chaqueta?
Clerk: It's forty dollars. || Cuesta cuarenta dólares.
You: Can I try it on? || ¿Me la puedo probar?
Clerk: Of course. What size are you? || Claro. ¿Qué talla es usted?
You: Medium. Oh no, it's too big. Do you have a smaller size? || Mediana. Ay no, me queda muy grande. ¿Tiene una talla más pequeña?
Clerk: Here is a small. || Aquí tiene una pequeña.
You: It fits well. I'll take it! || Me queda bien. ¡Me la llevo!
"""),
         story("El regalo de cumpleaños", "🎁", """
It's Lia's birthday on Saturday. Her brother Tom wants a present for her. || El cumpleaños de Lia es el sábado. Su hermano Tom quiere un regalo para ella.
He goes to a store. He sees a red dress and a black bag. || Va a una tienda. Ve un vestido rojo y un bolso negro.
The dress is beautiful, but it's very expensive. || El vestido es hermoso, pero es muy caro.
The bag is cheap and Lia loves black. || El bolso es barato y a Lia le encanta el negro.
Tom pays in cash. "I'll take this bag, please." || Tom paga en efectivo. "Me llevo este bolso, por favor."
On Saturday, Lia opens the present. She is very happy! || El sábado, Lia abre el regalo. ¡Está muy feliz!
""", questions=[
             ("¿Para quién es el regalo?", ["Para Tom", "Para Lia", "Para su mamá"], 1),
             ("¿Por qué no compra el vestido?", ["Es muy caro", "Es feo", "Es pequeño"], 0),
             ("¿Cómo paga Tom?", ["Con tarjeta", "En efectivo", "No paga"], 1),
         ]),
         roleplay("Cambiar la talla", "👟 Te pruebas unos tenis en la tienda.", """
Clerk: How are the sneakers? || ¿Qué tal los tenis?
+ They're too small. Do you have a bigger size? || Me quedan pequeños. ¿Tiene una talla más grande?
- I'm too small. || Yo soy muy pequeño. || Hablas de ti, no de los tenis.
Clerk: Yes, here you are. || Sí, aquí tiene.
+ Thank you. They fit well! || Gracias. ¡Me quedan bien!
- They fit well yesterday. || Me quedaron bien ayer. || Te los estás probando ahora.
Clerk: Cash or credit card? || ¿Efectivo o tarjeta?
+ Credit card, please. || Con tarjeta, por favor.
- Yes, please. || Sí, por favor. || Te preguntaron cuál de las dos opciones.
"""),
     ],
     writes="""
¿Me lo puedo probar? | Can I try it on?
Estos zapatos me quedan muy pequeños. | These shoes are too small.
Me lo llevo. | I'll take it. | I will take it.
""",
     dictations="""
Do you have it in black? || ¿Lo tiene en negro?
How much are these shoes? || ¿Cuánto cuestan estos zapatos?
""")

unit("u12-habilidades", "A1", "Lo que sé hacer", "🎸",
     "Ya puedo decir lo que sé y no sé hacer",
     "Deportes, hobbies y el verbo can para hablar de habilidades y pedir permiso.",
     grammar=["Can / can't"],
     items="""
I can swim | Sé nadar | 🏊 | ai kan suím
I can't dance | No sé bailar | 🙅 | ai kant dans
Can you sing? | ¿Sabes cantar? | 🎤
swim | nadar | 🏊‍♀️ | suím
dance | bailar | 💃 | dans
sing | cantar | 🎤 | sing
draw | dibujar | 🎨 | dró
paint | pintar | 🖌️ | péint
ride a bike | montar en bicicleta | 🚲 | ráid a báik
play football | jugar fútbol | ⚽
play basketball | jugar baloncesto | 🏀
play the guitar | tocar la guitarra | 🎸 | pléi de gi-tár
play the piano | tocar el piano | 🎹
speak English | hablar inglés | 🗣️
take photos | tomar fotos | 📷
climb | escalar / trepar | 🧗 | kláim
jump | saltar | 🦘 | yamp
fly | volar | 🕊️ | flái
fix a computer | arreglar un computador | 🛠️
very well | muy bien | 🌟
a little | un poco | 🤏
not at all | para nada | ❌
hobby | pasatiempo | 🧩 | jó-bi
team | equipo | 👥 | tíim
game | juego / partido | 🎲 | guéim
Can I open the window? | ¿Puedo abrir la ventana? | 🪟
Can you help me? | ¿Me puedes ayudar? | 🙏
Sure! | ¡Claro! | 👌 | shúr
""",
     extras=[
         D("Can / can't",
           "Lee y escucha. ¿Notas algo raro en el verbo después de can?",
           """
I can swim. || Sé nadar. || can
She can sing very well. || Ella canta muy bien. || can
He can't dance. || Él no sabe bailar. || can't
We can play the guitar. || Sabemos tocar la guitarra. || can
Can you draw? Yes, I can. || ¿Sabes dibujar? Sí. || Can
""",
           "Después de can, el verbo…",
           ["Lleva -s con he y she", "Siempre queda igual", "Va con to"], 1,
           "can sirve para habilidades (saber hacer) y para pedir permiso o ayuda. Es igual para todas las personas y el verbo siguiente nunca cambia: She can swim (no cans ni swims). Negativo: can't. Pregunta: Can you…?",
           """
Can I help you? || ¿Le puedo ayudar?
My brother can't swim. || Mi hermano no sabe nadar.
""",
           fills="""
She can ___ the piano. | play / plays | 0 | Ella sabe tocar el piano.
I ___ swim. I'm afraid of water. | can / can't | 1 | No sé nadar. Le tengo miedo al agua.
___ you help me, please? | Can / Do | 0 | ¿Me puedes ayudar, por favor?
He ___ speak English very well. | can / cans | 0 | Él habla inglés muy bien.
"""),
         tip("👂", "can vs can't al oído", "can suele sonar corto y débil (kən): I kən swim. can't suena fuerte y claro (kant): I KANT swim. Escucha el volumen, no solo la t final."),
         dialogue("En la clase de música", "🎵 Primer día en un club de música.", """
Teacher: Welcome! Can you play an instrument? || ¡Bienvenido! ¿Sabes tocar algún instrumento?
Leo: I can play the guitar a little. || Sé tocar un poco la guitarra.
Teacher: Great! Can you sing? || ¡Genial! ¿Sabes cantar?
Leo: No, I can't sing at all! || ¡No, no sé cantar para nada!
Teacher: That's OK. You can learn here. || No pasa nada. Aquí puedes aprender.
"""),
         story("El equipo del barrio", "⚽", """
In my neighborhood there is a small football team. || En mi barrio hay un pequeño equipo de fútbol.
Carlos can run very fast. Ana can jump very high. || Carlos corre muy rápido. Ana salta muy alto.
Sam can't play football very well, but he can take great photos. || Sam no juega muy bien fútbol, pero toma fotos excelentes.
On Saturday the team has a big game. || El sábado el equipo tiene un partido importante.
Sam takes photos of every goal. Now he is the team photographer! || Sam toma fotos de cada gol. ¡Ahora es el fotógrafo del equipo!
""", questions=[
             ("¿Qué sabe hacer Ana?", ["Correr rápido", "Saltar muy alto", "Tomar fotos"], 1),
             ("¿Sam juega bien fútbol?", ["Sí, muy bien", "No muy bien"], 1),
             ("¿Cuál es el nuevo papel de Sam?", ["Portero", "Entrenador", "Fotógrafo del equipo"], 2),
         ]),
         roleplay("¿Me ayudas?", "💻 Tu computador no funciona y le pides ayuda a una amiga.", """
You see Mia. || Ves a Mia.
+ Hi Mia! Can you help me? || ¡Hola Mia! ¿Me puedes ayudar?
- Hi Mia! You can't help me. || ¡Hola Mia! No me puedes ayudar. || Así no estás pidiendo ayuda.
Mia: Sure! What's the problem? || ¡Claro! ¿Cuál es el problema?
+ My computer doesn't work. Can you fix it? || Mi computador no funciona. ¿Lo puedes arreglar?
- My computer can swim. || Mi computador sabe nadar. || No tiene sentido.
Mia: I can try. Can I open it? || Puedo intentarlo. ¿Lo puedo abrir?
+ Yes, of course. Thank you! || Sí, claro. ¡Gracias!
- No, I can't. || No, yo no puedo. || Ella pidió permiso; respóndele sí o no a ella.
""".replace("You see Mia. || Ves a Mia.", "Narrador: You see your friend Mia. || Ves a tu amiga Mia.")),
     ],
     writes="""
Sé nadar, pero no sé bailar. | I can swim, but I can't dance. | I can swim but I can't dance.
¿Me puedes ayudar? | Can you help me?
Ella toca muy bien la guitarra. | She can play the guitar very well.
""",
     dictations="""
Can you ride a bike? || ¿Sabes montar en bicicleta?
He can't sing at all. || Él no sabe cantar para nada.
""",
     speak="""
I can speak English a little. || Hablo un poco de inglés.
""")

unit("u13-ciudad", "A1", "Por la ciudad", "🗺️",
     "Ya puedo pedir y dar direcciones",
     "Lugares de la ciudad, cómo preguntar dónde queda algo y cómo indicar el camino.",
     grammar=["Imperativo: turn, go, take", "Preposiciones de lugar"],
     items="""
bank | banco | 🏦 | bank
hospital | hospital | 🏥 | jós-pi-tal
pharmacy | farmacia | 💊 | fár-ma-si
supermarket | supermercado | 🛒 | su-per-már-ket
park | parque | 🌳 | park
church | iglesia | ⛪ | cherch
museum | museo | 🏛️ | miu-síi-um
library | biblioteca | 📚 | lái-bre-ri
post office | oficina de correo | 🏤
bus stop | parada de bus | 🚏
train station | estación de tren | 🚉
airport | aeropuerto | ✈️ | ér-port
hotel | hotel | 🏨 | jou-tél
restaurant | restaurante | 🍽️ | rés-to-rant
street | calle | 🛣️ | stríit
corner | esquina | 📐 | kór-ner
traffic light | semáforo | 🚦 | trá-fik láit
Where is the bank? | ¿Dónde queda el banco? | ❓
Is it far? | ¿Queda lejos? | 🗺️
It's near here | Queda cerca de aquí | 📍 | its níer jíer
Go straight | Siga derecho | ⬆️ | góu stréit
Turn left | Gire a la izquierda | ⬅️ | tern left
Turn right | Gire a la derecha | ➡️ | tern ráit
It's on the left | Está a la izquierda | 👈
It's on the right | Está a la derecha | 👉
across from | enfrente de | ↕️ | a-krós from
behind | detrás de | 🔙 | bi-jáind
in front of | delante de / frente a | 🔜
walk two blocks | camine dos cuadras | 🚶
I'm lost | Estoy perdido | 😵‍💫 | áim lost
""",
     extras=[
         D("Dar instrucciones (imperativo)",
           "Así dan direcciones las personas en la calle. Mira cómo empiezan las frases.",
           """
Go straight. || Siga derecho. || Go
Turn left at the corner. || Gire a la izquierda en la esquina. || Turn
Take the bus number five. || Tome el bus número cinco. || Take
Walk two blocks. || Camine dos cuadras. || Walk
Don't turn right. || No gire a la derecha. || Don't
""",
           "¿Cómo se da una instrucción en inglés?",
           ["Con el verbo al principio, sin persona", "Con you + verbo + -s", "Con can al final"], 0,
           "Para dar instrucciones se usa el verbo solo, al principio y sin sujeto: Turn left. Para decir que NO se haga algo: Don't + verbo. Es la misma forma para usted, tú y ustedes.",
           """
Go straight and turn right at the traffic light. || Siga derecho y gire a la derecha en el semáforo.
""",
           fills="""
___ left at the bank. | Turn / Turns | 0 | Gire a la izquierda en el banco.
___ straight for two blocks. | Go / Goes | 0 | Siga derecho dos cuadras.
The pharmacy is ___ from the park. | across / behind | 0 | La farmacia queda enfrente del parque.
___ take that bus! It's the wrong one. | Don't / Not | 0 | ¡No tome ese bus! Es el equivocado.
"""),
         dialogue("Perdido en el centro", "🗺️ Le preguntas a una señora en la calle.", """
You: Excuse me. Where is the train station? || Disculpe. ¿Dónde queda la estación de tren?
Woman: Go straight and turn left at the traffic light. || Siga derecho y gire a la izquierda en el semáforo.
You: Is it far? || ¿Queda lejos?
Woman: No, it's near here. Walk two blocks. It's on the right, across from the park. || No, queda cerca. Camine dos cuadras. Está a la derecha, enfrente del parque.
You: Thank you very much! || ¡Muchas gracias!
Woman: You're welcome. || Con gusto.
"""),
         story("Un día en una ciudad nueva", "🏙️", """
Lia is in London for the first time. She is very excited. || Lia está en Londres por primera vez. Está muy emocionada.
In the morning she visits a museum near her hotel. || Por la mañana visita un museo cerca de su hotel.
Then she wants to go to the park, but she is lost. || Luego quiere ir al parque, pero está perdida.
She asks a man: "Excuse me, where is the park?" || Le pregunta a un señor: "Disculpe, ¿dónde queda el parque?"
"Go straight and turn right. It's behind the church." || "Siga derecho y gire a la derecha. Está detrás de la iglesia."
She finds the park and eats a sandwich under a big tree. || Encuentra el parque y se come un sándwich debajo de un árbol grande.
""", questions=[
             ("¿Dónde está Lia?", ["En Londres", "En Nueva York", "En Pasto"], 0),
             ("¿Qué visita por la mañana?", ["Un parque", "Un museo", "Un banco"], 1),
             ("¿Dónde queda el parque?", ["Detrás de la iglesia", "Al lado del hotel", "Enfrente del museo"], 0),
         ]),
         roleplay("Ayuda a un turista", "🧳 Un turista te pregunta por una farmacia. Está a dos cuadras, a la izquierda.", """
Tourist: Excuse me, is there a pharmacy near here? || Disculpe, ¿hay una farmacia cerca de aquí?
+ Yes, there is. Walk two blocks. || Sí, hay una. Camine dos cuadras.
- Yes, I'm a pharmacy. || Sí, soy una farmacia. || Tú no eres la farmacia.
Tourist: Do I turn right? || ¿Giro a la derecha?
+ No, turn left. It's on the left. || No, gire a la izquierda. Está a la izquierda.
- No, turns left. || No, gira a la izquierda. || Para instrucciones el verbo va sin -s: turn.
Tourist: Thank you so much! || ¡Muchísimas gracias!
+ You're welcome. Have a nice day! || Con gusto. ¡Que tenga un buen día!
- I'm lost. || Estoy perdido. || El perdido es el turista.
"""),
     ],
     writes="""
¿Dónde queda el banco? | Where is the bank? | Where's the bank?
Gire a la derecha en la esquina. | Turn right at the corner.
Estoy perdido. | I'm lost. | I am lost.
""",
     dictations="""
It's across from the supermarket. || Queda enfrente del supermercado.
Go straight and turn left. || Siga derecho y gire a la izquierda.
""")

unit("u14-ahora", "A1", "Lo que pasa ahora", "📱",
     "Ya puedo contar lo que estoy haciendo ahora mismo",
     "El presente continuo para lo que pasa en este momento, y la diferencia con la rutina.",
     grammar=["Presente continuo: I'm working", "Presente simple vs continuo"],
     items="""
I'm working | Estoy trabajando | 💻 | áim uér-king
She's sleeping | Ella está durmiendo | 😴
What are you doing? | ¿Qué estás haciendo? | 🤔 | uát ar iu dú-ing
I'm cooking dinner | Estoy cocinando la cena | 🍝
They're watching a movie | Están viendo una película | 🎬
It's raining | Está lloviendo | 🌧️ | its réi-ning
now | ahora | ⏱️ | náu
right now | ahora mismo | ⚡ | ráit náu
at the moment | en este momento | 🕐
wait | esperar | ⏳ | uéit
call | llamar (por teléfono) | 📞 | kól
text | escribir un mensaje | 💬 | tekst
send | enviar | 📤 | send
look for | buscar | 🔍 | luk for
talk | hablar / conversar | 🗨️ | tók
sit | sentarse | 🪑
stand | estar de pie | 🧍 | stand
smile | sonreír | 😊 | smáil
cry | llorar | 😢 | krái
laugh | reírse | 😂 | laf
wear | llevar puesto | 🧥 | uér
carry | cargar | 🧳 | ká-ri
open | abrir | 📂 | óu-pen
close | cerrar | 📁 | klóus
busy | ocupado | 📵 | bí-si
free | libre / gratis | 🆓 | fríi
Are you busy? | ¿Estás ocupado? | 📵
I'm on my way | Voy en camino | 🛣️ | áim on mai uéi
""",
     extras=[
         D("Presente continuo (lo que pasa ahora)",
           "Mira lo que la gente está haciendo en este momento.",
           """
I'm cooking dinner right now. || Estoy cocinando la cena ahora mismo. || 'm, cooking
She's talking on the phone. || Ella está hablando por teléfono. || 's, talking
They're watching a movie. || Están viendo una película. || 're, watching
We're waiting for the bus. || Estamos esperando el bus. || 're, waiting
It's raining now. || Está lloviendo ahora. || 's, raining
""",
           "¿Cómo se forma lo que pasa en este momento?",
           ["am/is/are + verbo con -ing", "do/does + verbo", "verbo + -ed"], 0,
           "Esto se llama PRESENTE CONTINUO: am / is / are + verbo con -ing. Es como 'estoy + -ando/-iendo'. Se usa para lo que pasa ahora. Para rutinas sigues usando el presente simple: I work every day, pero I'm working now.",
           """
Every day I walk to work, but today I'm taking the bus. || Todos los días camino al trabajo, pero hoy estoy tomando el bus.
""",
           fills="""
Shh! The baby ___ sleeping. | is / are | 0 | ¡Shh! El bebé está durmiendo.
What are you ___? | do / doing | 1 | ¿Qué estás haciendo?
I ___ to work every day. (rutina) | walk / am walking | 0 | Camino al trabajo todos los días.
Look! It ___ raining. | is / does | 0 | ¡Mira! Está lloviendo.
"""),
         tip("✍️", "Cómo se escribe el -ing", "La mayoría solo agrega -ing (work → working). Si termina en e, se quita la e (smile → smiling). Si es corta y termina en vocal + consonante, se dobla la consonante (sit → sitting, run → running)."),
         dialogue("¿Qué estás haciendo?", "📞 Tu amiga te llama.", """
Mia: Hi! What are you doing? || ¡Hola! ¿Qué estás haciendo?
You: I'm cooking dinner. And you? || Estoy cocinando la cena. ¿Y tú?
Mia: I'm waiting for the bus. It's raining! || Estoy esperando el bus. ¡Está lloviendo!
You: Oh no! Are you wearing a jacket? || ¡Ay no! ¿Llevas chaqueta?
Mia: Yes. Oh, the bus is coming. I'm on my way! || Sí. Ah, ya viene el bus. ¡Voy en camino!
"""),
         story("Una foto en la plaza", "📸", """
This is a photo of the main square on a Sunday. || Esta es una foto de la plaza principal un domingo.
A man is sitting on a chair. He is reading a newspaper. || Un señor está sentado en una silla. Está leyendo el periódico.
Two children are running and laughing. || Dos niños están corriendo y riéndose.
A woman is carrying a big bag. She is looking for her keys. || Una mujer está cargando un bolso grande. Está buscando sus llaves.
A dog is sleeping under a tree. || Un perro está durmiendo debajo de un árbol.
And me? I'm taking the photo, of course! || ¿Y yo? ¡Estoy tomando la foto, claro!
""", questions=[
             ("¿Qué está haciendo el señor?", ["Leyendo el periódico", "Corriendo", "Durmiendo"], 0),
             ("¿Qué busca la mujer?", ["Su perro", "Sus llaves", "Un periódico"], 1),
             ("¿Dónde duerme el perro?", ["En una silla", "Debajo de un árbol", "En el bolso"], 1),
         ]),
         roleplay("Un mensaje de tu jefe", "💬 Tu jefe te llama mientras almuerzas.", """
Boss: Hi! Are you busy? || ¡Hola! ¿Estás ocupado?
+ I'm having lunch right now. || Estoy almorzando ahora mismo.
- I have lunch every day yesterday. || Almuerzo todos los días ayer. || Mezcla rutina y pasado; él pregunta por ahora.
Boss: OK. Can you call me later? || Bueno. ¿Me puedes llamar más tarde?
+ Sure. I'm free at two. || Claro. Estoy libre a las dos.
- Sure. I'm calling you later. || Claro. Te estoy llamando más tarde. || Para planes de luego, aquí suena mejor "I'll call you later".
Boss: Perfect. Enjoy your lunch! || Perfecto. ¡Disfruta tu almuerzo!
+ Thank you! || ¡Gracias!
- You're welcome! || ¡De nada! || Él te deseó algo; se responde "Thank you".
"""),
     ],
     writes="""
¿Qué estás haciendo? | What are you doing?
Estoy esperando el bus. | I'm waiting for the bus. | I am waiting for the bus.
Está lloviendo. | It's raining. | It is raining.
""",
     dictations="""
They're watching a movie right now. || Están viendo una película ahora mismo.
I'm on my way. || Voy en camino.
""",
     speak="""
Right now I'm studying English. || Ahora mismo estoy estudiando inglés.
""")
