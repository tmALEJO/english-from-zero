# B2 · Parte 3 (unidades 70-74)

unit("u70-arte", "B2", "Arte, cine y literatura", "🎬",
     "Ya puedo hablar y opinar sobre películas, libros, música y arte",
     "Géneros, reseñas y crítica cultural; participios como adjetivos y orden enfático.",
     grammar=["Participios como adjetivos: a well-written book", "so / such para enfatizar"],
     items="""
plot | trama / argumento | 📖 | plot
character | personaje | 🎭 | ká-rak-ter
main character | protagonista | ⭐
setting | ambientación | 🏞️ | sé-ting
genre | género | 🎞️ | yán-ra
masterpiece | obra maestra | 🖼️ | más-ter-piis
review | reseña / reseñar | 📝 | ri-viú
critic | crítico (persona) | 🧐 | krí-tik
audience | público / audiencia | 👥 | ó-di-ens
soundtrack | banda sonora | 🎵 | sáund-trak
subtitles | subtítulos | 💬 | sáb-tai-tols
scene | escena | 🎬 | síin
twist | giro inesperado | 🔀 | tuist
spoiler | spoiler / destripe | 🚫 | spói-ler
sequel | secuela | ▶️ | síi-kuel
cast | elenco | 🎭 | kast
director | director | 🎥 | di-rék-tor
performance | actuación / interpretación | 🎤 | per-fór-mans
thriller | suspenso | 😱 | zrí-ler
documentary | documental | 🎞️ | do-kiu-mén-ta-ri
sci-fi | ciencia ficción | 🚀 | sái-fai
fiction | ficción | 📚 | fík-shon
non-fiction | no ficción | 📘
novel | novela | 📕 | nó-vel
poetry | poesía | 🖋️ | póu-e-tri
chapter | capítulo | 📑 | cháp-ter
author | autor | ✒️ | ó-zor
playwright | dramaturgo | 🎭 | pléi-rait
lyrics | letra (de canción) | 🎶 | lí-riks
melody | melodía | 🎼 | mé-lo-di
painting | pintura / cuadro | 🖼️ | péin-ting
sculpture | escultura | 🗿 | skálp-cher
exhibition | exposición | 🏛️ | ek-si-bí-shon
gallery | galería | 🖼️ | gá-le-ri
masterful | magistral | 👏 | más-ter-ful
moving | conmovedor | 🥹 | múu-ving
overrated | sobrevalorado | 📉 | ou-ver-réi-ted
underrated | subvalorado | 📈 | an-der-réi-ted
predictable | predecible | 🔮 | pri-dík-ta-bol
well-written | bien escrito | ✍️
fast-paced | de ritmo rápido | 🏎️
slow-paced | de ritmo lento | 🐢
thought-provoking | que hace pensar | 💭
based on a true story | basado en hechos reales | 📰
It's worth watching | Vale la pena verla | 👍
I couldn't put it down | No pude dejarlo (un libro) | 📖
It gave me goosebumps | Me puso la piel de gallina | 😮
""",
     extras=[
         D("Participios como adjetivos y so / such",
           "Mira cómo se forman estos adjetivos y cómo se enfatiza.",
           """
It's a well-written novel. || Es una novela bien escrita. || well-written
The movie was a bit overrated. || La película estaba un poco sobrevalorada. || overrated
It's a thought-provoking documentary. || Es un documental que hace pensar. || thought-provoking
The ending was so surprising! || ¡El final fue tan sorprendente! || so
It was such a moving film. || Fue una película tan conmovedora. || such a
""",
           "¿Cuándo se usa such a en vez de so?",
           ["Con adjetivo + sustantivo (such a good film)", "Con adjetivo solo (so good)", "Nunca"], 0,
           "Muchos adjetivos culturales son participios o compuestos: well-written, fast-paced, thought-provoking. Para enfatizar: so + adjetivo (so good), such a + adjetivo + sustantivo (such a good film). Ojo: es such a, no 'so a'.",
           """
It was such a predictable plot that I guessed the twist, but the acting was so good! || Fue una trama tan predecible que adiviné el giro, ¡pero la actuación fue tan buena!
""",
           fills="""
It's a ___ book. I read it in one day. | well-written / well-write | 0 | Es un libro bien escrito. Lo leí en un día.
The film was ___ boring that I fell asleep. | so / such | 0 | La película era tan aburrida que me quedé dormido.
It was ___ an amazing performance! | such / so | 0 | ¡Fue una actuación tan increíble!
The documentary was really ___. It made me think a lot. | thought-provoking / thought-provoke | 0 | El documental hacía pensar mucho.
"""),
         dialogue("Recomendando una serie", "📺 Hablando de qué ver.", """
Ana: Have you seen that new sci-fi series? || ¿Viste esa nueva serie de ciencia ficción?
Leo: Not yet. Is it any good? || Todavía no. ¿Es buena?
Ana: It's amazing. The plot is so original and the soundtrack gave me goosebumps. || Es increíble. La trama es muy original y la banda sonora me puso la piel de gallina.
Leo: Is it fast-paced? I don't like slow shows. || ¿Es de ritmo rápido? No me gustan las series lentas.
Ana: Very. And there's a twist at the end you'll never guess. No spoilers! || Mucho. Y hay un giro al final que nunca vas a adivinar. ¡Sin spoilers!
Leo: You've convinced me. It sounds worth watching. || Me convenciste. Suena a que vale la pena verla.
"""),
         story("El libro que no pude soltar", "📖", """
Last month a friend lent me a novel by a Colombian author I didn't know. || El mes pasado un amigo me prestó una novela de un autor colombiano que no conocía.
At first I thought it would be slow, but the first chapter was so gripping that I couldn't put it down. || Al principio pensé que sería lenta, pero el primer capítulo era tan atrapante que no pude soltarlo.
The main character was a young detective in a small, rainy town full of secrets. || El protagonista era un joven detective en un pueblo pequeño y lluvioso lleno de secretos.
The writing was masterful, and the plot was full of twists I never saw coming. || La escritura era magistral, y la trama estaba llena de giros que nunca vi venir.
It's based on a true story, which made it even more moving. || Está basada en hechos reales, lo cual la hizo aún más conmovedora.
I finished it in two days and immediately bought the sequel. It's one of the most underrated books I've ever read. || La terminé en dos días e inmediatamente compré la secuela. Es uno de los libros más subvalorados que he leído.
""", questions=[
             ("¿Quién era el protagonista?", ["Un joven detective", "Un profesor", "Un cantante"], 0),
             ("¿En qué está basada la novela?", ["En hechos reales", "En un sueño", "En una película"], 0),
             ("¿Qué hizo el narrador al terminarla?", ["Compró la secuela", "La regaló", "La olvidó"], 0),
         ]),
         roleplay("Opinar sobre una película", "🎥 Sales del cine con un amigo que la amó.", """
Friend: Wasn't that movie incredible? || ¿No estuvo increíble esa película?
+ Honestly, I found it a bit overrated. The plot was predictable. || Honestamente, me pareció un poco sobrevalorada. La trama era predecible.
- Honestly, it was so a masterpiece. || Honestamente, fue tan una obra maestra. || Se dice "such a masterpiece".
Friend: Really? I thought the acting was amazing. || ¿En serio? A mí me pareció que la actuación fue increíble.
+ The acting was great, I'll give you that. But the ending was too long. || La actuación sí fue buenísima, te lo concedo. Pero el final fue muy largo.
- The acting was very amazing. || La actuación fue muy increíble. || Con "amazing" se dice "really/absolutely amazing", no "very".
Friend: Fair enough. What would you recommend instead? || Justo. ¿Qué recomendarías en cambio?
+ There's a documentary that's really thought-provoking. It's worth watching. || Hay un documental que hace pensar mucho. Vale la pena verlo.
- There's a spoiler worth watching. || Hay un spoiler que vale la pena ver. || No tiene sentido.
"""),
     ],
     writes="""
Es un libro bien escrito. | It's a well-written book. | It is a well-written book.
Fue una película tan conmovedora. | It was such a moving film. | It was such a moving movie.
Vale la pena verla. | It's worth watching. | It is worth watching.
""",
     dictations="""
The plot was so predictable that I guessed the ending. || La trama era tan predecible que adiviné el final.
It's one of the most underrated novels I've ever read. || Es una de las novelas más subvaloradas que he leído.
""")

