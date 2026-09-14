---
title: OAuth::getRequestToken
description: Lee el token de solicitud
source_url: https://www.php.net/manual/es/oauth.getrequesttoken.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/getrequesttoken.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: true
translation_revision: bdee7e8c1
order: 56810
---

OAuth::getRequestToken

Lee el token de solicitud

## Descripción

```php
public OAuth::getRequestToken(string $request_token_url, [string $callback_url], [string $http_method]): array
```php

Lee el token de solicitud, el secreto y cualquier información adicional del proveedor de servicios.

## Parámetros

`request_token_url`  
La URL de la que se debe obtener el token.

`callback_url`  
URL de devolución de llamada OAuth. Si `callback_url` es pasado y su valor es vacío, entonces toma el valor de `"oob"` para cumplir con los requisitos de `OAuth 2009.1 advisory`.

`http_method`  
Método HTTP a utilizar, por ejemplo `GET` o `POST`.

## Valores devueltos

Devuelve un array que contiene la respuesta OAuth analizada, en caso de éxito, o `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |
| PECL oauth 0.99.9 | Se ha añadido el parámetro `callback_url` |

## Ejemplos

Ejemplo con `OAuth::getRequestToken`

```
<?php
try {
    $oauth = new OAuth(OAUTH_CONSUMER_KEY,OAUTH_CONSUMER_SECRET);
    $request_token_info = $oauth->getRequestToken("https://example.com/oauth/request_token");
    if(!empty($request_token_info)) {
        print_r($request_token_info);
    } else {
        print "Failed fetching request token, response was: " . $oauth->getLastResponse();
    }
} catch(OAuthException $E) {
    echo "Response: ". $E->lastResponse . "\n";
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [oauth_token] => some_token
        [oauth_token_secret] => some_token_secret
    )

## Véase también

OAuth::getLastResponse

OAuth::getLastResponseInfo
