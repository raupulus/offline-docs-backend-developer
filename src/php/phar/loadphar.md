---
title: Phar::loadPhar
description: Carga cualquier archivo phar con un alias
source_url: https://www.php.net/manual/es/phar.loadphar.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/loadPhar.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64250
---

Phar::loadPhar

Carga cualquier archivo phar con un alias

## Descripción

```php
final public static Phar::loadPhar(string $filename, [string $alias]): bool
```php

Este método puede ser utilizado para leer el contenido de un archivo Phar externo. Esto es principalmente útil para asignar un alias a un phar de tal forma que las referencias posteriores al phar puedan realizarse mediante un alias más corto o para cargar archivos Phar que contienen solo datos y que no están destinados a ser ejecutados/incluidos en scripts PHP.

## Parámetros

`filename`  
la ruta relativa o absoluta hacia el archivo phar a abrir

`alias`  
El alias que podrá ser utilizado para referirse al archivo phar. Tenga en cuenta que muchos archivos phar especifican un alias explícito dentro del archivo phar, y se lanzará una excepción `PharException` si se especifica un nuevo alias en este caso.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una excepción `PharException` si se pasa un alias mientras que el archivo phar ya tiene un alias explícito

## Ejemplos

Un ejemplo con `Phar::loadPhar`

Phar::loadPhar puede ser utilizada en cualquier lugar para cargar un archivo phar externo mientras que Phar::mapPhar debe ser utilizada en un contenedor de carga para un Phar.

```
<?php
try {
    Phar::loadPhar('/ruta/al/phar.phar', 'mi.phar');
    echo file_get_contents('phar://mi.phar/fichero.txt');
} catch (PharException $e) {
    echo $e;
}
?>

    
```php

## Véase también

`Phar::mapPhar`
