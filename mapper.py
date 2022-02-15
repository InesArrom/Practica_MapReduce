# importam sys per llegir i escriure a STDIN i STDOUT
from nltk.corpus import stopwords
import sys
import io
import re
import nltk
nltk.download('stopwords', quiet=True)

# signes que volem evitar
signs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Creem les stopwords dels idiomes que tenim en els llibres
stop_words = set(stopwords.words('catalan') + stopwords.words('spanish'))
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

for line in input_stream:
    # eliminem els espais en blanc del principi i final
    line = line.strip()
    line = re.sub(r'[^\w\s]', '', line)
    # convertim tot en minúscules
    line = line.lower()
    # sustituim els signes per espais
    for char in line:
        if char in signs:
            line = line.replace(char, " ")

    # De cada paraula comprovem que no sigui una stopword
    words = line.split()
    for word in words:
        if word not in stop_words:
            # primera lletra de la paraula
            letter = word[0:1]
            # si la lletra es troba a la llista farem el seu compteig
            if letter in list('abcdefghijklmnñopqrstuvwxyzç'):
                print('%s\t%s' % (letter, 1))
