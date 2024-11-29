# Przemysław Oneksiak, s34225

Jest to finalna wersja mini-projektu na zajęcia PAD. 
Celem tego projektu było porównanie cen kawy znajdującej się na trzech popularnych serwisach internetowych: 

https://coffeecave.pl/  
https://www.przyjacielekawy.pl/  
https://www.konesso.pl/

Przy pomocy bibliotek:  
pandas  
scrapy  
matplotlib  
Ich pełne wersje znajdują się w pliku **requirements.txt**

Dla każdej z tych stron napisana została oddzielna klasa dziedzicząca po scrapy.Spider - wszystkie znajdują się w 
podkatalogu **/spiders**. W celu wyczyszczenia pobranych danych w podkatalogu **/notebooks** powstały pliki **%cleaner.ipynb** 
służące do przetworzenia oraz normalizacji danych. Klasy Spiders zostały uruchomione w tychże plikach, a pobrane wyniki
(pliki **output_nazwa_strony.csv**) zapisane zostały w podkatalogu **/scrapped_pages**. Dane zostały przetworzone przez funkcje 
im dedykowane oraz za pośrednictwem wyrażeń regularnych (pakier **re**). Z uwagi na zróznicowaną postać pobranych danych
funkcje zostały napisane bezpośrednio w notatnikach, a nie w osobnych plikach .py - z uwagi na znikome możliwości ich 
dalszego powielenia i wykorzystania. Końcowym etapem procesu czyszczenia było zapisanie plików z gotowymi danymi do
wizualizacji w podkatalogu **/cleaned_data**.

Finalnym elementem projektu była wizualizacja oraz wnioskowanie z przygotowanych danych. Odbyło się to w pliku
**plotter_final.ipynb**, który znajduje się w podkatalogu **/notebooks**. Zawiera on trzy wykresy przedstawiające zakres cen 
dla poszczególnych stron internetowych oraz wykres przedstawiający średnie obniżki cen, z uwagi na zbliżające się wydarzenie
**Black Friday**. Przedstawione zostały one jedynie na stronach **konesso** oraz **przyjacielekawy**, ponieważ **CoffeeCave**
nie informuje klientów o rabatach. Funkcje które zostały wykorzystane do tworzenia wykresów przy użyciu biblioteki 
matplotlib zostały umieszczone w pliku **helpers.py**, sugerując się ich potencjałem do wykorzystania w wielu miejsach w 
projekcie. 

Wnioski:
- Średnio najtańszą stroną jest https://www.przyjacielekawy.pl/
- Średnio najdroższą stroną jest https://coffeecave.pl/  
- Najtańszy produkt znajduje się w https://www.konesso.pl/ - jest to LaCava Limy Nitro Cold Bru 200ml, kosztująca 7.19
- Najdroższy produkt znajduje się w https://www.konesso.pl/ - jest to ZESTAW 6x Kawa ziarnista Bazzara DODICIGRANCRU, kosztujący 780.54
- Średnia obniżka cen związana z Black Friday jest większa na stronie https://www.konesso.pl/ niż na https://www.przyjacielekawy.pl/
- Największą ilość artykułów można znaleźc na https://www.konesso.pl/, a najmniejszą na https://coffeecave.pl/  
- Na stronie https://coffeecave.pl/ posiada każdy rodzaj kawy w dwóch rodzajach - ziearnistej oraz mielonej