unit("u71-negocios", "B2", "Emprender y negocios", "🚀",
     "Ya puedo hablar de emprendimiento, startups y presentar una idea de negocio",
     "Startups, finanzas de empresa y cómo presentar un pitch; condicionales mixtos.",
     grammar=["Condicional mixto", "wish + would para quejas"],
     items="""
entrepreneur | emprendedor | 🚀 | on-tre-pre-nér
startup | emprendimiento / startup | 💡 | stárt-ap
business plan | plan de negocio | 📋
investor | inversionista | 💰 | in-vés-tor
funding | financiación | 💵 | fán-ding
capital | capital | 🏦 | ká-pi-tal
revenue | ingresos (de empresa) | 📈 | ré-ve-niu
profit margin | margen de ganancia | 💹
break even | alcanzar el punto de equilibrio | ⚖️
scale up | escalar / crecer | 📊
market | mercado | 🏪 | már-ket
target market | mercado objetivo | 🎯
competitor | competidor | 🥊 | kom-pé-ti-tor
competitive | competitivo | 💪 | kom-pé-ti-tiv
demand | demanda | 📊 | di-mánd
supply | oferta / suministro | 📦 | su-plái
niche | nicho | 🎯 | niich
brand | marca | ™️ | brand
launch | lanzar / lanzamiento | 🚀 | lonch
customer base | base de clientes | 👥
market share | cuota de mercado | 🥧
strategy | estrategia | ♟️ | strá-te-yi
growth | crecimiento | 🌱 | gróuz
partnership | sociedad / alianza | 🤝 | párt-ner-ship
shareholder | accionista | 📜 | shér-jóul-der
bankruptcy | quiebra | 📉 | bánk-rap-si
risk-taker | arriesgado | 🎲
cash flow | flujo de caja | 💸
invest | invertir | 📈 | in-vést
return on investment | retorno de la inversión | 💹
pitch | presentar una idea / pitch | 🎤 | pich
negotiation | negociación | 🤝 | ni-go-si-éi-shon
deal | trato / negocio | 🤝 | diil
contract | contrato | 📃 | kón-trakt
franchise | franquicia | 🏪 | frán-chais
e-commerce | comercio electrónico | 🛒 | íi-kó-mers
freelance | independiente / freelance | 💻 | fríi-lans
side hustle | negocio secundario | 🌙
scalable | escalable | 📈 | skéi-la-bol
sustainable | sostenible | 🌿 | sas-téi-na-bol
innovative | innovador | ✨ | í-no-vei-tiv
disrupt | revolucionar (un sector) | ⚡ | dis-rápt
value proposition | propuesta de valor | 💎
Our product solves… | Nuestro producto resuelve… | 🔧
We're looking for investment | Buscamos inversión | 💰
""",
     extras=[
         D("Condicional mixto",
           "A veces una condición del pasado afecta el presente, o al revés.",
           """
If I had saved money, I would have more options now. || Si hubiera ahorrado, tendría más opciones ahora. || had saved, would have
If I had studied business, I would understand this better. || Si hubiera estudiado negocios, entendería mejor esto. || had studied, would understand
If I were more organized, I wouldn't have missed the deadline. || Si fuera más organizado, no habría perdido la fecha límite. || were, wouldn't have missed
I wish my partner would reply faster. || Ojalá mi socio respondiera más rápido. || would reply
""",
           "En 'If I had studied business, I would understand this now', ¿de qué tiempos se mezcla?",
           ["Pasado (condición) y presente (resultado)", "Solo presente", "Solo futuro"], 0,
           "El CONDICIONAL MIXTO combina tiempos: condición pasada + resultado presente (If I had saved, I would have money now) o condición presente + resultado pasado (If I were richer, I would have bought it). wish + would se usa para quejarse de algo molesto que otra persona hace: I wish he would listen.",
           """
If our team had launched earlier, we would be the market leaders today. || Si nuestro equipo hubiera lanzado antes, hoy seríamos los líderes del mercado.
""",
           fills="""
If I had learned to code, I ___ build the app myself now. | would / would have | 0 | Si hubiera aprendido a programar, ahora podría hacer la app yo mismo.
If she weren't so busy, she ___ have come to the pitch. | would / will | 0 | Si no estuviera tan ocupada, habría venido al pitch.
I wish investors ___ answer my emails. | would / will | 0 | Ojalá los inversionistas respondieran mis correos.
If we had more funding, we ___ scale up faster. | could / can | 0 | Si tuviéramos más financiación, podríamos crecer más rápido.
"""),
         dialogue("Presentando a un inversionista", "🎤 Un emprendedor presenta su idea.", """
Investor: So, what does your startup do? || Entonces, ¿qué hace tu emprendimiento?
Founder: Our app connects small farmers directly with restaurants. We solve the problem of middlemen. || Nuestra app conecta a los pequeños agricultores directamente con restaurantes. Resolvemos el problema de los intermediarios.
Investor: Interesting. What's your target market? || Interesante. ¿Cuál es tu mercado objetivo?
Founder: Medium-sized cities in Colombia. There's high demand and few competitors. || Ciudades medianas de Colombia. Hay mucha demanda y pocos competidores.
Investor: And your revenue model? || ¿Y tu modelo de ingresos?
Founder: We charge a small commission on each order. It's scalable and sustainable. We're looking for investment to scale up. || Cobramos una pequeña comisión por cada pedido. Es escalable y sostenible. Buscamos inversión para crecer.
"""),
         story("Del fracaso al éxito", "📈", """
When Mariana started her first business at twenty-four, it failed within a year. || Cuando Mariana empezó su primer negocio a los veinticuatro, quebró en menos de un año.
She had spent all her capital on marketing and ran out of cash flow. || Había gastado todo su capital en mercadeo y se quedó sin flujo de caja.
"If I had planned better, I wouldn't have gone bankrupt," she often thought. || "Si hubiera planeado mejor, no habría quebrado", pensaba a menudo.
But she didn't give up. She learned from her mistakes and studied business online for free. || Pero no se rindió. Aprendió de sus errores y estudió negocios en internet gratis.
Two years later she launched a new startup, this time with a clear business plan and a small, loyal customer base. || Dos años después lanzó un nuevo emprendimiento, esta vez con un plan de negocio claro y una base de clientes pequeña y leal.
Today her company has fifteen employees. "If I hadn't failed the first time, I wouldn't be here now," she says. || Hoy su empresa tiene quince empleados. "Si no hubiera fracasado la primera vez, no estaría aquí ahora", dice.
""", questions=[
             ("¿Por qué quebró su primer negocio?", ["Gastó todo el capital y se quedó sin flujo de caja", "Nadie quería el producto", "Se enfermó"], 0),
             ("¿Qué hizo después de fracasar?", ["Se rindió", "Aprendió de sus errores y estudió", "Pidió un préstamo grande"], 1),
             ("¿Qué dice Mariana sobre su fracaso?", ["Que fue inútil", "Que sin él no estaría donde está hoy", "Que no volvería a emprender"], 1),
         ]),
         roleplay("Negociar una comisión", "🤝 Un posible socio quiere una comisión muy alta.", """
Partner: I'll distribute your product, but I want a forty percent commission. || Distribuyo tu producto, pero quiero el cuarenta por ciento de comisión.
+ That's too high for us. Our profit margin wouldn't cover it. || Es muy alto para nosotros. Nuestro margen de ganancia no lo cubriría.
- Yes, take fifty percent. || Sí, llévate el cincuenta por ciento. || Estás cediendo aún más, en contra tuya.
Partner: What can you offer? || ¿Qué puedes ofrecer?
+ Twenty percent, plus a bonus if we reach our sales target. || Veinte por ciento, más un bono si alcanzamos la meta de ventas.
- Nothing. Take it or leave it. || Nada. Lo tomas o lo dejas. || Demasiado brusco para una negociación.
Partner: Make it twenty-five and we have a deal. || Que sean veinticinco y hay trato.
+ Deal. Let's put it in the contract. || Trato hecho. Pongámoslo en el contrato.
- Deal. I wish you would answer. || Trato hecho. Ojalá respondieras. || No encaja en la conversación.
"""),
     ],
     writes="""
Buscamos inversión para crecer. | We're looking for investment to scale up. | We are looking for investment to scale up. ; We're looking for investment to grow.
Si hubiera ahorrado, ahora tendría más opciones. | If I had saved money, I would have more options now. | If I'd saved money, I would have more options now.
Nuestro producto resuelve un problema real. | Our product solves a real problem.
""",
     dictations="""
There's high demand and few competitors. || Hay mucha demanda y pocos competidores.
If we had more funding, we could scale up faster. || Si tuviéramos más financiación, podríamos crecer más rápido.
""",
     speak="""
Our app solves a real problem and we're looking for investment. || Nuestra app resuelve un problema real y buscamos inversión.
""")

