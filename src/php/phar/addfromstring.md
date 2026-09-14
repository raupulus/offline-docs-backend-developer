---
title: Phar::addFromString
description: Añade un fichero desde un string al archivo phar
source_url: https://www.php.net/manual/es/phar.addfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/addFromString.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63890
---

Phar::addFromString

Añade un fichero desde un string al archivo phar

## Descripción

```php
public Phar::addFromString(string $localName, string $contents): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Esta función permite añadir cualquier string a un archivo phar. El fichero se almacenará en el archivo con `localname` como ruta. Esta función es idéntica a `ZipArchive::addFromString`.

## Parámetros

`localName`  
Ruta donde el fichero será almacenado en el archivo.

`contents`  
El contenido del fichero a almacenar

## Valores devueltos

No devuelve ningún valor, se lanza una excepción en caso de error.

## Ejemplos

Ejemplo con `Phar::addFromString`

```
<?php
try {
    $a = new Phar('/ruta/al/archivo.phar');

    $a->addFromString('ruta/al/fichero.txt', 'mi fichero simple');
    $b = $a['ruta/al/fichero.txt']->getContent();

    // para añadir contenido desde un descriptor de flujo para archivos grandes, utilice offsetSet()
    $c = fopen('/ruta/al/archivo_grande.bin');
    $a['archivo_grande.bin'] = $c;
    fclose($c);
} catch (Exception $e) {
    // manejo de errores aquí
}
?>

    
```php

## Notas

> [!NOTE]
> `Phar::addFile`, `Phar::addFromString` y `Phar::offsetSet` registran un nuevo archivo phar cada vez que son llamadas. Si las prestaciones son una preocupación, `Phar::buildFromDirectory` o `Phar::buildFromIterator` deberían ser utilizadas en su lugar.

## Véase también

`Phar::offsetSet`, `PharData::addFromString`, `Phar::addFile`, `Phar::addEmptyDir`
