import io
import json

infile = io.open('aux1.txt', mode='r', encoding='utf-8')
text = infile.read()
infile.close()

practices = map(unicode.strip, text.split('----'))
practices_obj = {"practices": practices}

outfile = io.open('aux.json', mode='w+')
outfile.write(json.dumps(practices_obj, ensure_ascii=False))
outfile.close()
