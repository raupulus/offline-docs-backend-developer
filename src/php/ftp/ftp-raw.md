---
title: ftp_raw
description: Envía una orden FTP bruta
source_url: https://www.php.net/manual/es/function.ftp-raw.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-raw.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 0773339dc
order: 24620
---

ftp_raw

Envía una orden FTP bruta

## Descripción

```php
ftp_raw(FTP\Connection $ftp, string $command): array
```php

`ftp_raw` envía la orden FTP bruta `command` al servidor FTP identificado por `ftp`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`command`  
La orden a ejecutar.

## Valores devueltos

Devuelve la respuesta del servidor como un array de strings, o `null` en caso de fallo. No se realiza ningún análisis sobre la cadena de respuesta, ni si la orden ha tenido éxito.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Uso de `ftp_raw` para identificarse manualmente en un servidor FTP

```
<?php
$ftp = ftp_connect("ftp.example.com");

/* Esto es equivalente a:
   ftp_login($ftp, "joeblow", "secret");
 */

ftp_raw($ftp, "USER joeblow");
ftp_raw($ftp, "PASS secret");
?>

    
```php

## Véase también

`ftp_exec`
