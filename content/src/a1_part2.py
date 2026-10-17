# A1 · Parte 2 (unidades 15–22)

unit("u15-mercado", "A1", "Comida y mercado", "🧺",
     "Ya puedo hacer el mercado en inglés",
     "Frutas, verduras y alimentos; cuánto y cuántos; some y any.",
     grammar=["Some / any", "How much / how many"],
     items="""
banana | banano | 🍌 | ba-ná-na
orange | naranja (fruta) | 🍊 | ó-ranch
grapes | uvas | 🍇 | gréips
strawberry | fresa | 🍓 | stró-be-ri
pineapple | piña | 🍍 | páin-a-pol
lemon | limón | 🍋 | lé-mon
tomato | tomate | 🍅 | to-méi-tou
potato | papa | 🥔 | po-téi-tou
carrot | zanahoria | 🥕 | ká-rot
onion | cebolla | 🧅 | á-nion
corn | maíz | 🌽 | korn
beans | fríjoles | 🫘 | bíins
egg | huevo | 🥚 | eg
cheese | queso | 🧀 | chíis
milk | leche | 🥛 | milk
meat | carne | 🥩 | míit
fish | pescado | 🐟 | fish
sugar | azúcar | 🍬 | shú-gar
salt | sal | 🧂 | solt
oil | aceite | 🫒 | óil
breakfast | desayuno | 🥣 | brék-fast
lunch | almuerzo | 🍱 | lanch
dinner | cena | 🍽️ | dí-ner
a kilo of | un kilo de | ⚖️
a bottle of | una botella de | 🍾
a bag of | una bolsa de | 🛍️
some | algo de / unos | 🫳 | sam
any | nada de / algún (en preguntas y negativos) | ❔ | é-ni
How many apples? | ¿Cuántas manzanas? | 🔢
How much milk? | ¿Cuánta leche? | 🥛
fresh | fresco | 🌿 | fresh
hungry | con hambre | 😋 | ján-gri
thirsty | con sed | 🥤 | zérs-ti
I'm hungry | Tengo hambre | 🍽️
We need eggs | Necesitamos huevos | 📝
""",
     extras=[
         D("some y any",
           "Mira cuándo aparece some y cuándo any.",
           """
There are some bananas. || Hay unos bananos. || some
I need some milk. || Necesito (algo de) leche. || some
There isn't any cheese. || No hay nada de queso. || any
Do we have any eggs? || ¿Tenemos huevos? || any
We don't have any sugar. || No tenemos azúcar. || any
""",
           "¿Dónde se usa any?",
           ["En frases afirmativas", "En preguntas y negativos", "Solo con frutas"], 1,
           "some = algo de / unos, en frases afirmativas. any = en preguntas (Do you have any…?) y en negativos (There isn't any…). Con cosas que se cuentan se usa How many (how many eggs); con cosas que no se cuentan, How much (how much milk).",
           """
How many potatoes do we need? || ¿Cuántas papas necesitamos?
How much rice is there? || ¿Cuánto arroz hay?
""",
           fills="""
There are ___ grapes in the fridge. | some / any | 0 | Hay unas uvas en la nevera.
We don't have ___ salt. | some / any | 1 | No tenemos sal.
How ___ eggs do you want? | much / many | 1 | ¿Cuántos huevos quieres?
How ___ sugar do you need? | much / many | 0 | ¿Cuánta azúcar necesitas?
"""),
         dialogue("La lista del mercado", "📝 En casa, antes de ir al mercado.", """
Rosa: What do we need for dinner? || ¿Qué necesitamos para la cena?
Tom: We need some potatoes and an onion. || Necesitamos unas papas y una cebolla.
Rosa: Do we have any meat? || ¿Tenemos carne?
Tom: No, we don't have any. And we need a bottle of oil. || No, no hay nada. Y necesitamos una botella de aceite.
Rosa: How many eggs are there? || ¿Cuántos huevos hay?
Tom: Only two. Let's buy a dozen. || Solo dos. Compremos una docena.
"""),
         story("En la plaza de mercado", "🍍", """
Every Saturday, Ana goes to the market with her grandmother. || Todos los sábados, Ana va al mercado con su abuela.
The fruit is fresh and cheap. There are pineapples, strawberries and lemons. || La fruta es fresca y barata. Hay piñas, fresas y limones.
Her grandmother buys a kilo of potatoes, some carrots and some corn. || Su abuela compra un kilo de papas, unas zanahorias y algo de maíz.
"Do you have any fish today?" she asks. "No, sorry, there isn't any fish." || "¿Tiene pescado hoy?", pregunta. "No, lo siento, no hay pescado."
They buy chicken for lunch. Ana is hungry, so they eat a banana. || Compran pollo para el almuerzo. Ana tiene hambre, así que se comen un banano.
""", questions=[
             ("¿Cuándo van al mercado?", ["Todos los domingos", "Todos los sábados", "Todos los días"], 1),
             ("¿Qué no hay hoy?", ["Pollo", "Pescado", "Papas"], 1),
             ("¿Qué compran para el almuerzo?", ["Pollo", "Pescado", "Queso"], 0),
         ]),
         roleplay("En la tienda de la esquina", "🏪 Compras para el desayuno.", """
Seller: Good morning! What do you need? || ¡Buenos días! ¿Qué necesita?
+ Good morning. I need some eggs and milk. || Buenos días. Necesito unos huevos y leche.
- I need any eggs. || Necesito nada de huevos. || En afirmativo se usa "some".
Seller: How many eggs? || ¿Cuántos huevos?
+ Six, please. || Seis, por favor.
- How much eggs. || Cuánto huevos. || Responde con una cantidad.
Seller: Do you need any bread? || ¿Necesita pan?
+ No, thanks. That's all. || No, gracias. Eso es todo.
- Yes, I'm bread. || Sí, soy pan. || Se dice "Yes, please".
"""),
     ],
     writes="""
Tengo hambre. | I'm hungry. | I am hungry.
No tenemos leche. | We don't have any milk. | We do not have any milk. ; We have no milk.
¿Cuántos huevos necesitas? | How many eggs do you need?
""",
     dictations="""
There isn't any cheese in the fridge. || No hay queso en la nevera.
I need a kilo of tomatoes. || Necesito un kilo de tomates.
""")

