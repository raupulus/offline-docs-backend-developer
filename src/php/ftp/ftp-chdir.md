---
title: ftp_chdir
description: Modifica el directorio FTP actual
source_url: https://www.php.net/manual/es/function.ftp-chdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-chdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24380
---

ftp_chdir

Modifica el directorio FTP actual

## Descripción

```php
ftp_chdir(FTP\Connection $ftp, string $directory): bool
```php

`ftp_chdir` modifica el directorio actual a `directory`.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`directory`  
El directorio destino.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si el cambio falla, PHP también generará una advertencia.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_chdir`

```
<?php

// Configuración de una conexión básica
$ftp = ftp_connect($ftp_server);

// Autenticación con nombre de usuario y contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Verificación de la conexión
if ((!$ftp) || (!$login_result)) {
    die("¡Fallo en la conexión FTP!");
}

echo "Directorio actual: " . ftp_pwd($ftp) . "\n";

// Intento de cambiar al directorio "somedir"
if (ftp_chdir($ftp, "somedir")) {
    echo "El directorio actual es ahora: " . ftp_pwd($ftp) . "\n";
} else {
    echo "No se pudo cambiar de directorio\n";
}

// Cierre de la conexión
ftp_close($ftp);
?>

    
```php

## Véase también

`ftp_cdup`, `ftp_pwd`
