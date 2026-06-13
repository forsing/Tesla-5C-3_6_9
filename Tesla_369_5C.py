"""
SRBIN Nikola Tesla, za sva vremena, najveci naucnik sveta.

SERBIAN Nikola Tesla, for all time, the greatest scientist in the world.
"""



"""
Tesla 5C - 21-piramidna konvergenciona geometrija.

  21 piramida, oko 4pi pokrivanja, solid angle 0.598 sr, 0.618 nesting,
  opcioni zlatni ugao 137.5 stepeni, tier raspodela 1-7 / 8-14 / 15-21.
"""


import numpy as np

from Tesla_5_common import (
    PIRAMIDA,
    MNOZIOCI,
    SOLID_ANGLE,
    ZLATNI_ODNOS_INV,
    ZLATNI_UGAO_RAD,
    fokusni_omotac,
    normalizuj_signal,
    izvod_polja,
    ispisi_i_snimi_model,
)

OSNOVA = "tesla_369_5C"


def simuliraj_5c(nx):
    x = np.linspace(0.0, 1.0, nx)
    s = np.zeros(nx)

    for n in range(PIRAMIDA):
        tier = n // 7
        m = MNOZIOCI[tier]
        ugao = n * ZLATNI_UGAO_RAD
        amp = SOLID_ANGLE * (ZLATNI_ODNOS_INV ** tier)
        sigma = 0.28 / (tier + 1)
        centar = 0.5 + 0.018 * np.cos(ugao)
        faza = ugao + 0.35 * np.sin(ugao)

        # Fokalni zbir: vektori se ponistavaju u centru, ali gradijent ostaje jak.
        sloj = amp * fokusni_omotac(x, sigma=sigma, centar=centar)
        s += sloj * np.sin(2.0 * np.pi * m * (n + 1) * x + faza)

    s = normalizuj_signal(s)
    e_x = izvod_polja(x, s)
    detalji = {
        "izvor": "harmonic_convergence_model.md",
        "piramida": PIRAMIDA,
        "solid_angle_po_piramidi": SOLID_ANGLE,
        "ukupni_solid_angle": f"{PIRAMIDA * SOLID_ANGLE:.3f}",
        "zlatni_ugao_stepeni": "137.5",
        "nesting": ZLATNI_ODNOS_INV,
    }
    return x, s, e_x, detalji


def main():
    ispisi_i_snimi_model(
        OSNOVA,
        "Tesla Scalar - GRUPA 5C / 21-piramidna konvergencija",
        simuliraj_5c,
        "Model koristi 21 geometrijski rasporedjen izvor i 0.618 slojeve.",
    )


if __name__ == "__main__":
    main()





"""
Slika talasa: /Tesla/tesla_369_5C.png
Slika talasa: /Tesla/tesla_369_5C.jpg

Tesla Scalar - GRUPA 5C / 21-piramidna konvergencija
CSV: /data/loto7hh_4632_k47.csv| Izvlacenja: 4632 | tezine: talas=0.7 freq=0.3
max S: 0.8712724739 | max |E_x|: 362.0546510572

Brojevi po kombinovanom skoru (tezinski talas + frekvencija):
  06  skor=0.8034482759  freq=0.02517  (pojava=816)
  08  skor=0.7561148444  freq=0.02810  (pojava=911)
  09  skor=0.6049138732  freq=0.02600  (pojava=843)
  34  skor=0.6040271126  freq=0.02692  (pojava=873)
  23  skor=0.5464946392  freq=0.02791  (pojava=905)
  02  skor=0.4997517635  freq=0.02544  (pojava=825)
  12  skor=0.4377203694  freq=0.02498  (pojava=810)
  22  skor=0.4225661609  freq=0.02625  (pojava=851)
  01  skor=0.4158339359  freq=0.02430  (pojava=788)
  37  skor=0.4066761044  freq=0.02652  (pojava=860)
  27  skor=0.4023824018  freq=0.02433  (pojava=789)
  03  skor=0.4001515472  freq=0.02547  (pojava=826)
  13  skor=0.3993970220  freq=0.02554  (pojava=828)
  07  skor=0.3982697328  freq=0.02603  (pojava=844)
  16  skor=0.3763680416  freq=0.02581  (pojava=837)
  26  skor=0.3730517528  freq=0.02680  (pojava=869)
  33  skor=0.3697627411  freq=0.02634  (pojava=854)
  10  skor=0.3572465516  freq=0.02606  (pojava=845)
  20  skor=0.3486633971  freq=0.02375  (pojava=770)
  11  skor=0.3375407079  freq=0.02655  (pojava=861)
  28  skor=0.3275501584  freq=0.02532  (pojava=821)
  18  skor=0.3215881860  freq=0.02532  (pojava=821)
  38  skor=0.3140821299  freq=0.02597  (pojava=842)
  14  skor=0.3070301513  freq=0.02495  (pojava=809)
  35  skor=0.3063367729  freq=0.02600  (pojava=843)
  24  skor=0.3052220700  freq=0.02591  (pojava=840)
  31  skor=0.3011446154  freq=0.02560  (pojava=830)
  25  skor=0.2520973675  freq=0.02591  (pojava=840)
  21  skor=0.2186799963  freq=0.02551  (pojava=827)
  15  skor=0.2057117012  freq=0.02461  (pojava=798)
  32  skor=0.2048090387  freq=0.02643  (pojava=857)
  04  skor=0.1962302563  freq=0.02504  (pojava=812)
  19  skor=0.1781363520  freq=0.02510  (pojava=814)
  29  skor=0.1761424712  freq=0.02618  (pojava=849)
  39  skor=0.1717241379  freq=0.02618  (pojava=849)
  17  skor=0.1534194666  freq=0.02362  (pojava=766)
  30  skor=0.1456489166  freq=0.02427  (pojava=787)
  36  skor=0.1434047216  freq=0.02424  (pojava=786)
  05  skor=0.1373758470  freq=0.02554  (pojava=828)

Predlozene kombinacije (rangirane po skoru kombinacije):
  01. 06 08 09 18 20 22 30  skor_komb=3.4029436542
  02. 06 08 12 18 22 29 31  skor_komb=3.2187249232
  03. 08 09 18 26 27 33 38  skor_komb=3.1418959291
  04. 06 10 12 23 24 28 31  skor_komb=3.0788266798
  05. 01 03 07 09 10 16 38  skor_komb=2.8668658121
  06. 01 08 16 20 28 31 38  skor_komb=2.8397571227
  07. 08 16 20 24 28 37 38  skor_komb=2.8346767458
  08. 03 04 06 20 24 27 35  skor_komb=2.7624347211
  09. 05 08 09 13 29 31 33  skor_komb=2.7448514144
  10. 12 13 16 21 25 36 39  skor_komb=1.9993916563

Sacuvano: /Tesla/tesla_369_5C.txt
"""



