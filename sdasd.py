# import re
#
# b = 'dupa(fdsf)dupa'
#
# pattern = '^ala$'
# # ^ - to jest curret
# text = 'ola ula i ala ma kota'
# # pierwszy sposób znajdź ala
# result = re.match(pattern, text)
# # Match sprawdza tylko czy cały tekst pasuje 1 do 1
#
# print(result)
#
# tekst = """Wyobraz sobie, ze ten tekst zawiera numer
# PIN 9434 twojej karty do bankomatu, a ty wlasnie go
# zapomniales. Jak szybko go odnalezc?"""
#
# sciezka = r'\d\d\d\d'
# dopasowanie = re.search(sciezka, tekst)
# print(dopasowanie)
#
# if dopasowanie:  # Sprawdzamy czy udalo sie cos znalezc
#     numer = dopasowanie.group()
#     print(numer)
