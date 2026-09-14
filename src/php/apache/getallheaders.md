---
title: getallheaders
description: Recupera todos los encabezados de la petición HTTP
source_url: https://www.php.net/manual/es/function.getallheaders.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/getallheaders.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: 68e52ef14
order: 4820
---

getallheaders

Recupera todos los encabezados de la petición HTTP

## Descripción

```php
getallheaders(): array
```php

Recupera todos los encabezados de la petición HTTP.

Esta función es un alias de la función `apache_request_headers`. Consúltense la documentación de `apache_request_headers` para obtener más información sobre el funcionamiento de esta función.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array asociativo con todos los encabezados HTTP de la petición actual.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | Esta función se hace disponible para la API servidor (SAPI) FPM (FastCGI Process Manager). |

## Ejemplos

Ejemplo con `getallheaders`

```
<?php

foreach (getallheaders() as $name => $value) {
    echo "$name: $value\n";
}

?>

    
```php

## Véase también

`apache_response_headers`
