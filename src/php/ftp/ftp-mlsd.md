---
title: ftp_mlsd
description: Devuelve la lista de ficheros de un directorio dado
source_url: https://www.php.net/manual/es/function.ftp-mlsd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-mlsd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24510
---

ftp_mlsd

Devuelve la lista de ficheros de un directorio dado

## Descripción

```php
ftp_mlsd(FTP\Connection $ftp, string $directory): array
```php

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`directory`  
El directorio a recorrer.

## Valores devueltos

Devuelve un array de arrays con la información de los ficheros del directorio especificado en caso de éxito o `false` si hay un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_mlsd`

```
<?php

// establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// conexión con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// obtiene el contenido del directorio actual
$contents = ftp_mlsd($ftp, ".");

// muestra $contents
var_dump($contents);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(5) {
      [0]=>
      array(8) {
        ["name"]=>
        string(1) "."
        ["modify"]=>
        string(14) "20171212154511"
        ["perm"]=>
        string(7) "flcdmpe"
        ["type"]=>
        string(4) "cdir"
        ["unique"]=>
        string(11) "811U5740002"
        ["UNIX.group"]=>
        string(2) "33"
        ["UNIX.mode"]=>
        string(4) "0755"
        ["UNIX.owner"]=>
        string(2) "33"
      }
      [1]=>
      array(8) {
        ["name"]=>
        string(2) ".."
        ["modify"]=>
        string(14) "20171212154511"
        ["perm"]=>
        string(7) "flcdmpe"
        ["type"]=>
        string(4) "pdir"
        ["unique"]=>
        string(11) "811U5740002"
        ["UNIX.group"]=>
        string(2) "33"
        ["UNIX.mode"]=>
        string(4) "0755"
        ["UNIX.owner"]=>
        string(2) "33"
      }
      [2]=>
      array(8) {
        ["name"]=>
        string(11) "public_html"
        ["modify"]=>
        string(14) "20171211171525"
        ["perm"]=>
        string(7) "flcdmpe"
        ["type"]=>
        string(3) "dir"
        ["unique"]=>
        string(11) "811U5740525"
        ["UNIX.group"]=>
        string(2) "33"
        ["UNIX.mode"]=>
        string(4) "0755"
        ["UNIX.owner"]=>
        string(2) "33"
      }
      [3]=>
      array(8) {
        ["name"]=>
        string(10) "public_ftp"
        ["modify"]=>
        string(14) "20171211174536"
        ["perm"]=>
        string(7) "flcdmpe"
        ["type"]=>
        string(3) "dir"
        ["unique"]=>
        string(11) "811U57405EE"
        ["UNIX.group"]=>
        string(2) "33"
        ["UNIX.mode"]=>
        string(4) "0755"
        ["UNIX.owner"]=>
        string(2) "33"
      }
      [4]=>
      array(8) {
        ["name"]=>
        string(3) "www"
        ["modify"]=>
        string(14) "www"
        ["perm"]=>
        string(7) "flcdmpe"
        ["type"]=>
        string(3) "dir"
        ["unique"]=>
        string(11) "811U5740780"
        ["UNIX.group"]=>
        string(2) "33"
        ["UNIX.mode"]=>
        string(4) "0755"
        ["UNIX.owner"]=>
        string(2) "33"
      }
    }

## Véase también

`ftp_rawlist`, `ftp_nlist`
