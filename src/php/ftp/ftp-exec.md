---
title: ftp_exec
description: Ejecuta un comando en un servidor FTP
source_url: https://www.php.net/manual/es/function.ftp-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24430
---

ftp_exec

Ejecuta un comando en un servidor FTP

## Descripción

```php
ftp_exec(FTP\Connection $ftp, string $command): bool
```php

`ftp_exec` envía un comando SITE EXEC al servidor FTP, para que ejecute el programa `command`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`command`  
El comando a ejecutar.

## Valores devueltos

Devuelve `true` si el comando se ejecutó con éxito (el servidor envía el código de respuesta: `200`); de lo contrario, devuelve `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_exec`

```
<?php

// Inicialización de la variable
$command = 'ls -al >files.txt';

// Inicialización de la conexión
$ftp = ftp_connect($ftp_server);

// Identificación
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Ejecución de un comando
if (ftp_exec($ftp, $command)) {
    echo "$command se ejecutó con éxito\n";
} else {
    echo "No se pudo ejecutar: $command\n";
}

// Cierre de la conexión
ftp_close($ftp);

?>

    
```php

## Véase también

`ftp_raw`