"""
Analiza Tesla_369_5C.py
Tesla_369_5C.py je geometrijski konvergencioni motor. 
Dok 5B radi sa fazom i senzorima, 5C radi sa prostornim rasporedom 21 piramide. 

Glavni princip je prostorna konvergencija mnogo izvora ka jednoj tački.

21 piramida je raspoređena sferno, sa vrhovima usmerenim ka centru, 
tako da zajedno pokrivaju skoro ceo prostorni ugao 4π. 

Ključni pojmovi:
solid angle 0.598 sr po piramidi → 21 x 0.598 ≈ 12.56 sr ≈ 4π
zlatni ugao 137.5° za ravnomeran raspored (filotaksija)
nesting 0.618 (inverzni zlatni odnos) za slabljenje viših slojeva
tier raspodela: piramide 1-7, 8-14, 15-21 dobijaju 3, 6, 9

Ovo je model vektorske harmonijske interferencije, gde se mnogo izvora sabira, 
vektori se delimično poništavaju u centru, ali gradijent (E_x) ostaje jak. 
To je opisano kao „skalarni čvor”.

Funkcija simuliraj_5c(nx) prolazi kroz 21 piramidu i svaku tretira kao zaseban izvor.

Za svaku piramidu n:
tier = n // 7 → određuje da li pripada grupi 3, 6 ili 9
ugao = n x 137.5° → pozicija po zlatnom uglu
amp = 0.598 x

Tier raspodela 3/6/9
Prva trećina piramida nosi 3, druga 6, treća 9. 
Tako se 3-6-9 izražava kroz geometriju, a ne kroz jedan talas.

Zlatni ugao 137.5°
Svaka piramida je zarotirana za zlatni ugao. 
To daje ravnomeran, neponavljajući raspored faza i centara.

Nesting 0.618
Viši tier dobija manju amplitudu (0.618, 0.618²), 
kao u ugnježdenim šupljinama.

Promenljiv centar fokusa
Svaka piramida ima blago pomeren centar omotača. 
To simulira da izvori gledaju ka centru iz različitih pravaca.

Različita frekvencija po piramidi
m · (n+1) znači da svaka piramida ima svoju efektivnu frekvenciju, 
pa je polje bogatije i manje pravilno.

Zajednički pipeline
Skor, frekvencija, kombinacije i slike rade se kroz Tesla_5_common.py.

5C pokriva geometriju i prostorni raspored:

5 + 5A + 5B + 5C + 5D + 5E -> Tesla_5final.py

Za razliku od ostalih, 5C nema „čist” centriran talas. 
Zato je max S = 0.871 i max |E_x| = 362, što je niže od drugih modela 
— polje je razuđenije jer dolazi iz 21 različito postavljenog izvora.

Kratka Analiza Rezultata
Top 10 za 5C:
06, x, 09, y, 23, z, 12, x, 01, 37

Predlozene kombinacije (rangirane po skoru kombinacije):
  01. 06 x 09 y 20 z 30  skor_komb=3.4029436542

Ovde je veliko iznenađenje broj 06 na prvom mestu, 
koga nije bilo u vrhu kod 5, 5A ni 5B. 
Takođe se javljaju 34, 01, 27 kojih nema u vrhu drugih modela. 
To znači da geometrijski model daje najrazličitiji signal u grupi 5 do sada 
— dobro za raznovrsnost u 5final.
"""




"""
source ~/tesla_env/bin/activate

Bitne verzije za tesla_env:

Paket	Verzija
python  3.11.13
numpy   2.2.6
scipy   1.15.3
pandas  3.0.3
matplotlib    3.10.9
k-Wave-python 0.6.2
pycharge      2.0.1
jax        0.10.1
jaxlib     0.10.1
jaxtyping  0.3.7
equinox    0.13.8
lineax     0.1.1
optimistix 0.1.0
ml-dtypes
(uz jax)
opencv-python 4.13.0.92
h5py          3.16.0
"""