unit("u16-cuerpo", "A1", "El cuerpo y cómo me siento", "🧍",
     "Ya puedo decir qué me duele y cómo me siento",
     "Las partes del cuerpo, decir que algo te duele y expresar cómo te sientes.",
     grammar=["have / has", "I have a headache"],
     items="""
head | cabeza | 🧠 | jed
face | cara | 🙂 | féis
eye | ojo | 👁️ | ái
ear | oreja / oído | 👂 | íer
nose | nariz | 👃 | nóus
mouth | boca | 👄 | máuz
tooth | diente | 🦷 | tuz
hair | pelo / cabello | 💇 | jér
neck | cuello | 🧣 | nek
arm | brazo | 💪 | arm
hand | mano | ✋ | jand
finger | dedo | ☝️ | fín-ger
leg | pierna | 🦵 | leg
foot | pie | 🦶 | fut
back | espalda | 🔙 | bak
stomach | estómago | 🫃 | stó-mak
heart | corazón | ❤️ | jart
I have a headache | Me duele la cabeza | 🤕 | ai jav a jé-deik
I have a stomachache | Me duele el estómago | 🤢
My back hurts | Me duele la espalda | 😣 | mai bak jerts
I have a cold | Tengo gripa | 🤧 | ai jav a kóuld
I have a fever | Tengo fiebre | 🌡️ | fí-ver
sick | enfermo | 🤒 | sik
tired | cansado | 😩
sad | triste | 😢 | sad
angry | bravo / enojado | 😠 | án-gri
scared | asustado | 😨 | skerd
bored | aburrido | 🥱 | bord
nervous | nervioso | 😬 | nér-vos
I feel better | Me siento mejor | 😌
Get well soon! | ¡Que te mejores! | 💐
doctor | médico | 👩‍⚕️ | dók-tor
medicine | medicina / remedio | 💊 | mé-di-sin
""",
     extras=[
         D("have / has",
           "Mira el verbo 'tener' con cada persona.",
           """
I have a cold. || Tengo gripa. || have
You have green eyes. || Tienes ojos verdes. || have
She has long hair. || Ella tiene el pelo largo. || has
He has a headache. || Él tiene dolor de cabeza. || has
We have two hands. || Tenemos dos manos. || have
""",
           "¿Qué forma de have va con he y she?",
           ["have", "has", "haves"], 1,
           "El verbo tener es have, pero con he, she, it cambia a has (como la -s del presente simple). Para dolores y enfermedades se usa have: I have a fever, she has a cold.",
           """
Does she have a fever? No, she has a cold. || ¿Ella tiene fiebre? No, tiene gripa.
""",
           fills="""
My brother ___ a stomachache. | have / has | 1 | Mi hermano tiene dolor de estómago.
I ___ two sisters. | have / has | 0 | Tengo dos hermanas.
Do you ___ a headache? | have / has | 0 | ¿Te duele la cabeza? | Con do/does va have.
My leg ___. | hurt / hurts | 1 | Me duele la pierna.
"""),
         dialogue("En el médico", "🩺 Vas al médico porque te sientes mal.", """
Doctor: Hello. What's the problem? || Hola. ¿Cuál es el problema?
You: I feel sick. I have a fever and my head hurts. || Me siento enfermo. Tengo fiebre y me duele la cabeza.
Doctor: Do you have a cough? || ¿Tiene tos?
You: Yes, a little. || Sí, un poco.
Doctor: You have a cold. Take this medicine and rest. || Tiene gripa. Tome este medicamento y descanse.
You: Thank you, doctor. || Gracias, doctor.
"""),
         story("Un lunes difícil", "🤒", """
On Monday morning, Sam doesn't feel well. || El lunes por la mañana, Sam no se siente bien.
He has a headache and his throat hurts. || Tiene dolor de cabeza y le duele la garganta.
His mother touches his face. "You have a fever!" || Su mamá le toca la cara. "¡Tienes fiebre!"
Sam doesn't go to school. He stays in bed and drinks hot tea. || Sam no va al colegio. Se queda en la cama y toma té caliente.
His friend Leo sends a message: "Get well soon!" || Su amigo Leo le manda un mensaje: "¡Que te mejores!"
On Wednesday Sam feels better. He is happy, but he is a little bored. || El miércoles Sam se siente mejor. Está feliz, pero un poco aburrido.
""", questions=[
             ("¿Qué le duele a Sam?", ["La cabeza y la garganta", "La pierna", "El estómago"], 0),
             ("¿Qué toma Sam?", ["Jugo frío", "Té caliente", "Leche"], 1),
             ("¿Cómo se siente el miércoles?", ["Peor", "Mejor", "Igual"], 1),
         ]),
         roleplay("Llamar al trabajo", "📞 Estás enfermo y llamas a tu jefa.", """
Boss: Hello? || ¿Aló?
+ Hi, it's me. I'm sorry, I'm sick today. || Hola, soy yo. Lo siento, hoy estoy enfermo.
- Hi, I'm doctor. || Hola, soy médico. || Llamas para avisar que estás enfermo.
Boss: Oh no! What's wrong? || ¡Ay no! ¿Qué te pasa?
+ I have a fever and a headache. || Tengo fiebre y dolor de cabeza.
- I has a fever. || Yo tiene fiebre. || Con I es "have".
Boss: Rest today. Get well soon! || Descansa hoy. ¡Que te mejores!
+ Thank you. See you tomorrow. || Gracias. Nos vemos mañana.
- Get well soon too! || ¡Que te mejores tú también! || Ella no está enferma.
"""),
     ],
     writes="""
Me duele la cabeza. | I have a headache. | My head hurts.
Ella tiene el pelo largo. | She has long hair.
Me siento mejor. | I feel better.
""",
     dictations="""
My back hurts. || Me duele la espalda.
He has a cold and a fever. || Él tiene gripa y fiebre.
""")

