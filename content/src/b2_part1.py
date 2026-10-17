# B2 · Parte 1 (unidades 59–64)

unit("u59-noticias", "B2", "Noticias y medios", "📰",
     "Ya puedo entender y resumir una noticia",
     "Vocabulario periodístico, la pasiva en todos los tiempos y cómo resumir lo que se informa.",
     grammar=["Pasiva en todos los tiempos", "It is said that… / He is believed to…"],
     items="""
breaking news | noticia de última hora | 🚨
headline (B2) | titular
front page | primera plana | 🗞️
coverage | cubrimiento | 📡 | ká-ve-rich
broadcast | transmitir / emisión | 📺 | bród-kast
anchor | presentador de noticias | 🎙️ | án-ker
correspondent | corresponsal | 🌍 | ko-res-pón-dent
editor | editor | ✏️ | é-di-tor
press | prensa | 🗞️
press conference | rueda de prensa | 🎤
interview (B2) | entrevista
eyewitness | testigo presencial | 👁️ | ái-uit-nes
spokesperson | vocero | 🗣️ | spóuks-per-son
statement | declaración / comunicado | 📃 | stéit-ment
claim | afirmar / afirmación | ☝️ | kléim
deny | negar | 🙅 | di-nái
confirm | confirmar | ✅ | kon-férm
reveal | revelar | 🔦 | ri-víil
announce | anunciar | 📣 | a-náuns
report (B2) | informar
investigate | investigar | 🕵️ | in-vés-ti-gueit
investigation | investigación | 🔍
scandal | escándalo | 💣 | skán-dal
corruption | corrupción | 💰 | ko-ráp-shon
election | elecciones | 🗳️ | i-lék-shon
vote (B2) | votar
candidate (B2) | candidato
campaign (B2) | campaña
policy | política (medida) | 📋 | pó-li-si
politician | político | 🏛️ | po-li-tí-shan
minister | ministro | 🎩 | mí-nis-ter
mayor | alcalde | 🏙️ | méi-or
protest | protesta / protestar | ✊ | próu-test
strike | huelga | 🪧 | stráik
crisis | crisis | ⚠️ | krái-sis
disaster | desastre | 🌪️ | di-sás-ter
earthquake | terremoto | 🌐 | érz-kueik
hurricane | huracán | 🌀 | já-ri-kein
landslide | derrumbe | ⛰️ | lánd-slaid
injured | herido | 🤕 | ín-yerd
victim | víctima | 🩹 | vík-tim
casualties | víctimas (muertos y heridos) | ⚰️ | ká-shual-tis
rescue | rescate / rescatar | 🚁 | rés-kiu
evacuate | evacuar | 🏃 | i-vá-kiu-eit
aid | ayuda (humanitaria) | 🤝 | éid
damage (B2) | daño
estimate | calcular / estimar | 📊 | és-ti-meit
according to (B2) | según
allegedly | supuestamente | 🤨 | a-lé-yed-li
reportedly | según informes | 📰 | ri-pór-ted-li
officially | oficialmente | 🏛️ | o-fí-sha-li
unconfirmed | sin confirmar | ❓
biased | parcializado | ⚖️ | bái-ast
objective | objetivo (neutral) | 🎯 | ob-yék-tiv
censorship | censura | 🚫 | sén-sor-ship
freedom of speech | libertad de expresión | 🗽
public opinion | opinión pública | 👥
poll | encuesta | 📊 | póul
survey | encuesta / estudio | 📋 | sér-vei
statistics | estadísticas | 📈 | sta-tís-tiks
majority | mayoría | 👥 | ma-yó-ri-ti
minority | minoría | 👤 | mai-nó-ri-ti
increase sharply | aumentar bruscamente | 📈
remain | permanecer / seguir | ⏸️ | ri-méin
take place | tener lugar / ocurrir | 📍
It is said that… | Se dice que… | 💬
He is believed to be… | Se cree que él es… | 🤔
It has been reported that… | Se ha informado que… | 📰
The suspect was arrested | El sospechoso fue arrestado | 🚔
Talks are being held | Se están llevando a cabo conversaciones | 🗣️
""",
     extras=[
         D("La pasiva en todos los tiempos",
           "Las noticias usan mucho la pasiva. Mira el verbo be en cada frase.",
           """
The road is being repaired. || Están reparando la carretera. || is being repaired
Ten people have been injured. || Diez personas han resultado heridas. || have been injured
The suspect was arrested last night. || El sospechoso fue arrestado anoche. || was arrested
The results will be announced tomorrow. || Los resultados se anunciarán mañana. || will be announced
The bridge had been closed before the storm. || El puente había sido cerrado antes de la tormenta. || had been closed
It is believed that the fire started in the kitchen. || Se cree que el incendio empezó en la cocina. || It is believed
""",
           "¿Qué cambia entre una pasiva y otra?",
           ["El tiempo del verbo be (is being, has been, will be…)", "El participio", "Nada"], 0,
           "La pasiva es siempre be + participio, y solo cambia el tiempo de be: is done, is being done, was done, has been done, will be done, had been done. Las noticias usan formas impersonales para informar sin afirmar: It is said / believed / reported that… o He is said to be… (se dice que él es…).",
           """
The minister is reported to have resigned, but it hasn't been confirmed yet. || Según informes, el ministro renunció, pero aún no se ha confirmado.
""",
           fills="""
The new hospital ___ built at the moment. | is being / has being | 0 | El nuevo hospital se está construyendo en este momento.
Three people ___ been rescued so far. | have / has | 0 | Hasta ahora han sido rescatadas tres personas.
The winner will ___ announced on Friday. | be / been | 0 | El ganador será anunciado el viernes.
It ___ said that the mayor will resign. | is / was being | 0 | Se dice que el alcalde va a renunciar.
The singer is believed ___ in Miami now. | to be / being | 0 | Se cree que la cantante está ahora en Miami.
"""),
         dialogue("¿Viste las noticias?", "📺 Dos compañeros de trabajo comentan una noticia.", """
Ana: Did you hear about the landslide on the highway? || ¿Supiste del derrumbe en la autopista?
Pedro: Yes. Apparently the road has been closed since yesterday. || Sí. Al parecer la vía está cerrada desde ayer.
Ana: Were there any casualties? || ¿Hubo víctimas?
Pedro: According to the news, two people were injured, but nobody was killed. || Según las noticias, dos personas resultaron heridas, pero nadie murió.
Ana: Thank God. Do they know when it will be reopened? || Gracias a Dios. ¿Saben cuándo la van a reabrir?
Pedro: It's estimated that it'll take at least a week. Aid is being sent to the nearby towns. || Se calcula que tomará al menos una semana. Se está enviando ayuda a los pueblos cercanos.
"""),
         story("Cómo leer una noticia con ojo crítico", "🧐", """
Every day we are bombarded with headlines, but not all of them are reliable. || Cada día nos bombardean con titulares, pero no todos son confiables.
First, check who wrote the article and when it was published. || Primero, revisa quién escribió el artículo y cuándo fue publicado.
Second, notice the language. Words like "allegedly" or "reportedly" mean that the information hasn't been confirmed. || Segundo, fíjate en el lenguaje. Palabras como "supuestamente" o "según informes" significan que la información no ha sido confirmada.
Third, ask yourself whether the article is objective or biased. Does it present different points of view? || Tercero, pregúntate si el artículo es objetivo o parcializado. ¿Presenta distintos puntos de vista?
Finally, compare the coverage in several media outlets before you form an opinion. || Por último, compara el cubrimiento en varios medios antes de formarte una opinión.
In a world full of misinformation, critical reading is one of the most valuable skills you can develop. || En un mundo lleno de desinformación, la lectura crítica es una de las habilidades más valiosas que puedes desarrollar.
""", questions=[
             ("¿Qué significa 'allegedly'?", ["Que la información está confirmada", "Que la información no ha sido confirmada", "Que es una opinión"], 1),
             ("¿Qué recomienda hacer antes de formarse una opinión?", ["Compartir la noticia", "Comparar el cubrimiento en varios medios", "Leer solo el titular"], 1),
             ("Según el texto, ¿qué habilidad es muy valiosa?", ["La lectura crítica", "Escribir rápido", "Usar redes sociales"], 0),
         ]),
         roleplay("Resumir una noticia", "🗞️ Tu jefa no vio las noticias y te pregunta qué pasó.", """
Boss: What happened in the city center this morning? || ¿Qué pasó en el centro esta mañana?
+ There was a protest. Thousands of workers went on strike. || Hubo una protesta. Miles de trabajadores se fueron a huelga.
- There was protested a strike. || Hubo protestado una huelga. || Frase mal construida.
Boss: Was anybody hurt? || ¿Hubo heridos?
+ It's been reported that a few people were slightly injured. || Se ha informado que unas pocas personas resultaron levemente heridas.
- It has reported that people injured. || Ha informado que gente hirió. || Falta la pasiva: "It has been reported… were injured".
Boss: What does the government say? || ¿Qué dice el gobierno?
+ A spokesperson said talks are being held with the unions. || Un vocero dijo que se están llevando a cabo conversaciones con los sindicatos.
- The government is said nothing. || El gobierno es dicho nada. || Se dice "The government hasn't said anything".
"""),
     ],
     writes="""
Se dice que el alcalde va a renunciar. | It is said that the mayor will resign. | It's said that the mayor will resign. ; The mayor is said to be resigning. ; It is said that the mayor is going to resign.
La carretera está siendo reparada. | The road is being repaired.
Diez personas han sido rescatadas. | Ten people have been rescued.
""",
     dictations="""
The results will be announced tomorrow morning. || Los resultados se anunciarán mañana por la mañana.
According to eyewitnesses, the fire started at midnight. || Según testigos, el incendio empezó a la medianoche.
""")

