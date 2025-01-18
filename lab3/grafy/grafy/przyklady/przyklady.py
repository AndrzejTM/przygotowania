from graf.graf import Graf
from wizualizacja.wizualizacja import rysuj_graf


def infrastruktura_sieci():
    '''
    Węzły:
    - load balancer - rozdziela ruch między serwery aplikacyjne, równoważąc obciążenie systemu,
    - serwery aplikacji - dwa serwery, przetwarzające żądania użytkowników i współpracujące z bazą danych,
    - serwer Bazy Danych - przechowuje dane aplikacji dostępne dla obu serwerów aplikacyjnych,
    - klient mobilny i klient stacjonarny - użytkownicy aplikacji, łączący się odpowiednio przez urządzenia mobilne i komputery.

    Krawędzie:
    - klienci łączą się z load balancerem,
    - load balancer przesyła ruch do serwerów aplikacyjnych,
    - serwery aplikacyjne komunikują się z bazą danych.
    '''
    graf = Graf()
    graf.dodaj_wezel("Load Balancer")
    graf.dodaj_wezel("Serwer Aplikacji 1")
    graf.dodaj_wezel("Serwer Aplikacji 2")
    graf.dodaj_wezel("Serwer Bazy Danych")
    graf.dodaj_wezel("Klient Mobilny")
    graf.dodaj_wezel("Klient Stacjonarny")

    graf.dodaj_krawedz("Klient Mobilny", "Load Balancer", kierunek="S")
    graf.dodaj_krawedz("Klient Stacjonarny", "Load Balancer", kierunek="S")
    graf.dodaj_krawedz("Load Balancer", "Serwer Aplikacji 1", kierunek="N")
    graf.dodaj_krawedz("Load Balancer", "Serwer Aplikacji 2", kierunek="N")
    graf.dodaj_krawedz("Serwer Aplikacji 1", "Serwer Bazy Danych",
                       kierunek="S")
    graf.dodaj_krawedz("Serwer Aplikacji 2", "Serwer Bazy Danych",
                       kierunek="S")

    rysuj_graf(graf)
