# A2 · Parte 1 (unidades 23–28)

unit("u23-pasado-be", "A2", "¿Dónde estabas?", "🕰️",
     "Ya puedo decir dónde estuve y cómo estuvo",
     "El pasado del verbo to be (was / were) para hablar de ayer, el fin de semana o tu infancia.",
     grammar=["Pasado de to be: was / were"],
     items="""
was | fue / estuvo / era (I, he, she, it) | ⏪ | uós
were | fueron / estuvieron / eran (you, we, they) | ⏪ | uér
wasn't | no fue / no estuvo | 🚫 | uó-sent
weren't | no fueron / no estuvieron | 🚫 | uérnt
last night | anoche | 🌙 | last náit
last week | la semana pasada | 📅
last year | el año pasado | 🗓️
two days ago | hace dos días | ⏮️ | tu déis a-góu
when I was a child | cuando era niño | 🧒
born | nacido | 👶 | born
I was born in 2002 | Nací en 2002 | 🎂
Where were you? | ¿Dónde estabas? | 📍
How was your weekend? | ¿Qué tal tu fin de semana? | 🛋️
It was fun | Fue divertido | 🎉
It was terrible | Fue terrible | 😖 | its uós té-ri-bol
crowded | lleno de gente | 👥 | kráu-ded
empty | vacío | 🫙 | émp-ti
noisy | ruidoso | 🔊 | nói-si
expensive | caro | 💸
delicious | delicioso | 😋
excited | emocionado | 🤩 | ek-sái-ted
worried | preocupado | 😟 | uó-rid
surprised | sorprendido | 😲 | sur-práisd
proud | orgulloso | 🦁 | práud
lucky | con suerte | 🍀 | lá-ki
concert | concierto | 🎸 | kón-sert
party | fiesta | 🥳 | pár-ti
wedding | boda | 💒 | ué-ding
holiday | día festivo / vacaciones | 🏖️ | jó-li-dei
trip | viaje (corto) | 🧳 | trip
childhood | infancia | 🪁 | cháild-jud
neighbor | vecino | 🏘️ | néi-bor
classmate | compañero de clase | 🧑‍🎓 | klás-meit
teacher's pet | el consentido del profesor | 🍎
village | pueblo | 🏡 | ví-lich
town | pueblo / ciudad pequeña | 🏘️ | táun
city | ciudad | 🏙️ | sí-ti
at home | en casa | 🏠
at work | en el trabajo | 💼
""",
     extras=[
         D("was / were",
           "Compara el presente con el pasado de estas frases.",
           """
I am at home. → I was at home last night. || Estoy en casa. → Estuve en casa anoche. || was
She is tired. → She was tired yesterday. || Está cansada. → Estaba cansada ayer. || was
They are happy. → They were happy at the party. || Están felices. → Estaban felices en la fiesta. || were
We are in Bogotá. → We were in Bogotá last week. || Estamos en Bogotá. → Estuvimos en Bogotá la semana pasada. || were
It is cold. → It wasn't cold yesterday. || Hace frío. → Ayer no hizo frío. || wasn't
""",
           "¿Qué forma va con they, we y you?",
           ["was", "were"], 1,
           "Este es el PASADO DEL VERBO TO BE. am e is cambian a was (I was, she was); are cambia a were (you were, we were, they were). Negativo: wasn't / weren't. Pregunta: Were you…? Was she…?",
           """
Where were you last night? I was at a concert. || ¿Dónde estabas anoche? Estaba en un concierto.
""",
           fills="""
I ___ at work yesterday. | was / were | 0 | Ayer estuve en el trabajo.
My parents ___ at the wedding. | was / were | 1 | Mis papás estuvieron en la boda.
The concert ___ very crowded. | was / were | 0 | El concierto estaba muy lleno.
___ you at home last night? | Was / Were | 1 | ¿Estabas en casa anoche?
The tickets ___ cheap. | wasn't / weren't | 1 | Los boletos no eran baratos.
"""),
         dialogue("El lunes en la oficina", "☕ Lunes por la mañana.", """
Ana: Hi Ben! How was your weekend? || ¡Hola Ben! ¿Qué tal tu fin de semana?
Ben: It was great! I was in Cartagena with my family. || ¡Estuvo genial! Estuve en Cartagena con mi familia.
Ana: Wow! Was it hot? || ¡Uy! ¿Hacía calor?
Ben: Yes, it was very hot. And the beach was crowded. || Sí, hacía mucho calor. Y la playa estaba llena.
Ana: Were the hotels expensive? || ¿Los hoteles eran caros?
Ben: No, they weren't. We were lucky! || No. ¡Tuvimos suerte!
"""),
         story("Cuando mi abuelo era niño", "👴", """
My grandfather was born in a small village in 1950. || Mi abuelo nació en un pueblo pequeño en 1950.
His house was small, but it was always full of people. || Su casa era pequeña, pero siempre estaba llena de gente.
There were eight children in his family. He was the youngest. || Eran ocho niños en su familia. Él era el menor.
The school was far, and the roads weren't good. || La escuela quedaba lejos y los caminos no eran buenos.
He wasn't a good student, but he was very good at football. || No era buen estudiante, pero era muy bueno en fútbol.
"Life was difficult, but we were happy," he always says. || "La vida era difícil, pero éramos felices", siempre dice.
""", questions=[
             ("¿Dónde nació el abuelo?", ["En una ciudad grande", "En un pueblo pequeño", "En la playa"], 1),
             ("¿Cuántos niños había en su familia?", ["Tres", "Ocho", "Cinco"], 1),
             ("¿En qué era bueno?", ["En matemáticas", "En fútbol", "En música"], 1),
         ]),
         roleplay("¿Dónde estabas?", "📱 Tu mamá te llama preocupada porque no contestabas.", """
Mom: Where were you? I called you three times! || ¿Dónde estabas? ¡Te llamé tres veces!
+ Sorry, Mom. I was at a concert. || Perdón, mamá. Estaba en un concierto.
- Sorry, Mom. I am at a concert yesterday. || Perdón, mamá. Estoy en un concierto ayer. || Habla en pasado: "I was".
Mom: A concert? Was it good? || ¿Un concierto? ¿Estuvo bueno?
+ Yes, it was amazing, but it was very noisy. || Sí, estuvo increíble, pero era muy ruidoso.
- Yes, they was amazing. || Sí, ellos estuvo increíble. || Con they va "were".
Mom: OK. I was worried! || Bueno. ¡Estaba preocupada!
+ I'm sorry. Next time I'll text you. || Lo siento. La próxima vez te escribo.
- You were lucky. || Tuviste suerte. || No responde a su preocupación.
"""),
     ],
     writes="""
¿Qué tal tu fin de semana? | How was your weekend?
Estuve en casa anoche. | I was at home last night.
Nací en 2002. | I was born in 2002.
""",
     dictations="""
Where were you last night? || ¿Dónde estabas anoche?
The party was fun, but it was very crowded. || La fiesta fue divertida, pero estaba muy llena.
""")