unit("u60-imaginar", "B2", "Si yo fuera…", "💭",
     "Ya puedo hablar de situaciones imaginarias e hipotéticas",
     "El segundo condicional (If I had…, I would…) para imaginar, dar consejos y soñar.",
     grammar=["Segundo condicional", "If I were you…", "would / could / might"],
     items="""
would | (condicional: haría, iría…) | 💭
wouldn't | no (haría) | 🚫
If I were you | Yo que tú / Si yo fuera tú | 🫵
If I had more time | Si tuviera más tiempo | ⏳
I would travel the world | Viajaría por el mundo | 🌍
What would you do if…? | ¿Qué harías si…? | ❓
imagine | imaginar | 🌈 | i-má-yin
imaginary | imaginario | 🦄 | i-má-yi-ne-ri
hypothetical | hipotético | 🤔 | jai-po-zé-ti-kal
situation | situación | 🎬 | si-chu-éi-shon
dilemma | dilema | ⚖️ | di-lé-ma
lottery | lotería | 🎰 | ló-te-ri
win the lottery | ganarse la lotería | 💰
millionaire | millonario | 💎 | mi-lio-nér
desert island | isla desierta | 🏝️
superpower | superpoder | 🦸 | sú-per-pau-er
invisible | invisible | 👻 | in-ví-si-bol
time travel | viajar en el tiempo | ⏳
read minds | leer la mente | 🧠
fly (B2) | volar
choose (B2) | escoger
decide (B2) | decidir
might | podría (posibilidad) | 🎲 | máit
could (ability) | podría (habilidad o posibilidad) | 💪
otherwise (B2) | de lo contrario
in that case | en ese caso | ➡️
suppose | suponer | 🤔 | su-póus
supposing | suponiendo que | 💭
as long as | siempre y cuando | 🔗
even if | aun si / incluso si | 🔁
provided that | con tal de que | ✅
ideal | ideal | ✨ | ai-díil
perfect world | mundo perfecto | 🌎
dream job | trabajo soñado | 💼
quit my job | renunciar a mi trabajo | 🚪
buy a mansion | comprar una mansión | 🏰
donate | donar | 🎁 | dóu-neit
charity | beneficencia / obra de caridad | 🤲 | chá-ri-ti
take a gap year | tomarse un año sabático | 🗓️
live on the moon | vivir en la luna | 🌙
be in charge | estar a cargo | 👑
president | presidente | 🎩 | pré-si-dent
change the world | cambiar el mundo | 🌍
regret (B2) | arrepentirse
advice (B2) | consejo
recommend | recomendar | 👍 | re-ko-ménd
honestly | honestamente | 🫡 | ó-nest-li
I'd rather… | Preferiría… | ⚖️
I wouldn't mind… | No me molestaría… | 😌
It would be great | Sería genial | 🤩
It would be a disaster | Sería un desastre | 🌪️
That would never happen | Eso nunca pasaría | 🙅
""",
     extras=[
         D("Segundo condicional",
           "Compara una situación real con una imaginaria.",
           """
If I have time, I'll call you. (posible) || Si tengo tiempo, te llamo. || have, 'll
If I had more time, I would learn Japanese. (imaginario) || Si tuviera más tiempo, aprendería japonés. || had, would
If she won the lottery, she would buy a house. || Si ella se ganara la lotería, compraría una casa. || won, would
If I were you, I wouldn't accept the offer. || Yo que tú, no aceptaría la oferta. || were, wouldn't
What would you do if you could fly? || ¿Qué harías si pudieras volar? || would, could
""",
           "En una situación imaginaria, ¿qué tiempo va después de if?",
           ["Presente (if I have)", "Pasado (if I had)", "Futuro (if I will have)"], 1,
           "El SEGUNDO CONDICIONAL imagina situaciones irreales o poco probables: If + pasado, would + verbo. Aunque usa pasado, habla del presente o futuro. Con be se usa were para todos: If I were rich… Para aconsejar: If I were you, I would… could y might también sirven (podría).",
           """
If I lived by the sea, I would swim every morning. But I live in the mountains! || Si viviera junto al mar, nadaría todas las mañanas. ¡Pero vivo en las montañas!
""",
           fills="""
If I ___ rich, I would travel the world. | were / am | 0 | Si fuera rico, viajaría por el mundo.
If she had a car, she ___ drive to work. | would / will | 0 | Si tuviera carro, iría manejando al trabajo.
If I were you, I ___ talk to him. | would / will | 0 | Yo que tú, hablaría con él.
What would you do if you ___ invisible? | were / are | 0 | ¿Qué harías si fueras invisible?
I ___ go to the party if I didn't have to work. | might / may to | 0 | Tal vez iría a la fiesta si no tuviera que trabajar.
"""),
         dialogue("Preguntas imposibles", "🎲 Un juego en una reunión de amigos.", """
Leo: OK, here's one. What would you do if you won the lottery? || Bueno, ahí va una. ¿Qué harías si te ganaras la lotería?
María: I'd pay off my parents' debts and I'd travel for a year. || Pagaría las deudas de mis papás y viajaría un año.
Leo: Would you quit your job? || ¿Renunciarías a tu trabajo?
María: Honestly? Yes, but I'd start my own business. What about you? || ¿Honestamente? Sí, pero empezaría mi propio negocio. ¿Y tú?
Leo: I'd buy a farm and live a quiet life. And I'd donate part of it to charity. || Compraría una finca y viviría tranquilo. Y donaría una parte a la caridad.
María: That's sweet. If I were you, I'd buy a mansion too, ha ha! || Qué lindo. Yo que tú, ¡compraría también una mansión, ja ja!
"""),
         story("Si pudiera viajar en el tiempo", "⏳", """
If I could travel in time, I wouldn't go to the future. I would go to the past. || Si pudiera viajar en el tiempo, no iría al futuro. Iría al pasado.
I would visit my grandparents when they were young, before I was born. || Visitaría a mis abuelos cuando eran jóvenes, antes de que yo naciera.
I would love to see how they met, at a dance in a small village. || Me encantaría ver cómo se conocieron, en un baile en un pueblo pequeño.
If I had the chance, I would ask them about their dreams and their fears. || Si tuviera la oportunidad, les preguntaría por sus sueños y sus miedos.
Of course, I wouldn't tell them who I was. That would change history! || Claro, no les diría quién soy. ¡Eso cambiaría la historia!
It's only a dream, but sometimes imagining is the best way to understand where we come from. || Es solo un sueño, pero a veces imaginar es la mejor forma de entender de dónde venimos.
""", questions=[
             ("¿A dónde iría el narrador?", ["Al futuro", "Al pasado", "A otro planeta"], 1),
             ("¿Qué le encantaría ver?", ["Cómo se conocieron sus abuelos", "Una guerra", "Su propia boda"], 0),
             ("¿Por qué no les diría quién es?", ["Porque cambiaría la historia", "Porque no le creerían", "Porque le da vergüenza"], 0),
         ]),
         roleplay("Dar un consejo difícil", "💼 Tu amiga recibió una oferta de trabajo en otra ciudad.", """
Friend: They offered me a job in Medellín, but my family is here. What would you do? || Me ofrecieron un trabajo en Medellín, pero mi familia está aquí. ¿Tú qué harías?
+ If I were you, I'd accept it. It's a great opportunity. || Yo que tú, lo aceptaría. Es una gran oportunidad.
- If I am you, I will accept. || Si yo soy tú, aceptaré. || Imaginario: "If I were you, I'd…".
Friend: But I'd miss my family so much. || Pero extrañaría muchísimo a mi familia.
+ That's true, but you could visit them every month. || Es cierto, pero podrías visitarlos cada mes.
- You won't miss them never. || Nunca no los extrañarás. || Doble negación y no ayuda.
Friend: And if I didn't like the job? || ¿Y si no me gustara el trabajo?
+ In that case, you could always come back. || En ese caso, siempre podrías volver.
- In that case, you would can come back. || En ese caso, podrías poder volver. || "would can" no existe: usa "could".
"""),
     ],
     writes="""
Si tuviera más tiempo, aprendería a tocar piano. | If I had more time, I would learn to play the piano. | If I had more time, I'd learn to play the piano. ; If I had more time I would learn to play the piano.
Yo que tú, no lo haría. | If I were you, I wouldn't do it. | If I were you, I would not do it. ; If I were you I wouldn't do it.
¿Qué harías si fueras invisible? | What would you do if you were invisible?
""",
     dictations="""
If I won the lottery, I would buy a farm. || Si me ganara la lotería, compraría una finca.
It would be a disaster if we lost the files. || Sería un desastre si perdiéramos los archivos.
""",
     speak="""
If I could live anywhere, I would live near the sea. || Si pudiera vivir en cualquier parte, viviría cerca del mar.
""")