unit("u72-sociedad", "B2", "Sociedad y actualidad", "🌐",
     "Ya puedo opinar sobre temas sociales con argumentos equilibrados",
     "Temas sociales (educación, desigualdad, migración, tecnología) y lenguaje para argumentar con matices.",
     grammar=["Lenguaje de matización: tend to, to some extent", "The + adjetivo (the poor)"],
     items="""
society | sociedad | 🌍 | so-sái-e-ti
community | comunidad | 🏘️ | ko-miú-ni-ti
inequality | desigualdad | ⚖️ | i-ni-kuó-li-ti
poverty | pobreza | 🪫 | pó-ver-ti
wealth | riqueza | 💎 | uelz
the poor | los pobres | 🫙
the rich | los ricos | 💰
the elderly | los ancianos | 👵
the homeless | las personas sin hogar | 🏚️
gap | brecha | ↔️ | gap
opportunity | oportunidad | 🚪 | o-por-tiú-ni-ti
access | acceso | 🔑 | ák-ses
education system | sistema educativo | 🎓
healthcare | sistema de salud | 🏥 | jélz-ker
welfare | bienestar social / ayudas | 🤲 | uél-fer
unemployment | desempleo | 📉 | an-em-plói-ment
immigration | inmigración | 🛂 | i-mi-gréi-shon
immigrant | inmigrante | 🧳 | í-mi-grant
refugee | refugiado | ⛺ | re-fiu-yíi
integration | integración | 🤝 | in-te-gréi-shon
discrimination | discriminación | 🚫 | dis-kri-mi-néi-shon
equality | igualdad | ⚖️ | i-kuó-li-ti
rights | derechos | ✊ | ráits
freedom | libertad | 🕊️ | fríi-dom
democracy | democracia | 🗳️ | di-mó-kra-si
corruption | corrupción | 💰 | ko-ráp-shon
tax | impuesto | 🏛️ | taks
public services | servicios públicos | 🚰
infrastructure | infraestructura | 🏗️ | ín-fra-strak-cher
urbanization | urbanización | 🏙️ | er-ba-nai-séi-shon
population growth | crecimiento poblacional | 📈
aging population | envejecimiento de la población | 👴
generation gap | brecha generacional | 👨‍👦
social media impact | impacto de las redes sociales | 📱
digital divide | brecha digital | 💻
volunteer | voluntario | 🙋 | vo-lun-tíer
donate | donar | 🎁 | dóu-neit
raise awareness | concientizar | 📣
NGO | ONG | 🤝 | en-yi-óu
charity | obra benéfica | 🤲 | chá-ri-ti
tend to | tender a / soler | 🔁
to some extent | en cierta medida | ⚖️
on the whole | en general | 🌐
by and large | en términos generales | 📊
it could be argued that | podría argumentarse que | 💬
there's no denying that | no se puede negar que | ✔️
a growing concern | una preocupación creciente | 📈
""",
     extras=[
         D("Matizar y generalizar",
           "El inglés culto evita afirmaciones absolutas. Mira cómo se suaviza.",
           """
Young people spend too much time online. → Young people tend to spend a lot of time online. || Los jóvenes pasan demasiado tiempo en línea. → Los jóvenes suelen pasar mucho tiempo en línea. || tend to
Technology is good. → Technology is positive, to some extent. || La tecnología es buena. → La tecnología es positiva, en cierta medida. || to some extent
The rich don't pay enough taxes. || Los ricos no pagan suficientes impuestos. || The rich
The government should help the poor. || El gobierno debería ayudar a los pobres. || the poor
There's no denying that inequality is a growing concern. || No se puede negar que la desigualdad es una preocupación creciente. || There's no denying
""",
           "¿Qué significa 'tend to'?",
           ["Soler / tener tendencia a", "Estar obligado a", "Nunca"], 0,
           "Para argumentar con equilibrio: tend to (soler), to some extent (en cierta medida), on the whole / by and large (en general), it could be argued that (podría argumentarse que). The + adjetivo = un grupo de personas: the poor (los pobres), the elderly (los ancianos), the homeless.",
           """
On the whole, education tends to reduce inequality, but access isn't equal for everyone. || En general, la educación tiende a reducir la desigualdad, pero el acceso no es igual para todos.
""",
           fills="""
People in cities ___ to be busier. | tend / tends | 0 | La gente de las ciudades suele estar más ocupada.
The government should support ___ elderly. | the / — | 0 | El gobierno debería apoyar a los ancianos.
To some ___, social media connects people. | extent / point | 0 | En cierta medida, las redes sociales conectan a la gente.
There's no ___ that poverty is a serious problem. | denying / deny | 0 | No se puede negar que la pobreza es un problema serio.
"""),
         dialogue("Debate sobre la tecnología", "🎓 En una clase de inglés avanzado.", """
Teacher: Is technology making society better or worse? || ¿La tecnología está haciendo la sociedad mejor o peor?
Camilo: On the whole, I'd say better. It gives access to education and information. || En general, diría que mejor. Da acceso a la educación y la información.
Lucía: To some extent, yes. But there's a growing digital divide between the rich and the poor. || En cierta medida, sí. Pero hay una brecha digital creciente entre los ricos y los pobres.
Camilo: That's a fair point. Not everyone has the same opportunities. || Es un buen punto. No todos tienen las mismas oportunidades.
Lucía: Exactly. It could be argued that technology increases inequality if access isn't equal. || Exacto. Podría argumentarse que la tecnología aumenta la desigualdad si el acceso no es igual.
Teacher: Excellent arguments from both of you. || Excelentes argumentos de ambos.
"""),
         story("El proyecto de la biblioteca", "📚", """
In a poor neighborhood on the edge of the city, there was no library and few opportunities for the children. || En un barrio pobre a las afueras de la ciudad, no había biblioteca y había pocas oportunidades para los niños.
A group of university students decided to raise awareness about the problem. || Un grupo de estudiantes universitarios decidió concientizar sobre el problema.
They started an NGO and collected donations of books and computers. || Crearon una ONG y recogieron donaciones de libros y computadores.
Local volunteers helped build a small community library in an old building. || Voluntarios del barrio ayudaron a construir una pequeña biblioteca comunitaria en un edificio viejo.
Now, on the whole, children in that neighborhood have better access to education and the internet. || Ahora, en general, los niños de ese barrio tienen mejor acceso a la educación y a internet.
It's a small project, but there's no denying that it has changed many lives. || Es un proyecto pequeño, pero no se puede negar que ha cambiado muchas vidas.
""", questions=[
             ("¿Qué faltaba en el barrio?", ["Una biblioteca y oportunidades", "Agua", "Un hospital"], 0),
             ("¿Qué crearon los estudiantes?", ["Una empresa", "Una ONG", "Un colegio privado"], 1),
             ("¿Qué resultado tuvo el proyecto?", ["Mejor acceso a la educación e internet para los niños", "Nada", "Más desempleo"], 0),
         ]),
         roleplay("Opinar con matices", "🎤 Un periodista te entrevista sobre las redes sociales.", """
Reporter: Do you think social media is bad for young people? || ¿Cree que las redes sociales son malas para los jóvenes?
+ To some extent, yes, but it also has benefits. It's not that simple. || En cierta medida, sí, pero también tiene beneficios. No es tan sencillo.
- Yes, social media is absolutely always bad for everyone. || Sí, las redes son absolutamente siempre malas para todos. || Demasiado absoluto; matiza.
Reporter: Could you give an example of a benefit? || ¿Podría dar un ejemplo de un beneficio?
+ Sure. It tends to help people stay connected and learn new skills. || Claro. Suele ayudar a la gente a mantenerse conectada y a aprender nuevas habilidades.
- Sure. It tend to help people. || Claro. Suele ayudar a la gente. || Con "it" es "tends to".
Reporter: And the risks? || ¿Y los riesgos?
+ There's no denying that too much screen time can be a problem. || No se puede negar que demasiado tiempo de pantalla puede ser un problema.
- There's no denying nothing. || No se puede negar nada. || Doble negación y sin sentido.
"""),
     ],
     writes="""
No se puede negar que la desigualdad es un problema serio. | There's no denying that inequality is a serious problem. | There is no denying that inequality is a serious problem.
El gobierno debería ayudar a los pobres. | The government should help the poor.
Los jóvenes suelen usar mucho las redes sociales. | Young people tend to use social media a lot.
""",
     dictations="""
On the whole, education reduces inequality. || En general, la educación reduce la desigualdad.
There's a growing concern about the digital divide. || Hay una preocupación creciente por la brecha digital.
""")

