---
title: ftp_nlist
description: Devuelve la lista de ficheros de un directorio
source_url: https://www.php.net/manual/es/function.ftp-nlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ftp/functions/ftp-nlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ftp
translation_status: ready
translation_reviewed: false
translation_revision: 4d1c34c9b
order: 24570
---

ftp_nlist

Devuelve la lista de ficheros de un directorio

## Descripción

```php
ftp_nlist(FTP\Connection $ftp, string $directory): array
```php

## Parámetros

`ftp`  
Una instancia de `FTP\Connection`.

`directory`  
El directorio a listar. Este argumento puede incluir argumentos adicionales, e.g. `ftp_nlist($ftp, "-la /your/dir");` Tenga en cuenta que este argumento no se escapa, por lo que pueden producirse comportamientos no deseados si el nombre de los ficheros contiene espacios u otros caracteres.

## Valores devueltos

Devuelve un array con los nombres de ficheros presentes en el directorio especificado en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ftp` ahora espera una instancia de `FTP\Connection` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `ftp_nlist`

```
<?php

// Establecimiento de una conexión básica
$ftp = ftp_connect($ftp_server);

// Identificación con un nombre de usuario y una contraseña
$login_result = ftp_login($ftp, $ftp_user_name, $ftp_user_pass);

// Obtención del contenido de un directorio
$contents = ftp_nlist($ftp, ".");

// Visualización de $contents
var_dump($contents);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      [0]=>
      string(11) "public_html"
      [1]=>
      string(10) "public_ftp"
      [2]=>
      string(3) "www"

## Véase también

`ftp_rawlist`, `ftp_mlsd`
