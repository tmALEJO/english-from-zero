# A2 · Parte 3 (unidades 35–40)

unit("u35-fiestas", "A2", "Fiestas e invitaciones", "🎉",
     "Ya puedo invitar, aceptar y rechazar invitaciones con amabilidad",
     "Celebraciones, invitar con Would you like…?, aceptar, rechazar y dar excusas.",
     grammar=["Would you like to…?", "Let's… / How about…?"],
     items="""
invite | invitar | 💌 | in-váit
invitation | invitación | ✉️ | in-vi-téi-shon
accept | aceptar | ✅ | ak-sépt
refuse | rechazar | ❌ | ri-fiús
guest | invitado | 🧑‍🤝‍🧑 | gest
host | anfitrión | 🏠 | jóust
gift | regalo | 🎁 | guift
candle | vela | 🕯️ | kán-dol
balloon | globo | 🎈 | ba-lúun
cake | pastel / torta | 🍰 | kéik
decorations | decoración | 🎊 | de-ko-réi-shons
fireworks | fuegos artificiales | 🎆 | fáier-uerks
costume | disfraz | 🎭 | kós-tium
Christmas | Navidad | 🎄 | krís-mas
New Year's Eve | fin de año / Nochevieja | 🥂
Halloween | Halloween | 🎃 | ja-lou-íin
anniversary | aniversario | 💞 | a-ni-vér-sa-ri
graduation | graduación / grado | 🎓 | gra-yu-éi-shon
barbecue | asado | 🍖 | bár-bi-kiu
toast | brindis / brindar | 🥂 | tóust
cheers! | ¡salud! (al brindar) | 🍻 | chíers
congratulations! | ¡felicitaciones! | 👏 | kon-gra-chu-léi-shons
Happy birthday! | ¡Feliz cumpleaños! | 🎂
Merry Christmas! | ¡Feliz Navidad! | 🎅
Happy New Year! | ¡Feliz Año Nuevo! | 🎆
Would you like to come? | ¿Te gustaría venir? | 🙋
I'd love to! | ¡Me encantaría! | 😍
I'm afraid I can't | Me temo que no puedo | 😕
Maybe next time | Tal vez la próxima vez | 🔜
Let's go dancing | Vamos a bailar | 💃
How about Friday? | ¿Qué tal el viernes? | 📅
What should I bring? | ¿Qué llevo? | 🧺
dress code | código de vestimenta | 👔
surprise party | fiesta sorpresa | 🤫
have fun | divertirse | 🥳
enjoy | disfrutar | 😊 | en-yói
celebrate | celebrar | 🥂
tradition | tradición | 🪅 | tra-dí-shon
""",
     extras=[
         D("Invitar y proponer planes",
           "Mira tres formas de proponer algo.",
           """
Would you like to come to my party? || ¿Te gustaría venir a mi fiesta? || Would you like to
Let's go dancing on Saturday! || ¡Vamos a bailar el sábado! || Let's
How about a barbecue on Sunday? || ¿Qué tal un asado el domingo? || How about
How about going to the cinema? || ¿Qué tal si vamos al cine? || How about going
Would you like some cake? || ¿Quieres torta? || Would you like
""",
           "¿Qué va después de How about cuando es una acción?",
           ["El verbo con -ing", "to + verbo", "El verbo en pasado"], 0,
           "Would you like to + verbo = ¿te gustaría…? (invitación amable). Let's + verbo = ¡hagamos…! How about + cosa o verbo con -ing = ¿qué tal…? (How about going…?). Para rechazar con amabilidad: I'm afraid I can't… / Maybe next time.",
           """
Would you like to come? — I'd love to! / I'm afraid I can't. || ¿Te gustaría venir? — ¡Me encantaría! / Me temo que no puedo.
""",
           fills="""
Would you like ___ come to dinner? | to / — | 0 | ¿Te gustaría venir a cenar?
How about ___ to the beach? | going / go | 0 | ¿Qué tal si vamos a la playa?
___ go to the concert together! | Let's / Let | 0 | ¡Vamos juntos al concierto!
I'm ___ I can't. I have to work. | afraid / scared | 0 | Me temo que no puedo. Tengo que trabajar.
"""),
         dialogue("Una invitación", "📱 Tu amiga te llama para invitarte.", """
Ana: Hi! It's my birthday on Saturday. Would you like to come to my party? || ¡Hola! El sábado es mi cumpleaños. ¿Te gustaría venir a mi fiesta?
You: I'd love to! What time? || ¡Me encantaría! ¿A qué hora?
Ana: At eight. It's a costume party! || A las ocho. ¡Es una fiesta de disfraces!
You: Fun! What should I bring? || ¡Qué chévere! ¿Qué llevo?
Ana: Nothing, just bring your costume. || Nada, solo trae tu disfraz.
You: Great. See you on Saturday! || Genial. ¡Nos vemos el sábado!
"""),
         story("La fiesta sorpresa", "🤫", """
Last month it was Mr. and Mrs. López's anniversary: thirty years together! || El mes pasado fue el aniversario del señor y la señora López: ¡treinta años juntos!
Their children planned a surprise party. They invited all the family and friends. || Sus hijos planearon una fiesta sorpresa. Invitaron a toda la familia y los amigos.
The guests arrived early and hid in the dark living room. || Los invitados llegaron temprano y se escondieron en la sala oscura.
When the couple opened the door, everybody shouted "Surprise!" || Cuando la pareja abrió la puerta, todos gritaron "¡Sorpresa!"
Mrs. López cried with happiness. There were balloons, flowers and a big cake. || La señora López lloró de felicidad. Había globos, flores y una torta grande.
At midnight everybody made a toast: "Cheers to thirty more years!" || A la medianoche todos brindaron: "¡Salud por treinta años más!"
""", questions=[
             ("¿Qué celebraban?", ["Un cumpleaños", "Un aniversario de treinta años", "Una graduación"], 1),
             ("¿Dónde se escondieron los invitados?", ["En el jardín", "En la sala oscura", "En la cocina"], 1),
             ("¿Qué hizo la señora López?", ["Se enojó", "Lloró de felicidad", "Se fue"], 1),
         ]),
         roleplay("Rechazar con amabilidad", "💼 Un compañero te invita, pero tienes un examen.", """
Leo: We're going to a barbecue on Sunday. Would you like to come? || Vamos a hacer un asado el domingo. ¿Te gustaría venir?
+ Thanks for the invitation, but I'm afraid I can't. || Gracias por la invitación, pero me temo que no puedo.
- No. I don't like you. || No. No me caes bien. || Es grosero; recházalo con amabilidad.
Leo: Oh, why not? || Ah, ¿por qué no?
+ I have an important exam on Monday. I have to study. || Tengo un examen importante el lunes. Tengo que estudiar.
- I have an exam yesterday. || Tengo un examen ayer. || Mezcla tiempos.
Leo: No problem. Good luck! || No hay problema. ¡Buena suerte!
+ Thanks! Maybe next time. Have fun! || ¡Gracias! Tal vez la próxima. ¡Diviértanse!
- Congratulations! || ¡Felicitaciones! || No hay nada que felicitar aquí.
"""),
     ],
     writes="""
¿Te gustaría venir a mi fiesta? | Would you like to come to my party?
¡Me encantaría! | I'd love to! | I would love to!
Me temo que no puedo. | I'm afraid I can't. | I am afraid I can't. ; I'm afraid I cannot.
""",
     dictations="""
How about going to the beach on Sunday? || ¿Qué tal si vamos a la playa el domingo?
Congratulations on your graduation! || ¡Felicitaciones por tu grado!
""",
     speak="""
Thank you for the invitation. I'd love to come! || Gracias por la invitación. ¡Me encantaría ir!
""")

