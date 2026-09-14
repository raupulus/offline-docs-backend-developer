---
title: ftp_get_option
description: Lee diferentes opciones para la conexión FTP actual
source_url: https://www.php.net/manual/es/function.ftp-get-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-get-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24460
---

ftp_get_option

Lee diferentes opciones para la conexión FTP actual

## Descripción

```php
ftp_get_option(FTP\Connection $ftp, int $option): int
```php

`ftp_get_option` devuelve el valor de la opción `option` desde la conexión FTP especificada.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`option`  
Actualmente, las siguientes opciones son soportadas:

|  |  |
|----|----|
| `FTP_TIMEOUT_SEC` | Devuelve el tiempo de espera de conexión actual utilizado para las operaciones en la red. |
| `FTP_AUTOSEEK` | Devuelve `true` si esta opción está activa, `false` en caso contrario. |

Opciones FTP soportadas

## Valores devueltos

Devuelve el valor en caso de éxito, o `false` si la opción `option` no es soportada. En el último caso, un mensaje de alerta es igualmente enviado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_get_option`

```
<?php
// Obtención del tiempo de espera de conexión del flujo FTP actual
$timeout = ftp_get_option($ftp, FTP_TIMEOUT_SEC);
?>

    
```php

## Véase también

`ftp_set_option`
