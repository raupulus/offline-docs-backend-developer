---
title: apache_request_headers
description: Recupera todos los encabezados HTTP de la petición
source_url: https://www.php.net/manual/es/function.apache-request-headers.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-request-headers.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: 8a0888aeb
order: 4790
---

apache_request_headers

Recupera todos los encabezados HTTP de la petición

## Descripción

```php
apache_request_headers(): array
```php

Recupera todos los encabezados HTTP de la petición actual. Funciona con los servidores web Apache, LiteSpeed, FastCGI, CLI, y FPM.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un array asociativo con todos los encabezados HTTP de la petición actual.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | Esta función se hace disponible para la API de servidor (SAPI) FPM (FastCGI Process Manager). |

## Ejemplos

Ejemplo con `apache_request_headers`

```
<?php
$headers = apache_request_headers();

foreach ($headers as $header => $value) {
    echo "$header: $value <br />\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Accept: */*
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate
    User-Agent: Mozilla/4.0
    Host: www.example.com
    Connection: Keep-Alive

## Notas

> [!NOTE]
> También pueden obtenerse los valores de las variables CGI comunes leyéndolas en el entorno, lo cual funciona, ya sea en módulo Apache o no. Utilice la función `phpinfo` para conocer la lista de [variables de entorno](#language.variables.predefined) disponibles.

## Véase también

`apache_response_headers`
