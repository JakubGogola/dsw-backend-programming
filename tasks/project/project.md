# Projekt zaliczeniowy

Twoim zadaniem będzie stworzenie serwisu służącego do zarządzania **listą zakupów**. Powinien on udostępniać REST API zgodne z załączoną specyfikacją [OpenAPI](./open-api.yaml) i być oparty o framework [FastAPI](https://fastapi.tiangolo.com/):

| Metoda | Ścieżka | Opis |
|--------|---------|------|
| GET | /items | Pobranie wszystkich elementów |
| POST | /items | Utworzenie nowego elementu |
| GET | /items/:itemId | Pobranie elementu o określonym ID |
| PUT | /items/:itemId | Aktualizacja elementu o określonym ID |
| DELETE | /items/:itemId | Usunięcie elementu o określonym ID |

## Jak zacząć?

1. Wygeneruj kod serwisu używając generatora OpenAPI:
```shell
docker pull openapitools/openapi-generator-cli

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/open-api.yaml \
    -g python-fastapi \
    -o /local/backend
```

2. Zbuduj projekt:
```shell
docker compose build
```
3. Uruchom projekt:
```shell
docker compose up
```

## Wymagania na poszczególne oceny

### 3.0
* serwis implementuje logikę dla każdego z endpointów uwzględniając następujące wymagania:
  * poprawna walidacja wszystkich parametrów (danych) request'u *path, query string, body* oraz obsługa błędów walidacji (biblioteka [Pydantic](https://docs.pydantic.dev/latest/))
  * poprawna obsługa błędów, które mogą zostać rzucone podczas wykonywania kodu, np. element, który chcemy usunąć, o podanym ID nie istnieje
  * dane powinny być przechowywane w globalnej tablicy/obiekcie *(na ocenę 3.0 nie ma wymagania implementowania bazy danych)*
  
### 3.5
* wszystkie wymagania na ocenę 3.0
* dodanie funkcjonalności do endpointu `GET /items`: 
  * filtrowanie po parametrach: `name`, `category`, `purchased`
  * sortowanie po parametrach: `createdAt`, `updatedAt`

### 4.0
* wszystkie wymagania na ocenę 3.5
* implementacja bazy danych typu SQL (rekomendowany PostgreSQL):
  * dodanie kontenera udostępniającego instancję bazy danych, który łączy się w ramach wspólnej sieci *(network)* narzędzia Docker
  * użycie ORM-a [SQLAlchemy](https://www.sqlalchemy.org/)
  * poprawne zamodelowanie schematu bazy danych na poziomie kodu

### 4.5
* wszystkie wymagania na ocenę 4.0
* dodanie prostego uwierzytelnienia:
  * rozszerzenie API o endpointy `POST /register` oraz `POST /login`, które pozwalają na rejestrację oraz logowanie nowego użytkownika:
    * endpoint `POST /register` powinien przyjmować w body następujące parametry: `username`, `password`, `repeated_password`
    * endpoint `POST /login` powinien przyjmować w body następujące parametry: `username`, `password`
  * obsługa błędów rejestracji i logowania:
    * w endpoincie `POST /register` wszystkie pola muszą być niepuste, a hasła muszą się zgadzać
    * w endpoincie `POST /login` powinien być zwrócony błąd, jeżeli użytkownik o podanej nazwie i haśle nie istnieje

### 5.0
* wszystkie wymagania na ocenę 4.5
* dodanie zwracania tokenu autoryzacyjnego w formacie JWT do endpointu `POST /login`, który zawiera ID użytkownika
* dodanie autoryzacji do endpointów za pomocą tokena JWT:
  * każdy request powinien być walidowany pod kątem obecności nagłówka `Authorization: Bearer <token>` i w przypadku jego braku powinien być zgłaszany odpowiedni błąd
  * jeżeli token jest niepoprawny (nie zawiera wymaganych danych lub ID użytkownika nie istnieje w bazie), to powinien zostać zwrócony błąd

## Dodatkowe informacje
Przygotowane REST API powinno być możliwe do przetestowania za pomocą Swagger UI - narzędzia, które jest udostępniane przez framework FastAPI pod ścieżką `/docs`.

## Dodatkowe materiały

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Pydantic](https://docs.pydantic.dev/latest/)
* [JWT.IS](https://jwt.is/)
* [Lista metod HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
* [Lista błędów HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status)
