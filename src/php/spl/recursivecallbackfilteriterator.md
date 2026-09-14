---
title: La clase RecursiveCallbackFilterIterator
source_url: https://www.php.net/manual/es/class.recursivecallbackfilteriterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivecallbackfilteriterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 83050
---

## Introducción

## Sinopsis de la clase

RecursiveCallbackFilterIterator

extends

CallbackFilterIterator

implements

RecursiveIterator

Métodos

Métodos heredados

## Ejemplos

La función de devolución de llamada debe aceptar hasta 3 argumentos: el elemento actual, la clave actual, y el iterador actual, respectivamente.

Argumentos disponibles para la función de devolución de llamada

```php
<?php

/**
 * Función de devolución de llamada para RecursiveCallbackFilterIterator
 *
 * @param $current   El valor del elemento actual
 * @param $key       La clave del elemento actual
 * @param $iterator  Iterador a filtrar
 * @return boolean   TRUE para aceptar el elemento actual, FALSE en caso contrario
 */
function my_callback($current, $key, $iterator) {
    // Su filtro aquí
}

?>

    
```

El filtrado de un iterador recursivo implica generalmente 2 condiciones. La primera es que, para permitir la recursión, la función de devolución de llamada debe devolver `true` si el elemento del iterador actual tiene un hijo. La segunda es una condición de filtrado normal, como la verificación del tamaño de fichero o la verificación de la extensión como en el ejemplo siguiente.

Ejemplo simple de una función de devolución de llamada recursiva

```php
<?php

$dir = new RecursiveDirectoryIterator(__DIR__);

// Filtro de ficheros grandes ( > 100MB)
$files = new RecursiveCallbackFilterIterator($dir, function ($current, $key, $iterator) {
    // Permite la recursión
    if ($iterator->hasChildren()) {
        return TRUE;
    }
    // Verifica ficheros grandes
    if ($current->isFile() && $current->getSize() > 104857600) {
        return TRUE;
    }
    return FALSE;
});

foreach (new RecursiveIteratorIterator($files) as $file) {
    echo $file->getPathname() . PHP_EOL;
}

?>

    
```