unit("u36-sentimientos", "A2", "Sentimientos y razones", "💗",
     "Ya puedo explicar cómo me siento y por qué",
     "Emociones, causas y consecuencias con because, so, but y when.",
     grammar=["because / so / but", "Adjetivos -ed / -ing"],
     items="""
feelings | sentimientos | 💭 | fíi-lings
happy | feliz | 😄
glad | contento / me alegra | 😊 | glad
upset | molesto / afectado | 😞 | ap-sét
disappointed | decepcionado | 😔 | di-sa-póin-ted
embarrassed | avergonzado / apenado | 😳 | em-bá-rast
jealous | celoso | 😒 | yé-los
lonely | solo / sintiéndose solo | 🥀 | lóun-li
stressed | estresado | 😫 | strest
relaxed | relajado | 😌
calm | tranquilo / calmado | 🧘 | kaam | La l no suena.
confused | confundido | 😕 | kon-fiúsd
confident | seguro de sí mismo | 😎 | kón-fi-dent
grateful | agradecido | 🙏 | gréit-ful
hopeful | esperanzado | 🌅 | jóup-ful
afraid of | con miedo de | 😱
in love | enamorado | 💘
homesick | con nostalgia de casa | 🏡 | jóum-sik
exciting | emocionante | 🎢 | ek-sái-ting
relaxing | relajante | 🛀 | ri-lák-sing
surprising | sorprendente | 😮 | sur-prái-sing
annoying | fastidioso / molesto | 😤 | a-nói-ing
because | porque
so | así que / por eso | ➡️ | sóu
but | pero | ↔️
when | cuando | ⏰ | uen
cheer up | animarse / animar | 🌈
calm down | calmarse | 🫁
worry | preocuparse | 😟 | uó-ri
Don't worry | No te preocupes | 🤗
cry | llorar | 😭
hug | abrazo / abrazar | 🫂 | jag
miss | extrañar | 🥺 | mis
I miss you | Te extraño | 💌
What's wrong? | ¿Qué te pasa? | ❔
I'm glad to hear that | Me alegra oír eso | 😊
I'm sorry to hear that | Siento oír eso | 😔
mood | estado de ánimo | 🌦️ | muud
in a good mood | de buen humor | 😁
in a bad mood | de mal humor | 😠
""",
     extras=[
         D("because y so",
           "Una palabra da la causa, la otra el resultado.",
           """
I'm tired because I worked all night. || Estoy cansado porque trabajé toda la noche. || because
She's happy because she passed the exam. || Está feliz porque pasó el examen. || because
I worked all night, so I'm tired. || Trabajé toda la noche, así que estoy cansado. || so
It was raining, so we stayed home. || Estaba lloviendo, así que nos quedamos en casa. || so
I was nervous, but I was confident. || Estaba nervioso, pero me sentía seguro. || but
""",
           "¿Cuál palabra presenta el RESULTADO?",
           ["because", "so"], 1,
           "because (porque) presenta la causa: I'm sad because… so (así que) presenta el resultado: …, so I'm sad. but (pero) presenta un contraste. Y recuerda: -ed es cómo te sientes (bored, excited); -ing es lo que causa el sentimiento (boring, exciting).",
           """
I was bored because the class was boring. || Estaba aburrido porque la clase era aburrida.
""",
           fills="""
I'm stressed ___ I have three exams. | because / so | 0 | Estoy estresado porque tengo tres exámenes.
I missed the bus, ___ I was late. | so / because | 0 | Perdí el bus, así que llegué tarde.
The movie was very ___. | exciting / excited | 0 | La película fue muy emocionante.
She was ___ when she saw the gift. | surprised / surprising | 0 | Se sorprendió cuando vio el regalo.
"""),
         dialogue("¿Qué te pasa?", "😔 Tu amigo se ve triste.", """
You: Hey, what's wrong? You look upset. || Oye, ¿qué te pasa? Te ves afectado.
Ben: I didn't get the job. I'm really disappointed. || No me dieron el trabajo. Estoy muy decepcionado.
You: I'm sorry to hear that. || Siento oír eso.
Ben: I was so confident, but they chose another person. || Me sentía muy seguro, pero eligieron a otra persona.
You: Don't worry. There are other jobs. Cheer up! || No te preocupes. Hay otros trabajos. ¡Ánimo!
Ben: Thanks. I feel better when I talk to you. || Gracias. Me siento mejor cuando hablo contigo.
"""),
         story("Lejos de casa", "🏡", """
Valeria moved to Canada to study. At first everything was exciting. || Valeria se mudó a Canadá a estudiar. Al principio todo era emocionante.
But after two months she was homesick. She missed her family and the food. || Pero después de dos meses tenía nostalgia. Extrañaba a su familia y la comida.
She felt lonely because she didn't have any friends. || Se sentía sola porque no tenía amigos.
One day a classmate invited her to a party, so she went. || Un día una compañera la invitó a una fiesta, así que fue.
She was nervous, but everybody was friendly. She met people from ten countries! || Estaba nerviosa, pero todos fueron amables. ¡Conoció gente de diez países!
Now she's in a good mood and she calls her mom every Sunday, happy and grateful. || Ahora está de buen humor y llama a su mamá cada domingo, feliz y agradecida.
""", questions=[
             ("¿Por qué se sentía sola?", ["Porque no tenía amigos", "Porque hacía frío", "Porque tenía exámenes"], 0),
             ("¿Qué pasó en la fiesta?", ["Nadie le habló", "Conoció gente de diez países", "Se fue temprano"], 1),
             ("¿Cómo está ahora?", ["De mal humor", "De buen humor y agradecida", "Aburrida"], 1),
         ]),
         roleplay("Calmar a una amiga", "😫 Tu amiga está muy estresada antes de una presentación.", """
Mia: I'm so stressed! My presentation is in ten minutes. || ¡Estoy muy estresada! Mi presentación es en diez minutos.
+ Calm down. You practiced a lot, so you're ready. || Cálmate. Practicaste mucho, así que estás lista.
- You should be stressed. || Deberías estar estresada. || No ayuda a calmarla.
Mia: But what if I forget everything? || ¿Pero y si se me olvida todo?
+ Don't worry. Take a deep breath. You're going to be great. || No te preocupes. Respira profundo. Te va a ir muy bien.
- I'm sorry to hear that. || Siento oír eso. || Eso se dice ante una mala noticia.
Mia: Thanks. I feel more confident now. || Gracias. Ahora me siento más segura.
+ I'm glad to hear that. Good luck! || Me alegra oír eso. ¡Buena suerte!
- I'm jealous. || Estoy celoso. || No tiene sentido aquí.
"""),
     ],
     writes="""
Estoy cansado porque trabajé mucho. | I'm tired because I worked a lot. | I am tired because I worked a lot. ; I'm tired because I worked hard.
Llovía, así que nos quedamos en casa. | It was raining, so we stayed at home. | It was raining, so we stayed home.
Te extraño. | I miss you.
""",
     dictations="""
I'm sorry to hear that. || Siento oír eso.
She was nervous, but everybody was friendly. || Estaba nerviosa, pero todos fueron amables.
""")