unit("u17-clima", "A1", "El clima y las estaciones", "🌦️",
     "Ya puedo hablar del clima y planear según el tiempo",
     "Cómo está el tiempo, las estaciones y qué ponerse según el clima.",
     grammar=["It's + adjetivo para el clima", "What's the weather like?"],
     items="""
weather | clima / tiempo | 🌤️ | ué-der
What's the weather like? | ¿Cómo está el clima? | 🌍
It's sunny | Está soleado | ☀️ | its sá-ni
It's cloudy | Está nublado | ☁️ | its kláu-di
It's windy | Está haciendo viento | 🌬️ | its uín-di
It's hot | Hace calor | 🥵 | its jot
It's cold | Hace frío | 🥶 | its kóuld
It's warm | Está templado / calientito | 🌡️ | its uórm
It's cool | Está fresco | 🍃 | its kúul
It's snowing | Está nevando | 🌨️ | its snóu-ing
rain | lluvia / llover | 🌧️ | réin
snow | nieve | ❄️ | snóu
sun | sol | 🌞 | san
cloud | nube | ☁️ | kláud
storm | tormenta | ⛈️ | storm
rainbow | arcoíris | 🌈 | réin-bou
umbrella | sombrilla / paraguas | ☂️ | am-bré-la
sunglasses | gafas de sol | 🕶️ | sán-gla-ses
coat | abrigo | 🧥 | kóut
scarf | bufanda | 🧣 | skarf
season | estación del año | 🍂 | síi-son
spring | primavera | 🌸 | spring
summer | verano | 🏖️ | sá-mer
autumn | otoño | 🍁 | ó-tom
winter | invierno | ☃️ | uín-ter
degrees | grados | 🌡️ | di-gríis
outside | afuera | 🚪 | áut-said
inside | adentro | 🏠 | ín-said
beach | playa | 🏝️ | bíich
mountain | montaña | ⛰️ | máun-ten
Take an umbrella | Lleva sombrilla | ☂️
It's a beautiful day | Es un día hermoso | 🌻
""",
     extras=[
         D("Hablar del clima con it",
           "Fíjate en cómo empiezan todas estas frases.",
           """
It's sunny today. || Hoy está soleado. || It's
It's very cold in winter. || Hace mucho frío en invierno. || It's
It's raining. Take an umbrella. || Está lloviendo. Lleva sombrilla. || It's
Is it hot in Cartagena? Yes, it is. || ¿Hace calor en Cartagena? Sí. || Is it
It isn't windy. || No está haciendo viento. || isn't
""",
           "¿Cómo empieza casi siempre una frase sobre el clima?",
           ["Con It's / It is", "Con There are", "Con I have"], 0,
           "En inglés el clima siempre lleva sujeto it: It's sunny, It's raining. En español decimos 'hace frío', pero en inglés no se usa make ni have: It's cold (no 'It makes cold').",
           """
What's the weather like in Pasto? It's cool and cloudy. || ¿Cómo está el clima en Pasto? Fresco y nublado.
""",
           fills="""
___ cold today. | It's / It makes | 0 | Hoy hace frío. | En inglés no se dice "it makes cold".
Take your umbrella. It's ___. | raining / rain | 0 | Lleva sombrilla. Está lloviendo.
I love ___. It's hot and I go to the beach. | summer / winter | 0 | Me encanta el verano.
___ the weather like? | What's / How's is | 0 | ¿Cómo está el clima?
"""),
         dialogue("Planes para el fin de semana", "📱 Hablas con un amigo.", """
Leo: What's the weather like tomorrow? || ¿Cómo va a estar el clima mañana?
Mia: It's sunny and warm. Twenty-five degrees! || Soleado y templado. ¡Veinticinco grados!
Leo: Perfect for the beach! || ¡Perfecto para la playa!
Mia: Yes, but take your sunglasses. || Sí, pero lleva tus gafas de sol.
Leo: And on Sunday? || ¿Y el domingo?
Mia: On Sunday it's cloudy and windy. Maybe a storm. || El domingo nublado y con viento. Tal vez tormenta.
"""),
         story("Cuatro estaciones", "🍁", """
Jake lives in Canada. There are four seasons there. || Jake vive en Canadá. Allá hay cuatro estaciones.
In winter it's very cold and it snows a lot. He wears a coat and a scarf. || En invierno hace mucho frío y nieva mucho. Usa abrigo y bufanda.
In spring it's cool and there are flowers everywhere. || En primavera está fresco y hay flores por todas partes.
In summer it's hot. Jake goes to the beach with his family. || En verano hace calor. Jake va a la playa con su familia.
In autumn it's windy and the trees are red and orange. || En otoño hace viento y los árboles son rojos y anaranjados.
Now Jake is in Colombia. "It's always spring here!" he says. || Ahora Jake está en Colombia. "¡Aquí siempre es primavera!", dice.
""", questions=[
             ("¿Qué usa Jake en invierno?", ["Gafas de sol", "Abrigo y bufanda", "Sombrilla"], 1),
             ("¿Cómo son los árboles en otoño?", ["Verdes", "Rojos y anaranjados", "Blancos"], 1),
             ("¿Qué dice Jake de Colombia?", ["Siempre hace frío", "Siempre es primavera", "Siempre llueve"], 1),
         ]),
         roleplay("¿Salimos?", "🚪 Tu amiga quiere salir, pero mira por la ventana.", """
Ana: Let's go to the park! || ¡Vamos al parque!
+ OK! What's the weather like? || ¡Bueno! ¿Cómo está el clima?
- OK! What's the weather like yesterday? || ¡Bueno! ¿Cómo está el clima ayer? || Mezcla presente con ayer.
Ana: It's cloudy. Maybe it's going to rain. || Está nublado. Puede que llueva.
+ Let's take an umbrella. || Llevemos sombrilla.
- Let's take sunglasses. || Llevemos gafas de sol. || Con nubes y lluvia no sirven.
Ana: Good idea. Oh look, a rainbow! || Buena idea. ¡Mira, un arcoíris!
+ Wow, it's beautiful! || ¡Uy, qué hermoso!
- It's snowing. || Está nevando. || No tiene que ver con el arcoíris.
"""),
     ],
     writes="""
Hace calor hoy. | It's hot today. | It is hot today. ; Today it's hot.
¿Cómo está el clima? | What's the weather like? | What is the weather like?
Lleva sombrilla, está lloviendo. | Take an umbrella, it's raining. | Take an umbrella. It's raining.
""",
     dictations="""
It's cloudy and windy today. || Hoy está nublado y hace viento.
In winter it's very cold. || En invierno hace mucho frío.
""")