unit("u24-pasado-regular", "A2", "Mi fin de semana", "🏖️",
     "Ya puedo contar lo que hice el fin de semana",
     "El pasado simple con verbos regulares (-ed) y cómo se pronuncia esa terminación.",
     grammar=["Pasado simple regular: -ed", "Pronunciación de -ed: /t/, /d/, /id/"],
     items="""
worked | trabajé / trabajó | 💼 | uérkt
played | jugué / jugó | 🎮 | pléid
watched | vi / vio (TV, película) | 📺 | uócht
cooked | cociné | 🍳 | kukt
cleaned | limpié | 🧹 | klíind
visited | visité | 🏡 | ví-si-tid
studied | estudié | 📚 | stá-did
walked | caminé | 🚶 | uókt
talked | hablé / conversé | 💬 | tókt
listened | escuché | 🎧 | lí-send
danced | bailé | 💃 | danst
stayed | me quedé | 🛋️ | stéid
traveled | viajé | ✈️ | trá-veld
started | empecé | ▶️ | stár-tid
finished | terminé | 🏁 | fí-nisht
wanted | quería / quise | 🙏 | uón-tid
needed | necesitaba / necesité | 📝 | níi-did
called | llamé | 📞 | kóld
helped | ayudé | 🤝 | jelpt
opened | abrí | 📂 | óu-pend
closed | cerré | 📁 | klóusd
lived | viví | 🏠 | livd
liked | me gustó | 👍 | láikt
loved | me encantó | 😍 | lavd
hated | odié | 😤 | jéi-tid
tried | intenté / probé | 🧪 | tráid
arrived | llegué | 🛬 | a-ráivd
waited | esperé | ⏳ | uéi-tid
relaxed | descansé / me relajé | 🧘 | ri-lákst
rained | llovió | 🌧️ | réind
painted | pinté | 🖌️ | péin-tid
moved | me mudé / moví | 📦 | múuvd
picked up | recogí | 🫴
the day before yesterday | anteayer | ⏮️
on Saturday morning | el sábado por la mañana | 🌅
all day | todo el día | 🌞
for two hours | durante dos horas | ⏲️
then | luego / entonces | ➡️ | den
after that | después de eso | ⏭️
finally | por último / al final | 🏁 | fái-na-li
""",
     extras=[
         D("Pasado simple regular (-ed)",
           "Compara la rutina con lo que pasó ayer.",
           """
I work every day. → I worked yesterday. || Trabajo todos los días. → Trabajé ayer. || worked
She cooks dinner. → She cooked dinner last night. || Ella cocina. → Ella cocinó anoche. || cooked
They play football. → They played on Sunday. || Juegan fútbol. → Jugaron el domingo. || played
We visit grandma. → We visited grandma last week. || Visitamos a la abuela. → La visitamos la semana pasada. || visited
He studies. → He studied for two hours. || Él estudia. → Estudió dos horas. || studied
""",
           "¿Cómo se forma el pasado de estos verbos?",
           ["Agregando -ed al verbo", "Con will antes", "Con am/is/are + -ing"], 0,
           "Esto es el PASADO SIMPLE de los verbos regulares: verbo + -ed. ¡Y es igual para todas las personas! I worked, she worked, they worked (nada de -s). Si termina en e solo se agrega -d (lived); consonante + y cambia a -ied (study → studied).",
           """
Last Saturday I cleaned my room, then I watched a movie. || El sábado pasado limpié mi cuarto y luego vi una película.
""",
           fills="""
Yesterday I ___ my grandmother. | visit / visited | 1 | Ayer visité a mi abuela.
She ___ English for three hours. | studied / studyed | 0 | Ella estudió inglés tres horas.
We ___ at home all day. | stayed / staied | 0 | Nos quedamos en casa todo el día.
He ___ in Medellín when he was young. | lived / liveded | 0 | Él vivió en Medellín cuando era joven.
"""),
         tip("👄", "Cómo suena el -ed", "Casi nunca se pronuncia 'ed'. Después de sonidos como k, p, s, ch, sh suena /t/: worked (uérkt). Después de sonidos con voz suena /d/: played (pléid). Solo después de t o d suena /id/: wanted (uón-tid), needed (níi-did)."),
         dialogue("Contando el fin de semana", "🧃 En el descanso de clase.", """
Leo: What did you do on the weekend? || ¿Qué hiciste el fin de semana?
Mia: On Saturday morning I cleaned the house. Then I cooked lunch for my family. || El sábado por la mañana limpié la casa. Luego cociné el almuerzo para mi familia.
Leo: And on Sunday? || ¿Y el domingo?
Mia: It rained all day, so I stayed at home and watched three movies. || Llovió todo el día, así que me quedé en casa y vi tres películas.
Leo: I played football, but then it rained! || Yo jugué fútbol, ¡pero después llovió!
"""),
         story("Mudanza", "📦", """
Last month my family moved to a new apartment. || El mes pasado mi familia se mudó a un apartamento nuevo.
On Friday we packed everything in boxes. It took all day. || El viernes empacamos todo en cajas. Nos tomó todo el día.
On Saturday a big truck arrived at eight. My uncle helped us. || El sábado llegó un camión grande a las ocho. Mi tío nos ayudó.
We carried the sofa up the stairs. It was very heavy! || Subimos el sofá por las escaleras. ¡Estaba muy pesado!
In the evening we ordered pizza and talked about our new home. || En la noche pedimos pizza y hablamos de nuestro nuevo hogar.
Finally, at midnight, we closed the door and relaxed. || Por fin, a la medianoche, cerramos la puerta y descansamos.
""", questions=[
             ("¿Quién les ayudó?", ["Su tío", "Su vecino", "Su abuela"], 0),
             ("¿Qué cargaron por las escaleras?", ["La nevera", "El sofá", "La cama"], 1),
             ("¿Qué comieron en la noche?", ["Pizza", "Pollo", "Sopa"], 0),
         ]),
         roleplay("Llegaste tarde", "⏰ Llegas tarde a una reunión y tu jefe pregunta qué pasó.", """
Boss: You're late. What happened? || Llegas tarde. ¿Qué pasó?
+ I'm sorry. I waited for the bus for forty minutes. || Lo siento. Esperé el bus cuarenta minutos.
- I'm sorry. I wait the bus tomorrow. || Lo siento. Espero el bus mañana. || Cuenta lo que pasó, en pasado.
Boss: Did you call? || ¿Llamaste?
+ Yes, I called the office, but nobody answered. || Sí, llamé a la oficina, pero nadie contestó.
- Yes, I calling the office. || Sí, yo llamando a la oficina. || En pasado es "I called".
Boss: OK. The meeting started at nine. || Bueno. La reunión empezó a las nueve.
+ I understand. It won't happen again. || Entiendo. No volverá a pasar.
- I finished the meeting. || Terminé la reunión. || No tiene sentido; acabas de llegar.
"""),
     ],
     writes="""
Ayer trabajé todo el día. | Yesterday I worked all day. | I worked all day yesterday.
Ella estudió inglés anoche. | She studied English last night.
Nos quedamos en casa porque llovió. | We stayed at home because it rained. | We stayed home because it rained.
""",
     dictations="""
We visited my grandmother on Sunday. || Visitamos a mi abuela el domingo.
I watched a movie and then I relaxed. || Vi una película y luego descansé.
""")

