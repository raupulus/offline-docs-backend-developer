---
title: FilesystemIterator::setFlags
description: Configura las opciones
source_url: https://www.php.net/manual/es/filesystemiterator.setflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filesystemiterator/setflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: a7d00d0b9
order: 82090
---

FilesystemIterator::setFlags

Configura las opciones

## Descripción

```php
public FilesystemIterator::setFlags(int $flags): void
```php

Configura las opciones.

## Parámetros

`flags`  
Las opciones a configurar. Ver la lista de [constantes de `FilesystemIterator`](#filesystemiterator.constants).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con FilesystemIterator::key

Este ejemplo ilustra la diferencia entre las opciones [FilesystemIterator::KEY_AS_PATHNAME](#filesystemiterator.constants.key-as-pathname) y [FilesystemIterator::KEY_AS_FILENAME](#filesystemiterator.constants.key-as-filename).

```
<?php
$iterator = new FilesystemIterator(dirname(__FILE__), FilesystemIterator::KEY_AS_PATHNAME);
echo "Clave como nombre de ruta : \n";
foreach ($iterator as $key => $fileinfo) {
    echo $key . "\n";
}

$iterator->setFlags(FilesystemIterator::KEY_AS_FILENAME);
echo "\nClave como nombre de archivo : \n";
foreach ($iterator as $key => $fileinfo) {
    echo $key . "\n";
}
?>

    
```php

Resultado del ejemplo anterior en PHP 8.2 es similar a:

    Clave como nombre de ruta :
    /www/examples/.
    /www/examples/..  /www/examples/apple.jpg
    /www/examples/banana.jpg
    /www/examples/example.php

    Clave como nombre de archivo :
    .
    ..
    apple.jpg
    banana.jpg
    example.php

## Véase también

FilesystemIterator::\_\_construct, FilesystemIterator::getFlags
