#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import warnings


def test():
    # Benutzerdefinierte Warnung
    warnings.warn("Warungstext", DeprecationWarning)


# Warnungen werden normalerweise nicht angezeigt
test()

# Warnings Filter: https://docs.python.org/3.6/library/warnings.html#the-warnings-filter
# Mit warnings.simplefilter("always") kann man die Anzeige der Warnungen aktivieren
warnings.simplefilter("always")
test()
print()

# Mit warnings.simplefilter("ignore") kann man die Anzeige der Warnungen deaktivieren
warnings.simplefilter("ignore")
test()

# Mit warnings.simplefilter("error") zum Error hochstufen
warnings.simplefilter("error")

try:
    test()
except:
    print('Error')