unit("u37-estudios", "A2", "Estudios y aprendizaje", "🎓",
     "Ya puedo hablar de mis estudios, materias y planes académicos",
     "Colegio y universidad, materias, exámenes y verbos para hablar de aprender.",
     grammar=["Verbos + to: want to, need to, decide to", "Learn vs teach vs study"],
     items="""
subject | materia | 📒 | sáb-yekt
math | matemáticas | ➗ | maz
science | ciencias | 🔬 | sái-ens
history | historia | 🏺 | hís-to-ri
geography | geografía | 🗺️ | yi-ó-gra-fi
biology | biología | 🧬 | bai-ó-lo-yi
chemistry | química | ⚗️ | ké-mis-tri
physics | física | 🧲 | fí-siks
literature | literatura | 📚 | lí-te-ra-cher
art | arte | 🎨 | art
P.E. | educación física | 🤸 | pi-íi
computer science | informática / ciencias de la computación | 🖥️
university | universidad | 🏛️ | iu-ni-vér-si-ti
college | universidad / instituto | 🏫 | kó-lich
degree | título / carrera | 📜 | di-gríi
career | carrera profesional | 🧗 | ka-ríer
semester | semestre | 📆 | se-més-ter
classroom | salón de clase | 🏫 | klás-rum
exam | examen | 📝 | eg-sám
test | prueba / examen corto | ✏️ | test
grade | nota / grado | 🅰️ | gréid
pass an exam | pasar un examen | ✅
fail an exam | perder un examen | ❌
homework | tarea | 📓 | jóum-uerk
notebook | cuaderno | 📔 | nóut-buk
pen | esfero / bolígrafo | 🖊️ | pen
pencil | lápiz | ✏️ | pén-sil
eraser | borrador | 🧽 | i-réi-ser
backpack (school) | maleta del colegio | 🎒
scholarship | beca | 🏅 | skó-lar-ship
learn | aprender | 🧠
teach | enseñar | 🧑‍🏫 | tíich
practice | practicar | 🔁 | prák-tis
review | repasar | 🔄 | ri-viú
understand | entender | 💡 | an-der-stánd
memorize | memorizar | 🗃️ | mé-mo-rais
make progress | progresar | 📈
I want to learn English | Quiero aprender inglés | 🇬🇧
I need to study more | Necesito estudiar más | 📚
I decided to change careers | Decidí cambiar de carrera | 🔀
""",
     extras=[
         D("Verbos + to + verbo",
           "Fíjate qué va entre los dos verbos.",
           """
I want to learn English. || Quiero aprender inglés. || want to
She needs to study more. || Ella necesita estudiar más. || needs to
We decided to take a course. || Decidimos tomar un curso. || decided to
He hopes to get a scholarship. || Él espera conseguir una beca. || hopes to
They're planning to travel. || Están planeando viajar. || planning to
""",
           "¿Qué une want / need / decide con el siguiente verbo?",
           ["to", "-ing", "nada"], 0,
           "Muchos verbos van seguidos de to + verbo: want to, need to, decide to, hope to, plan to, try to, learn to. Ojo: learn = aprender (tú recibes), teach = enseñar (tú das), study = estudiar.",
           """
My sister teaches math, and I want to learn it too. || Mi hermana enseña matemáticas, y yo también quiero aprenderlas.
""",
           fills="""
I need ___ review for the exam. | to / — | 0 | Necesito repasar para el examen.
My teacher ___ us English. | teaches / learns | 0 | Mi profesor nos enseña inglés.
She decided ___ study medicine. | to / for | 0 | Decidió estudiar medicina.
I ___ my exam! I got an A. | passed / failed | 0 | ¡Pasé mi examen! Saqué una A.
"""),
         dialogue("Después del examen", "📝 Sales del examen de física.", """
Sara: How was the exam? || ¿Cómo te fue en el examen?
You: Difficult! I didn't understand the last question. || ¡Difícil! No entendí la última pregunta.
Sara: Me neither. I think I need to practice more. || Yo tampoco. Creo que necesito practicar más.
You: Do you want to study together for the next one? || ¿Quieres que estudiemos juntos para el próximo?
Sara: Sure! We can review in the library on Thursday. || ¡Claro! Podemos repasar en la biblioteca el jueves.
You: Great. I hope to get a good grade this time. || Genial. Espero sacar buena nota esta vez.
"""),
         story("Cambio de carrera", "🔀", """
When Camila finished school, she decided to study law. || Cuando Camila terminó el colegio, decidió estudiar derecho.
After two semesters she felt bored. She didn't like her subjects. || Después de dos semestres se sentía aburrida. No le gustaban sus materias.
She loved computers, so she took a free online course in programming. || Le encantaban los computadores, así que tomó un curso gratuito en línea de programación.
She practiced every night and made a lot of progress. || Practicaba todas las noches e hizo mucho progreso.
The next year she changed careers to computer science and got a scholarship. || Al año siguiente cambió a ciencias de la computación y consiguió una beca.
Now she teaches programming to children on Saturdays. || Ahora les enseña programación a niños los sábados.
""", questions=[
             ("¿Qué estudió Camila primero?", ["Medicina", "Derecho", "Arte"], 1),
             ("¿Por qué cambió?", ["Se aburría con sus materias", "Perdió los exámenes", "Se mudó"], 0),
             ("¿Qué hace los sábados?", ["Estudia derecho", "Enseña programación a niños", "Trabaja en un banco"], 1),
         ]),
         roleplay("Hablar con el profesor", "🧑‍🏫 Perdiste un examen y hablas con tu profesor.", """
Teacher: You wanted to talk to me? || ¿Querías hablar conmigo?
+ Yes. I failed the exam and I want to improve. || Sí. Perdí el examen y quiero mejorar.
- Yes. I teach the exam. || Sí. Yo enseño el examen. || Tú no enseñas; quieres mejorar.
Teacher: OK. What was difficult for you? || Bueno. ¿Qué se te hizo difícil?
+ I didn't understand the chemistry problems. || No entendí los problemas de química.
- I understanded the problems. || Yo entendí los problemas. || Además, "understand" en pasado es "understood".
Teacher: You need to practice more. I can give you extra exercises. || Necesitas practicar más. Te puedo dar ejercicios extra.
+ Thank you! I'm going to practice every day. || ¡Gracias! Voy a practicar todos los días.
- Thank you! I need practice to every day. || ¡Gracias! Necesito práctica a todos los días. || Orden extraño; di "I'm going to practice every day".
"""),
     ],
     writes="""
Quiero aprender inglés. | I want to learn English.
Necesito estudiar más. | I need to study more.
Pasé el examen. | I passed the exam. | I passed my exam.
""",
     dictations="""
She got a scholarship to study abroad. || Ella consiguió una beca para estudiar en el exterior.
I need to review before the test. || Necesito repasar antes de la prueba.
""")

