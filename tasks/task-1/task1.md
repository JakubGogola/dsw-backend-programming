# Lista 1

Celem tej listy jest przećwiczenie wiedzy dotyczącej podstaw REST API z wykorzystaniem standardu OpenAPI oraz frameworka FastAPI dla języka Python. 
Twoim zadaniem będzie wygenerowanie kodu serwera na podstawie załączonej specyfikacji, zaimplementowanie logiki dla wygenerowanych endpointów 
(na tym etapie używamy *mocków*) i przetestowanie, czy API działa zgodnie z oczekiwaniami.

## Zadanie

1. Zapoznaj się ze specyfikacją OpenAPI sklepu internetowego z kawą, która jest dostępna [tutaj](./coffee-shop-api-spec.yaml);
2. Przy pomocy narzędzia [OpenAPI Generator](https://openapi-generator.tech/docs/installation/) wygeneruj kod serwera. Poniżej znajdziesz polecenia konsolowe, które uruchomią generator przy użyciu Dockera:
```bash
docker pull openapitools/openapi-generator-cli

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/coffee-shop-api-spec.yaml \
    -g python-fastapi \
    -o /local/backend
```
3. Uruchom serwer przy pomocy narzędzia Docker. Pamiętaj, aby *wejść* w konsoli do katalogu `/backend`, w którym znajduje się wygenerowany kod, a następnie użyj polecenia:
```bash
docker compose up --build
```
4. Zaimplementuj proste REST API, odpowiednio dopisując logikę dla każdego z endpointów w pliku znajdującym się w katalogu `/src/openapi_server/apis/coffees_api.py`. Serwer jest dostępny pod URL-em `http://0.0.0.0:8080`. Może się zdarzyć, że po dokonaniu zmian w kodzie konieczne będzie zresetowanie serwera. Możesz to zrobić, używając kombinacji klawiszy `Ctrl + C`, a gdy kontener zostanie zniszczony, możesz ponownie uruchomić serwer, korzystając z polecenia dostępnego w punkcie 3.
5. Przetestuj, czy Twoje API działa poprawnie, wykorzystując interaktywną dokumentację dostępną pod adresem `http://0.0.0.0:8080/docs`.
