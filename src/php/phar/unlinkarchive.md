---
title: Phar::unlinkArchive
description: Elimina completamente un archivo phar del disco y de la memoria
source_url: https://www.php.net/manual/es/phar.unlinkarchive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/unlinkArchive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64410
---

Phar::unlinkArchive

Elimina completamente un archivo phar del disco y de la memoria

## Descripción

```php
final public static Phar::unlinkArchive(string $filename): true
```php

Elimina completamente un archivo phar del disco y de la memoria

## Parámetros

`filename`  
La ruta en el disco hacia el archivo phar.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Se lanza una excepción `PharException` si existen punteros abiertos hacia ficheros del archivo phar, o si objetos `Phar`, `PharData`, o `PharFileInfo` hacen referencia al archivo phar.

## Ejemplos

Un ejemplo con `Phar::unlinkArchive`

```
<?php
// uso simple
Phar::unlinkArchive('/ruta/al/archivo.phar');

// un ejemplo más común:
$p = new Phar('archivo.phar');
$fp = fopen('phar://archivo.phar/fichero.txt', 'r');
// esto crea 'archivo.phar.gz'
$gp = $p->compress(Phar::GZ);
// elimina todas las referencias al archivo
unset($p);
fclose($fp);
// borra ahora todo rastro del archivo
Phar::unlinkArchive('archivo.phar');
?>

    
```php

## Véase también

`Phar::delete`, `Phar::offsetUnset`
