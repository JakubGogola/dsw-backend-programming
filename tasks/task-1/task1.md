# Lista 1

Celem tej listy jest przećwiczenie wiedzy dotyczącej podstaw REST API z wykorzystaniem standardu OpenAPI oraz framework'a FastAPI dla języka Python.
Twoim zadaniem będzie wygenerowanie kodu serwera na podstawie załączonej specyfikacji, zaimplementowanie logiki dla wygenerowanych endpointów 
(na tym etapie używamy *mock'ów*) i przetestowanie czy API działa zgodnie z oczekiwaniami.

## Zadanie

1. Zapoznaj się ze specyfikacją Open API sklepu internetowego z kawą, która jest dostępna [tutaj](./coffee-shop-api-spec.yaml);
2. Przy pomocy narzędzia [OpenAPI Generator](https://openapi-generator.tech/docs/installation/) wugeneruj kod serwera. Poniżej znajdziesz polecenia konsolowe, które uruchomią generator przy użyciu Docker'a
```bash
docker pull openapitools/openapi-generator-cli

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/coffee-shop-api-spec.yaml \
    -g python-fastapi \
    -o /local/backend
```
3. Uruchom serwer przy pomocy narzędzia Docker. Pamiętaj, aby *wejść* w konsoli w katalogu `/backend`, w którym znajduje się wygenerowany kod, a następnie użyj polecenia:
```bash
docker compose up --build
```
4. Zaimplementuj proste REST API odpowiednio dopisując logikę dla każdego z endpoint'ów w pliku znajdującym się w katalogu `/src/openapi_server/apis/coffees_api.py`. Serwer jest pod URL'em `http://0.0.0.0:8080`. Może się zdarzyć, że po dokonaniu zmian w kodzie koniecznie będzie zresetowanie serwera. Możesz to zrobić używając kombinacji klawiszy `Ctrl + C`, a gdy kontener zostanie zniszczony możesz ponownie uruchomić serwer korzystając z polecenia dostępnego w punkcie 3.
5. Przetestuj czy Twoje API działa poprawnie wykorzystując interaktywną dokumentacją dostępną pod adresm `http://0.0.0.0:8080/docs`.