unit("u38-como", "A2", "Cómo hacemos las cosas", "🏃‍♂️",
     "Ya puedo describir cómo y con qué frecuencia hago las cosas",
     "Adverbios de modo (-ly) y expresiones de frecuencia para describir acciones.",
     grammar=["Adverbios de modo: quickly, carefully", "How often…?"],
     items="""
quickly | rápidamente | ⚡ | kuík-li
slowly | lentamente | 🐢 | slóu-li
carefully | con cuidado | 🧐 | kér-fu-li
easily | fácilmente | 👌 | íi-si-li
quietly | en voz baja / en silencio | 🤫 | kuái-et-li
loudly | en voz alta / duro | 📢 | láud-li
badly | mal | 👎 | bád-li
well | bien | 👍 | uel
hard | duro / con esfuerzo | 💪 | jard
fast (adverb) | rápido | 🏎️
early (adverb) | temprano | 🌅
late (adverb) | tarde | 🌙
suddenly | de repente | 💥 | sá-den-li
fortunately | afortunadamente | 🍀 | fór-chu-net-li
unfortunately | desafortunadamente | 😓 | an-fór-chu-net-li
perfectly | perfectamente | 💯 | pér-fekt-li
clearly | claramente | 🔊 | klíer-li
politely | educadamente | 🎩 | po-láit-li
happily | felizmente / con alegría | 😄 | já-pi-li
together | juntos | 🤝 | tu-gué-der
alone | solo / solos | 🧍 | a-lóun
How often? | ¿Con qué frecuencia? | 🔁
once a week | una vez a la semana | 1️⃣
twice a month | dos veces al mes | 2️⃣
three times a year | tres veces al año | 3️⃣
every morning | todas las mañanas | 🌄
once in a while | de vez en cuando | 🎲
almost never | casi nunca | 🚫
hardly ever | casi nunca | 🚫 | hárd-li é-ver
often | a menudo | 🔄 | ó-fen
rarely | rara vez | 🌑 | rér-li
still | todavía | ⏸️ | stil
already | ya | ✔️ | ol-ré-di
yet | todavía (en negativo) / ya (en preguntas) | ⏳ | iet
again | otra vez | 🔂 | a-guén
almost | casi | 🔜 | ól-moust
""",
     extras=[
         D("Adverbios con -ly",
           "Compara la palabra que describe a la persona con la que describe la acción.",
           """
She's a careful driver. She drives carefully. || Es una conductora cuidadosa. Maneja con cuidado. || carefully
He's a quick runner. He runs quickly. || Es un corredor rápido. Corre rápidamente. || quickly
The music is loud. They sing loudly. || La música está duro. Cantan duro. || loudly
He's a good singer. He sings well. || Es un buen cantante. Canta bien. || well
She's a hard worker. She works hard. || Es muy trabajadora. Trabaja duro. || hard
""",
           "¿Qué se agrega al adjetivo para describir cómo se hace algo?",
           ["-ly", "-ing", "-er"], 0,
           "El adjetivo describe a la persona o cosa (a careful driver); el ADVERBIO describe la acción (drives carefully). Casi siempre es adjetivo + -ly (como '-mente' en español). Irregulares: good → well, fast → fast, hard → hard.",
           """
I speak English slowly, but I speak it clearly. || Hablo inglés despacio, pero lo hablo claramente.
""",
           fills="""
Please drive ___. The road is dangerous. | carefully / careful | 0 | Por favor maneja con cuidado. La carretera es peligrosa.
She speaks English very ___. | well / good | 0 | Ella habla inglés muy bien.
How ___ do you go to the gym? | often / much | 0 | ¿Con qué frecuencia vas al gimnasio?
I go to the dentist ___ a year. | twice / two | 0 | Voy al odontólogo dos veces al año.
"""),
         tip("⏳", "already / yet / still", "already = ya (antes de lo esperado): I already finished. yet = ya / todavía, en preguntas y negativos al final: Did you finish yet? I didn't finish yet. still = todavía (sigue pasando): I still live with my parents."),
         dialogue("Hábitos saludables", "🏃 Una entrevista para una revista de salud.", """
Reporter: How often do you exercise? || ¿Con qué frecuencia hace ejercicio?
Runner: I run every morning and I go to the gym twice a week. || Corro todas las mañanas y voy al gimnasio dos veces por semana.
Reporter: Do you eat fast food? || ¿Come comida rápida?
Runner: Hardly ever. Maybe once in a while with my kids. || Casi nunca. Tal vez de vez en cuando con mis hijos.
Reporter: And do you sleep well? || ¿Y duerme bien?
Runner: Yes, I sleep perfectly. I go to bed early. || Sí, duermo perfectamente. Me acuesto temprano.
"""),
         story("El examen de conducción", "🚗", """
Pablo took his driving test last Tuesday. He was very nervous. || Pablo presentó su examen de conducción el martes pasado. Estaba muy nervioso.
He started the car slowly and drove carefully through the city. || Prendió el carro despacio y manejó con cuidado por la ciudad.
Suddenly a dog ran into the street! || ¡De repente un perro se atravesó en la calle!
Fortunately Pablo stopped quickly and the dog was OK. || Afortunadamente Pablo frenó rápido y el perro estuvo bien.
The examiner smiled and said, "You reacted perfectly." || El examinador sonrió y dijo: "Reaccionó perfectamente."
Pablo passed the test. He still remembers that dog! || Pablo pasó el examen. ¡Todavía se acuerda de ese perro!
""", questions=[
             ("¿Cómo manejó Pablo?", ["Rápido y sin cuidado", "Con cuidado", "Muy mal"], 1),
             ("¿Qué pasó de repente?", ["Llovió", "Un perro se atravesó", "Se dañó el carro"], 1),
             ("¿Pasó el examen?", ["Sí", "No"], 0),
         ]),
         roleplay("Pedir que hablen más despacio", "📞 Una persona te habla en inglés muy rápido por teléfono.", """
Agent: Hithankyouforcallinghowcanihelpyoutoday? || Holagraciasporllamarenquélepuedoayudar?
+ Sorry, could you speak more slowly, please? || Perdón, ¿podría hablar más despacio, por favor?
- Sorry, could you speak more slow quickly? || Perdón, ¿podría hablar más lento rápidamente? || Contradictorio.
Agent: Of course. How… can… I… help… you? || Claro. ¿En… qué… le… puedo… ayudar?
+ Thank you. I'd like to change my address. || Gracias. Quisiera cambiar mi dirección.
- Thank you. You speak badly. || Gracias. Usted habla mal. || Es grosero.
Agent: No problem. Can you spell your name, please? || No hay problema. ¿Me puede deletrear su nombre?
+ Sure. It's S-A-M. || Claro. Es S-A-M.
- Sure. It's quickly. || Claro. Es rápidamente. || No responde.
"""),
     ],
     writes="""
Maneja con cuidado. | Drive carefully.
Ella habla inglés muy bien. | She speaks English very well.
Voy al gimnasio dos veces a la semana. | I go to the gym twice a week.
""",
     dictations="""
Could you speak more slowly, please? || ¿Podría hablar más despacio, por favor?
I still live with my parents. || Todavía vivo con mis papás.
""")

