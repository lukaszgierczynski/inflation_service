Aplikacja internetowa napisana w języku Python przy użyciu framework'a Django. Przed uruchomieniem aplikacji konieczne jest zainstalowanie
bibliotek znajdujących się w pliku requirements.txt.

Celem aplikacji jest generowanie wykresów obrazujących przebieg inflacji w Polsce w ostatnich latach. Dane potrzebne do tworzenia wykresów
pobierane są przy użyciu biblioteki requests z zewnętrznego REST API udostępnionego przez Główny Urząd Statystyczny. Wykresy powstają
z wykorzystaniem biblioteki plotly.

Aplikacja umożliwia użytkownikowi tworzenie trzech różnych wykresów, które przypisane są do trzech różnych endpointów. W pierwszym z nich
użytkownik może stworzć wykres z przebiegiem ogólnej inlfacji w określonym przedziale czasowym, w drugim - wykres z przebiegiem inflacji
w poszczególnych kategoriach towarów i usług, a w trzecim - wykres z przebiegiem własnej inflacji ustalonej na podstawie wag wydatków
użytkownika w poszczególnych kategoriach.

Technologie: Python, Django, REST API, requests, plotly, HTML, CSS
