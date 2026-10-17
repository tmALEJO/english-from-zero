# B2 · Parte 2 (unidades 65-69)

unit("u65-deducir", "B2", "Deducir y especular", "🕵️",
     "Ya puedo hacer deducciones sobre el presente y el pasado",
     "Modales de deducción: must, might, can't (be / have been) para especular con lógica.",
     grammar=["must / might / can't + be", "must have / might have / can't have + participio"],
     items="""
must be | debe de ser / seguro es | 🎯
might be | puede que sea | 🎲
could be | podría ser | 🤔
can't be | no puede ser | 🚫
must have been | debió de haber sido | 🔙
might have forgotten | puede que se le haya olvidado | 🤷
can't have seen | no pudo haber visto | 🙈
deduce | deducir | 🧠 | di-diús
assume | asumir / suponer | 🤔 | a-siúm
assumption | suposición | 💭 | a-sámp-shon
speculate | especular | 🌀 | spé-kiu-leit
evidence | pruebas / evidencia | 🧾 | é-vi-dens
proof | prueba | ✅ | pruuf
clue | pista | 🗝️ | kluu
mystery | misterio | ❓ | mís-te-ri
detective | detective | 🕵️ | di-ték-tiv
suspect | sospechoso / sospechar | 🦹 | sás-pekt
suspicious | sospechoso (adj.) | 🤨 | sas-pí-shos
alibi | coartada | 📅 | á-li-bai
fingerprint | huella digital | 👆 | fín-ger-print
footprint | huella (de pie) | 👣 | fút-print
trace | rastro | 🔎 | tréis
missing | desaparecido / que falta | ❔ | mí-sing
obvious | obvio | 💡 | ób-vi-os
logical | lógico | 🧮 | ló-yi-kal
certainly | ciertamente | ✔️ | sér-ten-li
possibly | posiblemente | 🎲 | pó-si-bli
judging by | a juzgar por | ⚖️
it looks like | parece que | 👀
it seems that | parece que | 🤔
there's no way | de ninguna manera | 🙅
for sure | con seguridad | 💯
I bet | apuesto a que | 🎰
no wonder | con razón | 💡
That explains it | Eso lo explica | ✅
What could have happened? | ¿Qué pudo haber pasado? | ❓
She must be exhausted | Debe de estar agotada | 😩
exhausted | agotado | 😫 | eg-sós-ted
starving | muerto de hambre | 🍽️ | stár-ving
freezing | muerto de frío | 🥶 | fríi-sing
soaked | empapado | 💦 | sóukt
thrilled | emocionadísimo | 🤩 | zrild
puzzled | desconcertado | 🧩 | pá-sold
astonished | asombrado | 😲 | as-tó-nisht
relieved | aliviado | 😮‍💨 | ri-líivd
""",
     extras=[
         D("Deducciones sobre el presente y el pasado",
           "El detective saca conclusiones. Mira qué tan seguro está.",
           """
The lights are on. They must be at home. || Las luces están prendidas. Seguro están en casa. || must be
She isn't answering. She might be busy. || No contesta. Puede que esté ocupada. || might be
He can't be hungry. He just ate. || No puede tener hambre. Acaba de comer. || can't be
The ground is wet. It must have rained. || El suelo está mojado. Debió de haber llovido. || must have rained
He didn't come. He might have forgotten. || No vino. Puede que se le haya olvidado. || might have forgotten
She can't have seen me. I was hiding. || No pudo haberme visto. Estaba escondido. || can't have seen
""",
           "Para deducir algo del PASADO, ¿qué estructura se usa?",
           ["must / might / can't + have + participio", "must / might + verbo en pasado", "did + must"], 0,
           "Modales de DEDUCCIÓN: must = casi seguro que sí; might / could / may = posible; can't = casi seguro que no. Presente: modal + be / verbo (She must be tired). Pasado: modal + have + participio (She must have been tired). Ojo: para 'casi seguro que no' se usa can't, no mustn't.",
           """
You must be Laura! I've heard so much about you. || ¡Tú debes de ser Laura! He oído mucho de ti.
""",
           fills="""
He's been working for 12 hours. He ___ be exhausted. | must / can't | 0 | Lleva 12 horas trabajando. Debe de estar agotado.
That ___ be true! I saw her yesterday. | can't / must | 0 | ¡Eso no puede ser cierto! La vi ayer.
The door was open. Someone ___ have forgotten to lock it. | must / can't | 0 | La puerta estaba abierta. Alguien debió de olvidar cerrarla.
I'm not sure where Ana is. She ___ be at the gym. | might / must have | 0 | No estoy seguro de dónde está Ana. Puede que esté en el gimnasio.
"""),
         dialogue("¿Dónde está Daniel?", "📱 Daniel no llegó a la reunión.", """
Laura: Daniel isn't here yet. The meeting started twenty minutes ago. || Daniel todavía no llega. La reunión empezó hace veinte minutos.
Mario: He must be stuck in traffic. There's a protest downtown. || Debe de estar atascado en el tráfico. Hay una protesta en el centro.
Laura: But he lives five minutes away. || Pero vive a cinco minutos.
Mario: Then he might have overslept. He was working late last night. || Entonces puede que se haya quedado dormido. Anoche trabajó hasta tarde.
Laura: He can't have forgotten the meeting. He organized it! || No pudo haber olvidado la reunión. ¡Él la organizó!
Mario: Look, a message: "Sorry, my phone died." No wonder! || Mira, un mensaje: "Perdón, se me descargó el celular." ¡Con razón!
"""),
         story("El misterio del jardín", "🔍", """
One morning Mrs. Ortiz found that all the tomatoes in her garden had disappeared. || Una mañana la señora Ortiz encontró que todos los tomates de su jardín habían desaparecido.
The gate was closed, so it can't have been a stranger from the street. || La reja estaba cerrada, así que no pudo haber sido un desconocido de la calle.
There were small footprints in the soil. "It must have been a child," she thought. || Había huellas pequeñas en la tierra. "Debió de ser un niño", pensó.
But the footprints had four toes. They couldn't have been human. || Pero las huellas tenían cuatro dedos. No podían ser humanas.
That night she waited behind the window. At midnight she saw the thief: a raccoon! || Esa noche esperó detrás de la ventana. A la medianoche vio al ladrón: ¡un mapache!
"That explains it," she laughed. "He must have been starving." || "Eso lo explica", se rió. "Debía de estar muerto de hambre."
""", questions=[
             ("¿Por qué no pudo ser un desconocido de la calle?", ["Porque la reja estaba cerrada", "Porque había un perro", "Porque llovía"], 0),
             ("¿Qué tenían de raro las huellas?", ["Eran muy grandes", "Tenían cuatro dedos", "Eran de zapatos"], 1),
             ("¿Quién era el ladrón?", ["Un niño", "Un mapache", "El vecino"], 1),
         ]),
         roleplay("Hacer de detective", "🧐 Tu compañero encuentra la nevera vacía.", """
Roommate: All the food in the fridge is gone! What happened? || ¡Se acabó toda la comida de la nevera! ¿Qué pasó?
+ Your brother was here last night. He must have eaten it. || Tu hermano estuvo aquí anoche. Debe de habérsela comido.
- Your brother must eat it yesterday. || Tu hermano debe comérsela ayer. || Para el pasado: "must have eaten".
Roommate: No way. He's on a diet. || Imposible. Está a dieta.
+ Then it can't have been him. Maybe the fridge broke? || Entonces no pudo haber sido él. ¿Tal vez se dañó la nevera?
- Then it mustn't have been him. || Entonces no debe haber sido él. || Para "casi seguro que no" se usa "can't have".
Roommate: Oh… you're right. The fridge broke on Monday! || Ay… tienes razón. ¡La nevera se dañó el lunes!
+ No wonder it's empty! || ¡Con razón está vacía!
- I bet you're thrilled. || Apuesto a que estás emocionadísimo. || No encaja.
"""),
     ],
     writes="""
Debe de estar cansado. | He must be tired. | She must be tired.
No puede ser cierto. | It can't be true. | That can't be true. ; It cannot be true.
Debió de haber llovido anoche. | It must have rained last night.
""",
     dictations="""
She might have missed the bus. || Puede que haya perdido el bus.
That can't have been an accident. || Eso no pudo haber sido un accidente.
""")