unit("u18-trabajos", "A1", "Trabajos y profesiones", "👷",
     "Ya puedo decir a qué me dedico y dónde trabajo",
     "Profesiones, lugares de trabajo y el artículo a/an con los oficios.",
     grammar=["a / an con profesiones", "Where do you work?"],
     items="""
teacher | profesor / profesora | 🧑‍🏫 | tíi-cher
nurse | enfermero / enfermera | 👩‍⚕️ | ners
engineer | ingeniero | 👷 | en-yi-níer
lawyer | abogado | ⚖️ | ló-ier
police officer | policía | 👮 | po-líis ó-fi-ser
firefighter | bombero | 🧑‍🚒 | fáier-fái-ter
farmer | agricultor / campesino | 🧑‍🌾 | fár-mer
chef | chef / cocinero | 🧑‍🍳 | shef
waiter | mesero | 🤵 | uéi-ter
driver | conductor | 🚕 | drái-ver
mechanic | mecánico | 🔧 | me-ká-nik
programmer | programador | 👨‍💻 | próu-gra-mer
designer | diseñador | 🎨 | di-sái-ner
artist | artista | 🖼️ | ár-tist
singer | cantante | 🎙️ | sín-ger
dentist | odontólogo | 🦷 | dén-tist
pilot | piloto | 👨‍✈️ | pái-lot
scientist | científico | 🔬 | sái-en-tist
manager | gerente / jefe | 📊 | má-na-yer
boss | jefe | 🧑‍💼 | bos
office | oficina | 🏢 | ó-fis
factory | fábrica | 🏭 | fák-to-ri
store | tienda | 🏬 | stor
job | trabajo / empleo | 💼 | yob
salary | salario | 💰 | sá-la-ri
I'm a nurse | Soy enfermera | 👩‍⚕️
I work in a hospital | Trabajo en un hospital | 🏥
I work from home | Trabajo desde casa | 🏡
I'm looking for a job | Estoy buscando trabajo | 🔎
I love my job | Me encanta mi trabajo | 🥰
help people | ayudar a la gente | 🤝
build | construir | 🏗️ | bild
""",
     extras=[
         D("a / an con las profesiones",
           "En español decimos 'soy ingeniero'. Mira el inglés.",
           """
I'm a teacher. || Soy profesor. || a
She's a nurse. || Ella es enfermera. || a
He's an engineer. || Él es ingeniero. || an
My father is a driver. || Mi papá es conductor. || a
I'm an artist. || Soy artista. || an
""",
           "¿Qué falta en inglés que en español no usamos?",
           ["El artículo a/an antes de la profesión", "La palabra 'work'", "Nada, es igual"], 0,
           "En inglés la profesión lleva a o an: I'm a teacher (no 'I'm teacher'). Se usa an cuando la profesión empieza con sonido de vocal: an engineer, an artist. En plural no lleva artículo: They're doctors.",
           """
What do you do? I'm a programmer. || ¿A qué te dedicas? Soy programador.
""",
           fills="""
My sister is ___ lawyer. | a / an | 0 | Mi hermana es abogada.
He's ___ engineer. | a / an | 1 | Él es ingeniero.
I'm ___ student. | a / — | 0 | Soy estudiante. | En inglés no se puede omitir el artículo.
Where ___ she work? | do / does | 1 | ¿Dónde trabaja ella?
"""),
         dialogue("En una fiesta", "🎉 Conoces a alguien nuevo.", """
Ben: So, what do you do? || Entonces, ¿a qué te dedicas?
Lia: I'm a nurse. I work in a hospital. || Soy enfermera. Trabajo en un hospital.
Ben: Wow! Do you like your job? || ¡Uy! ¿Te gusta tu trabajo?
Lia: Yes, I love it. I help people every day. And you? || Sí, me encanta. Ayudo a la gente todos los días. ¿Y tú?
Ben: I'm a programmer. I work from home. || Soy programador. Trabajo desde casa.
Lia: That's cool! || ¡Qué chévere!
"""),
         story("La familia Gómez", "👨‍👩‍👧‍👦", """
Everyone in the Gómez family works, but they all have different jobs. || Todos en la familia Gómez trabajan, pero todos tienen trabajos diferentes.
Mr. Gómez is a mechanic. He fixes cars in a small garage. || El señor Gómez es mecánico. Arregla carros en un taller pequeño.
Mrs. Gómez is a teacher. She teaches math at a big school. || La señora Gómez es profesora. Enseña matemáticas en un colegio grande.
Their son Andrés is an engineer. He builds bridges. || Su hijo Andrés es ingeniero. Construye puentes.
Their daughter Sofía is a designer. She works from home. || Su hija Sofía es diseñadora. Trabaja desde casa.
And their grandmother? She is a farmer. She has coffee plants! || ¿Y la abuela? Es agricultora. ¡Tiene matas de café!
""", questions=[
             ("¿Qué hace el señor Gómez?", ["Es profesor", "Es mecánico", "Es ingeniero"], 1),
             ("¿Quién trabaja desde casa?", ["Andrés", "Sofía", "La abuela"], 1),
             ("¿Qué cultiva la abuela?", ["Café", "Maíz", "Papa"], 0),
         ]),
         roleplay("Entrevista de trabajo", "💼 Te entrevistan para trabajar en un restaurante.", """
Manager: Nice to meet you. Are you a waiter? || Mucho gusto. ¿Usted es mesero?
+ Yes, I am. I'm a waiter. || Sí. Soy mesero.
- Yes, I'm waiter. || Sí, soy mesero. || Falta el artículo: "a waiter".
Manager: Where do you work now? || ¿Dónde trabaja ahora?
+ I work in a hotel. || Trabajo en un hotel.
- I works in a hotel. || Yo trabaja en un hotel. || Con I el verbo no lleva -s.
Manager: Why do you want this job? || ¿Por qué quiere este trabajo?
+ I love restaurants and I like helping people. || Me encantan los restaurantes y me gusta ayudar a la gente.
- I don't like people. || No me gusta la gente. || No es buena idea en una entrevista.
"""),
     ],
     writes="""
Soy ingeniero. | I'm an engineer. | I am an engineer.
Ella trabaja en una oficina. | She works in an office.
Estoy buscando trabajo. | I'm looking for a job. | I am looking for a job.
""",
     dictations="""
My mother is a nurse. || Mi mamá es enfermera.
He works from home. || Él trabaja desde casa.
""")

