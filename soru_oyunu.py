sorular = ['Hangisi Kaymağı İle Ünlü Olan İlimizdir ?','Hangisi Dondurması İle Ünlü Olan İlimizdir ?',

'Hangisi Pidesi İle Ünlü Olan İlimizdir ?']

soru_1_cevaplar = ['A) Afyon','B) Mersin','C) Yozgat','D) Bursa']

soru_2_cevaplar = ['A) Denizli','B) Konya','C) KahramanMaraş','D) Eskişehir']

soru_3_cevaplar = ['A) Bursa','B) Konya','C) İstanbul','D) Ankara']

dogru_cevaplar = ['a','c','b']



def sor():

    puan = 0

    print('Soru 1:',sorular[0])

    for x in soru_1_cevaplar:

        print(x)

    cevap_1 = input('Cevabınız Nedir: ')

    if (cevap_1.lower() == dogru_cevaplar[0]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)

    

    print('Soru 2:',sorular[1])

    for x in soru_2_cevaplar:

        print(x)

    cevap_2 = input('Cevabınız Nedir: ')

    if (cevap_2.lower() == dogru_cevaplar[1]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap C Şıkkı.')

    print('-'*50)



    print('Soru 3:',sorular[2])

    for x in soru_3_cevaplar:

        print(x)

    cevap_3 = input('Cevabınız Nedir: ')

    if (cevap_3.lower() == dogru_cevaplar[2]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)

    print('Soru Oyunumuz Bitmiştir. Toplamda {} Soruya Doğru Cevap Verdiniz.'.format(puan))



sor()