unit("u25-irregulares", "A2", "Historias que pasaron", "📖",
     "Ya puedo narrar una historia corta en pasado",
     "Los verbos irregulares más usados del inglés, aprendidos dentro de historias.",
     grammar=["Verbos irregulares más usados"],
     items="""
went | fui / fue (go) | 🚶 | uent
had | tuve / tuvo (have) | 🤲 | jad
did | hice / hizo (do) | ✅ | did
made | hice / preparé (make) | 🛠️ | méid
got | conseguí / recibí / llegué (get) | 📦 | got
saw | vi (see) | 👀 | só
came | vine / vino (come) | 🏃 | kéim
took | tomé / llevé (take) | 📸 | tuk
gave | di (give) | 🎁 | guéiv
ate | comí (eat) | 🍽️ | éit
drank | tomé / bebí (drink) | 🥤 | drank
bought | compré (buy) | 🛍️ | bot
found | encontré (find) | 🔍 | fáund
lost | perdí (lose) | ❓ | lost
said | dije (say) | 💬 | sed
told | conté / le dije (tell) | 🗣️ | tóuld
thought | pensé (think) | 💭 | zot
knew | sabía / conocía (know) | 🧠 | niú
met | conocí (a alguien) / me encontré (meet) | 🤝 | met
left | salí / dejé (leave) | 🚪 | left
began | empecé (begin) | ▶️ | bi-gán
wrote | escribí (write) | ✍️ | róut
read (past) | leí (read) | 📖 | red | Se escribe igual que el presente, pero suena "red".
spoke | hablé (speak) | 🗣️ | spóuk
broke | rompí (break) | 💔 | bróuk
forgot | olvidé (forget) | 🤦 | for-gót
slept | dormí (sleep) | 😴 | slept
woke up | me desperté (wake up) | ⏰ | uóuk ap
ran | corrí (run) | 🏃‍♀️ | ran
swam | nadé (swim) | 🏊 | suam
sang | canté (sing) | 🎤 | sang
won | gané (win) | 🏆 | uan
paid | pagué (pay) | 💳 | péid
sent | envié (send) | 📤 | sent
felt | sentí (feel) | 💓 | felt
heard | oí / escuché (hear) | 👂 | herd
put | puse (put) | 📥 | put
sat | me senté (sit) | 🪑 | sat
stood | estuve de pie (stand) | 🧍 | stud
became | me volví / llegué a ser (become) | 🦋 | bi-kéim
""",
     extras=[
         D("Los verbos irregulares",
           "Estos verbos NO usan -ed. Mira cómo cambian.",
           """
I go to the beach. → I went to the beach. || Voy a la playa. → Fui a la playa. || went
She has a cat. → She had a cat. || Ella tiene un gato. → Ella tenía un gato. || had
We eat pizza. → We ate pizza. || Comemos pizza. → Comimos pizza. || ate
They see a movie. → They saw a movie. || Ven una película. → Vieron una película. || saw
He buys a car. → He bought a car. || Él compra un carro. → Compró un carro. || bought
""",
           "¿Qué tienen de especial estos verbos?",
           ["Su pasado cambia de forma, no lleva -ed", "No tienen pasado", "Solo existen en presente"], 0,
           "Estos son VERBOS IRREGULARES: su pasado tiene una forma propia que hay que aprender (go → went, have → had). Son pocos, pero son los más usados. La buena noticia: igual que los regulares, son iguales para todas las personas (I went, she went, they went).",
           """
Yesterday I woke up late, had breakfast and went to work. || Ayer me desperté tarde, desayuné y me fui al trabajo.
""",
           fills="""
Last night I ___ a great movie. | saw / seed | 0 | Anoche vi una película buenísima.
We ___ to the beach in December. | goed / went | 1 | Fuimos a la playa en diciembre.
She ___ a new phone yesterday. | bought / buyed | 0 | Ella compró un celular nuevo ayer.
I ___ my keys at the bar. | lost / losed | 0 | Perdí mis llaves en el bar.
They ___ the game 3-1! | won / winned | 0 | ¡Ganaron el partido 3-1!
"""),
         tip("🧠", "Cómo aprenderlos sin tablas", "No memorices listas. Aprende cada verbo dentro de una frase tuya: 'I went to Pasto', 'I ate empanadas'. El repaso espaciado de la app los traerá de vuelta hasta que salgan solos."),
         dialogue("¿Qué te pasó?", "😮 Tu amigo llega con el brazo vendado.", """
You: What happened to your arm? || ¿Qué le pasó a tu brazo?
Sam: I broke it! I went to the mountains last weekend. || ¡Me lo rompí! Fui a la montaña el fin de semana pasado.
You: Oh no! How? || ¡Ay no! ¿Cómo?
Sam: I ran down a hill, I fell and I hit a rock. || Corrí bajando una loma, me caí y me pegué con una piedra.
You: Did you go to the hospital? || ¿Fuiste al hospital?
Sam: Yes. A doctor gave me medicine and I slept for twelve hours! || Sí. Un médico me dio medicina ¡y dormí doce horas!
"""),
         story("El celular perdido", "📱", """
Last Friday Carla went to a concert in the city. || El viernes pasado Carla fue a un concierto en la ciudad.
She took the bus, met her friends and had a great time. || Tomó el bus, se encontró con sus amigas y la pasó muy bien.
They sang, danced and drank a lot of water. It was hot! || Cantaron, bailaron y tomaron mucha agua. ¡Hacía calor!
At midnight she put her hand in her bag. Her phone wasn't there! || A la medianoche metió la mano en el bolso. ¡Su celular no estaba!
She felt terrible. She thought, "I lost it!" || Se sintió fatal. Pensó: "¡Lo perdí!"
The next morning a man called her house. He found the phone under a seat! || A la mañana siguiente un señor llamó a su casa. ¡Encontró el celular debajo de una silla!
""", questions=[
             ("¿A dónde fue Carla?", ["A una boda", "A un concierto", "Al cine"], 1),
             ("¿Qué perdió?", ["Su bolso", "Su celular", "Sus llaves"], 1),
             ("¿Dónde estaba el celular?", ["En el bus", "Debajo de una silla", "En su casa"], 1),
         ]),
         roleplay("Una historia en la cena", "🍽️ Tu familia te pregunta por tu día.", """
Dad: So, how was your day? || Bueno, ¿cómo te fue hoy?
+ Interesting! I met a famous singer at the airport. || ¡Interesante! Conocí a un cantante famoso en el aeropuerto.
- Interesting! I meet a famous singer tomorrow. || ¡Interesante! Conozco a un cantante famoso mañana. || Cuenta lo que pasó, en pasado.
Dad: Really? What did you say? || ¿En serio? ¿Qué le dijiste?
+ I said hello and I took a photo with him. || Le dije hola y me tomé una foto con él.
- I sayed hello. || Yo decí hola. || El pasado de say es "said".
Dad: Wow! Can I see the photo? || ¡Uy! ¿Puedo ver la foto?
+ Sure! Here it is. || ¡Claro! Aquí está.
- No, I bought a car. || No, compré un carro. || No tiene que ver con la foto.
"""),
     ],
     writes="""
Ayer fui al cine. | Yesterday I went to the cinema. | I went to the cinema yesterday. ; I went to the movies yesterday. ; Yesterday I went to the movies.
Perdí mis llaves. | I lost my keys.
Comimos pizza y tomamos jugo. | We ate pizza and drank juice.
""",
     dictations="""
She bought a new dress for the wedding. || Ella compró un vestido nuevo para la boda.
I woke up late and forgot my phone. || Me desperté tarde y olvidé mi celular.
""",
     speak="""
Last weekend I went to the park and saw my friends. || El fin de semana pasado fui al parque y vi a mis amigos.
""")

