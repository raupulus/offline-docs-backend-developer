---
title: Phar::addFile
description: Añade un fichero del sistema de ficheros al archivo phar
source_url: https://www.php.net/manual/es/phar.addfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/addFile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63880
---

Phar::addFile

Añade un fichero del sistema de ficheros al archivo phar

## Descripción

```php
public Phar::addFile(string $filename, [string $localName]): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Mediante este método, cualquier fichero o URL puede ser añadido al archivo phar. Si el segundo parámetro opcional `localName` es un `string`, el fichero será almacenado en el archivo con ese nombre, de lo contrario el parámetro `filename` se utiliza como ruta hacia donde almacenar el archivo. Las URL deben ser locales, de lo contrario se lanza una excepción. Este método es idéntico a `ZipArchive::addFile`.

## Parámetros

`filename`  
Ruta absoluta o relativa hacia un fichero del disco a añadir al archivo phar.

`localName`  
Ruta donde el fichero será almacenado en el archivo.

## Valores devueltos

No hay valor de retorno, se lanza una excepción en caso de fallo.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `localName` ahora es nullable. |

## Ejemplos

Un ejemplo con `Phar::addFile`

```
<?php
try {
    $a = new Phar('/ruta/al/phar.phar');

    $a->addFile('/ruta/completa/al/fichero');
    // demuestra cómo el fichero es almacenado
    $b = $a['ruta/completa/al/fichero']->getContent();

    $a->addFile('/ruta/completa/al/fichero', 'mi/fichero.txt');
    $c = $a['mi/fichero.txt']->getContent();

    // demuestra el uso de URL
    $a->addFile('http://www.ejemplo.com', 'ejemplo.html');
} catch (Exception $e) {
    // maneja los errores aquí
}
?>

    
```php

## Notas

> [!NOTE]
> `Phar::addFile`, `Phar::addFromString` y `Phar::offsetSet` registran un nuevo archivo phar cada vez que son llamadas. Si las prestaciones son una preocupación, `Phar::buildFromDirectory` o `Phar::buildFromIterator` deberían ser utilizadas en su lugar.

## Véase también

`Phar::offsetSet`, `PharData::addFile`, `Phar::addFromString`, `Phar::addEmptyDir`
