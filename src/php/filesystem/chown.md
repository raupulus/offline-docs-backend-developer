---
title: chown
description: Cambia el propietario del fichero
source_url: https://www.php.net/manual/es/function.chown.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/chown.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23300
---

chown

Cambia el propietario del fichero

## Descripción

```php
chown(string $filename, string $user): bool
```php

Cambia el propietario del fichero `filename` a `user`. Solo el superusuario (root) puede cambiar arbitrariamente el propietario de un fichero.

## Parámetros

`filename`  
Ruta hacia el fichero.

`user`  
Un nombre o un número de usuario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `chown`

```
<?php

// Nombre del fichero y nombre de usuario a utilizar
$file_name= "foo.php";
$path = "/home/sites/php.net/public_html/sandbox/" . $file_name ;
$user_name = "root";

// Define el usuario
chown($path, $user_name);

// Verificación del resultado
$stat = stat($path);
print_r(posix_getpwuid($stat['uid']));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [name] => root
        [passwd] => x
        [uid] => 0
        [gid] => 0
        [gecos] => root
        [dir] => /root
        [shell] => /bin/bash
    )

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

> [!NOTE]
> En Windows, esta función falla silenciosamente cuando se aplica sobre un fichero ordinario.

## Véase también

`chmod`, `chgrp`