unit("u26-preguntas-pasado", "A2", "Preguntar por el pasado", "🔎",
     "Ya puedo preguntar qué pasó y negar en pasado",
     "did / didn't para preguntas y negaciones en pasado, y las preguntas con wh-.",
     grammar=["Did / didn't", "Wh- questions en pasado"],
     items="""
Did you see it? | ¿Lo viste? | 👀
Yes, I did | Sí (en pasado) | 👍
No, I didn't | No (en pasado) | 👎 | nóu, ai dí-dent
I didn't go | No fui | 🚫
What did you do? | ¿Qué hiciste? | ❓
Where did you go? | ¿A dónde fuiste? | 🗺️
When did it happen? | ¿Cuándo pasó? | 📅
Why did you leave? | ¿Por qué te fuiste? | 🚪
Who did you meet? | ¿A quién conociste? | 🤝
How did you know? | ¿Cómo supiste? | 🤔
What happened? | ¿Qué pasó? | 😮 | uát já-pend
because | porque | 💡 | bi-kós
happen | pasar / suceder | ⚡ | já-pen
accident | accidente | 💥 | ák-si-dent
problem | problema | ⚠️ | pró-blem
news | noticias | 📰 | niús
story | historia / cuento | 📚 | stó-ri
truth | verdad | ✔️ | truz
lie | mentira / mentir | 🤥 | lái
secret | secreto | 🤫 | síi-kret
mistake | error | ❌ | mis-téik
answer | respuesta / responder | 🅰️ | án-ser
question | pregunta | ❓ | kués-chon
remember | recordar | 🧠 | ri-mém-ber
believe | creer | 🙏 | bi-líiv
explain | explicar | 🧑‍🏫 | eks-pléin
ask | preguntar / pedir | 🙋 | ask
agree | estar de acuerdo | 🤝 | a-gríi
anybody | alguien / nadie (en preguntas y negativos) | 👤 | é-ni-ba-di
nothing | nada | 🫥 | ná-zing
something | algo | 🎁 | sám-zing
somewhere | en algún lugar | 📍 | sám-uer
everybody | todo el mundo | 👨‍👩‍👧‍👦 | év-ri-ba-di
I don't remember | No me acuerdo | 🤷
Are you sure? | ¿Estás seguro? | 🧐
""",
     extras=[
         D("did / didn't",
           "Mira cómo se pregunta y se niega en pasado.",
           """
Did you go to the party? Yes, I did. || ¿Fuiste a la fiesta? Sí. || Did
Did she call you? No, she didn't. || ¿Ella te llamó? No. || Did, didn't
I didn't see the news. || No vi las noticias. || didn't
Where did you go? || ¿A dónde fuiste? || did
He didn't eat breakfast. || Él no desayunó. || didn't
""",
           "Después de did / didn't, el verbo va…",
           ["En pasado (went, saw)", "En su forma normal (go, see)", "Con -ing"], 1,
           "En pasado, las preguntas y negaciones usan did / didn't, y el verbo vuelve a su forma normal: Did you go? (no 'Did you went?'), I didn't see (no 'I didn't saw'). El pasado ya está en did.",
           """
What did you do yesterday? I didn't do anything. || ¿Qué hiciste ayer? No hice nada.
""",
           fills="""
Did you ___ the movie? | see / saw | 0 | ¿Viste la película?
I didn't ___ to work yesterday. | go / went | 0 | Ayer no fui al trabajo.
Where ___ you buy that jacket? | did / were | 0 | ¿Dónde compraste esa chaqueta?
She ___ answer my message. | didn't / don't | 0 | Ella no contestó mi mensaje.
Why did they ___ early? | leave / left | 0 | ¿Por qué se fueron temprano?
"""),
         dialogue("¿Qué pasó anoche?", "🕵️ Tu compañera de apartamento encuentra la cocina desordenada.", """
Eva: What happened in the kitchen? || ¿Qué pasó en la cocina?
You: I don't know. I didn't cook last night. || No sé. Anoche no cociné.
Eva: Did you invite anybody? || ¿Invitaste a alguien?
You: No, I didn't. Wait… Did you leave the window open? || No. Espera… ¿Dejaste la ventana abierta?
Eva: Yes, I did. Why? || Sí. ¿Por qué?
You: Because the neighbor's cat came in! || ¡Porque se entró el gato del vecino!
"""),
         story("El misterio del pastel", "🎂", """
On Sunday Grandma made a chocolate cake for the family. || El domingo la abuela hizo un pastel de chocolate para la familia.
She put it on the table and went to the garden. || Lo puso en la mesa y se fue al jardín.
When she came back, half of the cake wasn't there! || Cuando volvió, ¡la mitad del pastel no estaba!
"Who ate my cake?" she asked. Nobody answered. || "¿Quién se comió mi pastel?", preguntó. Nadie contestó.
"Did you eat it, Tom?" "No, I didn't! I was in my room." || "¿Te lo comiste tú, Tom?" "¡No! Estaba en mi cuarto."
Then she saw the dog. Its nose was brown with chocolate! || Entonces vio al perro. ¡Tenía la nariz café de chocolate!
""", questions=[
             ("¿Qué hizo la abuela?", ["Un pastel de chocolate", "Una sopa", "Pan"], 0),
             ("¿Dónde estaba Tom?", ["En el jardín", "En su cuarto", "En la cocina"], 1),
             ("¿Quién se comió el pastel?", ["Tom", "El perro", "La abuela"], 1),
         ]),
         roleplay("El testigo", "👮 Viste un pequeño accidente en la calle y un policía te pregunta.", """
Officer: Excuse me, did you see the accident? || Disculpe, ¿vio el accidente?
+ Yes, I did. I was at the bus stop. || Sí. Estaba en la parada del bus.
- Yes, I saw it tomorrow. || Sí, lo vi mañana. || "Tomorrow" es futuro.
Officer: What happened? || ¿Qué pasó?
+ A motorcycle didn't stop at the red light. || Una moto no paró en el semáforo en rojo.
- A motorcycle didn't stopped. || Una moto no paró. || Después de didn't, el verbo va en forma normal: stop.
Officer: Did the driver leave? || ¿El conductor se fue?
+ No, he didn't. He is over there. || No. Está allá.
- No, he don't. || No, él no (presente). || En pasado: "No, he didn't".
"""),
     ],
     writes="""
¿Qué hiciste ayer? | What did you do yesterday?
No fui a la fiesta. | I didn't go to the party. | I did not go to the party.
¿A dónde fueron ustedes? | Where did you go?
""",
     dictations="""
Did you remember my birthday? || ¿Te acordaste de mi cumpleaños?
I didn't understand the question. || No entendí la pregunta.
""")

