---
title: DirectoryIterator::__construct
description: Construye un nuevo iterador de directorio a partir de una ruta
source_url: https://www.php.net/manual/es/directoryiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/directoryiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 81810
---

DirectoryIterator::\_\_construct

Construye un nuevo iterador de directorio a partir de una ruta

## Descripción

```php
public DirectoryIterator::__construct(string $directory)
```php

Construye un nuevo iterador de directorio a partir de una ruta.

## Parámetros

`directory`  
La ruta del directorio a recorrer.

## Errores/Excepciones

Lanza una excepción `UnexpectedValueException` si el directorio no existe.

Lanza una excepción `ValueError` si `directory` es una string vacía.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Lanza ahora una excepción `ValueError` cuando `directory` es una string vacía; Anteriormente, se lanzaba una `RuntimeException`. |

## Ejemplos

Ejemplo con DirectoryIterator::\_\_construct

Este ejemplo listará el contenido del directorio que contiene el script.

```
<?php
$dir = new DirectoryIterator(dirname(__FILE__));
foreach ($dir as $fileinfo) {
    if (!$fileinfo->isDot()) {
        var_dump($fileinfo->getFilename());
    }
}
?>

    
```php

## Véase también

`SplFileInfo`, `Iterator`
