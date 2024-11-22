# TAU  ZJAZD2

 Empik

    Otwarcie strony Empik
        Działanie: Otwórz stronę główną Empik (https://www.empik.com/) w przeglądarce i ustaw maksymalny rozmiar okna.

    Weryfikacja poprawności URL strony
        Działanie: Sprawdź, czy URL otwartej strony to dokładnie „https://www.empik.com/”.
        Wynik: Jeśli URL jest niepoprawny, test zgłasza błąd.

    Sprawdzenie tytułu strony
        Działanie: Sprawdź, czy tytuł strony zawiera słowo „Empik”.
        Wynik: Test zgłasza błąd, jeśli tytuł nie zawiera oczekiwanej frazy.

    Weryfikacja widoczności nagłówka strony
        Działanie: Znajdź element <header> i sprawdź, czy jest widoczny.
        Wynik: Test zgłasza błąd, jeśli nagłówek nie jest widoczny na stronie.

    Akceptacja cookies
        Działanie: Spróbuj znaleźć i kliknąć przycisk akceptacji cookies, jeśli jest widoczny i klikalny.
        Wynik: Jeśli przycisk nie istnieje lub nie można go kliknąć, zgłoszenie błędu jest wypisywane do konsoli.

    Weryfikacja widoczności pola wyszukiwania
        Działanie: Znajdź pole wyszukiwania (klasa css-1sobvo3) i sprawdź, czy jest widoczne.
        Wynik: Jeśli pole wyszukiwania nie jest widoczne, test zgłasza błąd.

    Wyszukiwanie frazy "SQL"
        Działanie: Wpisz „SQL” w pole wyszukiwania i naciśnij Enter.
        Wynik: Oczekuje się, że strona zostanie przekierowana na wyniki wyszukiwania dla frazy „SQL”.

    Sprawdzenie wyników wyszukiwania
        Działanie: Sprawdź, czy na stronie wyników wyszukiwania jest widoczny obrazek oraz co najmniej jeden link.
        Wynik: Test zgłasza błąd, jeśli nie znajdzie żadnego obrazka lub linku.

    Sprawdzenie widoczności przycisku "Biznes"
        Działanie: Sprawdź, czy widoczny jest przycisk z tekstem „Biznes” i kliknij go.
        Wynik: Jeśli przycisk jest niewidoczny lub nie klika się, test zgłasza błąd.

    Test w różnych przeglądarkach
        Działanie: Uruchom powyższy scenariusz testowy w przeglądarkach Chrome, Edge oraz Firefox.
        Wynik: Test zamyka każdą przeglądarkę po zakończeniu, niezależnie od wyniku testu.


  Google

Otwarcie strony Google

    Działanie: Otwórz stronę https://www.google.com i ustaw maksymalny rozmiar okna przeglądarki.
    Oczekiwany wynik: Strona Google jest otwarta, a okno przeglądarki zajmuje cały ekran.

Akceptacja cookies

    Działanie: Znajdź przycisk akceptacji cookies o ID L2AGLb i kliknij go.
    Oczekiwany wynik: Jeśli przycisk akceptacji cookies jest widoczny i klikalny, zostaje kliknięty, a strona przechodzi do stanu gotowego do użycia.

Weryfikacja tytułu strony Google

    Działanie: Sprawdź, czy tytuł strony zawiera słowo „Google”.
    Oczekiwany wynik: Tytuł strony powinien zawierać słowo „Google”.

Wpisanie zapytania do pola wyszukiwania

    Działanie: Znajdź pole wyszukiwania (nazwa pola q), wpisz frazę „Selenium” i naciśnij Enter, aby rozpocząć wyszukiwanie.
    Oczekiwany wynik: Wyszukiwanie dla frazy „Selenium” rozpoczyna się i pojawiają się wyniki.

Weryfikacja wyników wyszukiwania

    Działanie: Sprawdź, czy wyniki wyszukiwania zawierają słowo „Selenium”.
    Oczekiwany wynik: Strona wyników wyszukiwania powinna zawierać frazę „Selenium” w wynikach lub opisie.

Kliknięcie w pierwszy wynik wyszukiwania

    Działanie: Znajdź pierwszy widoczny wynik wyszukiwania (element h3) i kliknij go, aby przejść do strony Selenium.
    Oczekiwany wynik: Przeglądarka przechodzi na stronę Selenium po kliknięciu pierwszego wyniku.

Weryfikacja tytułu strony Selenium

    Działanie: Sprawdź, czy tytuł otwartej strony zawiera słowo „Selenium”.
    Oczekiwany wynik: Tytuł strony Selenium powinien zawierać słowo „Selenium”.

Weryfikacja obecności obrazka na stronie Selenium

    Działanie: Znajdź na stronie Selenium dowolny element obrazka (znacznik img) i sprawdź, czy jest widoczny.
    Oczekiwany wynik: Na stronie powinien być widoczny co najmniej jeden obrazek.

Sprawdzenie zawartości strony Selenium

    Działanie: Upewnij się, że strona zawiera tekst „Selenium”.
    Oczekiwany wynik: W kodzie strony powinna występować fraza „Selenium”.

Weryfikacja widoczności nawigacji (navbar)

    Działanie: Znajdź element nawigacji z ID main_navbar i sprawdź, czy jest widoczny.
    Oczekiwany wynik: Element nawigacji powinien być widoczny na stronie.

Weryfikacja widoczności stopki

    Działanie: Znajdź element stopki (znacznik footer) i sprawdź, czy jest widoczny.
    Oczekiwany wynik: Stopka powinna być widoczna na stronie.

Sprawdzenie przycisku do dokumentacji

    Działanie: Znajdź przycisk „Documentation” i sprawdź, czy jest widoczny, a następnie kliknij, aby przejść do strony dokumentacji.
    Oczekiwany wynik: Przycisk „Documentation” powinien być widoczny i dostępny do kliknięcia, co przekierowuje do odpowiedniej sekcji dokumentacji.

Uruchomienie testu w różnych przeglądarkach

    Działanie: Przeprowadź powyższy scenariusz testowy w przeglądarkach Chrome, Firefox oraz Edge.
    Oczekiwany wynik: Test zakończy się sukcesem we wszystkich przeglądarkach lub zgłosi błędy dla elementów, które nie spełniają oczekiwań.


   
  OpenMRS

    Otwarcie strony logowania OpenMRS
        Działanie: Otwórz stronę https://demo.openmrs.org/openmrs/login.htm i ustaw maksymalny rozmiar okna przeglądarki.
        Oczekiwany wynik: Strona logowania OpenMRS jest otwarta, a okno przeglądarki zajmuje cały ekran.

    Logowanie do systemu
        Działanie: Wprowadź nazwę użytkownika admin, hasło Admin123, wybierz lokalizację Inpatient Ward i kliknij przycisk logowania.
        Oczekiwany wynik: System loguje użytkownika na stronie głównej aplikacji.

    Nawigacja do zakładki „Register a Patient”
        Działanie: Kliknij przycisk „Register a Patient”, aby przejść do formularza rejestracji pacjenta.
        Oczekiwany wynik: Strona rejestracji pacjenta jest widoczna i gotowa do wprowadzenia danych.

    Wprowadzenie imienia i nazwiska pacjenta
        Działanie: W polu „Given Name” wpisz „Test” oraz w polu „Family Name” wpisz „Patient”, a następnie kliknij przycisk „Next”.
        Oczekiwany wynik: Imię i nazwisko są wprowadzone poprawnie, a system przechodzi do następnego kroku.

    Wprowadzenie płci pacjenta
        Działanie: Wybierz „Male” jako płeć pacjenta i kliknij przycisk „Next”.
        Oczekiwany wynik: Płeć jest wprowadzona poprawnie, a system przechodzi do kroku wprowadzenia daty urodzenia.

    Wprowadzenie daty urodzenia pacjenta
        Działanie: Wprowadź dzień 01, miesiąc January i rok 1990, a następnie kliknij przycisk „Next”.
        Oczekiwany wynik: Data urodzenia jest poprawnie zapisana, a system przechodzi do kroku wprowadzenia adresu.

    Wprowadzenie adresu pacjenta
        Działanie: W polu „Address” wpisz „123 Main Street” i kliknij przycisk „Next”.
        Oczekiwany wynik: Adres pacjenta jest wprowadzony, a system przechodzi do kroku wprowadzenia numeru telefonu.

    Wprowadzenie numeru telefonu pacjenta
        Działanie: W polu „Phone Number” wpisz „123456789” i kliknij przycisk „Next”.
        Oczekiwany wynik: Numer telefonu pacjenta jest poprawnie zapisany, a system przechodzi do następnego kroku rejestracji.

    Weryfikacja danych pacjenta i zakończenie rejestracji
        Działanie: Zatwierdź dane i zakończ proces rejestracji pacjenta, przechodząc przez wszelkie pozostałe kroki formularza.
        Oczekiwany wynik: Pacjent zostaje pomyślnie zarejestrowany, a system wyświetla potwierdzenie rejestracji.

    Zakończenie testu
        Działanie: Zamknij przeglądarkę po zakończeniu testu.
        Oczekiwany wynik: Przeglądarka zamyka się, kończąc test.

Wikipedia

Otwarcie strony głównej Wikipedii

    Działanie: Otwórz stronę https://pl.wikipedia.org/wiki/Wikipedia:Strona_główna i ustaw maksymalny rozmiar okna przeglądarki.
    Oczekiwany wynik: Strona główna Wikipedii jest otwarta, a przeglądarka jest w trybie pełnoekranowym.

Weryfikacja tytułu strony

    Działanie: Sprawdź, czy tytuł strony zawiera słowo „Wikipedia”.
    Oczekiwany wynik: Tytuł strony zawiera „Wikipedia”, co oznacza, że użytkownik jest na właściwej stronie.

Weryfikacja obecności „Strona główna” na stronie

    Działanie: Sprawdź, czy na stronie widnieje tekst „Strona główna”.
    Oczekiwany wynik: Na stronie jest widoczna fraza „Strona główna”, co potwierdza prawidłowe załadowanie strony głównej.

Weryfikacja widoczności pola wyszukiwania

    Działanie: Upewnij się, że pole wyszukiwania jest widoczne na stronie.
    Oczekiwany wynik: Pole wyszukiwania jest widoczne i dostępne do wpisania tekstu.

Wyszukiwanie hasła „Selenium”

    Działanie: Wpisz „Selenium” w polu wyszukiwania i naciśnij klawisz Enter.
    Oczekiwany wynik: Wyniki wyszukiwania zawierają hasło „Selenium”, a użytkownik jest przekierowany na stronę wyników wyszukiwania.

Sprawdzenie widoczności linku do artykułu o Selenium

    Działanie: Upewnij się, że na stronie widoczny jest link do artykułu „Selenium”.
    Oczekiwany wynik: Link do artykułu „Selenium” jest widoczny, co pozwala na przejście do pełnego artykułu.

Weryfikacja obecności obrazka na stronie Selenium

    Działanie: Upewnij się, że strona wyników wyszukiwania lub artykuł zawiera obrazek.
    Oczekiwany wynik: Obrazek jest widoczny, co wskazuje na obecność elementów wizualnych na stronie.

Sprawdzenie widoczności stopki

    Działanie: Upewnij się, że stopka (footer) strony jest widoczna.
    Oczekiwany wynik: Stopka jest wyświetlona na dole strony, zawierając dodatkowe linki i informacje.

Sprawdzenie widoczności przycisku „Zaloguj się”

    Działanie: Upewnij się, że przycisk „Zaloguj się” jest widoczny w górnej części strony.
    Oczekiwany wynik: Przycisk „Zaloguj się” jest wyświetlony i widoczny.

Przejście na stronę logowania

    Działanie: Kliknij przycisk „Zaloguj się”.
    Oczekiwany wynik: Użytkownik zostaje przekierowany na stronę logowania.

Weryfikacja tytułu strony logowania

    Działanie: Sprawdź, czy tytuł strony zawiera frazę „Zaloguj się”.
    Oczekiwany wynik: Tytuł strony zawiera „Zaloguj się”, co potwierdza, że użytkownik znajduje się na stronie logowania.
