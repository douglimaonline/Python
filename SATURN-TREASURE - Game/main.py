print('''
                                                                    ..;===+.
                                                                  .:=iiiiii=+=
                                                               .=i))=;::+)i=+,
                                                            ,=i);)I)))I):=i=;
                                                         .=i==))))ii)))I:i++
                                                       +)+))iiiiiiii))I=i+:'
                                  .,:;;++++++;:,.       )iii+:::;iii))+i='
                               .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                             ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                           ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                          ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                        ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                       ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                      ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                      =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                     +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                     =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                    .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                    :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                    :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                    .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                    =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                  +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
                +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
               =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
             +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
           :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
         .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
        ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
       +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
     .+=:))iiiiiiii)))+ii;
    .+=;))iiiiii)));ii+
   .+=i:)))))))=+ii+
  .;==i+::::=)i=;
  ,+==iiiiii+,
  `+=+++;`
''')
print("                          TESOURO DE SATURNO")
print("Olá pirata espacial...")
print("Missão 01: Localizar o lendário tesouro perdido em saturno.")



print ('''.........................................''')
print ("\n")
print ("Se aproximando de Saturno, seu radar indica um estranho sinal vindo de uma das 65 luas do planeta, Você vai checar?")
moon = input("(Y/N) ")

if moon.lower() == "y":
  print ("Sua nave estava muito veloz, você bateu na lua e explodiu fazendo um cogumelo de fogo visível da terra. GAME OVER!")
elif moon.lower() == "n":
  print ("Ao passar ao lado da lua você consegue ver que ela estava prestes a explodir. Você resolve acelerar para fugir do raio da explosão")
  mach = int(input ("Qual velocidade? (Mach: 10 a 1000) "))
  if mach > 10 and mach < 650:
    print ("O raio da explosão te alcançou, churrasquinho de astronauta assado a milanesa com molho barbecure, sal a gosto. GAME OVER!")
  elif mach >750:
    print ("Você perdeu o controle da nave e foi parar fora da galáxia. GAME OVER!")
  elif mach >=650 and mach <=750:
    print ("Você se aproxima de saturno e vê dois brilhos em pontos distintos, uma amarelo e outro branco.")
  
    shine = input ("Sua nave vai em direção a qual brilho? (A/B) ")
    if shine.lower() == "b":
      print ("O tesouro estava escondido em um baú com símbolos estranhos, agora ele esta em sua nave em direção a Terra. MISSÃO CUMPRIDA!")
    elif shine.lower() == "a":
      print ("Sua nave se chocou com um dos anéis de Saturno e você foi torrado. GAME OVER!")
    else:
          print ("Dados incorretos, você não é um verdadeiro astronauta, DISPENSADO. GAME OVER!")
  else:
    print ("Dados incorretos, você não é um verdadeiro astronauta, DISPENSADO. GAME OVER!")
else:
  print ("Dados incorretos, você não é um verdadeiro astronauta, DISPENSADO. GAME OVER!")