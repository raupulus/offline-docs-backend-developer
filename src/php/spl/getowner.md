---
title: SplFileInfo::getOwner
description: Obtiene el dueño de el fichero
source_url: https://www.php.net/manual/es/splfileinfo.getowner.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getowner.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 84120
---

SplFileInfo::getOwner

Obtiene el dueño de el fichero

## Descripción

```php
public SplFileInfo::getOwner(): int
```php

Obtiene el dueño de el fichero. El ID del dueño retornado en formato numérico.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El id del dueño en formato numérico en caso de éxito, o `false` en caso de error.

## Errores/Excepciones

Lanza una `RuntimeException` en caso de error.

## Ejemplos

Ejemplo de SplFileInfo::getOwner

```
<?php
$info = new SplFileInfo('example.jpg');
echo $info->getFilename() . ' belongs to owner id ' . $info->getOwner() . "\n";
print_r(posix_getpwuid($info->getOwner()));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    example.jpg belongs to user id 501
    Array
    (
        [name] => tom
        [passwd] => x
        [uid] => 501
        [gid] => 42
        [gecos] => Tom Cat
        [dir] => /home/tom
        [shell] => /bin/bash
    )

## Véase también

`posix_getpwuid`, SplFileInfo::getGroup