unit("u19-transporte", "A1", "Transporte y viajes cortos", "🚌",
     "Ya puedo moverme en bus, taxi y tren",
     "Medios de transporte, comprar un pasaje y preguntar cuánto tarda un viaje.",
     grammar=["by bus / by car / on foot", "How long does it take?"],
     items="""
bus | bus | 🚌 | bas
taxi | taxi | 🚕 | ták-si
train | tren | 🚆 | tréin
plane | avión | ✈️ | pléin
bike | bicicleta | 🚲 | báik
motorcycle | moto | 🏍️ | mó-tor-sái-kol
subway | metro | 🚇 | sáb-uei
ship | barco | 🚢
truck | camión | 🚚 | trak
by bus | en bus | 🚌
by car | en carro | 🚗
on foot | a pie | 🚶
ticket | pasaje / boleto | 🎫 | tí-ket
one-way ticket | pasaje de ida | ➡️
round-trip ticket | pasaje de ida y vuelta | 🔄
seat | puesto / asiento | 💺
platform | andén / plataforma | 🚉 | plát-form
leave | salir / partir | 🛫 | líiv
arrive | llegar | 🛬 | a-ráiv
get on | subirse (al bus) | ⬆️
get off | bajarse (del bus) | ⬇️
How long does it take? | ¿Cuánto se demora? | ⏱️
It takes twenty minutes | Se demora veinte minutos | ⏲️
minute | minuto | ⏱️ | mí-nit
hour | hora | ⌛ | áur | La h no suena: "aur".
fast | rápido | 💨 | fast
slow | lento | 🐌 | slóu
traffic | tráfico / trancón | 🚗🚗 | trá-fik
on time | a tiempo | ✅
Where does this bus go? | ¿A dónde va este bus? | 🚏
Stop here, please | Pare aquí, por favor | 🛑
""",
     extras=[
         D("by bus / on foot",
           "Mira cómo se dice el medio de transporte.",
           """
I go to work by bus. || Voy al trabajo en bus. || by bus
She goes to school by bike. || Ella va al colegio en bicicleta. || by bike
We travel by plane. || Viajamos en avión. || by plane
He goes to the park on foot. || Él va al parque a pie. || on foot
""",
           "Para 'a pie' se dice…",
           ["by foot", "on foot", "in foot"], 1,
           "Para decir cómo viajas se usa by + transporte, sin artículo: by bus, by car, by train. La excepción es a pie: on foot. Para preguntar el tiempo de un viaje: How long does it take? — It takes + tiempo.",
           """
How long does it take by train? It takes two hours. || ¿Cuánto se demora en tren? Se demora dos horas.
""",
           fills="""
I go to work ___ subway. | by / on | 0 | Voy al trabajo en metro.
It ___ thirty minutes. | takes / is | 0 | Se demora treinta minutos.
We go to school ___ foot. | by / on | 1 | Vamos al colegio a pie.
How long ___ it take? | does / is | 0 | ¿Cuánto se demora?
"""),
         dialogue("En la terminal", "🚉 Compras un pasaje de bus a Ipiales.", """
You: Hello. A ticket to Ipiales, please. || Hola. Un pasaje a Ipiales, por favor.
Clerk: One-way or round-trip? || ¿Solo ida o ida y vuelta?
You: Round-trip, please. What time does the bus leave? || Ida y vuelta, por favor. ¿A qué hora sale el bus?
Clerk: It leaves at ten from platform three. || Sale a las diez del andén tres.
You: How long does it take? || ¿Cuánto se demora?
Clerk: About two hours. || Unas dos horas.
"""),
         story("Tres maneras de llegar", "🚦", """
Ana, Ben and Carlos work in the same office downtown. || Ana, Ben y Carlos trabajan en la misma oficina en el centro.
Ana goes to work by car. With traffic, it takes forty minutes. || Ana va al trabajo en carro. Con el tráfico, se demora cuarenta minutos.
Ben goes by subway. It's fast. It takes fifteen minutes. || Ben va en metro. Es rápido. Se demora quince minutos.
Carlos goes by bike. It takes twenty-five minutes, and it's good exercise. || Carlos va en bicicleta. Se demora veinticinco minutos y es buen ejercicio.
Today there is a big storm. Ana is late, Carlos is wet, and Ben arrives on time! || Hoy hay una tormenta grande. Ana llega tarde, Carlos está mojado, ¡y Ben llega a tiempo!
""", questions=[
             ("¿Cómo va Ben al trabajo?", ["En carro", "En metro", "En bicicleta"], 1),
             ("¿Cuánto se demora Ana?", ["Quince minutos", "Cuarenta minutos", "Veinticinco minutos"], 1),
             ("¿Quién llega a tiempo el día de la tormenta?", ["Ana", "Carlos", "Ben"], 2),
         ]),
         roleplay("En el taxi", "🚕 Tomas un taxi al aeropuerto.", """
Driver: Good morning. Where to? || Buenos días. ¿Para dónde?
+ To the airport, please. || Al aeropuerto, por favor.
- To the yesterday, please. || Al ayer, por favor. || Di un lugar.
Driver: OK. There's a lot of traffic today. || Bueno. Hoy hay mucho tráfico.
+ How long does it take? || ¿Cuánto se demora?
- How long is it take? || ¿Cuánto es se demora? || Se dice "How long does it take?".
Driver: About thirty minutes. || Unos treinta minutos.
+ That's OK. Thank you. || Está bien. Gracias.
- Stop here, please. || Pare aquí, por favor. || Todavía no has llegado.
"""),
     ],
     writes="""
Voy al trabajo en bus. | I go to work by bus.
¿Cuánto se demora? | How long does it take?
El tren sale a las ocho. | The train leaves at eight. | The train leaves at 8.
""",
     dictations="""
Where does this bus go? || ¿A dónde va este bus?
It takes about two hours. || Se demora unas dos horas.
""")

