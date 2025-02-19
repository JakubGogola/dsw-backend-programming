
#### **REST vs GraphQL**  
| Cecha | REST | GraphQL |
|------|------|---------|
| Struktura | Zasoby i endpointy | Zapytania i typy danych |
| Pobieranie danych | Wiele żądań do różnych endpointów | Jedno zapytanie, zwracane tylko wymagane dane |
| Typowanie danych | Brak wbudowanego typowania | Silne typowanie |
| Optymalizacja zapytań | Możliwe nadmiarowe dane | Możliwość precyzyjnego wyboru danych |

```graphql
query {
  user(id: 123) {
    id
    name
    email
    orders {
      id
      total
      status
    }
  }
}
```

```json
{
  "data": {
    "user": {
      "id": 123,
      "name": "John Doe",
      "email": "john@example.com",
      "orders": [
        {
          "id": 1,
          "total": 99.99,
          "status": "Shipped"
        },
        {
          "id": 2,
          "total": 49.50,
          "status": "Processing"
        }
      ]
    }
  }
}

```