"""Testit lippu.py-moduulille. Täydennä tehtävien mukaan (ks. README.md)."""

import pytest

from lippu import kokonaishinta, lippuhinta


def test_aikuisen_hinta():
    # Arrange: valmistellaan syöte
    ika = 30
    # Act: kutsutaan testattavaa funktiota
    hinta = lippuhinta(ika)
    # Assert: tarkistetaan tulos
    assert hinta == 15.0


# TEHTÄVÄ 2: Raja-arvot yhdellä parametrisoidulla testillä.
# Täydennä alla olevaan listaan pareja (ikä, odotettu hinta).
# Poista sen jälkeen rivi @pytest.mark.skip.

@pytest.mark.parametrize(
    "ika, odotettu",
    [
        (0, 0.0),
        (6, 0.0),
        (7, 8.0),
        (17, 8.0),
        (18, 15.0),
        (64, 15.0),
        (65, 10.0),
        (120, 10.0),
    ],
)
def test_lippuhinta_raja_arvot(ika, odotettu):
    assert lippuhinta(ika) == odotettu


# TEHTÄVÄ 3: Virheelliset iät nostavat ValueErrorin.
# Vinkki: with pytest.raises(ValueError):
@pytest.mark.parametrize("virheellinen_ika", [-1, 121])
def test_lippuhinta_virheellinen_ika(virheellinen_ika):
    with pytest.raises(ValueError):
        lippuhinta(virheellinen_ika)
# TEHTÄVÄ 4: Kokonaishinta ja ryhmäalennuksen raja (9 ja 10 lippua).


@pytest.mark.parametrize(
    "iat, odotettu_hinta",
    [
        ([], 0.0),
        ([20, 20, 20, 20, 20, 20, 20, 20, 20], 135),
        ([20, 20, 20, 20, 20, 20, 20, 20, 20, 20], 135),
    ],
)
def test_kokonaishinta(iat, odotettu_hinta):
    assert kokonaishinta(iat) == odotettu_hinta
