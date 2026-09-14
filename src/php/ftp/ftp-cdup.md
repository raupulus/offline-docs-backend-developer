---
title: ftp_cdup
description: Cambia de directorio y pasa al directorio padre
source_url: https://www.php.net/manual/es/function.ftp-cdup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-cdup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24370
---

ftp_cdup

Cambia de directorio y pasa al directorio padre

## Descripción

```php
ftp_cdup(FTP\Connection $ftp): bool
```php

`ftp_cdup` cambia de directorio y pasa al directorio padre.

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

Ejemplo con `ftp_cdup`

```
<?php
// Configuración de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con nombre de usuario y contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Modifica el directorio actual a html
ftp_chdir($ftp, 'html');

echo ftp_pwd($ftp); // /html

// Regreso al directorio padre
if (ftp_cdup($ftp)) {
  echo "éxito de cdup\n";
} else {
  echo "Fallo de cdup\n";
}

echo ftp_pwd($ftp); // /

ftp_close($ftp);
?>

    
```php

## Véase también

`ftp_chdir`, `ftp_pwd`