unit("u20-gustos", "A1", "Gustos y opiniones", "❤️",
     "Ya puedo decir lo que me gusta y lo que no",
     "like, love y hate con -ing, y adjetivos para dar tu opinión.",
     grammar=["like / love / hate + -ing", "Adjetivos de opinión"],
     items="""
love | encantar / amar | 😍 | lav
hate | odiar | 😤 | jéit
don't mind | no me molesta | 😐 | dóunt máind
prefer | preferir | ⚖️ | pri-fér
I love dancing | Me encanta bailar | 💃
I hate waking up early | Odio madrugar | ⏰
I don't like cooking | No me gusta cocinar | 🙅
Do you like reading? | ¿Te gusta leer? | 📖
favorite | favorito | ⭐ | féi-vo-rit
music | música | 🎶 | miú-sik
movie | película | 🎬 | múu-vi
book | libro | 📕 | buk
video games | videojuegos | 🎮 | ví-di-o guéims
series | serie | 📺 | sí-ris
sport | deporte | 🏅 | sport
good | bueno | 👍 | gud
bad | malo | 👎 | bad
great | genial / excelente | 🤩 | gréit
boring | aburrido (que aburre) | 🥱 | bó-ring
interesting | interesante | 🧐 | ín-tres-ting
funny | chistoso / gracioso | 😆 | fá-ni
scary | de miedo | 👻 | ské-ri
beautiful | hermoso | 🌺 | biú-ti-ful
ugly | feo | 👺 | á-gli
easy | fácil | 🟢 | íi-si
difficult | difícil | 🔴 | dí-fi-kalt
amazing | increíble | 🤯 | a-méi-sing
I think it's great | Creo que es genial | 💭
Me too | Yo también | 🙋‍♂️ | mi túu
Me neither | Yo tampoco | 🙅‍♀️ | mi ní-der
What's your favorite movie? | ¿Cuál es tu película favorita? | 🎞️
""",
     extras=[
         D("like / love / hate + -ing",
           "Mira la forma del verbo después de like, love y hate.",
           """
I like reading. || Me gusta leer. || reading
She loves dancing. || A ella le encanta bailar. || dancing
They hate waking up early. || Odian madrugar. || waking
Do you like cooking? || ¿Te gusta cocinar? || cooking
He doesn't like running. || A él no le gusta correr. || running
""",
           "¿Qué forma tiene el verbo que va después de like?",
           ["Termina en -ing", "Lleva to siempre", "Va en pasado"], 0,
           "Después de like, love, hate y don't mind el segundo verbo suele ir con -ing: I love dancing. Ojo con el orden: en español 'me gusta', pero en inglés la persona va primero: I like (yo gusto), She likes (ella gusta).",
           """
I love music, but I hate dancing. || Me encanta la música, pero odio bailar.
""",
           fills="""
I love ___ to music. | listening / listen | 0 | Me encanta escuchar música.
She ___ cooking. | likes / like | 0 | A ella le gusta cocinar.
This movie is ___. I want to sleep. | boring / bored | 0 | Esta película es aburrida.
"I love pizza." "Me ___!" | too / neither | 0 | "Me encanta la pizza." "¡A mí también!"
"""),
         tip("😴", "boring o bored", "boring = algo que aburre (The movie is boring). bored = cómo te sientes (I'm bored). Lo mismo con interesting/interested y scary/scared."),
         dialogue("¿Qué vemos?", "🍿 Viernes en la noche, eligiendo qué ver.", """
Ben: Do you like scary movies? || ¿Te gustan las películas de miedo?
Mia: No, I hate them. I prefer funny movies. || No, las odio. Prefiero las películas chistosas.
Ben: Me too! What's your favorite movie? || ¡Yo también! ¿Cuál es tu película favorita?
Mia: Toy Story. It's amazing. || Toy Story. Es increíble.
Ben: I think it's great too. Let's watch it! || A mí también me parece genial. ¡Veámosla!
"""),
         story("Gustos muy distintos", "🎮", """
Leo and Sofía are best friends, but they like different things. || Leo y Sofía son mejores amigos, pero les gustan cosas diferentes.
Leo loves video games. He thinks books are boring. || A Leo le encantan los videojuegos. Cree que los libros son aburridos.
Sofía loves reading. Her favorite book is about a dragon. || A Sofía le encanta leer. Su libro favorito es sobre un dragón.
Leo hates waking up early. Sofía doesn't mind it. || Leo odia madrugar. A Sofía no le molesta.
But they both love music and dancing. || Pero a los dos les encanta la música y bailar.
On Saturdays they go dancing together. It's their favorite day! || Los sábados van a bailar juntos. ¡Es su día favorito!
""", questions=[
             ("¿Qué piensa Leo de los libros?", ["Que son aburridos", "Que son increíbles", "Que son fáciles"], 0),
             ("¿A quién no le molesta madrugar?", ["A Leo", "A Sofía", "A ninguno"], 1),
             ("¿Qué les gusta a los dos?", ["Leer", "Los videojuegos", "La música y bailar"], 2),
         ]),
         roleplay("Conociendo gustos", "☕ Charlas con una compañera nueva.", """
Eva: Do you like sports? || ¿Te gustan los deportes?
+ Yes! I love playing football. || ¡Sí! Me encanta jugar fútbol.
- Yes! I love play football yesterday. || ¡Sí! Me encanta jugar fútbol ayer. || Se dice "playing" y sin "yesterday".
Eva: Me too! Do you like running? || ¡A mí también! ¿Te gusta correr?
+ Not really. I think it's boring. || No mucho. Me parece aburrido.
- Not really. I'm boring. || No mucho. Soy aburrido. || "I'm boring" significa que tú aburres a los demás.
Eva: Ha ha. What's your favorite series? || Ja ja. ¿Cuál es tu serie favorita?
+ I love Stranger Things. It's scary but amazing. || Me encanta Stranger Things. Da miedo pero es increíble.
- Me neither. || Yo tampoco. || No responde la pregunta.
"""),
     ],
     writes="""
Me encanta bailar. | I love dancing.
No me gusta cocinar. | I don't like cooking. | I do not like cooking.
¿Cuál es tu película favorita? | What's your favorite movie? | What is your favorite movie?
""",
     dictations="""
I think it's interesting. || Creo que es interesante.
She hates waking up early. || Ella odia madrugar.
""")

