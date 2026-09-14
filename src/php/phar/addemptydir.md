---
title: Phar::addEmptyDir
description: Añade un directorio vacío al archivo phar
source_url: https://www.php.net/manual/es/phar.addemptydir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/addEmptyDir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 63870
---

Phar::addEmptyDir

Añade un directorio vacío al archivo phar

## Descripción

```php
public Phar::addEmptyDir(string $directory): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Mediante este método se crea un directorio vacío con la ruta `dirname`. Este método es idéntico a `ZipArchive::addEmptyDir`.

## Parámetros

`directory`  
El nombre del directorio vacío a crear en el archivo phar

## Valores devueltos

No se devuelve ningún valor, se lanza una excepción en caso de error.

## Ejemplos

Un ejemplo con `Phar::addEmptyDir`

```
<?php
try {
    $a = new Phar('/ruta/al/archivo.phar');

    $a->addEmptyDir('/ruta/completa/al/fichero');
    // demuestra cómo se almacena el fichero
    $b = $a['ruta/completa/al/fichero']->isDir();
} catch (Exception $e) {
    // maneja los errores aquí
}
?>

    
```php

## Véase también

`PharData::addEmptyDir`, `Phar::addFile`, `Phar::addFromString`
