#import biblioteki do obsługi zapytania
import openai 

#nasz klucz API ze strony OPENAI
openai.api_key='YOUR_API_KEY' 

#pobranie zapytania od uzytkownika
#za pomocą natywnej funkcji INPUT
_prompt = input("Cześć jestem modelem OpenAI! Jak mogę Ci pomóc? ")

#funkcja główna
wynik = openai.ChatCompletion.create(
  #model którego będziemy uywać
  model="gpt-3.5-turbo",
  #treść zapytania do modelu i jej parametry
  messages=[
        {"role": "user", "content": _prompt}
    ]
)

#pobieramy wynik z odpowiedzi
#z pozycji nr 0 pobieramy wiadomość: message
#oraz jesj zawartość:content
_tekst_wyniku = wynik['choices'][0]['message']['content']

#wyświetlamy tekst wynikowy
print(_tekst_wyniku)