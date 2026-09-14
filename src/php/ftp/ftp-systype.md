---
title: ftp_systype
description: Devuelve un identificador del tipo de servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-systype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-systype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24700
---

ftp_systype

Devuelve un identificador del tipo de servidor FTP

## Descripción

```php
ftp_systype(FTP\Connection $ftp): string
```php

`ftp_systype` devuelve el tipo de servidor FTP remoto.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

## Valores devueltos

Devuelve el tipo de servidor remoto o `false` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_systype`

```
<?php

// Conexión ftp
$ftp = ftp_connect('ftp.example.com');
ftp_login($ftp, 'user', 'password');

// Obtención del tipo de servidor
if ($type = ftp_systype($ftp)) {
    echo "Example.com es ejecutado por $type\n";
} else {
    echo "No es posible recuperar el tipo del servidor";
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Example.com es ejecutado por UNIX