unit("u39-cocina", "A2", "En la cocina", "👨‍🍳",
     "Ya puedo seguir y dar una receta",
     "Verbos de cocina, utensilios y cómo dar instrucciones en orden.",
     grammar=["Imperativo en recetas", "Secuencia: first, then, next, finally"],
     items="""
recipe | receta | 📜 | ré-si-pi
ingredients | ingredientes | 🧺 | in-gríi-di-ents
cut | cortar | 🔪 | kat
chop | picar | 🥬 | chop
slice | tajar / tajada | 🍕 | sláis
peel | pelar | 🍌 | píil
mix | mezclar | 🥣 | miks
stir | revolver | 🥄 | ster
boil | hervir | ♨️ | bóil
fry | freír | 🍳 | frái
bake | hornear | 🧁 | béik
grill | asar a la parrilla | 🍖 | gril
heat | calentar | 🔥 | jíit
add | agregar | ➕ | ad
pour | verter / echar (líquido) | 🫗 | por
melt | derretir | 🧈 | melt
taste | probar (sabor) / sabor | 👅 | téist
serve | servir | 🍽️ | serv
pan | sartén | 🍳 | pan
pot | olla | 🍲 | pot
oven | horno | ♨️ | á-ven
stove | estufa | 🔥 | stóuv
knife | cuchillo | 🔪 | náif | La k no suena.
spoon | cuchara | 🥄 | spuun
fork | tenedor | 🍴 | fork
plate | plato | 🍽️ | pléit
bowl | tazón / bowl | 🥣 | bóul
cup | taza | ☕ | kap
glass | vaso | 🥛 | glas
flour | harina | 🌾 | fláur
butter | mantequilla | 🧈 | bá-ter
garlic | ajo | 🧄 | gár-lik
pepper | pimienta | 🌶️ | pé-per
spicy | picante | 🌶️ | spái-si
sweet | dulce | 🍭 | suíit
salty | salado | 🧂 | sól-ti
raw | crudo | 🥩 | ró
first | primero | 1️⃣ | ferst
next | luego / después | ➡️
finally (recipe) | por último | 🏁
""",
     extras=[
         D("Dar una receta en orden",
           "Así se escribe una receta. Mira cómo empiezan los pasos.",
           """
First, chop the onion and the garlic. || Primero, pica la cebolla y el ajo. || First
Then, heat some oil in a pan. || Luego, calienta un poco de aceite en una sartén. || Then
Next, add the vegetables and stir. || Después, agrega las verduras y revuelve. || Next
Fry for five minutes. Don't burn them! || Fríe cinco minutos. ¡No las quemes! || Don't
Finally, add salt and serve. || Por último, agrega sal y sirve. || Finally
""",
           "¿Cómo están escritos los pasos de una receta?",
           ["Con el verbo al principio (imperativo)", "En pasado", "Con 'you should' siempre"], 0,
           "Las recetas usan el IMPERATIVO (el verbo solo, al principio): Chop, Add, Stir. Para ordenar los pasos: First → Then → Next → After that → Finally. Para algo que NO se debe hacer: Don't + verbo.",
           """
First, boil the water. Then add the rice. Finally, wait twenty minutes. || Primero, hierve el agua. Luego agrega el arroz. Por último, espera veinte minutos.
""",
           fills="""
___, peel the potatoes. (primer paso) | First / Finally | 0 | Primero, pela las papas.
___ the eggs and the sugar in a bowl. | Mix / Mixes | 0 | Mezcla los huevos y el azúcar en un tazón.
___ the cake in the oven for forty minutes. | Bake / Fry | 0 | Hornea la torta en el horno cuarenta minutos.
Don't ___ the milk. It burns easily. | boil / boiling | 0 | No hiervas la leche. Se quema fácil.
"""),
         dialogue("Cocinando juntos", "🍳 Le enseñas a tu amigo extranjero a hacer arepas.", """
Mark: What do we need? || ¿Qué necesitamos?
You: Corn flour, water, salt and cheese. || Harina de maíz, agua, sal y queso.
Mark: OK. What do I do first? || Bueno. ¿Qué hago primero?
You: First, mix the flour with warm water and a little salt. || Primero, mezcla la harina con agua tibia y un poco de sal.
Mark: Like this? || ¿Así?
You: Perfect. Next, make small balls and press them. Then cook them in a hot pan. || Perfecto. Luego, haz bolitas y aplánalas. Después ásalas en una sartén caliente.
Mark: Mmm, they smell amazing! || ¡Mmm, huelen increíble!
"""),
         story("El desastre de la torta", "🎂", """
For her mom's birthday, Isabel wanted to bake a chocolate cake. || Para el cumpleaños de su mamá, Isabel quería hornear una torta de chocolate.
She found a recipe online and bought all the ingredients. || Encontró una receta en internet y compró todos los ingredientes.
First she melted the butter and the chocolate. Then she mixed the flour, eggs and sugar. || Primero derritió la mantequilla y el chocolate. Luego mezcló la harina, los huevos y el azúcar.
She put the cake in the oven, but she forgot to set the timer! || Puso la torta en el horno, ¡pero se le olvidó poner el temporizador!
After two hours the kitchen smelled terrible. The cake was black! || Después de dos horas la cocina olía horrible. ¡La torta estaba negra!
She laughed, bought a cake at the bakery and wrote "Made with love" on the box. || Se rió, compró una torta en la panadería y escribió "Hecha con amor" en la caja.
""", questions=[
             ("¿Qué quería hornear Isabel?", ["Pan", "Una torta de chocolate", "Galletas"], 1),
             ("¿Qué se le olvidó?", ["Comprar huevos", "Poner el temporizador", "Prender el horno"], 1),
             ("¿Qué hizo al final?", ["Lloró", "Compró una torta en la panadería", "Hizo otra torta"], 1),
         ]),
         roleplay("Explica tu receta", "🍲 Un amigo quiere saber cómo haces tu sopa favorita.", """
Friend: How do you make your soup? || ¿Cómo haces tu sopa?
+ First, I boil water in a big pot. || Primero, hiervo agua en una olla grande.
- First, I bake water in the oven. || Primero, horneo agua en el horno. || El agua se hierve, no se hornea.
Friend: And then? || ¿Y luego?
+ Then I add potatoes, carrots and chicken. || Luego agrego papas, zanahorias y pollo.
- Then I add a knife. || Luego agrego un cuchillo. || El cuchillo no va en la sopa.
Friend: How long does it take? || ¿Cuánto se demora?
+ About an hour. Finally, I add salt and serve it hot. || Como una hora. Por último, agrego sal y la sirvo caliente.
- About an hour ago. || Hace como una hora. || "Ago" es pasado; aquí es duración.
"""),
     ],
     writes="""
Primero, pica la cebolla. | First, chop the onion. | First chop the onion.
Agrega sal y revuelve. | Add salt and stir. | Add some salt and stir.
No quemes el arroz. | Don't burn the rice. | Do not burn the rice.
""",
     dictations="""
Mix the flour with the eggs. || Mezcla la harina con los huevos.
Bake the cake for forty minutes. || Hornea la torta durante cuarenta minutos.
""")