unit("u73-futuro-planeta", "B2", "El futuro del planeta", "🌱",
     "Ya puedo debatir sobre sostenibilidad, energía y el futuro del medio ambiente",
     "Energías, economía circular y soluciones climáticas; estructuras para proponer y predecir.",
     grammar=["unless / provided that / as long as", "be likely to / be bound to"],
     items="""
sustainability | sostenibilidad | 🌿 | sas-tei-na-bí-li-ti
carbon footprint | huella de carbono | 👣
emissions | emisiones | 💨 | i-mí-shons
renewable | renovable | 🔄 | ri-niú-a-bol
solar power | energía solar | ☀️
wind power | energía eólica | 🌬️
hydropower | energía hidroeléctrica | 💧 | jái-dro-pau-er
nuclear | nuclear | ⚛️ | niú-kli-ar
fossil fuels | combustibles fósiles | ⛽
electric vehicle | vehículo eléctrico | 🔌
battery | batería | 🔋 | bá-te-ri
grid | red eléctrica | ⚡ | grid
efficiency | eficiencia | ⚙️ | i-fí-shen-si
consumption | consumo | 📊 | kon-sámp-shon
circular economy | economía circular | ♻️
recycling | reciclaje | ♻️ | ri-sái-kling
upcycle | reutilizar creativamente | 🎨 | áp-sai-kol
single-use | de un solo uso | 🥤
biodegradable | biodegradable | 🍂 | bai-o-di-gréi-da-bol
compost | compostaje / abono | 🪱 | kóm-post
conservation | conservación | 🌲 | kon-ser-véi-shon
biodiversity | biodiversidad | 🦋 | bai-o-dai-vér-si-ti
ecosystem | ecosistema | 🌊 | íi-ko-sis-tem
habitat | hábitat | 🏞️ | já-bi-tat
endangered species | especies en peligro | 🐆
reforestation | reforestación | 🌳 | ri-fo-res-téi-shon
greenhouse gas | gas de efecto invernadero | 🏭
sea level | nivel del mar | 🌊
extreme weather | clima extremo | 🌪️
melting | derretimiento | 🧊
drought | sequía | 🏜️ | dráut
flooding | inundaciones | 🌊 | flá-ding
footprint | huella | 👣
offset | compensar | ⚖️ | óf-set
sustainable development | desarrollo sostenible | 🌍
climate action | acción climática | ✊
policy | política / medida | 📋 | pó-li-si
regulation | regulación | 📜 | re-giu-léi-shon
subsidy | subsidio | 💵 | sáb-si-di
incentive | incentivo | 🎯 | in-sén-tiv
be likely to | ser probable que | 📈
be bound to | ser casi seguro que | 🔒
It's up to us | Depende de nosotros | 🙌
make a difference | marcar la diferencia | ✨
future generations | generaciones futuras | 👶
""",
     extras=[
         D("Probabilidad y condiciones",
           "Mira cómo se expresa qué tan probable es algo y bajo qué condición.",
           """
Sea levels are likely to rise. || Es probable que suba el nivel del mar. || likely to
If we don't act, disasters are bound to increase. || Si no actuamos, es casi seguro que aumenten los desastres. || bound to
We can reduce emissions provided that governments invest. || Podemos reducir emisiones con tal de que los gobiernos inviertan. || provided that
We'll meet our goals as long as everyone helps. || Cumpliremos las metas siempre y cuando todos ayuden. || as long as
Unless we change, the planet will suffer. || A menos que cambiemos, el planeta sufrirá. || Unless
""",
           "¿Qué es más seguro: be likely to o be bound to?",
           ["be bound to (casi seguro)", "be likely to (casi seguro)"], 0,
           "be likely to = probable; be unlikely to = improbable; be bound to = casi seguro. Para condiciones: provided that / as long as = con tal de que, siempre y cuando; unless = a menos que. Todas van seguidas de presente, no de futuro.",
           """
Renewable energy is likely to become cheaper, provided that governments offer incentives. || Es probable que la energía renovable se abarate, con tal de que los gobiernos ofrezcan incentivos.
""",
           fills="""
Temperatures are ___ to rise this century. | likely / like | 0 | Es probable que las temperaturas suban este siglo.
We'll succeed ___ as everyone does their part. | as long / so long | 0 | Lo lograremos siempre y cuando todos hagan su parte.
___ we act now, the problem will get worse. | Unless / If | 0 | A menos que actuemos ya, el problema empeorará.
Electric cars are ___ to become more common. | bound / bind | 0 | Es casi seguro que los carros eléctricos se vuelvan más comunes.
"""),
         dialogue("¿Carro eléctrico?", "🔌 Dos amigos hablan de comprar carro.", """
Leo: I'm thinking of buying an electric car. || Estoy pensando en comprar un carro eléctrico.
Ana: Good idea. They're likely to be the norm in ten years. || Buena idea. Es probable que sean la norma en diez años.
Leo: But aren't they expensive? || ¿Pero no son caros?
Ana: A bit, but prices are bound to drop as long as demand keeps growing. || Un poco, pero los precios seguro bajarán siempre y cuando la demanda siga creciendo.
Leo: And charging? || ¿Y la carga?
Ana: It's getting easier, provided that the city builds more charging stations. || Cada vez es más fácil, con tal de que la ciudad construya más estaciones de carga.
"""),
         story("El pueblo que cambió", "🌞", """
A small town in the mountains used to depend entirely on fossil fuels for its energy. || Un pueblo pequeño en las montañas dependía totalmente de los combustibles fósiles para su energía.
The air was polluted and the electricity bills were high. || El aire estaba contaminado y las facturas de luz eran altas.
Then the mayor proposed an ambitious plan: to make the town run on renewable energy. || Entonces el alcalde propuso un plan ambicioso: que el pueblo funcionara con energía renovable.
With government subsidies, they installed solar panels on the roofs and a small wind farm on the hill. || Con subsidios del gobierno, instalaron paneles solares en los techos y un pequeño parque eólico en la loma.
They also started a recycling program and a community compost. || También empezaron un programa de reciclaje y un compostaje comunitario.
Five years later, the town's carbon footprint had dropped by seventy percent. "It's up to all of us to protect future generations," the mayor said. || Cinco años después, la huella de carbono del pueblo había bajado un setenta por ciento. "Depende de todos nosotros proteger a las generaciones futuras", dijo el alcalde.
""", questions=[
             ("¿De qué dependía el pueblo al principio?", ["De los combustibles fósiles", "De la energía solar", "Del carbón importado"], 0),
             ("¿Qué instalaron?", ["Paneles solares y un parque eólico", "Una fábrica", "Una represa grande"], 0),
             ("¿Cuánto bajó la huella de carbono?", ["Un 70 %", "Un 10 %", "Nada"], 0),
         ]),
         roleplay("Proponer una medida en el trabajo", "♻️ Propones reducir el plástico en tu oficina.", """
Boss: You wanted to propose something? || ¿Querías proponer algo?
+ Yes. We could reduce our plastic waste by using reusable cups. || Sí. Podríamos reducir nuestros residuos plásticos usando vasos reutilizables.
- Yes. We should use more single-use plastic. || Sí. Deberíamos usar más plástico de un solo uso. || Es lo contrario de reducir residuos.
Boss: Interesting. Would it be expensive? || Interesante. ¿Sería caro?
+ Not really. It'll save money as long as everyone uses their own cup. || No mucho. Ahorrará dinero siempre y cuando todos usen su propio vaso.
- Not really. It'll save money unless everyone helps. || No mucho. Ahorrará dinero a menos que todos ayuden. || "Unless" aquí dice lo contrario de lo que quieres.
Boss: Alright. What else do you suggest? || Bien. ¿Qué más sugieres?
+ A recycling program. It's likely to improve our image too. || Un programa de reciclaje. Es probable que también mejore nuestra imagen.
- A recycling program. It's bound to make a difference next century. || Un programa de reciclaje. Seguro marcará la diferencia el próximo siglo. || Exageradamente lejano.
"""),
     ],
     writes="""
Es probable que suba el nivel del mar. | Sea levels are likely to rise. | The sea level is likely to rise.
A menos que actuemos, el planeta sufrirá. | Unless we act, the planet will suffer.
Depende de nosotros proteger el planeta. | It's up to us to protect the planet. | It is up to us to protect the planet.
""",
     dictations="""
We can reduce emissions provided that governments invest. || Podemos reducir emisiones con tal de que los gobiernos inviertan.
Electric cars are bound to become more common. || Es casi seguro que los carros eléctricos se vuelvan más comunes.
""",
     speak="""
I think renewable energy is likely to be cheaper in the future. || Creo que es probable que la energía renovable sea más barata en el futuro.
""")