unit("u66-profesional", "B2", "Inglés profesional", "📧",
     "Ya puedo escribir correos formales y participar en reuniones de trabajo",
     "Registro formal en correos y reuniones: proponer, interrumpir con educación, concluir y hacer seguimiento.",
     grammar=["Registro formal vs informal", "Frases para reuniones"],
     items="""
Dear Mr. Smith | Estimado señor Smith | ✉️
To whom it may concern | A quien corresponda | 📨
I am writing to… | Le escribo para… | ✍️
I would like to inform you that… | Quisiera informarle que… | 📢
Please find attached… | Adjunto encontrará… | 📎
As requested | Según lo solicitado | ✅
I look forward to hearing from you | Quedo atento a su respuesta | 📬
Kind regards | Saludos cordiales | 🤝
Sincerely | Atentamente | 🖊️
Could you please…? | ¿Podría por favor…? | 🙏
I would appreciate it if… | Le agradecería si… | 🙏
I apologize for the inconvenience | Disculpe las molestias | 😔
Following up on… | Haciendo seguimiento a… | 🔁
agenda | agenda / orden del día | 🗒️ | a-yén-da
schedule a meeting | programar una reunión | 📅
reschedule | reprogramar | 🔄 | ri-ské-yul
postpone | posponer | ⏭️ | pous-póun
call off | cancelar | ❌
brainstorm | lluvia de ideas | 🧠 | bréin-storm
proposal | propuesta | 📄 | pro-póu-sal
deadline | fecha límite | ⏰ | déd-lain
milestone | hito | 🏁 | máil-stoun
deliverable | entregable | 📦 | di-lí-ve-ra-bol
client | cliente | 🤝 | klái-ent
supplier | proveedor | 🚚 | su-plái-er
negotiate | negociar | 🤝 | ni-góu-shi-eit
agreement | acuerdo | 📃 | a-gríi-ment
invoice | factura | 🧾 | ín-vois
quote (price) | cotización | 💲
approve | aprobar | ✅ | a-prúuv
feedback | retroalimentación | 💬 | fíid-bak
update | actualización / actualizar | 🔄 | ap-déit
report (document) | informe | 📊
presentation | presentación | 📽️ | pre-sen-téi-shon
target | objetivo | 🎯 | tár-guet
priority | prioridad | ⭐ | prai-ó-ri-ti
assign | asignar | 👉 | a-sáin
delegate | delegar | 🤝 | dé-le-geit
efficient | eficiente | ⚡ | i-fí-shent
productive | productivo | 📈 | pro-dák-tiv
workload | carga de trabajo | 🏋️ | uérk-loud
remote work | trabajo remoto | 🏡
headquarters | sede principal | 🏢 | jéd-kuor-ters
branch | sucursal | 🏬 | branch
Let's get started | Empecemos | ▶️
Sorry to interrupt, but… | Perdón que interrumpa, pero… | ✋
I see your point, however… | Entiendo su punto, sin embargo… | ⚖️
Let's move on to… | Pasemos a… | ➡️
To sum up… | En resumen… | 🧾
I'll get back to you on that | Le confirmo eso más adelante | 🔁
Let's touch base next week | Hablemos la próxima semana | 📞
on the same page | en la misma sintonía | 🤝
""",
     extras=[
         D("Formal vs informal",
           "Compara cómo dirías lo mismo a un amigo y a un cliente.",
           """
Hi Tom! → Dear Mr. Brown, || ¡Hola Tom! → Estimado señor Brown: || Dear
I want to know… → I would like to know… || Quiero saber… → Quisiera saber… || would like
Can you send me the file? → Could you please send me the file? || ¿Me mandas el archivo? → ¿Podría por favor enviarme el archivo? || Could you please
Sorry! → I apologize for the inconvenience. || ¡Perdón! → Disculpe las molestias. || apologize
Bye! → Kind regards, || ¡Chao! → Saludos cordiales, || Kind regards
""",
           "¿Qué caracteriza al inglés formal?",
           ["Frases más largas e indirectas, sin contracciones ni jerga", "Usar gonna y wanna", "Escribir todo en mayúsculas"], 0,
           "El REGISTRO FORMAL usa frases más indirectas (Could you please…, I would appreciate…), evita contracciones (I am, no I'm), jerga y abreviaturas, y tiene saludos y despedidas fijas (Dear…, Kind regards). Ojo: look forward to va seguido de -ing: I look forward to hearing from you.",
           """
Dear Ms. López, I am writing to confirm our meeting on Monday. Please find attached the agenda. Kind regards, Santiago. || Estimada señora López: le escribo para confirmar nuestra reunión del lunes. Adjunto encontrará la agenda. Saludos cordiales, Santiago.
""",
           fills="""
I look forward to ___ from you. | hearing / hear | 0 | Quedo atento a su respuesta.
___ find attached the invoice. | Please / Pleased | 0 | Adjunto encontrará la factura.
I would ___ it if you could reply today. | appreciate / thank | 0 | Le agradecería si pudiera responder hoy.
We need to ___ the meeting to Friday. | reschedule / call off | 0 | Necesitamos reprogramar la reunión para el viernes.
"""),
         dialogue("Una reunión de proyecto", "💻 Reunión virtual con un cliente.", """
Manager: Good morning, everyone. Let's get started. First item: the project timeline. || Buenos días a todos. Empecemos. Primer punto: el cronograma del proyecto.
You: We've reached the first milestone. The prototype is ready. || Alcanzamos el primer hito. El prototipo está listo.
Client: Great. However, we'd like to add a new feature. Is that possible before the deadline? || Excelente. Sin embargo, nos gustaría agregar una funcionalidad nueva. ¿Es posible antes de la fecha límite?
You: I see your point, however that would increase the workload. Could we discuss the budget? || Entiendo su punto, sin embargo eso aumentaría la carga de trabajo. ¿Podríamos hablar del presupuesto?
Client: Fair enough. Please send us a quote. || Me parece justo. Por favor envíennos una cotización.
Manager: To sum up: we'll send the quote by Friday and touch base next week. || En resumen: enviaremos la cotización el viernes y hablaremos la próxima semana.
"""),
         story("Un correo que salvó un contrato", "📧", """
Last year Andrea's company almost lost its biggest client because of a delayed delivery. || El año pasado la empresa de Andrea casi pierde su cliente más grande por una entrega retrasada.
The client sent an email complaining about the delay. || El cliente envió un correo quejándose del retraso.
Instead of making excuses, Andrea wrote a clear and professional reply. || En vez de poner excusas, Andrea escribió una respuesta clara y profesional.
She apologized for the inconvenience, explained what had happened and proposed a solution with a new deadline. || Se disculpó por las molestias, explicó lo que había pasado y propuso una solución con una nueva fecha límite.
She also offered a discount on the next invoice as a gesture of goodwill. || También ofreció un descuento en la siguiente factura como gesto de buena voluntad.
The client replied: "Thank you for your prompt reply." The contract was renewed. || El cliente respondió: "Gracias por su pronta respuesta." El contrato se renovó.
""", questions=[
             ("¿Por qué el cliente estaba molesto?", ["Por una entrega retrasada", "Por un precio alto", "Por un error en el nombre"], 0),
             ("¿Qué hizo Andrea?", ["Puso excusas", "Escribió una respuesta profesional con una solución", "No respondió"], 1),
             ("¿Qué ofreció como gesto de buena voluntad?", ["Un regalo", "Un descuento en la siguiente factura", "Una reunión"], 1),
         ]),
         roleplay("Interrumpir con educación", "🖥️ En una reunión, tu colega da un dato equivocado.", """
Colleague: …so the project will be ready in March. || …así que el proyecto estará listo en marzo.
+ Sorry to interrupt, but I think the deadline is in April. || Perdón que interrumpa, pero creo que la fecha límite es en abril.
- You're wrong! Be quiet. || ¡Estás equivocado! Cállate. || Demasiado brusco para una reunión.
Colleague: Oh, are you sure? || Ah, ¿estás seguro?
+ Yes, it was rescheduled last week. I'll send you the updated timeline. || Sí, se reprogramó la semana pasada. Te envío el cronograma actualizado.
- Yes, it was reschedule last week. || Sí, se reprogramar la semana pasada. || Falta el participio: "rescheduled".
Manager: Thanks for clarifying. Let's move on to the budget. || Gracias por aclarar. Pasemos al presupuesto.
+ Could I add something before we move on? || ¿Puedo agregar algo antes de seguir?
- I'll get back to you on the budget never. || Le confirmo el presupuesto nunca. || No tiene sentido.
"""),
     ],
     writes="""
Quedo atento a su respuesta. | I look forward to hearing from you.
Adjunto encontrará el informe. | Please find attached the report. | Please find the report attached.
Disculpe las molestias. | I apologize for the inconvenience. | We apologize for the inconvenience.
""",
     dictations="""
Could you please send me the updated budget? || ¿Podría por favor enviarme el presupuesto actualizado?
Let's touch base next week. || Hablemos la próxima semana.
""",
     speak="""
Sorry to interrupt, but could I add something? || Perdón que interrumpa, pero ¿puedo agregar algo?
""")

