# B2 · Parte 5 (unidades 102–103) — cierre del nivel

unit("u102-dinero-b2", "B2", "Dinero y finanzas personales", "🏦",
     "Ya manejo vocabulario de dinero, banco y gastos",
     "Vocabulario para hablar de dinero, el banco, ahorrar, gastar y las finanzas del día a día.",
     grammar=["Vocabulario temático"],
     items="""
cash | efectivo | 💵 | kash
coin | moneda | 🪙 | koin
bill (money) | billete | 💴 | bil
wallet | billetera | 👛 | uó-let
bank account | cuenta bancaria | 🏦
card (bank) | tarjeta | 💳
to withdraw | retirar (dinero) | 🏧 | uiz-dró
to deposit | depositar | 📥 | di-pó-sit
to transfer | transferir | 🔁 | tráns-fer
to borrow | pedir prestado | 🙏 | bó-rou
to lend | prestar | 🤲 | lend
to owe | deber (dinero) | 📌 | ou
debt | deuda | ⛓️ | det
loan | préstamo | 🏦 | loun
interest | interés | 📈 | ín-trest
to afford | poder permitirse | 💰 | a-fórd
to save up | ahorrar | 🐷
savings | ahorros | 💰 | séi-vings
to spend | gastar | 🛍️
to waste (money) | malgastar | 🗑️
expensive | caro | 💸
affordable | asequible | 👍 | a-fór-da-bol
to earn | ganar (dinero) | 💼 | ern
income | ingresos | 📥 | ín-kam
to charge | cobrar | 🧾
refund | reembolso | ↩️ | rí-fand
receipt | recibo | 🧾 | ri-síit
to budget | hacer un presupuesto | 📊
on a tight budget | con poco presupuesto | 🤏
bill (to pay) | factura / cuenta | 📄
fee | tarifa / comisión | 💲 | fii
rich | rico | 🤑
to be worth | valer | ⚖️
discount | descuento | 🏷️ | dís-kaunt
to go bankrupt | quebrar | 💥
currency | moneda (de un país) | 💱
to pay off | terminar de pagar | ✅
in debt | endeudado | ⛓️
to make a living | ganarse la vida | 💪
""",
     extras=[
         D("borrow vs. lend (prestar en dos direcciones)",
           "Las dos hablan de préstamos, pero desde lados opuestos.",
           """
Can I borrow your pen? || ¿Me prestas tu bolígrafo? (yo lo tomo) || borrow
I'll lend you my car. || Te presto mi carro. (yo lo doy) || lend
He borrowed money from the bank. || Pidió dinero prestado al banco. || borrowed
The bank lent him the money. || El banco le prestó el dinero. || lent
""",
           "Si YO tomo algo prestado de ti, uso…",
           ["lend", "borrow", "owe"], 1,
           "borrow = pedir prestado (yo recibo): 'I borrow from you'. lend = prestar (yo doy): 'I lend to you'. owe = deber: 'I owe you money'. En español 'prestar' sirve para los dos, por eso confunde.")
     ])

unit("u103-situaciones-b2", "B2", "Situaciones y reacciones", "💬",
     "Ya reacciono con naturalidad en conversaciones cotidianas",
     "Frases hechas para reaccionar, acordar, dudar o responder en situaciones del día a día.",
     grammar=["Expresiones de conversación"],
     items="""
It depends | depende | 🤔
I guess so | supongo que sí | 🤷
I'm not sure | no estoy seguro | 😕
Let me think | déjame pensar | 💭
That makes sense | eso tiene sentido | ✔️
Fair enough | me parece justo | 👌
No wonder | con razón | 💡
Good point | buen punto | 👍
I see what you mean | entiendo lo que dices | 👀
That's a relief | qué alivio | 😮‍💨
What a shame | qué lástima | 😞
Never mind | no importa / olvídalo | 🙃
It's up to you | tú decides | 🫵
Suit yourself | como quieras | 🤷
Take your time | tómate tu tiempo | ⏳
Hang on | espera un momento | ✋
By the way | por cierto | 💬
As I was saying | como decía | 🔁
To be honest | para ser sincero | 🫡
Come to think of it | ahora que lo pienso | 🤔
On second thought | pensándolo mejor | 💭
In any case | en todo caso | 📌
Either way | de cualquier forma | 🔀
Sort of | más o menos | 〰️
Kind of | algo así | 🙂
No way | de ninguna manera | 🚫
You bet | por supuesto / claro | 💯
I can't believe it | no puedo creerlo | 😲
That's too bad | qué mal | 😔
Good for you | me alegro por ti | 🎉
Well done | bien hecho | 👏
Cheer up | anímate | 🙂
Calm down | cálmate | 🧘
Watch out | cuidado | ⚠️
Go ahead | adelante | ➡️
Hold on a second | espera un segundo | ⏸️
I'd rather not | prefiero no hacerlo | 🙅
It's worth a try | vale la pena intentarlo | 🎯
Let's face it | admitámoslo | 😤
""",
     extras=[
         roleplay("Un amigo te cuenta un problema", "🗣️ Tu amigo está estresado por el trabajo. Responde con naturalidad.",
                  """
Friend: I'm so stressed about my job. || Estoy muy estresado por mi trabajo.
+ Take it easy, that sounds tough. || Tranquilo, eso suena difícil. || Reconoces su sentimiento con empatía.
- No big deal, forget it. || No es para tanto, olvídalo. || Suena frío y resta importancia a su problema.
- That's your problem. || Ese es tu problema. || Es brusco y poco empático.
Friend: Maybe I should look for another job. || Quizá debería buscar otro trabajo.
+ That makes sense. It's worth a try. || Eso tiene sentido. Vale la pena intentarlo. || Apoyas su idea de forma positiva.
- No way, don't do that. || De ninguna manera, no hagas eso. || Cierras la conversación sin escuchar.
""")
     ])