unit("u40-narrar", "A2", "Contar lo que estaba pasando", "🎬",
     "Ya puedo contar una historia con lo que estaba pasando cuando algo ocurrió",
     "El pasado continuo (was doing) junto con el pasado simple para narrar historias.",
     grammar=["Pasado continuo: was / were + -ing", "when / while"],
     items="""
I was sleeping | Estaba durmiendo | 😴
They were watching TV | Estaban viendo televisión | 📺
What were you doing? | ¿Qué estabas haciendo? | ❓
while | mientras | ⏸️ | uáil
suddenly | de repente
at that moment | en ese momento | ⚡
meanwhile | mientras tanto | 🔀 | míin-uail
the next day | al día siguiente | ➡️
in the end | al final | 🏁
once upon a time | había una vez | 📖
happen | pasar / suceder
fall (fell) | caer (cayó) | 🍂 | fol
drop | dejar caer | 🫳 | drop
hit | golpear / chocar | 👊 | jit
crash | chocar / estrellarse | 💥 | krash
scream | gritar | 😱 | skríim
shout | gritar / gritarle | 📣 | sháut
whisper | susurrar | 🤫 | uís-per
knock | tocar (la puerta) | 🚪 | nok | La k no suena.
ring | sonar (timbre / teléfono) | 🔔 | ring
steal (stole) | robar (robó) | 🦹 | stíil
thief | ladrón | 🦹 | zíif
escape | escapar | 🏃 | es-kéip
chase | perseguir | 🐕‍🦺 | chéis
hide (hid) | esconder (escondió) | 🙈 | jáid
search for | buscar | 🔎
notice | darse cuenta / notar | 👁️ | nóu-tis
realize | darse cuenta | 💡 | rí-a-lais
turn off | apagar | 📴
turn on | prender / encender | 🔛
power outage | apagón / se fue la luz | 🔌
candle (light) | vela | 🕯️
dark | oscuro | 🌑 | dark
noise | ruido | 🔉 | nóis
strange | extraño | 👽 | stréinch
ghost | fantasma | 👻 | góust
afraid | con miedo | 😨 | a-fréid
brave | valiente | 🦸 | bréiv
witness | testigo | 👀 | uít-nes
""",
     extras=[
         D("Pasado continuo + pasado simple",
           "Una acción estaba en curso y otra la interrumpió.",
           """
I was sleeping when the phone rang. || Estaba durmiendo cuando sonó el teléfono. || was sleeping
They were watching TV when the lights went out. || Estaban viendo televisión cuando se fue la luz. || were watching
She was cooking when somebody knocked on the door. || Estaba cocinando cuando alguien tocó la puerta. || was cooking
While we were walking, it started to rain. || Mientras caminábamos, empezó a llover. || were walking
What were you doing at ten last night? || ¿Qué estabas haciendo anoche a las diez? || were you doing
""",
           "¿Qué parte usa was / were + -ing?",
           ["La acción larga que estaba pasando", "La acción corta que interrumpe"], 0,
           "Este es el PASADO CONTINUO: was / were + verbo con -ing (estaba + -ando/-iendo). Describe la escena o la acción larga. El PASADO SIMPLE cuenta el suceso corto que la interrumpe: I was reading WHEN the phone RANG. while se usa con la acción larga.",
           """
While I was walking home, I saw a strange light in the sky. || Mientras caminaba a casa, vi una luz extraña en el cielo.
""",
           fills="""
I ___ a shower when you called. | was taking / took | 0 | Me estaba bañando cuando llamaste.
They were playing football when it ___ to rain. | started / was starting | 0 | Estaban jugando fútbol cuando empezó a llover.
___ she was cooking, the baby woke up. | While / When | 0 | Mientras ella cocinaba, el bebé se despertó.
What ___ you doing at midnight? | were / was | 0 | ¿Qué estabas haciendo a la medianoche?
"""),
         dialogue("Anoche se fue la luz", "🕯️ Hablas con tu vecina en el ascensor.", """
Neighbor: Did you notice the power outage last night? || ¿Se dio cuenta del apagón de anoche?
You: Yes! I was watching a movie when everything turned off. || ¡Sí! Estaba viendo una película cuando todo se apagó.
Neighbor: I was cooking dinner. I couldn't see anything! || Yo estaba cocinando la cena. ¡No veía nada!
You: What did you do? || ¿Qué hizo?
Neighbor: I found some candles and we ate in the dark. It was romantic! || Encontré unas velas y comimos a oscuras. ¡Fue romántico!
You: Ha ha. In the end it wasn't so bad! || Ja ja. ¡Al final no estuvo tan mal!
"""),
         story("Un ruido en la noche", "👻", """
It was a dark and rainy night. Lucía was reading in bed. || Era una noche oscura y lluviosa. Lucía estaba leyendo en la cama.
Her parents were sleeping and her brother was playing video games. || Sus papás estaban durmiendo y su hermano estaba jugando videojuegos.
Suddenly she heard a strange noise in the kitchen. || De repente oyó un ruido extraño en la cocina.
She was afraid, but she was brave. She took her phone and went downstairs. || Tenía miedo, pero fue valiente. Tomó su celular y bajó las escaleras.
While she was walking to the kitchen, the noise stopped. || Mientras caminaba hacia la cocina, el ruido paró.
She turned on the light and screamed… then she laughed. It was the cat! It was eating the chicken from dinner. || Prendió la luz y gritó… luego se rió. ¡Era el gato! Se estaba comiendo el pollo de la cena.
""", questions=[
             ("¿Qué estaba haciendo Lucía?", ["Durmiendo", "Leyendo en la cama", "Cocinando"], 1),
             ("¿Dónde oyó el ruido?", ["En el jardín", "En la cocina", "En su cuarto"], 1),
             ("¿Qué causaba el ruido?", ["Un ladrón", "Un fantasma", "El gato"], 2),
         ]),
         roleplay("Declaración a la policía", "👮 Te robaron el celular en la calle y hablas con un policía.", """
Officer: What happened? || ¿Qué pasó?
+ A man stole my phone while I was waiting for the bus. || Un hombre me robó el celular mientras esperaba el bus.
- A man was stealing my phone while I waited tomorrow. || Un hombre estaba robando mi celular mientras esperé mañana. || Mezcla tiempos.
Officer: What were you doing at that moment? || ¿Qué estaba haciendo en ese momento?
+ I was talking to my sister on the phone. || Estaba hablando con mi hermana por teléfono.
- I talk to my sister. || Hablo con mi hermana. || Debe ser pasado continuo: "I was talking".
Officer: Did you see where he went? || ¿Vio para dónde se fue?
+ Yes, he ran toward the park. || Sí, corrió hacia el parque.
- Yes, he was run toward the park. || Sí, él estaba corrió hacia el parque. || Se dice "he ran".
"""),
     ],
     writes="""
Estaba durmiendo cuando sonó el teléfono. | I was sleeping when the phone rang.
¿Qué estabas haciendo? | What were you doing?
Mientras caminaba, empezó a llover. | While I was walking, it started to rain. | While I was walking it started to rain.
""",
     dictations="""
They were watching TV when the lights went out. || Estaban viendo televisión cuando se fue la luz.
Suddenly she heard a strange noise. || De repente oyó un ruido extraño.
""",
     speak="""
I was studying English when my friend called me. || Estaba estudiando inglés cuando mi amigo me llamó.
""")