unit("u21-personas", "A1", "Describir personas", "🧑‍🤝‍🧑",
     "Ya puedo describir cómo es alguien",
     "Apariencia física, personalidad y cómo preguntar cómo es una persona.",
     grammar=["What does he look like?", "Orden de adjetivos sencillo"],
     items="""
tall | alto | 🦒 | tól
short | bajo / corto | 🐿️ | short
young | joven | 🧒 | iang
old | viejo / mayor | 🧓 | óuld
thin | delgado | 🥢 | zin
strong | fuerte | 🏋️ | strong
long hair | pelo largo | 💁‍♀️
short hair | pelo corto | 💇‍♂️
curly hair | pelo crespo | 👩‍🦱 | kér-li jér
straight hair | pelo liso | 👱 | stréit jér
blond | rubio | 👱‍♀️ | blond
dark hair | pelo oscuro | 🧑
brown eyes | ojos cafés | 👀
beard | barba | 🧔 | bíerd
glasses | gafas | 👓 | glá-ses
handsome | guapo (hombre) | 😎 | ján-som
pretty | bonita | 🌸 | prí-ti
kind | amable | 🤗 | káind
friendly | amigable | 😊 | frénd-li
shy | tímido | 🙈 | shái
smart | inteligente | 🧠 | smart
lazy | perezoso | 🦥 | léi-si
hard-working | trabajador | 🐝 | jard-uér-king
quiet | callado / tranquilo | 🤫 | kuái-et
talkative | conversador | 🗣️ | tó-ka-tiv
honest | honesto | 🤝 | ó-nest | La h no suena.
patient | paciente | 🧘 | péi-shent
What does she look like? | ¿Cómo es ella (físicamente)? | 🔍
What is he like? | ¿Cómo es él (de personalidad)? | 💬
She looks like her mother | Se parece a su mamá | 👩‍👧
""",
     extras=[
         D("look like vs be like",
           "Las dos preguntas se traducen '¿cómo es?'. Mira las respuestas.",
           """
What does she look like? She's tall and has curly hair. || ¿Cómo es ella? Es alta y tiene el pelo crespo. || look like
What does he look like? He has a beard and glasses. || ¿Cómo es él? Tiene barba y gafas. || look like
What is she like? She's kind and patient. || ¿Cómo es ella? Es amable y paciente. || like
What is he like? He's shy but very smart. || ¿Cómo es él? Es tímido pero muy inteligente. || like
""",
           "¿Qué pregunta sirve para la personalidad?",
           ["What does he look like?", "What is he like?"], 1,
           "What does … look like? pregunta por la apariencia (alto, pelo, ojos). What is … like? pregunta por la personalidad (amable, tímido). Y para el pelo y los ojos se usa have: She has brown eyes.",
           """
My brother is tall and strong, but he's very shy. || Mi hermano es alto y fuerte, pero muy tímido.
""",
           fills="""
She ___ long straight hair. | has / is | 0 | Ella tiene el pelo largo y liso.
What ___ your teacher like? | is / does | 0 | ¿Cómo es tu profesor?
He ___ tall and thin. | is / has | 0 | Él es alto y delgado.
What does she look ___? | like / as | 0 | ¿Cómo es ella físicamente?
"""),
         dialogue("¿Quién es?", "📸 Miran una foto del grupo de la universidad.", """
Lia: Who is that? The tall boy with glasses. || ¿Quién es ese? El muchacho alto con gafas.
Sam: That's Andrés. He's my classmate. || Ese es Andrés. Es mi compañero de clase.
Lia: What is he like? || ¿Cómo es él?
Sam: He's very smart and friendly, but a little shy. || Es muy inteligente y amigable, pero un poco tímido.
Lia: And the girl with curly hair? || ¿Y la muchacha de pelo crespo?
Sam: That's Camila. She's very talkative and funny! || Esa es Camila. ¡Es muy conversadora y chistosa!
"""),
         story("Mi mejor amiga", "👭", """
My best friend is called Valentina. She's twenty-two years old. || Mi mejor amiga se llama Valentina. Tiene veintidós años.
She's short and has long dark hair and big brown eyes. || Es bajita y tiene el pelo largo y oscuro y unos ojos cafés grandes.
She looks like her mother, but she has her father's smile. || Se parece a su mamá, pero tiene la sonrisa de su papá.
Valentina is very kind and patient. She always listens to me. || Valentina es muy amable y paciente. Siempre me escucha.
She's also hard-working. She studies and works at the same time. || También es muy trabajadora. Estudia y trabaja al mismo tiempo.
She isn't perfect: she's a little lazy on Sundays! || No es perfecta: ¡es un poquito perezosa los domingos!
""", questions=[
             ("¿Cómo es el pelo de Valentina?", ["Corto y rubio", "Largo y oscuro", "Crespo y rubio"], 1),
             ("¿A quién se parece?", ["A su mamá", "A su abuela", "A su hermana"], 0),
             ("¿Cuándo es perezosa?", ["Los lunes", "Los domingos", "Nunca"], 1),
         ]),
         roleplay("Buscando a alguien en el aeropuerto", "✈️ Debes recoger a tu primo, pero el conductor no lo conoce.", """
Driver: What does your cousin look like? || ¿Cómo es su primo?
+ He's tall and he has short blond hair. || Es alto y tiene el pelo corto y rubio.
- He's very kind and patient. || Es muy amable y paciente. || Eso es personalidad; te preguntaron cómo se ve.
Driver: Does he wear glasses? || ¿Usa gafas?
+ Yes, he does. And he has a beard. || Sí. Y tiene barba.
- Yes, he is glasses. || Sí, él es gafas. || Se dice "Yes, he does".
Driver: I think that's him, with the blue jacket! || ¡Creo que es él, el de la chaqueta azul!
+ Yes, that's him! Thank you. || ¡Sí, es él! Gracias.
- No, that's a pharmacy. || No, eso es una farmacia. || No tiene sentido aquí.
"""),
     ],
     writes="""
Ella es alta y tiene el pelo crespo. | She's tall and has curly hair. | She is tall and she has curly hair. ; She's tall and she has curly hair.
Él es muy amable. | He's very kind. | He is very kind.
Me parezco a mi papá. | I look like my father. | I look like my dad.
""",
     dictations="""
What does your brother look like? || ¿Cómo es tu hermano físicamente?
She's friendly but a little shy. || Es amigable pero un poco tímida.
""")