unit("u61-lamentar", "B2", "Lamentos y deseos", "😔",
     "Ya puedo hablar de lo que habría pasado y de lo que me gustaría que fuera distinto",
     "Tercer condicional, wish / if only, y should have para hablar del pasado que no pasó.",
     grammar=["Tercer condicional", "I wish / If only", "should have / could have"],
     items="""
If I had known | Si hubiera sabido | 🤦
I would have helped you | Te habría ayudado | 🤝
If she had studied, she would have passed | Si hubiera estudiado, habría pasado | 📚
I wish I had… | Ojalá tuviera… / Ojalá hubiera… | 🌠
I wish you were here | Ojalá estuvieras aquí | 💔
If only | Si tan solo | 😩
I should have listened | Debí haber escuchado | 👂
You shouldn't have said that | No debiste decir eso | 🤐
We could have won | Podríamos haber ganado | 🏆
It might have been… | Pudo haber sido… | 🎲
regret (verb) | lamentar / arrepentirse | 😞 | ri-grét
regret (noun) | arrepentimiento | 💭
mistake (B2) | error
blame | culpar / culpa | 👉 | bléim
fault | culpa | ⚠️ | folt
It's my fault | Es mi culpa | 🙋
guilty | culpable | 😣 | guíl-ti
ashamed | avergonzado | 😳 | a-shéimd
disappointed (B2) | decepcionado
missed opportunity | oportunidad perdida | 🚪
second chance | segunda oportunidad | 🔁
turning point | punto de quiebre | 🔀
looking back | mirando atrás | 👀
in hindsight | en retrospectiva | 🔙 | jáind-sait
lesson learned | lección aprendida | 📘
consequences (B2) | consecuencias
avoid (B2) | evitar
prevent | prevenir / evitar | 🛑 | pri-vént
realize (B2) | darse cuenta
notice (B2) | notar
warn | advertir | ⚠️ | uorn
advise | aconsejar | 🗨️ | ad-váis
ignore | ignorar | 🙉 | ig-nór
pay attention | prestar atención | 👀
on time (B2) | a tiempo
too late | demasiado tarde | ⌛
by mistake | por error | ❌
on purpose | a propósito | 🎯 | pér-pos
accidentally | accidentalmente | 💥 | ak-si-dén-ta-li
carelessly | descuidadamente | 🫠 | kér-les-li
wise | sabio | 🦉 | uáis
foolish | tonto / insensato | 🤪 | fúu-lish
impulsive | impulsivo | ⚡ | im-pál-siv
risky | arriesgado | 🎲 | rís-ki
lucky (B2) | con suerte
unlucky | de mala suerte | 🐈‍⬛ | an-lá-ki
fate | destino | 🌌 | féit
coincidence | coincidencia | 🍀 | kou-ín-si-dens
what if… | ¿y si…? | ❓
It's no use crying over spilled milk | No sirve de nada llorar sobre la leche derramada | 🥛
Live and learn | Vivir para aprender | 📚
It wasn't meant to be | No estaba destinado a ser | 🌌
""",
     extras=[
         D("Tercer condicional y wish",
           "Estas personas hablan de un pasado que ya no se puede cambiar.",
           """
If I had studied, I would have passed the exam. || Si hubiera estudiado, habría pasado el examen. || had studied, would have passed
If we had left earlier, we wouldn't have missed the flight. || Si hubiéramos salido antes, no habríamos perdido el vuelo. || had left, wouldn't have missed
I wish I had saved more money. || Ojalá hubiera ahorrado más plata. || wish, had saved
I wish I spoke French. (ahora) || Ojalá hablara francés. || wish, spoke
You should have told me the truth. || Debiste haberme dicho la verdad. || should have told
""",
           "¿Cómo se forma la parte de 'habría + participio'?",
           ["would have + participio", "will have + verbo", "would + pasado"], 0,
           "TERCER CONDICIONAL (pasado imposible de cambiar): If + had + participio, would have + participio. wish: con pasado para deseos del presente (I wish I had a car = ojalá tuviera), con had + participio para lamentos del pasado (I wish I had gone = ojalá hubiera ido). should have + participio = debí haber.",
           """
If I had known you were in the hospital, I would have visited you. || Si hubiera sabido que estabas en el hospital, te habría visitado.
""",
           fills="""
If I ___ known, I would have helped you. | had / have | 0 | Si hubiera sabido, te habría ayudado.
She would have come if you ___ invited her. | had / have | 0 | Ella habría venido si la hubieras invitado.
I wish I ___ more time. (ahora) | had / have | 0 | Ojalá tuviera más tiempo.
You should ___ called me. | have / had | 0 | Debiste haberme llamado.
If they had played better, they ___ won. | would have / will have | 0 | Si hubieran jugado mejor, habrían ganado.
"""),
         dialogue("El vuelo perdido", "✈️ Llegaron tarde al aeropuerto.", """
Juan: We missed the flight. I can't believe it. || Perdimos el vuelo. No lo puedo creer.
Ana: If we had left home an hour earlier, we would have made it. || Si hubiéramos salido de la casa una hora antes, habríamos alcanzado.
Juan: I know. I should have checked the traffic. It's my fault. || Ya sé. Debí haber revisado el tráfico. Es mi culpa.
Ana: Don't blame yourself. Nobody knew there would be an accident on the highway. || No te culpes. Nadie sabía que habría un accidente en la autopista.
Juan: I just wish we hadn't stopped for coffee. || Solo desearía que no hubiéramos parado a tomar café.
Ana: It's no use crying over spilled milk. Let's find another flight. || No sirve de nada lamentarse. Busquemos otro vuelo.
"""),
         story("La carta que nunca envié", "✉️", """
When I was twenty, I fell in love with a girl from my university called Elena. || Cuando tenía veinte años, me enamoré de una chica de mi universidad llamada Elena.
I wrote her a long letter, but I was too shy, so I never sent it. || Le escribí una carta larga, pero era muy tímido, así que nunca la envié.
At the end of the year she moved to Argentina. I never saw her again. || Al final del año se mudó a Argentina. Nunca la volví a ver.
For years I wondered: what if I had sent that letter? Would my life have been different? || Por años me pregunté: ¿y si hubiera enviado esa carta? ¿Habría sido distinta mi vida?
Last year I found her on social media. She was married and happy. || El año pasado la encontré en redes sociales. Estaba casada y feliz.
Looking back, I don't regret it. Maybe it wasn't meant to be, but I learned to be braver. || Mirando atrás, no me arrepiento. Tal vez no estaba destinado a ser, pero aprendí a ser más valiente.
""", questions=[
             ("¿Por qué no envió la carta?", ["Porque era muy tímido", "Porque la perdió", "Porque Elena se fue"], 0),
             ("¿A dónde se mudó Elena?", ["A España", "A Argentina", "A Chile"], 1),
             ("¿Qué aprendió el narrador?", ["A escribir cartas", "A ser más valiente", "A olvidar"], 1),
         ]),
         roleplay("Hablar de un error en el trabajo", "💼 Enviaste un correo con un error a un cliente importante.", """
Boss: The client received the wrong price list. What happened? || El cliente recibió la lista de precios equivocada. ¿Qué pasó?
+ I'm really sorry. I sent the old file by mistake. It's my fault. || Lo siento mucho. Envié el archivo viejo por error. Es mi culpa.
- It's not my fault. The client should have not open it. || No es mi culpa. El cliente no debió abrirlo. || Culpar al cliente no ayuda.
Boss: If you had checked it, this wouldn't have happened. || Si lo hubieras revisado, esto no habría pasado.
+ You're right. I should have double-checked it. I'll call the client now. || Tiene razón. Debí haberlo revisado dos veces. Llamo al cliente ya.
- You're right. I would checked it. || Tiene razón. Yo revisaría lo. || Debe ser "I should have checked it".
Boss: OK. Make sure it doesn't happen again. || Bueno. Asegúrate de que no vuelva a pasar.
+ Of course. Lesson learned. || Claro. Lección aprendida.
- I wish it happens again. || Ojalá pase otra vez. || Todo lo contrario.
"""),
     ],
     writes="""
Si hubiera sabido, te habría ayudado. | If I had known, I would have helped you. | If I'd known, I would have helped you. ; If I had known, I'd have helped you.
Ojalá tuviera más tiempo. | I wish I had more time.
Debí haberte escuchado. | I should have listened to you.
""",
     dictations="""
If we had left earlier, we wouldn't have missed the flight. || Si hubiéramos salido antes, no habríamos perdido el vuelo.
I wish I had saved more money when I was younger. || Ojalá hubiera ahorrado más plata cuando era más joven.
""")

