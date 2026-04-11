import unicodedata

texto_normalizado = unicodedata.normalize('NFKD', "pré texto")

print(''.join([c for c in texto_normalizado if not unicodedata.combining(c)]))