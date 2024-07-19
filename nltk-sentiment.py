#analiza senytymentu z uyciem bilblioteki NLTK

import nltk
import nltk.sentiment
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

#nltk.download('vader_lexicon')

tekst = "Bardzo dobra zupa!"
analizator = nltk.sentiment.SentimentIntensityAnalyzer()

wynik = analizator.polarity_scores(tekst)
print(wynik)