unit("u67-ciencia", "B2", "Ciencia y tecnología", "🔬",
     "Ya puedo hablar y leer sobre ciencia, tecnología e innovación",
     "Investigación, inventos, inteligencia artificial y ciberseguridad, con verbos para describir avances.",
     grammar=["Futuro continuo y perfecto: will be doing / will have done"],
     items="""
research | investigación / investigar | 🔬 | ri-sérch
researcher | investigador | 🧑‍🔬 | ri-sér-cher
experiment | experimento | 🧪 | eks-pé-ri-ment
laboratory | laboratorio | ⚗️ | la-bó-ra-to-ri
hypothesis | hipótesis | 💭 | jai-pó-ze-sis
theory | teoría | 📐 | zí-o-ri
data | datos | 📊 | déi-ta
analyze | analizar | 📈 | á-na-lais
findings | hallazgos | 💡 | fáin-dings
breakthrough | avance decisivo | 🚀 | bréik-zru
innovation | innovación | 💡 | i-no-véi-shon
cutting-edge | de vanguardia | ⚡
develop | desarrollar | 🛠️ | di-vé-lop
development | desarrollo | 🏗️
artificial intelligence | inteligencia artificial | 🤖
machine learning | aprendizaje automático | 🧠
algorithm | algoritmo | 🧮 | ál-go-ri-dem
software | software | 💾 | sóft-uer
hardware | hardware | 🖥️ | jard-uer
database | base de datos | 🗄️ | déi-ta-beis
cloud computing | computación en la nube | ☁️
network | red | 🌐 | nét-uerk
server | servidor | 🖥️ | sér-ver
code | código / programar | 💻 | kóud
programming | programación | 👨‍💻
user | usuario | 👤 | iú-ser
interface | interfaz | 🖼️ | ín-ter-feis
wireless | inalámbrico | 📶 | uáier-les
upgrade | mejorar / actualizar | ⬆️ | ap-gréid
install | instalar | 📥 | ins-tól
bug | error de programación | 🐞 | bag
cybersecurity | ciberseguridad | 🛡️ | sai-ber-se-kiú-ri-ti
vulnerability | vulnerabilidad | 🕳️ | val-ne-ra-bí-li-ti
encryption | cifrado | 🔐 | en-kríp-shon
data breach | filtración de datos | 💧
malware | software malicioso | 🦠 | mál-uer
phishing | suplantación (phishing) | 🎣 | fí-shing
firewall | cortafuegos | 🧱 | fáier-uol
authentication | autenticación | 🔑 | o-zen-ti-kéi-shon
genetics | genética | 🧬 | ye-né-tiks
vaccine | vacuna | 💉 | vak-síin
cure | cura / curar | 💊 | kiúr
disease | enfermedad | 🦠 | di-síis
satellite | satélite | 🛰️ | sá-te-lait
telescope | telescopio | 🔭 | té-les-koup
universe | universo | 🌌 | iú-ni-vers
gravity | gravedad | 🍎 | grá-vi-ti
robotics | robótica | 🦾 | rou-bó-tiks
drone | dron | 🛸 | dróun
virtual reality | realidad virtual | 🥽
ethical | ético | ⚖️ | é-zi-kal
In ten years we will be using… | En diez años estaremos usando… | 🔮
By 2040 scientists will have found… | Para 2040 los científicos habrán encontrado… | 🧪
""",
     extras=[
         D("Futuro continuo y futuro perfecto",
           "Dos formas de mirar el futuro con precisión.",
           """
This time next year, I will be working in Canada. || A esta hora el próximo año estaré trabajando en Canadá. || will be working
In 2050 we will be using flying cars. || En 2050 estaremos usando carros voladores. || will be using
By 2030 scientists will have found a cure. || Para 2030 los científicos habrán encontrado una cura. || will have found
By Friday I will have finished the code. || Para el viernes habré terminado el código. || will have finished
""",
           "¿Qué estructura indica que algo estará TERMINADO antes de un momento futuro?",
           ["will be + -ing", "will have + participio"], 1,
           "FUTURO CONTINUO (will be + -ing): algo que estará en curso en un momento futuro. FUTURO PERFECTO (will have + participio): algo que ya estará terminado antes de un momento futuro; suele ir con by (para / antes de): by 2030, by Friday.",
           """
By the time you arrive, I'll have fixed the bug, and I'll be testing the new version. || Para cuando llegues, habré arreglado el error y estaré probando la nueva versión.
""",
           fills="""
Don't call me at 9. I ___ be sleeping. | will / will have | 0 | No me llames a las 9. Estaré durmiendo.
By 2030, we will have ___ a new vaccine. | developed / develop | 0 | Para 2030 habremos desarrollado una vacuna nueva.
This time tomorrow, we will be ___ to Madrid. | flying / flown | 0 | Mañana a esta hora estaremos volando a Madrid.
___ the end of the month, I'll have saved enough. | By / Until | 0 | Para fin de mes habré ahorrado suficiente.
"""),
         dialogue("Una charla sobre IA", "🤖 Pregunta del público en una conferencia.", """
Student: Do you think artificial intelligence will replace programmers? || ¿Cree que la inteligencia artificial reemplazará a los programadores?
Speaker: I don't think so. In ten years, programmers will be working with AI, not against it. || No lo creo. En diez años los programadores estarán trabajando con la IA, no contra ella.
Student: What skills will be most important? || ¿Qué habilidades serán más importantes?
Speaker: Problem-solving, cybersecurity and ethics. Every new technology brings new vulnerabilities. || Resolución de problemas, ciberseguridad y ética. Toda tecnología nueva trae nuevas vulnerabilidades.
Student: So learning security is a good idea? || ¿Entonces aprender seguridad es buena idea?
Speaker: Definitely. By 2030, millions of new cybersecurity jobs will have been created. || Definitivamente. Para 2030 se habrán creado millones de nuevos empleos en ciberseguridad.
"""),
         story("Cómo se reportó una vulnerabilidad", "🛡️", """
Valeria is a cybersecurity researcher who tests apps to find weaknesses before criminals do. || Valeria es una investigadora de ciberseguridad que prueba aplicaciones para encontrar debilidades antes que los delincuentes.
Last month, while she was analyzing a banking app, she noticed something strange in the code. || El mes pasado, mientras analizaba una app bancaria, notó algo extraño en el código.
The app wasn't using proper encryption, so personal data could be exposed on public Wi-Fi networks. || La app no usaba un cifrado adecuado, así que los datos personales podían quedar expuestos en redes wifi públicas.
Instead of publishing the vulnerability, she reported it privately to the bank. This is called responsible disclosure. || En vez de publicar la vulnerabilidad, la reportó en privado al banco. Esto se llama divulgación responsable.
The developers fixed the bug in a week and released an update for all users. || Los desarrolladores arreglaron el error en una semana y lanzaron una actualización para todos los usuarios.
Thanks to ethical hackers like Valeria, millions of people are protected without even knowing it. || Gracias a hackers éticos como Valeria, millones de personas están protegidas sin siquiera saberlo.
""", questions=[
             ("¿Cuál es el trabajo de Valeria?", ["Robar datos", "Encontrar debilidades antes que los delincuentes", "Vender apps"], 1),
             ("¿Qué problema encontró?", ["La app no usaba un cifrado adecuado", "La app era muy lenta", "La app no tenía usuarios"], 0),
             ("¿Qué es la 'divulgación responsable'?", ["Publicar la falla en redes", "Reportar la falla en privado a la empresa", "Ignorar la falla"], 1),
         ]),
         roleplay("Soporte técnico avanzado", "🧑‍💻 Un cliente ve una alerta de inicio de sesión extraña.", """
Client: I received a strange login alert on my account. || Recibí una alerta de inicio de sesión extraña en mi cuenta.
+ Don't worry. First, change your password and enable two-factor authentication. || Tranquilo. Primero, cambie su contraseña y active la autenticación de dos factores.
- Send me your password and I'll check. || Envíeme su contraseña y yo reviso. || Nunca se pide la contraseña: eso es phishing.
Client: Done. Was my data exposed? || Listo. ¿Quedaron expuestos mis datos?
+ I'll analyze the activity log. By this afternoon I'll have finished the analysis. || Voy a analizar el registro de actividad. Para esta tarde habré terminado el análisis.
- By this afternoon I'll be finished analyze. || Para esta tarde estaré terminado analizar. || Futuro perfecto: "I'll have finished".
Client: Thank you. How did it happen? || Gracias. ¿Cómo pasó?
+ It might have been a phishing email. Never click on suspicious links. || Pudo haber sido un correo de phishing. Nunca haga clic en enlaces sospechosos.
- It must have been the satellite. || Debió de haber sido el satélite. || Explicación sin sentido.
"""),
     ],
     writes="""
Para 2030 habremos encontrado una cura. | By 2030 we will have found a cure. | By 2030, we will have found a cure. ; By 2030 we'll have found a cure.
Mañana a esta hora estaré trabajando. | This time tomorrow I will be working. | This time tomorrow, I'll be working. ; This time tomorrow I'll be working.
Active la autenticación de dos factores. | Enable two-factor authentication. | Turn on two-factor authentication.
""",
     dictations="""
The researchers published their findings last week. || Los investigadores publicaron sus hallazgos la semana pasada.
Every new technology brings new vulnerabilities. || Toda tecnología nueva trae nuevas vulnerabilidades.
""")

