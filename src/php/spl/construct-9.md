---
title: GlobIterator::__construct
description: Construye un iterador de tipo glob
source_url: https://www.php.net/manual/es/globiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/globiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: d51166ca1
order: 82340
---

GlobIterator::\_\_construct

Construye un iterador de tipo glob

## Descripción

```php
public GlobIterator::__construct(string $pattern, [int $flags])
```php

Construye un iterador de tipo glob.

## Parámetros

`pattern`  
Un patrón `glob`.

`flags`  
Las opciones, que pueden ser un campo de bits de constantes de clase `FilesystemIterator`.

## Errores/Excepciones

Se lanza una excepción `UnexpectedValueException` si el directorio no existe.

Se lanza una excepción `ValueError` si `directory` es una cadena vacía.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Ahora se lanza una excepción `ValueError` cuando `directory` es una cadena vacía; Anteriormente, se lanzaba una `RuntimeException`. |

## Ejemplos

Ejemplo con `GlobIterator`

```
<?php
$iterator = new GlobIterator('*.dll',  FilesystemIterator::KEY_AS_FILENAME);

if (!$iterator->count()) {
    echo 'No matches';
} else {
    $n = 0;

    printf("Matched  %d item(s)\r\n", $iterator->count());

    foreach ($iterator as $item) {
        printf("[%d] %s\r\n", ++$n, $iterator->key());
    }
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Matched 2 item(s)
    [1] php5ts.dll
    [2] php_gd2.dll

## Véase también

DirectoryIterator::\_\_construct, GlobIterator::count, `glob`
