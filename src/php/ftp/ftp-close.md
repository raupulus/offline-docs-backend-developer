---
title: ftp_close
description: Cierra una conexión FTP
source_url: https://www.php.net/manual/es/function.ftp-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24400
---

ftp_close

Cierra una conexión FTP

## Descripción

```php
ftp_close(FTP\Connection $ftp): bool
```php

`ftp_close` cierra la conexión `ftp` y libera los recursos.

> [!NOTE]
> Tras llamar a esta función, ya no es posible utilizar la antigua conexión, y debe abrirse una nueva con `ftp_connect`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_close`

```
<?php

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Autenticación con nombre de usuario y contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Mostrar el directorio actual
echo ftp_pwd($ftp); // /

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php

## Véase también

`ftp_connect`