unit("u62-indirecto", "B2", "Lo que dijo", "🗣️",
     "Ya puedo contar con precisión lo que otra persona dijo, preguntó u ordenó",
     "Estilo indirecto completo: cambios de tiempo, preguntas indirectas y verbos para reportar.",
     grammar=["Estilo indirecto completo", "Preguntas indirectas", "Verbos de reporte: admit, suggest, warn"],
     items="""
reported speech | estilo indirecto | 💬
direct speech | estilo directo | 🗨️
say (B2) | decir
tell (B2) | decirle a alguien
ask (B2) | preguntar / pedir
reply | responder | ↩️ | ri-plái
admit | admitir | 🙋 | ad-mít
explain (B2) | explicar
mention | mencionar | 📌 | mén-shon
insist | insistir | ☝️ | in-síst
complain | quejarse | 😤 | kom-pléin
suggest (B2) | sugerir
recommend (B2) | recomendar
warn (B2) | advertir
remind | recordarle a alguien | ⏰ | ri-máind
promise (B2) | prometer
agree to | aceptar (hacer algo) | 👍
refuse (B2) | negarse
offer (B2) | ofrecer
threaten | amenazar | 😠 | zré-ten
beg | rogar | 🙏 | beg
order | ordenar | 📢
encourage | animar / alentar | 📣 | en-ká-rich
persuade (B2) | persuadir
convince (B2) | convencer
deny (B2) | negar
confess | confesar | 🤐 | kon-fés
announce (B2) | anunciar
whisper (B2) | susurrar
shout (B2) | gritar
wonder | preguntarse | 🤔 | uán-der
whether | si (en preguntas indirectas) | ❔ | ué-der
the day before | el día anterior | ⏮️
the following day | al día siguiente | ⏭️
that day | ese día | 📅
there | allí | 📍
then | entonces / en ese momento | ⏱️
gossip | chisme / chismear | 🗯️ | gó-sip
rumor | rumor | 👂 | rú-mor
message (B2) | mensaje
quote | cita / citar | ❝ | kuóut
exact words | palabras exactas | 🔤
misunderstanding | malentendido | 😕 | mis-an-der-stán-ding
point out (B2) | señalar
make clear | dejar claro | 💡
She told me to wait | Me dijo que esperara | ⏳
He asked me where I lived | Me preguntó dónde vivía | 🏠
They asked if I was OK | Me preguntaron si estaba bien | ❓
She suggested going out | Sugirió salir | 🚶
He admitted breaking it | Admitió haberlo roto | 💔
Do you know what time it is? | ¿Sabes qué hora es? | ⌚
Could you tell me where the bank is? | ¿Podría decirme dónde queda el banco? | 🏦
""",
     extras=[
         D("Estilo indirecto completo",
           "Mira cómo cambian las palabras exactas al contarlas después.",
           """
"I'm working." → She said she was working. || "Estoy trabajando." → Dijo que estaba trabajando. || was working
"I've finished." → He said he had finished. || "Terminé." → Dijo que había terminado. || had finished
"I'll call you tomorrow." → She said she would call me the next day. || "Te llamo mañana." → Dijo que me llamaría al día siguiente. || would call, the next day
"Where do you live?" → He asked me where I lived. || "¿Dónde vives?" → Me preguntó dónde vivía. || where I lived
"Are you OK?" → They asked if I was OK. || "¿Estás bien?" → Me preguntaron si estaba bien. || if I was
"Wait here." → She told me to wait there. || "Espera aquí." → Me dijo que esperara allí. || told me to wait
""",
           "En una pregunta indirecta (He asked me where I lived), el orden es…",
           ["Como pregunta: where did I live", "Como afirmación: where I lived"], 1,
           "En ESTILO INDIRECTO el verbo retrocede un tiempo (is → was, have done → had done, will → would) y cambian palabras de tiempo y lugar (tomorrow → the next day, here → there). Las preguntas indirectas usan orden de afirmación, sin do: He asked where I lived. Si no hay palabra interrogativa, usa if o whether. Órdenes: tell / ask + persona + to.",
           """
I wonder whether she'll come. Could you tell me what time the meeting starts? || Me pregunto si vendrá. ¿Podría decirme a qué hora empieza la reunión?
""",
           fills="""
"I'm tired." → He said he ___ tired. | was / is being | 0 | "Estoy cansado." → Dijo que estaba cansado.
"Where is the station?" → She asked me where the station ___. | was / is it | 0 | "¿Dónde queda la estación?" → Me preguntó dónde quedaba la estación.
"Close the door." → He told me ___ the door. | to close / close | 0 | "Cierra la puerta." → Me dijo que cerrara la puerta.
"Do you like coffee?" → She asked ___ I liked coffee. | if / that | 0 | "¿Te gusta el café?" → Me preguntó si me gustaba el café.
Could you tell me where ___? | the bank is / is the bank | 0 | ¿Podría decirme dónde queda el banco?
"""),
         dialogue("Un malentendido", "📞 Le cuentas a un colega lo que dijo la gerente.", """
Carlos: What did the manager say in the meeting? || ¿Qué dijo la gerente en la reunión?
You: She said the project would be delayed and that we had to work on Saturday. || Dijo que el proyecto se retrasaría y que teníamos que trabajar el sábado.
Carlos: Saturday? She told me last week that we wouldn't have to. || ¿El sábado? Ella me dijo la semana pasada que no tendríamos que hacerlo.
You: I know. Someone asked her why the plans had changed. || Ya sé. Alguien le preguntó por qué habían cambiado los planes.
Carlos: And what did she reply? || ¿Y qué respondió?
You: She explained that the client had asked for more changes. She apologized and promised to give us a day off. || Explicó que el cliente había pedido más cambios. Se disculpó y prometió darnos un día libre.
"""),
         story("El chisme de la oficina", "🗯️", """
On Monday morning Sofía heard a rumor in the elevator. || El lunes por la mañana Sofía oyó un rumor en el ascensor.
Someone whispered that the company was going to close the Pasto office. || Alguien susurró que la empresa iba a cerrar la oficina de Pasto.
By lunchtime everybody was talking about it. People wondered whether they would lose their jobs. || A la hora del almuerzo todo el mundo hablaba de eso. La gente se preguntaba si perdería su trabajo.
Finally Sofía asked the director if it was true. || Al final Sofía le preguntó al director si era cierto.
He laughed and explained that they weren't closing the office. They were moving it to a bigger building! || Él se rió y explicó que no iban a cerrar la oficina. ¡La iban a trasladar a un edificio más grande!
He reminded everyone not to believe gossip and suggested asking him directly next time. || Les recordó a todos que no creyeran chismes y sugirió preguntarle directamente la próxima vez.
""", questions=[
             ("¿Qué decía el rumor?", ["Que habría aumento de sueldo", "Que iban a cerrar la oficina de Pasto", "Que despedirían al director"], 1),
             ("¿Qué pasaba en realidad?", ["Trasladaban la oficina a un edificio más grande", "Cerraban la empresa", "Nada"], 0),
             ("¿Qué sugirió el director?", ["Creer los chismes", "Preguntarle directamente la próxima vez", "Trabajar el sábado"], 1),
         ]),
         roleplay("Contar lo que dijo el médico", "🩺 Tu mamá no pudo ir a la cita de tu papá y te pregunta.", """
Mom: What did the doctor say? || ¿Qué dijo el médico?
+ He said Dad was fine, but that he had to reduce salt. || Dijo que papá estaba bien, pero que tenía que reducir la sal.
- He said Dad is fine tomorrow. || Dijo que papá está bien mañana. || Mezcla tiempos.
Mom: Did he give him any medicine? || ¿Le dio algún medicamento?
+ Yes. He told him to take one pill every morning. || Sí. Le dijo que se tomara una pastilla cada mañana.
- Yes. He told him take one pill. || Sí. Le dijo tomar una pastilla. || Falta "to": told him TO take.
Mom: And did Dad ask about exercise? || ¿Y papá preguntó por el ejercicio?
+ Yes, he asked if he could play football again. The doctor said he could, slowly. || Sí, preguntó si podía volver a jugar fútbol. El médico dijo que sí, despacio.
- Yes, he asked could he play football. || Sí, preguntó podía él jugar. || En pregunta indirecta: "if he could play".
"""),
     ],
     writes="""
Me dijo que estaba cansada. | She told me she was tired. | She told me that she was tired. ; She said she was tired.
Me preguntó dónde vivía. | He asked me where I lived. | She asked me where I lived.
¿Podría decirme dónde queda la estación? | Could you tell me where the station is? | Can you tell me where the station is?
""",
     dictations="""
She said she would call me the next day. || Dijo que me llamaría al día siguiente.
He asked me whether I had finished the report. || Me preguntó si había terminado el informe.
""")

