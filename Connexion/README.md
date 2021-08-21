
# Connexion

## Install
pip install connexion[swagger-ui]

## Swagger:
http://0.0.0.0:8080/ui/

### PUT:
pet_id: 123
pet: {"name":"tommy","animal_type":"dog"}

## PUT using CURL:
curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"name":"tommy","animal_type":"dog"}' 'http://0.0.0.0:8080/pets/123'

## GET using CURL:
http://0.0.0.0:8080/pets/123
