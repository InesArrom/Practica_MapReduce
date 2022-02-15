import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.lower()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        # count was not a number, ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word

# output the last word
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
