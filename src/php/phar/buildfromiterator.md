---
title: Phar::buildFromIterator
description: Construye un archivo phar a partir de un iterador
source_url: https://www.php.net/manual/es/phar.buildfromiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/buildFromIterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: f03806fcd
order: 63920
---

Phar::buildFromIterator

Construye un archivo phar a partir de un iterador

## Descripción

```php
public Phar::buildFromIterator(Traversable $iterator, [string $baseDirectory]): array
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Rellena un archivo phar a partir de un iterador. Dos estilos de iterador son soportados: los iteradores que hacen corresponder el nombre de archivo dentro del phar con el nombre de un archivo en el disco, y los iteradores como DirectoryIterator que devuelven objetos SplFileInfo. Para los iteradores que devuelven objetos SplFileInfo, el segundo parámetro es obligatorio.

## Parámetros

`iterator`  
Un iterador que asocia un archivo con una posición, o bien devuelve objetos SplFileInfo.

`baseDirectory`  
Para los iteradores que devuelven objetos SplFileInfo, la porción de ruta absoluta de cada archivo que debe ser eliminada al añadir al archivo phar.

## Valores devueltos

`Phar::buildFromIterator` devuelve un array asociativo que asocia la representación interna del archivo a un camino absoluto en el sistema.

## Errores/Excepciones

Este método emite una excepción `UnexpectedValueException` cuando el iterador devuelve valores falsos, tales como una clave entera en lugar de una cadena; una excepción `BadMethodCallException` cuando un iterador basado en SplFileInfo es pasado sin parámetro `baseDirectory`, o una excepción `PharException` si ha habido errores al guardar el archivo phar.

## Historial de cambios

| Versión | Descripción                                           |
|---------|-------------------------------------------------------|
| 8.1.0   | Phar::buildFromIterator ya no devuelve `false` ahora. |
| 8.0.0   | `baseDirectory` ahora es nullable.                    |

## Ejemplos

Ejemplo con `Phar::buildFromIterator` y SplFileInfo

Para la mayoría de archivos phar, el archivo refleja la estructura de un directorio, y el segundo estilo es el más útil. Por ejemplo, para crear un archivo phar que contenga los archivos de la estructura del directorio:

    /ruta/hacia/proyecto/
                     config/
                            dist.xml
                            debug.xml
                     lib/
                         file1.php
                         file2.php
                     src/
                         processthing.php
                     www/
                         index.php
                     cli/
                         index.php

       

Este código puede ser utilizado para añadir al archivo "proyecto.phar":

```
<?php
// crea con el alias "proyecto.phar"
$phar = new Phar('proyecto.phar', 0, 'proyecto.phar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new RecursiveDirectoryIterator('/ruta/hacia/proyecto')),
    '/ruta/hacia/proyecto');
$phar->setStub($phar->createDefaultStub('cli/index.php', 'www/index.php'));
?>

   
```php

El archivo proyecto.phar puede ser utilizado inmediatamente. `Phar::buildFromIterator` no establece parámetros tales como la compresión o los metadatos; esto puede ser hecho después de crear el archivo phar.

Es interesante notar que `Phar::buildFromIterator` también puede ser utilizado para copiar los elementos de un archivo phar existente, ya que el objeto Phar hereda de `DirectoryIterator`:

```
<?php
// crea con el alias "proyecto.phar"
$phar = new Phar('proyecto.phar', 0, 'proyecto.phar');
$phar->buildFromIterator(
    new RecursiveIteratorIterator(
     new Phar('/ruta/hacia/otrophar.phar')),
    'phar:///ruta/hacia/otrophar.phar/ruta/hacia/proyecto');
$phar->setStub($phar->createDefaultWebStub('cli/index.php', 'www/index.php'));
?>

   
```php

Ejemplo con `Phar::buildFromIterator` y otros iteradores

La segunda forma de iterador puede ser utilizada con cualquier iterador que devuelva una correspondencia clave =\> valor, tales como `ArrayIterator`:

```
<?php
// crea con el alias "proyecto.phar"
$phar = new Phar('proyecto.phar', 0, 'proyecto.phar');
$phar->buildFromIterator(
    new ArrayIterator(
     array(
        'interna/fichero.php' => dirname(__FILE__) . '/unfichero.php',
        'otro/fichero.jpg' => fopen('/ruta/hacia/grande.jpg', 'rb'),
     )));
$phar->setStub($phar->createDefaultWebStub('cli/index.php', 'www/index.php'));
?>

   
```php

## Véase también

`Phar::buildFromDirectory`