unit("u27-planes", "A2", "Planes para el futuro", "🧳",
     "Ya puedo hablar de mis planes",
     "going to para planes e intenciones, y el presente continuo para citas ya arregladas.",
     grammar=["Going to", "Presente continuo para planes"],
     items="""
I'm going to travel | Voy a viajar | 🧳 | áim góu-ing tu trá-vel
She's going to study | Ella va a estudiar | 📚
Are you going to come? | ¿Vas a venir? | ❔
I'm not going to work | No voy a trabajar | 🙅
gonna | contracción informal de going to | 🗣️ | gá-na | Muy común al hablar: I'm gonna eat.
plan | plan / planear | 🗒️ | plan
next week | la próxima semana | ⏭️
next month | el próximo mes | 📅
next year | el próximo año | 🎆
this weekend | este fin de semana | 🛋️
tonight | esta noche | 🌙 | tu-náit
soon | pronto | ⏩ | súun
later | más tarde | 🕓
in the future | en el futuro | 🔮
someday | algún día | 🌠 | sám-dei
vacation | vacaciones | 🏝️ | vei-kéi-shon
visit | visitar | 🧭
learn | aprender | 🧠 | lern
save money | ahorrar plata | 🐷
get married | casarse | 💍 | get má-rid
have a baby | tener un bebé | 👶
buy a house | comprar una casa | 🏡
start a business | empezar un negocio | 🚀
change jobs | cambiar de trabajo | 🔄
graduate | graduarse | 🎓 | grá-yu-eit
celebrate | celebrar | 🥂 | sé-le-breit
stay | quedarse | 🏨
pack | empacar | 🎒 | pak
book a hotel | reservar un hotel | 🏨
dream | sueño / soñar | 💭 | dríim
goal | meta | 🎯 | góul
maybe | tal vez | 🤷 | méi-bi
probably | probablemente | 📈 | pró-ba-bli
definitely | definitivamente | ✅ | dé-fi-nit-li
I can't wait! | ¡No veo la hora! | 🤩
What are you doing tonight? | ¿Qué vas a hacer esta noche? | 🌃
""",
     extras=[
         D("going to para planes",
           "Mira cómo hablan estas personas de lo que van a hacer.",
           """
I'm going to visit my parents next week. || Voy a visitar a mis papás la próxima semana. || going to
She's going to start a business. || Ella va a empezar un negocio. || going to
We're going to save money for a car. || Vamos a ahorrar para un carro. || going to
Are you going to graduate this year? || ¿Te vas a graduar este año? || going to
They aren't going to come tonight. || Ellos no van a venir esta noche. || going to
""",
           "¿Cómo se dice 'voy a + verbo'?",
           ["am/is/are + going to + verbo", "will + going", "go + verbo con -ing"], 0,
           "GOING TO sirve para planes e intenciones: am / is / are + going to + verbo. Es casi igual al español 'voy a + verbo'. Al hablar rápido suena 'gonna': I'm gonna travel. Para citas ya fijadas también se usa el presente continuo: I'm meeting Ana at six.",
           """
I'm going to learn English and someday I'm going to travel to London. || Voy a aprender inglés y algún día voy a viajar a Londres.
""",
           fills="""
I'm going ___ buy a car. | to / for | 0 | Voy a comprar un carro.
She ___ going to get married in June. | is / are | 0 | Ella se va a casar en junio.
___ you going to come tonight? | Are / Do | 0 | ¿Vas a venir esta noche?
We ___ going to stay at a hotel. | aren't / don't | 0 | No nos vamos a quedar en un hotel.
"""),
         dialogue("Las vacaciones", "🏝️ Faltan dos semanas para vacaciones.", """
Ben: What are you going to do on vacation? || ¿Qué vas a hacer en vacaciones?
Lia: I'm going to visit my cousins in Cali. And you? || Voy a visitar a mis primos en Cali. ¿Y tú?
Ben: I'm going to stay at home and save money. || Me voy a quedar en casa y ahorrar plata.
Lia: Boring! Are you going to do anything fun? || ¡Qué aburrido! ¿Vas a hacer algo divertido?
Ben: Maybe. I'm meeting my friends on Saturday. || Tal vez. Me voy a ver con mis amigos el sábado.
Lia: Good! I can't wait for vacation! || ¡Bien! ¡No veo la hora de las vacaciones!
"""),
         story("Los planes de Andrés", "🚀", """
Andrés is twenty-three and he has big plans. || Andrés tiene veintitrés años y tiene grandes planes.
Next year he's going to graduate from university. || El próximo año se va a graduar de la universidad.
Then he's going to start a business with his best friend. || Luego va a empezar un negocio con su mejor amigo.
They're going to make an app for small farmers. || Van a hacer una aplicación para pequeños agricultores.
He isn't going to buy a car. He's going to save money first. || No va a comprar carro. Primero va a ahorrar plata.
Someday he's going to buy a house in the mountains. That's his dream. || Algún día va a comprar una casa en la montaña. Ese es su sueño.
""", questions=[
             ("¿Qué va a hacer Andrés el próximo año?", ["Casarse", "Graduarse", "Comprar un carro"], 1),
             ("¿Qué van a crear?", ["Un restaurante", "Una aplicación para agricultores", "Una tienda"], 1),
             ("¿Cuál es su sueño?", ["Una casa en la montaña", "Viajar a Europa", "Un carro nuevo"], 0),
         ]),
         roleplay("Organizar el sábado", "📱 Una amiga te escribe para hacer planes.", """
Sara: Hi! What are you doing on Saturday? || ¡Hola! ¿Qué vas a hacer el sábado?
+ I'm going to clean my apartment in the morning. Why? || Voy a limpiar mi apartamento por la mañana. ¿Por qué?
- I cleaned my apartment on Saturday. || Limpié mi apartamento el sábado. || Ella pregunta por el futuro.
Sara: We're going to have a picnic in the afternoon. Do you want to come? || Vamos a hacer un picnic por la tarde. ¿Quieres venir?
+ Yes, definitely! What time? || ¡Sí, claro que sí! ¿A qué hora?
- Yes, I'm going to coming. || Sí, voy a viniendo. || Después de "going to" va el verbo normal: come.
Sara: At three. I'm going to bring sandwiches. || A las tres. Voy a llevar sándwiches.
+ Great! I'm going to bring juice. || ¡Genial! Yo voy a llevar jugo.
- Great! I bring juice yesterday. || ¡Genial! Llevo jugo ayer. || Mezcla tiempos.
"""),
     ],
     writes="""
Voy a viajar el próximo año. | I'm going to travel next year. | I am going to travel next year.
¿Qué vas a hacer esta noche? | What are you going to do tonight? | What are you doing tonight?
No voy a trabajar mañana. | I'm not going to work tomorrow. | I am not going to work tomorrow.
""",
     dictations="""
She's going to start a business next year. || Ella va a empezar un negocio el próximo año.
We're gonna be late! || ¡Vamos a llegar tarde!
""",
     speak="""
Next year I'm going to speak English very well. || El próximo año voy a hablar inglés muy bien.
""")

