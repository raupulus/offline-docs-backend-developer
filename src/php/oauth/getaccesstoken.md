---
title: OAuth::getAccessToken
description: Recupera un token de acceso
source_url: https://www.php.net/manual/es/oauth.getaccesstoken.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oauth/oauth/getaccesstoken.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oauth
translation_status: ready
translation_reviewed: true
translation_revision: bdee7e8c1
order: 56750
---

OAuth::getAccessToken

Recupera un token de acceso

## Descripción

```php
public OAuth::getAccessToken(string $access_token_url, [string $auth_session_handle], [string $verifier_token], [string $http_method]): array
```php

Lee un token de acceso, un secreto y cualquier información adicional en un proveedor de servicios.

## Parámetros

`access_token_url`  
La URL a utilizar.

`auth_session_handle`  
El identificador de sesión. Este parámetro no existe en las especificaciones OAuth 1.0, pero puede ser implementado por grandes implementaciones. Véase [`ScalableOAuth`](http://oauth.pbwiki.com/ScalableOAuth/) para más detalles.

`verifier_token`  
Para los proveedores de servicio que soportan 1.0a, el parámetro `verifier_token` debe ser proporcionado, al intercambiar el token de solicitud para obtener el token de acceso. Si `verifier_token` está presente en `$_GET` o `$_POST`, es automáticamente pasado y el llamante no necesita especificar el parámetro `verifier_token` (generalmente, el token de acceso es intercambiado vía la URL de devolución `callback_url`). Véase [ScalableOAuth](http://oauth.pbwiki.com/ScalableOAuth/) para más información.

`http_method`  
Método HTTP a utilizar, por ejemplo `GET` o `POST`.

## Valores devueltos

Devuelve un array que contiene la respuesta OAuth analizada, en caso de éxito, y `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL oauth 1.0.0 | Antes de esta versión, `null` era devuelto en lugar de `false`. |
| PECL oauth 0.99.9 | Se añadió el parámetro `verifier_token` |

## Ejemplos

Ejemplo con `OAuth::getAccessToken`

```
<?php
try {
    $oauth = new OAuth(OAUTH_CONSUMER_KEY,OAUTH_CONSUMER_SECRET);
    $oauth->setToken($request_token,$request_token_secret);
    $access_token_info = $oauth->getAccessToken("https://example.com/oauth/access_token");
    if(!empty($access_token_info)) {
        print_r($access_token_info);
    } else {
        print "Error al obtener el token de acceso, la respuesta fue: " . $oauth->getLastResponse();
    }
} catch(OAuthException $E) {
    echo "Respuesta: ". $E->lastResponse . "\n";
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

OAuth::setToken