unit("u63-precision", "B2", "Describir con precisión", "🔬",
     "Ya puedo describir personas, objetos y procesos con detalle y precisión",
     "Relativas no definitorias, compuestos y adjetivos precisos para descripciones de nivel avanzado.",
     grammar=["Relativas no definitorias (con comas)", "Orden de adjetivos", "Adjetivos compuestos"],
     items="""
which (non-defining) | lo cual / el cual | 🔗
whom | a quien | 👤 | juum
whereby | por el cual | ⚙️ | uer-bái
appearance | apariencia | 🪞 | a-pí-rans
personality | personalidad | 🧠 | per-so-ná-li-ti
features | rasgos | 👃 | fíi-chers
height | estatura | 📏 | jáit
build | contextura | 🏋️ | bild
slim | delgado (atractivo) | 🧍 | slim
overweight | con sobrepeso | ⚖️ | ou-ver-uéit
muscular | musculoso | 💪 | más-kiu-lar
wrinkles | arrugas | 👵 | rín-kols
freckles | pecas | 🌟 | fré-kols
bald | calvo | 👨‍🦲 | bold
ponytail | cola de caballo | 💁 | póu-ni-teil
fringe | flequillo / capul | 💇 | frinch
tattoo | tatuaje | 🐉 | ta-túu
scar | cicatriz | 🩹 | skar
pale | pálido | 😶 | péil
tanned | bronceado | 🏖️ | tand
good-looking | atractivo | 😎
well-dressed | bien vestido | 🤵
easy-going | relajado / tranquilo | 😌
open-minded | de mente abierta | 🧠
narrow-minded | cerrado de mente | 🚪
self-confident | seguro de sí mismo | 😎
short-tempered | de mal genio | 😠
absent-minded | despistado | 🤪
hard-headed | terco | 🐂
ambitious | ambicioso | 🧗 | am-bí-shos
stubborn | terco | 🐐 | stá-born
sensitive | sensible | 🌸 | sén-si-tiv
sensible | sensato | 🧠 | sén-si-bol | ¡Falso amigo! No es "sensible".
reliable (B2) | confiable
moody | temperamental / cambiante | 🌦️ | múu-di
outgoing | extrovertido | 🎉 | áut-gou-ing
introverted | introvertido | 📚 | in-tro-vér-ted
curious | curioso | 🧐 | kiú-ri-os
witty | ingenioso | 😏 | uí-ti
arrogant | arrogante | 🙄 | á-ro-gant
humble | humilde | 🙇 | jám-bol
shape | forma | 🔷 | shéip
round | redondo | ⚪ | ráund
square (shape) | cuadrado | ⬛
oval | ovalado | 🥚 | óu-val
rough | áspero | 🪨 | raf
smooth | suave / liso | 🫧 | smuud
soft | blando / suave | 🧸 | soft
hard (texture) | duro
shiny | brillante | ✨ | shái-ni
transparent | transparente | 🔍 | trans-pé-rent
striped | de rayas | 🦓 | stráipt
spotted | de puntos / manchado | 🐆 | spó-ted
plain | liso / sencillo | ⬜ | pléin
vintage | antiguo / de época | 📻 | vín-tich
handmade | hecho a mano | 🧶 | jand-méid
""",
     extras=[
         D("Relativas con comas",
           "Compara las frases con y sin comas.",
           """
My brother who lives in Cali is a doctor. (tengo varios hermanos) || Mi hermano que vive en Cali es médico. || who
My mother, who is sixty, still runs every day. (solo tengo una mamá) || Mi mamá, que tiene sesenta años, todavía corre todos los días. || , who
Bogotá, which is the capital, has eight million people. || Bogotá, que es la capital, tiene ocho millones de habitantes. || , which
He failed the exam, which surprised everybody. || Perdió el examen, lo cual sorprendió a todos. || , which
The man to whom I spoke was very kind. || El señor con quien hablé fue muy amable. || whom
""",
           "¿Para qué sirven las comas en estas relativas?",
           ["Para dar información extra, no necesaria para identificar", "Para preguntar", "No sirven para nada"], 0,
           "Las RELATIVAS NO DEFINITORIAS van entre comas y añaden información extra (si la quitas, la frase sigue clara). En ellas NO se puede usar that, solo who / which / where / whose. ', which' puede referirse a toda la idea anterior (lo cual). whom es la forma formal de who como objeto.",
           """
My grandfather, whose house is in the countryside, has a vintage car. || Mi abuelo, cuya casa queda en el campo, tiene un carro antiguo.
""",
           fills="""
Medellín, ___ is known for its weather, is a beautiful city. | which / that | 0 | Medellín, que es conocida por su clima, es una ciudad hermosa.
My boss, ___ is very easy-going, let us leave early. | who / which | 0 | Mi jefe, que es muy relajado, nos dejó salir temprano.
She arrived late, ___ made the teacher angry. | which / that | 0 | Llegó tarde, lo cual enojó al profesor.
He's very ___. He always makes good decisions. | sensible / sensitive | 0 | Es muy sensato. Siempre toma buenas decisiones.
"""),
         tip("🎨", "Orden de los adjetivos", "Cuando usas varios, el orden natural es: opinión → tamaño → edad → forma → color → origen → material → sustantivo. Ej.: a beautiful small old round brown Italian wooden table. En la práctica usa dos o tres: a lovely old wooden table."),
         dialogue("Describir a un sospechoso", "🕵️ Hablas con la policía después de un robo en tu tienda.", """
Officer: Can you describe the man? || ¿Puede describir al hombre?
You: He was tall and slim, with short dark hair and a beard. || Era alto y delgado, de pelo corto oscuro y barba.
Officer: Any special features? || ¿Algún rasgo especial?
You: He had a tattoo on his neck, which looked like a snake, and a scar on his left cheek. || Tenía un tatuaje en el cuello, que parecía una serpiente, y una cicatriz en la mejilla izquierda.
Officer: What was he wearing? || ¿Qué llevaba puesto?
You: A striped shirt and an old leather jacket. He seemed nervous and short-tempered. || Una camisa de rayas y una chaqueta de cuero vieja. Parecía nervioso y de mal genio.
"""),
         story("El reloj del abuelo", "⌚", """
On my desk there is a small, old, round silver watch, which belonged to my grandfather. || En mi escritorio hay un reloj pequeño, viejo, redondo y de plata, que perteneció a mi abuelo.
It's not very valuable, but it's the most important object I own. || No es muy valioso, pero es el objeto más importante que tengo.
My grandfather, who was a humble and witty man, bought it in 1965 with his first salary. || Mi abuelo, que era un hombre humilde e ingenioso, lo compró en 1965 con su primer salario.
The glass is scratched and the leather strap is soft and worn, but it still works perfectly. || El vidrio está rayado y la correa de cuero está blanda y gastada, pero todavía funciona perfectamente.
Every time I look at it, I remember his open-minded advice and his easy-going smile. || Cada vez que lo miro, recuerdo sus consejos de mente abierta y su sonrisa tranquila.
Objects, which seem so simple, can keep the memories of a whole life. || Los objetos, que parecen tan sencillos, pueden guardar los recuerdos de toda una vida.
""", questions=[
             ("¿De qué material es el reloj?", ["De oro", "De plata", "De plástico"], 1),
             ("¿Cuándo lo compró el abuelo?", ["En 1965 con su primer salario", "En un viaje", "Se lo regalaron"], 0),
             ("¿Cómo era el abuelo?", ["Humilde e ingenioso", "Arrogante y terco", "Tímido y triste"], 0),
         ]),
         roleplay("Vender algo en internet", "📦 Un comprador te pregunta por una lámpara que publicaste.", """
Buyer: Hi! Can you describe the lamp a bit more? || ¡Hola! ¿Puedes describir un poco más la lámpara?
+ Sure. It's a vintage brass lamp, which my aunt bought in Spain. || Claro. Es una lámpara antigua de bronce, que mi tía compró en España.
- Sure. It's a lamp that, which is old. || Claro. Es una lámpara que, la cual es vieja. || Usa un solo relativo.
Buyer: Is it in good condition? || ¿Está en buen estado?
+ Yes. The metal is a bit rough in one place, but it works perfectly. || Sí. El metal está un poco áspero en una parte, pero funciona perfectamente.
- Yes, it's very sensible. || Sí, es muy sensata. || "Sensible" es para personas sensatas.
Buyer: Great. Is it handmade? || Genial. ¿Es hecha a mano?
+ Yes, it was made by a local artisan, whose family has made lamps for generations. || Sí, la hizo un artesano local, cuya familia ha hecho lámparas por generaciones.
- Yes, it was made by an artisan who his family makes lamps. || Sí, por un artesano quien su familia hace lámparas. || Para posesión se usa "whose".
"""),
     ],
     writes="""
Mi mamá, que tiene sesenta años, todavía trabaja. | My mother, who is sixty, still works. | My mom, who is sixty, still works.
Llegó tarde, lo cual molestó al jefe. | He arrived late, which annoyed the boss. | She arrived late, which annoyed the boss. ; He arrived late, which upset the boss.
Es una persona muy sensata. | He's a very sensible person. | She's a very sensible person. ; He is a very sensible person. ; She is a very sensible person.
""",
     dictations="""
Bogotá, which is the capital, has about eight million people. || Bogotá, que es la capital, tiene unos ocho millones de habitantes.
She's open-minded, ambitious and very reliable. || Es de mente abierta, ambiciosa y muy confiable.
""")

