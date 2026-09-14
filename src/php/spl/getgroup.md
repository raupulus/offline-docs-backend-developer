---
title: SplFileInfo::getGroup
description: Obtiene el grupo de el fichero
source_url: https://www.php.net/manual/es/splfileinfo.getgroup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getgroup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 84080
---

SplFileInfo::getGroup

Obtiene el grupo de el fichero

## Descripción

```php
public SplFileInfo::getGroup(): int
```php

Obtiene el grupo del fichero. El ID del grupo es retornado en formato numérico.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El ID del grupo en formato numérico en caso de éxito, o `false` en caso de error.

## Errores/Excepciones

Lanza una `RuntimeException` en caso de error.

## Ejemplos

Ejemplo de SplFileInfo::getGroup

```
<?php
$info = new SplFileInfo('example.jpg');
echo $info->getFilename() . ' belongs to group id ' . $info->getGroup() . "\n";
print_r(posix_getgrgid($info->getGroup()));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    example.jpg belongs to group id 42
    Array
    (
        [name] => toons
        [passwd] => x
        [members] => Array
            (
                [0] => tom
                [1] => jerry
            )
        [gid] => 42
    )

## Véase también

`filegroup`, `posix_getgrgid`
