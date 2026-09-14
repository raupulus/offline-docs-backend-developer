---
title: FilesystemIterator::__construct
description: Construye un objeto FilesystemIterator
source_url: https://www.php.net/manual/es/filesystemiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filesystemiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: a7d00d0b9
order: 82030
---

FilesystemIterator::\_\_construct

Construye un objeto FilesystemIterator

## Descripción

```php
public FilesystemIterator::__construct(string $directory, [int $flags])
```php

Construye un objeto FilesystemIterator, configurado con la ruta `directory`.

## Parámetros

`directory`  
La ruta del directorio en el que se va a trabajar.

`flags`  
Las opciones que afectan el comportamiento de los métodos. La lista de opciones está disponible en [las constantes de `FilesystemIterator`](#filesystemiterator.constants). También pueden ser activadas posteriormente con FilesystemIterator::setFlags.

## Errores/Excepciones

Lanza una excepción `UnexpectedValueException` si el directorio no existe.

Lanza una excepción `ValueError` si `directory` es una cadena vacía.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | Antes de PHP 8.2.0, `FilesystemIterator::SKIP_DOTS` estaba siempre activado y no podía ser desactivado. |
| 8.0.0 | Ahora lanza una excepción `ValueError` cuando `directory` es una cadena vacía; Anteriormente, se lanzaba una `RuntimeException`. |

## Ejemplos

Ejemplo con `FilesystemIterator::__construct`

```
<?php
$it = new FilesystemIterator(dirname(__FILE__), FilesystemIterator::CURRENT_AS_FILEINFO);
foreach ($it as $fileinfo) {
    echo $fileinfo->getFilename() . "\n";
}
?>

    
```php

Resultado del ejemplo anterior en PHP 8.2 es similar a:

    .
    ..
    apples.jpg
    banana.jpg
    example.php

        

El resultado del ejemplo anterior, antes de PHP 8.2.0, es similar a:

    apples.jpg
    banana.jpg
    example.php

## Véase también

FilesystemIterator::setFlags, DirectoryIterator::\_\_construct