unit("u64-ingles-real", "B2", "Inglés real: cómo hablan los nativos", "🎧",
     "Ya entiendo el inglés hablado rápido y las reducciones de los nativos",
     "gonna, wanna, gotta, kinda y todo el habla conectada que no aparece en los libros pero sí en las series.",
     grammar=["Reducciones: gonna, wanna, gotta", "Habla conectada y sonidos que desaparecen"],
     items="""
gonna (going to) | voy a / va a | 🗣️ | gá-na
wanna (want to) | quiero / quieres | 🙋 | uá-na
gotta (have got to) | tengo que | ❗ | gá-ra
hafta (have to) | tengo que | 📌 | jáf-ta
kinda (kind of) | como que / medio | 🤏 | káin-da
sorta (sort of) | más o menos / algo así | 🤷 | sór-ta
dunno (don't know) | no sé | 🤷 | da-nóu
lemme (let me) | déjame | ✋ | lé-mi
gimme (give me) | dame | 🫴 | guí-mi
gotcha (got you) | entendido / te agarré | 👌 | gá-cha
whatcha (what are you) | qué estás… | ❓ | uá-cha
didja (did you) | ¿(tú) hiciste…? | ❔ | dí-ya
d'ya (do you) | ¿(tú)…? | ❔ | dya
ya (you) | tú / te (informal) | 🫵 | ya
'cause (because) | porque | 💡 | kos
'em (them) | los / las / ellos | 👥 | em
outta (out of) | fuera de | 🚪 | áu-ra
lotta (a lot of) | mucho(s) | 🔢 | lá-ra
coulda (could have) | pudo haber | 🎲 | kú-da
shoulda (should have) | debió haber | 🤦 | shú-da
woulda (would have) | habría | 💭 | uú-da
y'all (you all) | ustedes (sur de EE. UU.) | 👥 | yol
ain't | no es / no está / no hay (muy informal) | 🚫 | éint
innit (isn't it) | ¿no? (Reino Unido) | 🇬🇧 | í-nit
yeah | sí (informal) | 👍 | iéa
nope | no (informal) | 👎 | nóup
yep | sí (informal) | ✅ | iep
uh-huh | ajá | 👍 | a-já
uh-uh | no (con sonido) | 👎 | á-a
hey | oye / hola | 👋 | jéi
dude | parcero / man | 🤙 | duud
guys | gente / chicos (grupo, cualquier género) | 👥 | gáis
buddy | amigo / parce | 🫂 | bá-di
awesome | genial / chévere | 🤩 | ó-som
cool (B2) | chévere
no way! | ¡no puede ser! | 😱
for real? | ¿en serio? | 😮
my bad | mi culpa | 🙋
no worries | tranquilo / no hay problema | 😌
I'm down | me apunto | 👍
hang on | espera / un momento | ✋
What's up? | ¿Qué más? / ¿Qué hubo? | 👋
Not much | Nada, aquí | 🙂
How's it going? | ¿Cómo va todo? | 🙂
I'm beat | Estoy muerto (cansado) | 😩
That sucks | Qué mala onda / qué mamera | 👎
It's no big deal | No es para tanto | 🤷
Hold on a sec | Espera un segundo | ⏱️
You know what I mean? | ¿Me entiendes? | 🤔
I mean… | O sea… / quiero decir… | 💬
like (filler) | como (muletilla) | 💬
basically | básicamente | 💬 | béi-si-kli
literally | literalmente | 😂 | lí-te-ra-li
whatever | lo que sea / da igual | 🙄 | uat-é-ver
""",
     extras=[
         D("Cómo se 'comen' las palabras",
           "Lee la forma escrita formal y luego cómo suena de verdad. Escucha con atención.",
           """
I'm going to eat. → I'm gonna eat. || Voy a comer. || gonna
Do you want to go? → D'ya wanna go? || ¿Quieres ir? || wanna
I have got to leave. → I gotta leave. || Me tengo que ir. || gotta
I don't know. → I dunno. || No sé. || dunno
Let me see. → Lemme see. || Déjame ver. || Lemme
What are you doing? → Whatcha doin'? || ¿Qué estás haciendo? || Whatcha
""",
           "¿Cuándo se usan estas formas?",
           ["En exámenes y correos formales", "Al hablar informalmente (y en mensajes entre amigos)"], 1,
           "Estas REDUCCIONES son como los nativos hablan de verdad: las palabras se juntan y se acortan (going to → gonna, want to → wanna, got to → gotta). Debes ENTENDERLAS porque aparecen en series, canciones y conversaciones. Al escribir formal (trabajo, exámenes), usa siempre la forma completa.",
           """
"Whatcha gonna do this weekend?" "Dunno. Wanna hang out?" || "¿Qué vas a hacer este fin de semana?" "No sé. ¿Quieres que salgamos?"
""",
           fills="""
"I'm gonna call her." significa: I'm ___ to call her. | going / want | 0 | Voy a llamarla.
"I wanna sleep." significa: I want ___ sleep. | to / of | 0 | Quiero dormir.
"I gotta go." significa: I have ___ to go. | got / get | 0 | Me tengo que ir.
En un correo formal escribes: "I am ___ to attend." | going / gonna | 0 | Voy a asistir. | En escritura formal no se usa "gonna".
"""),
         tip("👂", "Más trucos del habla conectada", "1) La t entre vocales suena como una r suave en EE. UU.: water → 'wárer', better → 'bérer'. 2) Las palabras se unen: an apple → 'anápple'. 3) Las palabras pequeñas casi desaparecen: and → 'n' (rock 'n' roll), of → 'a' (cup of coffee → 'cuppa coffee'). Escucha esto en series con subtítulos en inglés."),
         dialogue("Conversación real entre amigos", "🎧 Así suena una conversación de verdad. Escúchala varias veces.", """
Jake: Hey dude, what's up? || Quiubo parce, ¿qué más?
Matt: Not much. I'm kinda tired. Whatcha doin' tonight? || Nada, aquí. Estoy medio cansado. ¿Qué vas a hacer esta noche?
Jake: I dunno. Wanna grab some pizza? || No sé. ¿Quieres que vayamos por una pizza?
Matt: I'm down, but I gotta finish this report first. Gimme an hour. || Me apunto, pero tengo que terminar este informe primero. Dame una hora.
Jake: No worries. Lemme know when you're ready. || Tranquilo. Avísame cuando estés listo.
Matt: Gotcha. See ya! || Listo. ¡Nos vemos!
"""),
         story("Primer mes en Estados Unidos", "🇺🇸", """
When Camilo arrived in Texas, he thought his English was pretty good. He had studied for years. || Cuando Camilo llegó a Texas, pensaba que su inglés era bastante bueno. Había estudiado por años.
But on his first day, his neighbor said, "Hey y'all, whatcha gonna do this weekend?" || Pero el primer día su vecino dijo: "Hey y'all, whatcha gonna do this weekend?"
Camilo didn't understand a single word. He just smiled and said, "Yes!" || Camilo no entendió ni una palabra. Solo sonrió y dijo: "¡Sí!"
He realized that people don't speak like textbooks. They connect words, shorten them and use a lotta slang. || Se dio cuenta de que la gente no habla como los libros. Unen palabras, las acortan y usan mucha jerga.
So he started watching series with English subtitles and repeating the dialogues out loud. || Así que empezó a ver series con subtítulos en inglés y a repetir los diálogos en voz alta.
After three months he could follow conversations easily. "Now I'm kinda used to it," he says, laughing. || Después de tres meses podía seguir conversaciones fácilmente. "Ahora como que ya me acostumbré", dice riéndose.
""", questions=[
             ("¿Por qué Camilo no entendió al vecino?", ["Porque el vecino hablaba otro idioma", "Porque los nativos unen y acortan palabras", "Porque había mucho ruido"], 1),
             ("¿Qué hizo para mejorar?", ["Ver series con subtítulos en inglés y repetir diálogos", "Leer gramática", "Nada"], 0),
             ("¿Cuánto tiempo le tomó?", ["Una semana", "Tres meses", "Dos años"], 1),
         ]),
         roleplay("Responder como nativo", "🎮 Un amigo gringo te escribe por chat de juego.", """
Tyler: yo whatcha doin? || oye qué haces?
+ Not much, just chillin'. Wanna play? || Nada, aquí relajado. ¿Quieres jugar?
- I am realizing activities of rest. || Estoy realizando actividades de descanso. || Demasiado formal para un chat entre amigos.
Tyler: yeah but I gotta eat first. gimme 10 min || sí pero tengo que comer primero. dame 10 min
+ No worries. Lemme know when you're ready. || Tranquilo. Avísame cuando estés listo.
- No. You must play now. || No. Debes jugar ya. || Suena brusco e inapropiado.
Tyler: my bad, I dunno if I can play tonight. my mom's mad lol || mi culpa, no sé si pueda jugar esta noche. mi mamá está brava jaja
+ That sucks. It's no big deal, we can play tomorrow. || Qué mamera. No es para tanto, podemos jugar mañana.
- Congratulations! || ¡Felicitaciones! || No encaja con la situación.
"""),
     ],
     writes="""
Escribe formal: "Voy a llamarte mañana." | I'm going to call you tomorrow. | I am going to call you tomorrow. ; I'll call you tomorrow.
Escribe formal: "No sé." | I don't know. | I do not know.
Escribe formal: "Tengo que irme." | I have to go. | I've got to go. ; I have got to go.
""",
     dictations="""
I'm gonna grab some coffee. Wanna come? || Voy a tomarme un café. ¿Quieres venir?
I dunno, I'm kinda tired. || No sé, estoy medio cansado.
""",
     speak="""
Hey, what's up? I'm gonna be a little late. || Hola, ¿qué más? Voy a llegar un poco tarde.
""")
