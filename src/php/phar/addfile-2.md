---
title: PharData::addFile
description: Añade un fichero del sistema de archivos al archivo tar/zip
source_url: https://www.php.net/manual/es/phardata.addfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/addFile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64450
---

PharData::addFile

Añade un fichero del sistema de archivos al archivo tar/zip

## Descripción

```php
public PharData::addFile(string $filename, [string $localName]): void
```php

Con este método, cualquier fichero o URL puede ser añadido al archivo tar/zip. Si el segundo argumento opcional `localname` es especificado, el fichero será almacenado en el archivo con este nombre, de lo contrario el argumento `file` es utilizado como ruta hacia donde almacenar el fichero dentro de el archivo. Las URLs deben tener un nombre local de lo contrario se lanza una excepción. Este método es idéntico a `ZipArchive::addFile`.

## Parámetros

`filename`  
Ruta relativa o absoluta hacia un fichero del disco a añadir al archivo phar.

`localName`  
Ruta hacia donde el fichero será almacenado dentro del archivo.

## Valores devueltos

No se devuelve ningún valor, se lanza una excepción en caso de fallo.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `localName` ahora es nullable. |

## Ejemplos

Un ejemplo con `PharData::addFile`

```
<?php
try {
    $a = new PharData('/ruta/al/archivo.tar');

    $a->addFile('/ruta/completa/al/fichero');
    // muestra cómo el fichero es almacenado
    $b = $a['ruta/completa/al/fichero']->getContent();

    $a->addFile('/ruta/completa/al/fichero', 'mi/fichero.txt');
    $c = $a['mi/fichero.txt']->getContent();

    // muestra el uso de URLs
    $a->addFile('http://www.ejemplo.com', 'ejemplo.html');
} catch (Exception $e) {
    // los errores son manejados aquí
}
?>

    
```php

## Notas

> [!NOTE]
> `PharData::addFile`, `PharData::addFromString` y `PharData::offsetSet` registran un nuevo archivo phar cada vez que son llamadas. Si las prestaciones son una preocupación, `PharData::buildFromDirectory` o `PharData::buildFromIterator` deberían ser utilizadas en su lugar.

## Véase también

`PharData::offsetSet`, `Phar::addFile`, `PharData::addFromString`, `PharData::addEmptyDir`
