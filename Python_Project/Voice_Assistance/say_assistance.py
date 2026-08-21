import pyttsx3
import wikipedia

assistance = pyttsx3.init()
SearchBar = input("Search Here : ")
SearchResult = wikipedia.summary(SearchBar,sentences=2)
print(SearchResult)
assistance.say(SearchResult)
assistance.runAndWait()
