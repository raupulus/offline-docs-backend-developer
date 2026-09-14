---
title: ftp_rawlist
description: Realiza una lista detallada de los ficheros de un directorio
source_url: https://www.php.net/manual/es/function.ftp-rawlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-rawlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: true
translation_revision: 4d1c34c9b
order: 24630
---

ftp_rawlist

Realiza una lista detallada de los ficheros de un directorio

## Descripción

```php
ftp_rawlist(FTP\Connection $ftp, string $directory, [bool $recursive]): array
```php

`ftp_rawlist` ejecuta el comando FTP `LIST`, y devuelve el resultado en un array.

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`directory`  
La ruta al directorio. Puede incluir los argumentos para el comando `LIST`.

`recursive`  
Si se establece en `true`, el comando será `LIST -R`.

## Valores devueltos

Devuelve un array donde los elementos corresponden a una línea de texto. Devuelve `false` cuando el argumento `directory` es inválido.

La salida nunca se analiza. El identificador del tipo de sistema devuelto por la función `ftp_systype` puede ser utilizado para determinar cómo deben interpretarse los resultados.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_rawlist`

```
<?php

// Configuración de una conexión básica
$ftp = ftp_connect($ftp_server);

// Autenticación con nombre de usuario y contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Obtiene la lista de ficheros de /
$buff = ftp_rawlist($ftp, '/');

// Cierre de la conexión
ftp_close($ftp);

// Muestra el buffer
var_dump($buff);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      string(65) "drwxr-x---   3 vincent  vincent      4096 Jul 12 12:16 public_ftp"
      [1]=>
      string(66) "drwxr-x---  15 vincent  vincent      4096 Nov  3 21:31 public_html"
      [2]=>
      string(73) "lrwxrwxrwx   1 vincent  vincent        11 Jul 12 12:16 www -> public_html"
    }

## Véase también

`ftp_nlist`, `ftp_mlsd`
