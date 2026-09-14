---
title: La clase CallbackFilterIterator
source_url: https://www.php.net/manual/es/class.callbackfilteriterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/callbackfilteriterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 81790
---

## Introducción

## Sinopsis de la clase

CallbackFilterIterator

extends

FilterIterator

Métodos

Métodos heredados

## Ejemplos

La llamada de retorno debería aceptar hasta tres argumentos: el elemento actual, la clave actual y el iterador, respectivamente.

Argumentos disponibles de la llamada de retorno

```php
<?php

/**
 * Llamada de retorno para CallbackFilterIterator
 *
 * @param $current   Valor del elemento actual
 * @param $key       Clave del elemento actual
 * @param $iterator  Iterador a filtrar
 * @return boolean   TRUE para aceptar el elemento actual, de lo contrario FALSE
 */
function my_callback($current, $key, $iterator) {
    // Aquí el código de filtrado
}

?>

    
```

Se posría usar algún `callable`,como un string que contenga nombre de función, un array para un método, o una función anónima.

Ejemplos básicos de llamada de retorno

```php
<?php

$dir = new FilesystemIterator(__DIR__);

// Filtrar ficheros de gran tamaño ( > 100MB)
function is_large_file($current) {
    return $current->isFile() && $current->getSize() > 104857600;
}
$large_files = new CallbackFilterIterator($dir, 'is_large_file');

// Filtrar directorios
$files = new CallbackFilterIterator($dir, function ($current, $key, $iterator) {
    return $current->isDir() && ! $iterator->isDot();
});

?>

    
```