unit("u68-justicia", "B2", "Normas y justicia", "⚖️",
     "Ya puedo hablar de delitos, del sistema judicial y de seguridad ciudadana",
     "Delitos, el proceso judicial y vocabulario para opinar sobre justicia y prevención.",
     grammar=["Pasiva con modales: should be punished", "Verbos + preposición: accuse of, charge with"],
     items="""
crime | delito | 🚔 | kráim
criminal | delincuente | 🦹 | krí-mi-nal
commit a crime | cometer un delito | ⚠️
illegal | ilegal | 🚫 | i-líi-gal
legal | legal | ✅ | líi-gal
theft | hurto / robo | 👜 | zeft
robbery | atraco / robo | 🔫 | ró-be-ri
burglary | robo en vivienda | 🏠 | bér-gla-ri
pickpocket | carterista | 👛 | pík-po-ket
shoplifting | robo en tiendas | 🛍️ | shóp-lif-ting
fraud | fraude | 💳 | frod
bribery | soborno | 💰 | brái-be-ri
smuggling | contrabando | 📦 | smá-gling
vandalism | vandalismo | 🧯 | ván-da-lism
gang | pandilla | 👥 | gang
witness | testigo | 👀 | uít-nes
investigate | investigar | 🔍 | in-vés-ti-gueit
arrest | arrestar | 🚔 | a-rést
charge with | acusar formalmente de | 📃
accuse of | acusar de | 👉
court | tribunal / juzgado | 🏛️ | kort
trial | juicio | ⚖️ | trái-al
judge | juez / juzgar | 👨‍⚖️ | yach
jury | jurado | 👥 | yú-ri
lawyer | abogado | 🧑‍⚖️ | ló-ier
evidence (court) | pruebas | 🧾
testify | testificar | 🗣️ | tés-ti-fai
guilty | culpable | ⛓️ | guíl-ti
innocent | inocente | 😇 | í-no-sent
verdict | veredicto | 📜 | vér-dikt
sentence | condena / condenar | ⛓️ | sén-tens
prison | cárcel | 🏢 | prí-son
fine | multa | 💸 | fáin
community service | servicio comunitario | 🧹
release | liberar | 🕊️ | ri-líis
appeal | apelar | 📄 | a-píil
justice | justicia | ⚖️ | yás-tis
fair trial | juicio justo | ⚖️
punishment | castigo | 🔒 | pá-nish-ment
rehabilitation | rehabilitación | 🌱 | ri-ja-bi-li-téi-shon
prevention | prevención | 🛑 | pri-vén-shon
security camera | cámara de seguridad | 📹
crime rate | índice de criminalidad | 📊
report a crime | denunciar un delito | 📞
Criminals should be punished | Los delincuentes deberían ser castigados | ⚖️
He was sentenced to ten years | Fue condenado a diez años | ⛓️
""",
     extras=[
         D("Pasiva con modales y verbos con preposición",
           "Las opiniones sobre justicia combinan modales y pasiva.",
           """
Criminals should be punished. || Los delincuentes deberían ser castigados. || should be punished
More cameras must be installed. || Se deben instalar más cámaras. || must be installed
The suspect can't be released yet. || El sospechoso no puede ser liberado todavía. || can't be released
She was accused of fraud. || Fue acusada de fraude. || accused of
He was charged with robbery. || Fue acusado formalmente de robo. || charged with
""",
           "¿Cómo se forma la pasiva con un modal (should, must, can)?",
           ["modal + be + participio", "modal + been + verbo", "modal + is + participio"], 0,
           "PASIVA CON MODALES: modal + be + participio (should be punished, can be prevented). Útil para opinar. Ojo con las preposiciones fijas: accuse someone OF, charge someone WITH, sentence someone TO.",
           """
In my opinion, crime can be prevented with education and better opportunities. || En mi opinión, el delito se puede prevenir con educación y mejores oportunidades.
""",
           fills="""
Vandalism should ___ punished with community service. | be / been | 0 | El vandalismo debería castigarse con servicio comunitario.
The man was accused ___ stealing a car. | of / for | 0 | El hombre fue acusado de robar un carro.
She was sentenced ___ five years in prison. | to / for | 0 | Fue condenada a cinco años de cárcel.
Crime ___ be reduced with more education. | can / is | 0 | El delito puede reducirse con más educación.
"""),
         dialogue("¿Cárcel o rehabilitación?", "📻 Debate en un programa de radio.", """
Host: Should young offenders be sent to prison? || ¿Los jóvenes infractores deberían ir a la cárcel?
Guest 1: I believe serious crimes must be punished. Otherwise, there's no justice for the victims. || Creo que los delitos graves deben castigarse. Si no, no hay justicia para las víctimas.
Guest 2: I see your point, but prison often turns young people into worse offenders. || Entiendo su punto, pero la cárcel muchas veces convierte a los jóvenes en peores infractores.
Host: So what's the alternative? || ¿Entonces cuál es la alternativa?
Guest 2: Rehabilitation and community service. Crime rates can be reduced that way. || Rehabilitación y servicio comunitario. Los índices de criminalidad pueden reducirse así.
Guest 1: That may work for minor crimes, but not for serious ones. || Eso puede servir para delitos menores, pero no para los graves.
"""),
         story("El testigo inesperado", "⚖️", """
Last year a jewelry store in the city center was robbed in the middle of the night. || El año pasado una joyería del centro fue robada en plena noche.
The police arrested a young man who lived nearby. He was charged with burglary. || La policía arrestó a un joven que vivía cerca. Fue acusado de robo.
During the trial, the lawyer for the defense noticed something in the security video. || Durante el juicio, el abogado de la defensa notó algo en el video de seguridad.
The man in the video was much taller than the suspect. He couldn't have been the same person. || El hombre del video era mucho más alto que el sospechoso. No podía ser la misma persona.
Then an unexpected witness testified: a taxi driver who had seen the real thief escape. || Luego un testigo inesperado testificó: un taxista que había visto escapar al verdadero ladrón.
The jury found the young man innocent and he was released. The real thief was caught a month later. || El jurado declaró inocente al joven y fue liberado. El verdadero ladrón fue capturado un mes después.
""", questions=[
             ("¿Qué notó el abogado defensor?", ["Que el hombre del video era más alto que el sospechoso", "Que no había video", "Que el sospechoso confesó"], 0),
             ("¿Quién fue el testigo inesperado?", ["Un policía", "Un taxista", "El dueño de la joyería"], 1),
             ("¿Cuál fue el veredicto?", ["Culpable", "Inocente"], 1),
         ]),
         roleplay("Denunciar un robo", "🚓 Te robaron la billetera en el bus y vas a la estación de policía.", """
Officer: Good afternoon. How can I help you? || Buenas tardes. ¿En qué le puedo ayudar?
+ I'd like to report a theft. My wallet was stolen on the bus. || Quisiera denunciar un hurto. Me robaron la billetera en el bus.
- I'd like to commit a crime. || Quisiera cometer un delito. || ¡Quieres denunciarlo, no cometerlo!
Officer: Did you see the thief? || ¿Vio al ladrón?
+ Not really. It must have been a pickpocket. It was very crowded. || No mucho. Debió de ser un carterista. Estaba muy lleno.
- Yes, he was the judge. || Sí, era el juez. || No tiene sentido.
Officer: What was in the wallet? || ¿Qué había en la billetera?
+ My ID and two cards. The cards should be blocked right away. || Mi cédula y dos tarjetas. Las tarjetas deben bloquearse de inmediato.
- My ID should blocked. || Mi cédula debería bloqueada. || Falta "be": should be blocked.
"""),
     ],
     writes="""
Los delincuentes deberían ser castigados. | Criminals should be punished.
Fue acusado de fraude. | He was accused of fraud. | She was accused of fraud.
Quisiera denunciar un robo. | I'd like to report a theft. | I would like to report a theft. ; I'd like to report a robbery.
""",
     dictations="""
The suspect was charged with burglary. || El sospechoso fue acusado formalmente de robo en vivienda.
Crime can be prevented with education. || El delito se puede prevenir con educación.
""")