unit("u74-idioms", "B2", "Expresiones que usan los nativos", "💬",
     "Ya entiendo y uso expresiones idiomáticas comunes del inglés",
     "Idioms frecuentes por temas (tiempo, dinero, trabajo, emociones) que aparecen a diario.",
     grammar=["Idioms y su significado no literal"],
     items="""
once in a blue moon | muy de vez en cuando | 🌙
in the long run | a la larga | ⏳
around the clock | las 24 horas | 🕐
call it a day | dar por terminado el día | 🛑
beat around the bush | irse por las ramas | 🌳
get to the point | ir al grano | 🎯
piece of cake | pan comido | 🍰
a rip-off | un robo (muy caro) | 💸
cost an arm and a leg | costar un ojo de la cara | 💰
save for a rainy day | ahorrar para una emergencia | ☔
tighten your belt | apretarse el cinturón | 🔧
break the bank | gastar de más | 🏦
be in the red | estar en números rojos | 📉
pull your weight | hacer tu parte | 🏋️
go the extra mile | hacer un esfuerzo extra | 🏃
learn the ropes | aprender cómo se hace | 🪢
think outside the box | pensar diferente | 📦
on the same page | estar de acuerdo | 📄
a long shot | poco probable | 🎯
hit the nail on the head | dar en el clavo | 🔨
the ball is in your court | te toca a ti decidir | 🎾
bite off more than you can chew | abarcar más de lo que puedes | 🍔
burn the midnight oil | trasnochar trabajando | 🕯️
under the weather | con malestar | 🤒
on cloud nine | feliz de la vida | ☁️
down to earth | sencillo / realista | 🌍
a pain in the neck | un fastidio | 😤
get cold feet | arrepentirse / echarse para atrás | 🥶
spill the beans | revelar un secreto | 🫘
let the cat out of the bag | revelar un secreto | 🐈
a blessing in disguise | un mal que vino por bien | 🎁
when pigs fly | cuando las ranas críen pelo | 🐷
break a leg | mucha suerte (antes de actuar) | 🎭
hang in there | aguanta / no te rindas | 🪢
it's not rocket science | no es tan difícil | 🚀
read between the lines | leer entre líneas | 📖
the last straw | la gota que rebasó el vaso | 🥤
mixed feelings | sentimientos encontrados | ⚖️
speak of the devil | hablando del rey de Roma | 😈
better late than never | más vale tarde que nunca | ⏰
to make matters worse | para colmo de males | 😩
no pain, no gain | sin esfuerzo no hay recompensa | 💪
actions speak louder than words | las acciones valen más que las palabras | 🤝
the early bird catches the worm | al que madruga Dios lo ayuda | 🐦
""",
     extras=[
         D("Qué es un idiom",
           "El significado NO es literal. Lee el contexto y adivina el sentido.",
           """
Learning this app is a piece of cake. || Aprender esta app es pan comido. || piece of cake
That phone cost an arm and a leg. || Ese celular costó un ojo de la cara. || an arm and a leg
Don't beat around the bush, get to the point. || No te vayas por las ramas, ve al grano. || beat around the bush
Losing that job was a blessing in disguise. || Perder ese trabajo fue un mal que vino por bien. || a blessing in disguise
Hang in there, things will get better. || Aguanta, las cosas van a mejorar. || Hang in there
""",
           "¿Cómo se entiende un idiom?",
           ["Palabra por palabra", "Por su significado completo, no literal, con el contexto"], 1,
           "Un IDIOM es una expresión cuyo significado no se deduce palabra por palabra: 'it's a piece of cake' no habla de torta, significa 'es muy fácil'. Hay que aprenderlos como bloques. Son muy comunes en conversación, series y correos, así que entenderlos te acerca al nivel nativo.",
           """
I was nervous before the interview, but my friend said "break a leg!" and it went great. || Estaba nervioso antes de la entrevista, pero mi amigo me dijo "¡mucha suerte!" y me fue muy bien.
""",
           fills="""
This exercise is easy. It's a piece of ___. | cake / pie | 0 | Este ejercicio es fácil. Es pan comido.
That car costs an arm and a ___. | leg / foot | 0 | Ese carro cuesta un ojo de la cara.
Don't give up. Just ___ in there! | hang / stay | 0 | No te rindas. ¡Solo aguanta!
Stop beating around the ___ and tell me. | bush / tree | 0 | Deja de irte por las ramas y dime.
"""),
         tip("🎬", "Cómo aprender idioms", "No intentes memorizar listas. Apréndelos cuando los veas en una serie o canción, en su contexto. Y ojo: suenan raros si los usas demasiado. Un idiom bien puesto, de vez en cuando (once in a blue moon), suena natural."),
         dialogue("Charla de oficina", "☕ Dos colegas en el descanso.", """
Sara: You look tired. Everything OK? || Te ves cansado. ¿Todo bien?
Juan: I'm a bit under the weather, and to make matters worse, the deadline got moved up. || Estoy un poco indispuesto, y para colmo, adelantaron la fecha límite.
Sara: Oh no. Were you burning the midnight oil again? || Ay no. ¿Trasnochaste trabajando otra vez?
Juan: Yeah, but hey, no pain, no gain. The project is almost done. || Sí, pero bueno, sin esfuerzo no hay recompensa. El proyecto ya casi está.
Sara: You always go the extra mile. Let's call it a day and get some coffee. || Siempre haces el esfuerzo extra. Demos por terminado el día y vamos por un café.
Juan: Now you're speaking my language! || ¡Ahora sí hablamos el mismo idioma!
"""),
         story("La apuesta del abuelo", "🎲", """
When I told my grandfather I wanted to quit my job and start a business, he didn't laugh. || Cuando le dije a mi abuelo que quería renunciar a mi trabajo y empezar un negocio, no se rió.
"It's a long shot," he said, "but actions speak louder than words. Show me you're serious." || "Es poco probable", dijo, "pero las acciones valen más que las palabras. Demuéstrame que vas en serio."
For a year I burned the midnight oil, learning the ropes and saving every peso for a rainy day. || Por un año trasnoché trabajando, aprendiendo cómo se hacía y ahorrando cada peso para una emergencia.
At first sales were so slow that I almost got cold feet and gave up. || Al principio las ventas iban tan lentas que casi me eché para atrás y me rendí.
But I hung in there, and little by little the business grew. || Pero aguanté, y poco a poco el negocio creció.
On my grandfather's birthday, I gave him the first profit. "Better late than never," he smiled. "I knew you had it in you." || En el cumpleaños de mi abuelo, le di la primera ganancia. "Más vale tarde que nunca", sonrió. "Sabía que lo tenías en ti."
""", questions=[
             ("¿Qué le dijo el abuelo al principio?", ["Que era poco probable, pero que demostrara con acciones", "Que era imposible", "Que no lo hiciera"], 0),
             ("¿Qué casi hace el narrador cuando las ventas iban lentas?", ["Echarse para atrás y rendirse", "Pedir un préstamo", "Mudarse"], 0),
             ("¿Qué le dio al abuelo en su cumpleaños?", ["La primera ganancia", "Un carro", "Una carta"], 0),
         ]),
         roleplay("Usar idioms naturalmente", "🎤 Tu amigo está nervioso antes de una presentación.", """
Friend: I'm so nervous about my presentation. What if I mess up? || Estoy muy nervioso por mi presentación. ¿Y si la riego?
+ Relax, you've practiced a lot. It's not rocket science. Break a leg! || Relájate, has practicado mucho. No es tan difícil. ¡Mucha suerte!
- Relax, break your leg literally. || Relájate, rómpete la pierna literalmente. || "Break a leg" es un idiom; no es literal.
Friend: Thanks. But the boss will be watching. He's a pain in the neck. || Gracias. Pero el jefe estará mirando. Es un fastidio.
+ Just hang in there. You've got this. || Solo aguanta. Tú puedes.
- Just spill the beans. || Solo revela el secreto. || No encaja con la situación.
Friend: You're right. Here goes nothing! || Tienes razón. ¡Allá voy!
+ Go get 'em. You'll do great. || Ve por ellos. Te va a ir genial.
- When pigs fly. || Cuando las ranas críen pelo. || Significa "nunca"; justo lo contrario de animarlo.
"""),
     ],
     writes="""
Ese celular cuesta un ojo de la cara. | That phone costs an arm and a leg.
A la larga, vale la pena. | In the long run, it's worth it. | In the long run, it is worth it. ; In the long run it's worth it.
No te vayas por las ramas. | Don't beat around the bush.
""",
     dictations="""
Learning this is a piece of cake. || Aprender esto es pan comido.
Hang in there, things will get better. || Aguanta, las cosas van a mejorar.
""",
     speak="""
Don't worry, it's not rocket science. You've got this! || No te preocupes, no es tan difícil. ¡Tú puedes!
""")
