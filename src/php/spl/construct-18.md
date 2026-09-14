---
title: RecursiveDirectoryIterator::__construct
description: Construye un objeto RecursiveDirectoryIterator
source_url: https://www.php.net/manual/es/recursivedirectoryiterator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/recursivedirectoryiterator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 83060
---

RecursiveDirectoryIterator::\_\_construct

Construye un objeto RecursiveDirectoryIterator

## Descripción

```php
public RecursiveDirectoryIterator::__construct(string $directory, [int $flags])
```php

Construye un objeto RecursiveDirectoryIterator para el directorio deseado.

## Parámetros

`directory`  
Ruta del directorio sobre el cual iterar.

`flags`  
Banderas a pasar para modificar el comportamiento del iterador. Una lista de banderas puede encontrarse en [ la lista de constantes de FilesystemIterator](#filesystemiterator.constants). También pueden ser especificadas más tarde mediante FilesystemIterator::setFlags

## Errores/Excepciones

Se lanza una excepción `UnexpectedValueException` si el directorio no existe.

Se lanza una excepción `ValueError` si `directory` es una cadena vacía.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Ahora se lanza una excepción `ValueError` cuando `directory` es una cadena vacía; Anteriormente se lanzaba una `RuntimeException`. |

## Ejemplos

Ejemplo con `RecursiveDirectoryIterator`

```
<?php

$directory = '/tmp';

$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($directory));

$it->rewind();
while($it->valid()) {

    if (!$it->isDot()) {
        echo 'SubPathName: ' . $it->getSubPathName() . "\n";
        echo 'SubPath:     ' . $it->getSubPath() . "\n";
        echo 'Key:         ' . $it->key() . "\n\n";
    }

    $it->next();
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    SubPathName: fruit/apple.xml
    SubPath:     fruit
    Key:         /tmp/fruit/apple.xml

    SubPathName: stuff.xml
    SubPath:
    Key:         /tmp/stuff.xml

    SubPathName: veggies/carrot.xml
    SubPath:     veggies
    Key:         /tmp/veggies/carrot.xml

## Véase también

FilesystemIterator::\_\_construct, RecursiveIteratorIterator::\_\_construct, [Constantes de FilesystemIterator](#filesystemiterator.constants)
