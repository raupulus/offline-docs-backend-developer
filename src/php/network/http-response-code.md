---
title: http_response_code
description: Obtiene o define el código de respuesta HTTP
source_url: https://www.php.net/manual/es/function.http-response-code.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/http-response-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56440
---

http_response_code

Obtiene o define el código de respuesta HTTP

## Descripción

```php
http_response_code([int $response_code]): int
```php

Obtiene o define el código de estado de respuesta HTTP.

## Parámetros

`response_code`  
El argumento opcional `response_code` definirá el código de respuesta.

## Valores devueltos

Si `response_code` es proporcionado, en ese caso el código de estado anterior será devuelto. Si `response_code` no es proporcionado, entonces el código de estado actual será devuelto. Ambos valores serán por omisión el código de estado `200` si se utiliza en un entorno de servidor web.

`false` será devuelto si `response_code` no es proporcionado y no es invocado en un entorno de servidor web (por ejemplo desde una aplicación CLI) `true` será devuelto si `response_code` es proporcionado y no es invocado en un entorno de servidor web (pero únicamente si ningún estado de respuesta anterior ha sido definido).

## Ejemplos

Utilizar `http_response_code` en un entorno de servidor web

```
<?php

// Obtener el código de respuesta actual y definir uno nuevo
var_dump(http_response_code(404));

// Obtener el nuevo código de respuesta
var_dump(http_response_code());
?>

    
```php

El ejemplo anterior mostrará:

    int(200)
    int(404)

Utilizar `http_response_code` en un entorno CLI

```
<?php

// Obtener el código de respuesta por omisión
var_dump(http_response_code());

// Definir un código de respuesta
http_response_code(404);

// Obtener el nuevo código de respuesta
var_dump(http_response_code());
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
    int(201)

## Véase también

`header`, `headers_list`
