# Testausharjoitus: lippuhinnat

Harjoituksessa testataan `lippu.py`-moduulia pytestillä. Osa A tehdään kerralla 1
(yksikkötestaus) ja osa B kerralla 2 (jatkuva integraatio, pareittain).

## Vaatimukset

| Ikä                   | Lippu        | Hinta        |
| ---                   | ---          | ---          |
| 0–6                   | ilmainen     | 0 €          |
| 7–17                  | lapsi        | 8 €          |
| 18–64                 | aikuinen     | 15 €         |
| 65–120                | eläkeläinen  | 10 €         |
| alle 0 tai yli 120    | virheellinen | `ValueError` |

Ryhmälle (vähintään 10 lippua) myönnetään 10 % alennus kokonaishinnasta.

## Valmistelu

```bash
python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Tuloksen pitäisi olla `1 passed, 1 skipped`.

## Osa A – yksikkötestaus (kerta 1, 30 min)

### Tehtävä 1: ekvivalenssiluokat ja raja-arvot

äydennä taulukko ennen koodaamista. Ekvivalenssiluokka on joukko syötteitä,
joita ohjelman pitäisi käsitellä samalla tavalla. Raja-arvot ovat luokkien reunoilla.

| Ekvivalenssiluokka | Esimerkkiarvo   | Raja-arvot    | Odotettu tulos  |
| ---                | ---             | ---           | ---             |
| liian pieni ikä    |     -10         | -1            | Virhe           |
| 0–6                |      2          | 0 ja 6        | 0€              |
| 7–17               |      8          | 7 ja 17       | 8,00€           |
| 18–64              |      20         | 18 ja 64      | 15,00€          |
| 65–120             |      70         | 65 ja 120     | 10,00€          |
| liian suuri ikä    |      127        | 121           | Virhe           |

### Tehtävä 2: raja-arvot parametrisoituna

Täydennä `test_lippuhinta_raja_arvot` tiedostossa `test_lippu.py` niin, että
jokainen kelvollinen raja-arvo on mukana. Poista rivi `@pytest.mark.skip` ja aja `pytest`.

**Löysitkö virheen?** Kirjoita ylös: millä syötteellä, mikä oli odotettu tulos
ja mikä todellinen tulos. Älä korjaa virhettä vielä.

### Tehtävä 3: virheelliset syötteet

Kirjoita testi, joka varmistaa, että iät `-1` ja `121` nostavat `ValueError`in.

```python
with pytest.raises(ValueError):
    lippuhinta(-1)
    lippuhinta(121)
```

### Tehtävä 4: kokonaishinta

Testaa `kokonaishinta`-funktiota vähintään näillä:

- tyhjä lista
- 9 aikuista (ei alennusta)
- 10 aikuista (alennus)

### Tehtävä 5: kattavuus

```bash
pytest --cov=lippu --cov-report=term-missing
```

Onko jokin rivi testaamatta (sarake `Missing`)? Lisää tarvittaessa testi.

### Tehtävä 6: korjaa virhe

Korjaa tehtävässä 2 löytämäsi virhe `lippu.py`-tiedostosta ja aja testit uudelleen.
Kaikkien testien pitää mennä läpi.

### Bonus: staattinen analyysi

```bash
pip install ruff
ruff check .
```

## Osa B – jatkuva integraatio (kerta 2, pareittain, 20 min)

Säilössä on valmiina työnkulku `.github/workflows/testit.yml`, joka ajaa testit
GitHubissa jokaisesta pushista ja pull requestista.

1. **A** luo GitHubiin tyhjän säilön ja vie sinne oman, korjatun versionsa osasta A.
   Tarkista Actions-välilehdeltä, että ajo on vihreä.
2. **A** kutsuu **B**:n säilöön (Settings → Collaborators). **B** hyväksyy kutsun ja kloonaa säilön.
3. Uusi vaatimus: *18–64-vuotias opiskelija maksaa 10 €.*
   **B** luo haaran `feature/opiskelija` ja kirjoittaa **ensin testin** uudelle vaatimukselle
   (esim. `lippuhinta(20, opiskelija=True) == 10.0`). B pushaa haaran ja avaa pull requestin.
   CI on punainen, koska toteutus puuttuu.
4. **B** toteuttaa vaatimuksen `lippu.py`-tiedostoon ja pushaa. CI muuttuu vihreäksi.
5. **A** katselmoi pull requestin, kommentoi ja yhdistää sen.
6. Bonus: vaihtakaa rooleja. Uusi vaatimus: *jos ostoksessa on alle 7-vuotias, siinä on oltava
   myös vähintään yksi 18 vuotta täyttänyt* (muuten `kokonaishinta` nostaa `ValueError`in).
