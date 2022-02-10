# -*- coding: utf-8 -*-
#!/usr/bin/env python

# importam sys per llegir i escriure a STDIN i STDOUT
import sys

# llegim les línies de STDIN (standard input)
for line in sys.stdin:
    # eliminem els espais en blanc del principi i final
    line = line.strip()
    # split de les línies a paraules
    words = line.split()
    # incrementem el contador
    for word in words:
        # write the results to STDOUT (standard output)
        print('%s\t%s' % (word, 1))
