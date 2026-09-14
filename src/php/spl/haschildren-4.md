---
title: RecursiveCallbackFilterIterator::hasChildren
description: Verifica si el elemento actual del iterador interno tiene un hijo
source_url: https://www.php.net/manual/es/recursivecallbackfilteriterator.haschildren.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivecallbackfilteriterator/haschildren.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 83040
---

RecursiveCallbackFilterIterator::hasChildren

Verifica si el elemento actual del iterador interno tiene un hijo

## Descripción

```php
public RecursiveCallbackFilterIterator::hasChildren(): bool
```php

Devuelve `true` si el elemento actual tiene un hijo, `false` en caso contrario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el elemento actual tiene hijos, `false` en caso contrario.

## Ejemplos

Ejemplo con RecursiveCallbackFilterIterator::hasChildren

```
<?php

$dir = new RecursiveDirectoryIterator(__DIR__);

// Iteración recursiva sobre ficheros XML
$files = new RecursiveCallbackFilterIterator($dir, function ($current, $key, $iterator) {
    // Permite la recursión en los directorios
    if ($iterator->hasChildren()) {
        return TRUE;
    }
    // Verifica el fichero XML
    if (!strcasecmp($current->getExtension(), 'xml')) {
        return TRUE;
    }
    return FALSE;
});

?>

    
```php

## Véase también

[Ejemplos con RecursiveCallbackFilterIterator](#recursivecallbackfilteriterator.examples), RecursiveCallbackFilterIterator::\_\_construct, RecursiveCallbackFilterIterator::getChildren