unit("u22-tecnologia", "A1", "El celular y la tecnología", "📲",
     "Ya puedo usar el celular y el computador en inglés",
     "Las palabras que ves todos los días en tu celular, apps y computador.",
     grammar=["Imperativos de las apps", "my / your / our"],
     items="""
phone | celular / teléfono | 📱 | fóun
computer | computador | 💻 | kom-piú-ter
screen | pantalla | 🖥️ | skríin
keyboard | teclado | ⌨️ | kíi-bord
mouse | mouse / ratón | 🖱️ | máus
charger | cargador | 🔌 | chár-yer
battery | batería | 🔋 | bá-te-ri
password | contraseña | 🔐 | pás-uerd
email | correo electrónico | 📧 | íi-meil
message | mensaje | 💬 | mé-sich
photo | foto | 🖼️ | fóu-tou
video | video | 🎥 | ví-di-ou
app | aplicación | 📲 | ap
internet | internet | 🌐 | ín-ter-net
Wi-Fi | wifi | 📶 | uái-fai
download | descargar | ⬇️ | dáun-loud
upload | subir (un archivo) | ⬆️ | áp-loud
save | guardar | 💾 | séiv
delete | borrar | 🗑️ | di-líit
search | buscar | 🔎 | serch
click | hacer clic | 🖱️ | klik
share | compartir | 🔗 | sher
log in | iniciar sesión | 🔓 | log in
sign up | registrarse | 📝 | sáin ap
settings | configuración / ajustes | ⚙️ | sé-tings
My battery is low | Tengo poca batería | 🪫
What's the Wi-Fi password? | ¿Cuál es la clave del wifi? | 📶
Send me a message | Mándame un mensaje | 💌
Can I charge my phone? | ¿Puedo cargar mi celular? | 🔌
our | nuestro | 👨‍👩‍👧 | áur
their | su / de ellos | 👥 | der
""",
     extras=[
         D("Los posesivos",
           "Mira cómo se dice 'de quién es' cada cosa.",
           """
This is my phone. || Este es mi celular. || my
Is this your charger? || ¿Este es tu cargador? || your
His password is easy. || Su contraseña (de él) es fácil. || His
Her computer is new. || Su computador (de ella) es nuevo. || Her
Our Wi-Fi is fast. || Nuestro wifi es rápido. || Our
Their app is great. || Su app (de ellos) es genial. || Their
""",
           "¿Cómo se dice 'nuestro'?",
           ["their", "our", "your"], 1,
           "Los posesivos van antes de la cosa y no cambian por plural: my phones, our computers. Son: my (mi), your (tu/su de usted), his (de él), her (de ella), its (de una cosa), our (nuestro), their (de ellos).",
           """
Our teacher sends us an email every week. || Nuestro profesor nos manda un correo cada semana.
""",
           fills="""
I can't find ___ charger. (yo) | my / me | 0 | No encuentro mi cargador.
Lia and Tom love ___ new phones. | their / our | 0 | A Lia y Tom les encantan sus celulares nuevos.
We need ___ password. | our / us | 0 | Necesitamos nuestra contraseña.
Is this ___ email, Mr. Pérez? | your / you | 0 | ¿Este es su correo, señor Pérez?
"""),
         tip("📱", "Cambia tu celular a inglés", "Un truco muy efectivo y gratis: pon tu celular en inglés. Ya conoces dónde está cada cosa, así que aprendes settings, download, share y delete sin esfuerzo."),
         dialogue("En la casa de un amigo", "🏠 Llegas y necesitas internet.", """
You: Can I charge my phone? My battery is low. || ¿Puedo cargar mi celular? Tengo poca batería.
Jake: Sure. The charger is next to the computer. || Claro. El cargador está al lado del computador.
You: Thanks! And what's the Wi-Fi password? || ¡Gracias! ¿Y cuál es la clave del wifi?
Jake: It's "happycat2024". All small letters. || Es "happycat2024". Todo en minúscula.
You: Got it. Can I send you the photos later? || Listo. ¿Te mando las fotos más tarde?
Jake: Yes, send me a message. || Sí, mándame un mensaje.
"""),
         story("La abuela y su celular nuevo", "👵📱", """
Grandma Rosa has a new phone. She doesn't know how to use it. || La abuela Rosa tiene un celular nuevo. No sabe cómo usarlo.
Her grandson Sam helps her. "First, go to settings." || Su nieto Sam le ayuda. "Primero, ve a configuración."
"Now download this app. Then sign up with your email." || "Ahora descarga esta aplicación. Luego regístrate con tu correo."
"Choose a password. Don't share it with anyone!" || "Elige una contraseña. ¡No se la compartas a nadie!"
Grandma takes a photo of Sam and shares it with the family. || La abuela le toma una foto a Sam y la comparte con la familia.
Now she sends messages every day. She loves her new phone! || Ahora manda mensajes todos los días. ¡Le encanta su celular nuevo!
""", questions=[
             ("¿Quién ayuda a la abuela?", ["Su hija", "Su nieto Sam", "Un vecino"], 1),
             ("¿Con qué se registra?", ["Con su correo", "Con su teléfono fijo", "Con una foto"], 0),
             ("¿Qué no debe compartir?", ["Las fotos", "La contraseña", "Los mensajes"], 1),
         ]),
         roleplay("Soporte técnico", "🛠️ Llamas porque no puedes entrar a tu cuenta.", """
Agent: Hello, how can I help you? || Hola, ¿en qué le puedo ayudar?
+ Hi. I can't log in to my account. || Hola. No puedo iniciar sesión en mi cuenta.
- Hi. I can't log in to your account. || Hola. No puedo entrar a su cuenta. || Es TU cuenta: "my account".
Agent: Do you remember your password? || ¿Recuerda su contraseña?
+ No, I don't. || No, no la recuerdo.
- No, I doesn't. || No, yo no recuerda. || Con I se dice "I don't".
Agent: OK. Click "Forgot password" and check your email. || Bueno. Haga clic en "Olvidé mi contraseña" y revise su correo.
+ Great, thank you! || ¡Perfecto, gracias!
- Delete my email, please. || Borre mi correo, por favor. || No es lo que necesitas.
"""),
     ],
     writes="""
¿Cuál es la clave del wifi? | What's the Wi-Fi password? | What is the Wi-Fi password? ; What's the wifi password?
Tengo poca batería. | My battery is low.
Mándame un mensaje. | Send me a message.
""",
     dictations="""
Can I charge my phone? || ¿Puedo cargar mi celular?
Don't share your password. || No compartas tu contraseña.
""",
     speak="""
I use my phone every day. || Uso mi celular todos los días.
""")