unit("u69-emociones", "B2", "Emociones y personalidad", "🎭",
     "Ya puedo describir emociones y rasgos de carácter con matices",
     "Adjetivos fuertes, expresiones idiomáticas de ánimo y rasgos de personalidad para hablar con naturalidad.",
     grammar=["Adjetivos fuertes: absolutely exhausted", "Expresiones idiomáticas de ánimo"],
     items="""
emotion | emoción | 💗 | i-móu-shon
mood | estado de ánimo | 🌦️ | muud
confidence | seguridad en sí mismo | 😎 | kón-fi-dens
self-esteem | autoestima | 🌟 | self-es-tíim
motivated | motivado | 🔥 | móu-ti-vei-ted
determined | decidido | 💪 | di-tér-mind
grateful | agradecido | 🙏 | gréit-ful
content | satisfecho / en paz | 😌 | kon-tént
overwhelmed | abrumado | 🌊 | ou-ver-uélmd
frustrated | frustrado | 😤 | fras-tréi-ted
envious | envidioso | 💚 | én-vi-os
empathy | empatía | 🫂 | ém-pa-zi
resilience | resiliencia | 🌱 | ri-sí-li-ens
cope with | sobrellevar / afrontar | 🧯
overcome | superar | 🏔️ | ou-ver-kám
mindset | mentalidad | 🧠 | máind-set
attitude | actitud | 😏 | á-ti-tud
patience | paciencia | ⏳ | péi-shens
willpower | fuerza de voluntad | 💪 | uíl-pau-er
curiosity | curiosidad | 🔍 | kiu-ri-ó-si-ti
introvert | introvertido | 📚 | ín-tro-vert
extrovert | extrovertido | 🎉 | éks-tro-vert
perfectionist | perfeccionista | 💯 | per-fék-sho-nist
optimist | optimista | ☀️ | óp-ti-mist
pessimist | pesimista | 🌧️ | pé-si-mist
generous | generoso | 🎁 | yé-ne-ros
down-to-earth | con los pies en la tierra | 🌍
easy-going | relajado | 😌
hard-working | trabajador | 🐝
thoughtful | considerado / atento | 💭 | zót-ful
reliable | confiable | 🛡️ | ri-lái-a-bol
absolutely exhausted | absolutamente agotado | 😩
really thrilled | emocionadísimo | 🤩
over the moon | feliz de la vida | 🌙
on top of the world | en la cima del mundo | 🏔️
butterflies in my stomach | mariposas en el estómago | 🦋
a weight off my shoulders | un peso de encima | 🎒
keep calm | mantener la calma | 🧘
cheer someone up | animar a alguien | 🌈
look on the bright side | ver el lado positivo | ☀️
It's not the end of the world | No es el fin del mundo | 🌍
pull yourself together | recomponerse | 💪
mixed feelings | sentimientos encontrados | ⚖️
in a good mood | de buen humor | 😁
in a bad mood | de mal humor | 😠
""",
     extras=[
         D("Adjetivos fuertes",
           "Algunos adjetivos ya son 'extremos'. Mira qué palabra los acompaña.",
           """
I'm very tired. → I'm absolutely exhausted. || Estoy muy cansado. → Estoy absolutamente agotado. || absolutely exhausted
The movie was very good. → It was absolutely amazing. || La película fue muy buena. → Fue absolutamente increíble. || absolutely amazing
I'm very happy. → I'm over the moon! || Estoy muy feliz. → ¡Estoy feliz de la vida! || over the moon
The food was very bad. → It was absolutely terrible. || La comida estuvo muy mala. → Estuvo absolutamente terrible. || absolutely terrible
""",
           "¿Qué palabra suele ir con adjetivos extremos (exhausted, amazing)?",
           ["very", "absolutely"], 1,
           "Con adjetivos normales (tired, good) usamos very. Con adjetivos EXTREMOS, que ya significan 'muy', no se usa very sino absolutely o really: absolutely exhausted (no 'very exhausted'), really thrilled. Para el ánimo hay muchas expresiones idiomáticas: over the moon (feliz), a weight off my shoulders (aliviado).",
           """
I'm not just happy, I'm absolutely thrilled! Getting the job was a weight off my shoulders. || No solo estoy feliz, ¡estoy emocionadísimo! Conseguir el trabajo fue un peso de encima.
""",
           fills="""
I'm ___ exhausted after the trip. | absolutely / very | 0 | Estoy absolutamente agotado después del viaje.
She's a ___ person; she always sees the bright side. | positive / positively | 0 | Es una persona positiva; siempre ve el lado bueno.
When I passed the exam, I was over the ___. | moon / sun | 0 | Cuando pasé el examen, estaba feliz de la vida.
Try to ___ calm. It's not the end of the world. | keep / make | 0 | Trata de mantener la calma. No es el fin del mundo.
"""),
         tip("🎭", "Describir el carácter", "Para sonar natural, combina rasgos: 'She's hard-working and reliable, but a bit of a perfectionist.' Un rasgo con 'but a bit of a…' suena muy nativo para matizar."),
         dialogue("Animar a un amigo", "☕ Tu amigo no pasó una entrevista.", """
You: Hey, you look down. What's wrong? || Oye, te ves bajoneado. ¿Qué pasa?
Leo: I didn't get the job. I'm really frustrated. || No me dieron el trabajo. Estoy muy frustrado.
You: I'm sorry. But look on the bright side: you got to the final interview. || Lo siento. Pero mira el lado positivo: llegaste a la entrevista final.
Leo: That's true. I guess it's not the end of the world. || Es cierto. Supongo que no es el fin del mundo.
You: Exactly. You're hard-working and reliable. The right job will come. || Exacto. Eres trabajador y confiable. El trabajo indicado va a llegar.
Leo: Thanks. I feel a bit better now. || Gracias. Ya me siento un poco mejor.
"""),
         story("Dos hermanas, dos mentalidades", "🌗", """
Camila and Daniela are sisters, but they have very different mindsets. || Camila y Daniela son hermanas, pero tienen mentalidades muy diferentes.
Camila is an optimist. When something goes wrong, she looks on the bright side. || Camila es optimista. Cuando algo sale mal, ve el lado positivo.
Daniela is more of a pessimist and a perfectionist. Small mistakes make her feel overwhelmed. || Daniela es más pesimista y perfeccionista. Los errores pequeños la hacen sentir abrumada.
Last year both of them started a small business together. The first months were really hard. || El año pasado las dos empezaron un pequeño negocio juntas. Los primeros meses fueron muy difíciles.
When sales dropped, Daniela wanted to give up, but Camila helped her keep calm. || Cuando cayeron las ventas, Daniela quería rendirse, pero Camila la ayudó a mantener la calma.
With patience and resilience, they overcame the hard times. Now their business is doing great. || Con paciencia y resiliencia, superaron los tiempos difíciles. Ahora su negocio va muy bien.
""", questions=[
             ("¿Cómo es Camila?", ["Optimista", "Pesimista", "Perezosa"], 0),
             ("¿Qué hace Daniela cuando comete errores pequeños?", ["Se ríe", "Se siente abrumada", "Los ignora"], 1),
             ("¿Cómo superaron los tiempos difíciles?", ["Con paciencia y resiliencia", "Cerrando el negocio", "Con suerte"], 0),
         ]),
         roleplay("Describir tu personalidad", "🧑‍💼 En una dinámica de grupo te piden describirte.", """
Facilitator: Tell us three words that describe you. || Dinos tres palabras que te describan.
+ I'd say I'm hard-working, curious and down-to-earth. || Diría que soy trabajador, curioso y con los pies en la tierra.
- I'd say I'm very exhausted. || Diría que soy muy agotado. || Eso es un estado, no un rasgo de carácter.
Facilitator: Nice. And a weakness? || Qué bien. ¿Y una debilidad?
+ I'm a bit of a perfectionist, so sometimes I'm too hard on myself. || Soy un poco perfeccionista, así que a veces soy muy duro conmigo mismo.
- I'm absolutely perfect. || Soy absolutamente perfecto. || Suena arrogante y no responde la pregunta.
Facilitator: How do you handle stress? || ¿Cómo manejas el estrés?
+ I try to keep calm and look on the bright side. || Trato de mantener la calma y ver el lado positivo.
- I lose the calm always. || Pierdo la calma siempre. || Se dice "I lose my temper" y no es ideal decirlo así.
"""),
     ],
     writes="""
Estoy absolutamente agotado. | I'm absolutely exhausted. | I am absolutely exhausted.
Trata de ver el lado positivo. | Try to look on the bright side.
Es trabajadora y confiable. | She's hard-working and reliable. | She is hard-working and reliable.
""",
     dictations="""
When I got the news, I was over the moon. || Cuando recibí la noticia, estaba feliz de la vida.
It's not the end of the world. Try to keep calm. || No es el fin del mundo. Trata de mantener la calma.
""",
     speak="""
I'm a hard-working and curious person who likes learning new things. || Soy una persona trabajadora y curiosa a la que le gusta aprender cosas nuevas.
""")
