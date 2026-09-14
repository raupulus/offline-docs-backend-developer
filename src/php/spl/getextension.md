---
title: DirectoryIterator::getExtension
description: Obtiene la extensión de un fichero
source_url: https://www.php.net/manual/es/directoryiterator.getextension.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/getextension.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 62126c55f
order: 81840
---

DirectoryIterator::getExtension

Obtiene la extensión de un fichero

## Descripción

```php
public DirectoryIterator::getExtension(): string
```php

Recupera la extensión de un fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` que contiene la extensión del ficher, o un `string` vacío si el fichoer no tiene extensión.

## Ejemplos

Ejemplo de `DirectoryIterator::getExtension`

```
<?php

$directory = new DirectoryIterator(__DIR__);
foreach ($directory as $fileinfo) {
    if ($fileinfo->isFile()) {
        echo $fileinfo->getExtension() . "\n";
    }
}

?>

   
```php

Resultado del ejemplo anterior es similar a:

    php
    txt
    jpg
    gz

## Notas

> [!NOTE]
> Otra manera de obtener la extensión es usar la función `pathinfo`.
>
> <div class="informalexample">
>
> ```
> <?php
> $extension = pathinfo($fileinfo->getFilename(), PATHINFO_EXTENSION);
> ?>
>
>     
> ```
>
> </div>

## Véase también

DirectoryIterator::getFilename

DirectoryIterator::getBasename

pathinfo