unit("u28-comparar", "A2", "Comparando cosas", "⚖️",
     "Ya puedo comparar productos, lugares y personas",
     "Comparativos (bigger than) y superlativos (the biggest) para elegir y opinar.",
     grammar=["Comparativos: -er / more", "Superlativos: the -est / the most"],
     items="""
bigger than | más grande que | 🐘
smaller than | más pequeño que | 🐭
cheaper than | más barato que | 🪙
more expensive than | más caro que | 💎
better than | mejor que | 👍 | bé-ter dan
worse than | peor que | 👎 | uers dan
the best | el mejor | 🥇 | de best
the worst | el peor | 🥉 | de uerst
the biggest | el más grande | 🏔️
the most beautiful | el más hermoso | 🌹
as tall as | tan alto como | 📏
fast | rápido | 🏎️
heavy | pesado | 🏋️ | jé-vi
light | liviano / claro | 🪶 | láit
hot | caliente | 🔥
cold | frío | 🧊
far | lejos | 🛣️ | far
near | cerca | 📍 | níer
safe | seguro | 🛡️ | séif
dangerous | peligroso | ☠️ | déin-ye-ros
comfortable | cómodo | 🛋️ | kámf-ta-bol
modern | moderno | 🏙️ | mó-dern
old-fashioned | anticuado | 📻 | óuld-fá-shond
popular | popular | 🌟 | pó-piu-lar
famous | famoso | 🎬 | féi-mos
rich | rico (con dinero) | 💰 | rich
poor | pobre | 🪫 | pur
clean | limpio | ✨ | klíin
dirty | sucio | 🦠 | dér-ti
quiet | tranquilo / silencioso | 🤫
healthy | saludable | 🥗 | jél-zi
high | alto (montaña, precio) | 🏔️ | jái
low | bajo | ⬇️ | lóu
wide | ancho | ↔️ | uáid
deep | profundo | 🌊 | díip
in the world | en el mundo | 🌍
Which one is better? | ¿Cuál es mejor? | 🤔
""",
     extras=[
         D("Comparativos y superlativos",
           "Mira cómo cambia el adjetivo al comparar.",
           """
A cat is smaller than a dog. || Un gato es más pequeño que un perro. || smaller than
The train is faster than the bus. || El tren es más rápido que el bus. || faster than
This phone is more expensive than that one. || Este celular es más caro que ese. || more expensive than
Everest is the highest mountain in the world. || El Everest es la montaña más alta del mundo. || the highest
This is the most beautiful beach. || Esta es la playa más hermosa. || the most beautiful
""",
           "¿Cuándo se usa more en vez de -er?",
           ["Con adjetivos cortos", "Con adjetivos largos", "Nunca"], 1,
           "Para comparar: adjetivo corto + -er + than (cheaper than); adjetivo largo: more + adjetivo + than (more expensive than). Para 'el más': the + -est (the cheapest) o the most + adjetivo (the most expensive). Irregulares: good → better → the best; bad → worse → the worst.",
           """
Pasto is colder than Cali, but Cali is hotter than Pasto. || Pasto es más frío que Cali, pero Cali es más caliente que Pasto.
""",
           fills="""
My car is ___ than your car. | older / more old | 0 | Mi carro es más viejo que el tuyo.
This hotel is ___ comfortable than the other. | more / most | 0 | Este hotel es más cómodo que el otro.
She's the ___ student in the class. | better / best | 1 | Ella es la mejor estudiante de la clase.
Today is ___ than yesterday. It's raining more. | worse / worst | 0 | Hoy está peor que ayer.
Is Bogotá ___ than Pasto? | bigger / more big | 0 | ¿Bogotá es más grande que Pasto?
"""),
         dialogue("¿Cuál compro?", "💻 Eliges un computador con un vendedor.", """
You: Which one is better, this laptop or that one? || ¿Cuál es mejor, este portátil o ese?
Seller: This one is faster and lighter. || Este es más rápido y más liviano.
You: Is it more expensive? || ¿Es más caro?
Seller: Yes, it's a little more expensive, but the battery is better. || Sí, es un poco más caro, pero la batería es mejor.
You: What is the cheapest one? || ¿Cuál es el más barato?
Seller: That black one. But it's the slowest. || Ese negro. Pero es el más lento.
"""),
         story("Dos ciudades", "🏙️", """
Medellín and Pasto are two very different cities in Colombia. || Medellín y Pasto son dos ciudades muy diferentes de Colombia.
Medellín is bigger and more modern than Pasto. It has a metro. || Medellín es más grande y más moderna que Pasto. Tiene metro.
Pasto is smaller and quieter. The streets are less crowded. || Pasto es más pequeña y tranquila. Las calles están menos llenas.
Medellín is warmer. Pasto is colder, but the views of the volcano are amazing. || Medellín es más cálida. Pasto es más fría, pero la vista del volcán es increíble.
For many people, the Carnival in Pasto is the most beautiful party in Colombia. || Para mucha gente, el Carnaval de Pasto es la fiesta más hermosa de Colombia.
Which city is better? It depends on you! || ¿Qué ciudad es mejor? ¡Depende de ti!
""", questions=[
             ("¿Qué ciudad es más grande?", ["Pasto", "Medellín", "Son iguales"], 1),
             ("¿Qué ciudad es más tranquila?", ["Pasto", "Medellín"], 0),
             ("¿Qué fiesta mencionan?", ["La Feria de las Flores", "El Carnaval de Pasto", "El Festival Vallenato"], 1),
         ]),
         roleplay("Elegir un hotel", "🏨 Ayudas a tu pareja a elegir hotel para el viaje.", """
Partner: Hotel Sol or Hotel Mar? || ¿Hotel Sol o Hotel Mar?
+ Hotel Mar is closer to the beach. || El Hotel Mar queda más cerca de la playa.
- Hotel Mar is the more close. || El Hotel Mar es el más cerca. || Se dice "closer" o "the closest".
Partner: But it's more expensive. || Pero es más caro.
+ Yes, but it's cleaner and more comfortable. || Sí, pero es más limpio y más cómodo.
- Yes, but it's the cheaper in the world. || Sí, pero es el más barato del mundo. || Acaban de decir que es más caro.
Partner: OK, let's book the best one! || ¡Bueno, reservemos el mejor!
+ Perfect. I'm going to book it now. || Perfecto. Lo voy a reservar ya.
- I'm going to book the worst. || Voy a reservar el peor. || Quieren el mejor.
"""),
     ],
     writes="""
El tren es más rápido que el bus. | The train is faster than the bus.
Esta es la mejor pizza de la ciudad. | This is the best pizza in the city. | This is the best pizza in town.
Mi celular es más caro que el tuyo. | My phone is more expensive than yours. | My phone is more expensive than your phone.
""",
     dictations="""
Which one is cheaper? || ¿Cuál es más barato?
It's the most beautiful beach in the world. || Es la playa más hermosa del mundo.
""")
