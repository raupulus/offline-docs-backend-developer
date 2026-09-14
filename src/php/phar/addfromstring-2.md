---
title: PharData::addFromString
description: Añade un fichero a partir de un string al archivo tar/zip
source_url: https://www.php.net/manual/es/phardata.addfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/addFromString.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: true
translation_revision: '887736980'
order: 64460
---

PharData::addFromString

Añade un fichero a partir de un string al archivo tar/zip

## Descripción

```php
public PharData::addFromString(string $localName, string $contents): void
```php

Añade un string al archivo tar/zip. El fichero será almacenado en el archivo con la ruta `localname`. Este método es idéntico a `ZipArchive::addFromString`.

## Parámetros

`localName`  
Ruta hacia la cual el fichero será almacenado dentro del archivo.

`contents`  
El contenido del fichero a almacenar

## Valores devueltos

No hay valor de retorno, se lanza una excepción en caso de fallo.

## Ejemplos

Ejemplo con `PharData::addFromString`

```
<?php
try {
    $a = new PharData('/ruta/versus/mon.tar');

    $a->addFromString('ruta/versus/fichero.txt', 'mi fichero simple');
    $b = $a['ruta/versus/fichero.txt']->getContent();

    // para añadir contenido a partir de un manejador de flujo para archivos grandes, utilice offsetSet()
    $c = fopen('/ruta/versus/grandearchivo.bin');
    $a['grandearchivo.bin'] = $c;
    fclose($c);
} catch (Exception $e) {
    // los errores son tratados aquí
}
?>

    
```php

## Notas

> [!NOTE]
> `Phar::addFile`, `Phar::addFromString` y `Phar::offsetSet` registran un nuevo archivo phar cada vez que son llamadas. Si las prestaciones son una preocupación, `Phar::buildFromDirectory` o `Phar::buildFromIterator` deberían ser utilizadas en su lugar.

## Véase también

`PharData::offsetSet`, `Phar::addFromString`, `PharData::addFile`, `PharData::addEmptyDir`
