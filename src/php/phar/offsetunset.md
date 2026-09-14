---
title: Phar::offsetUnset
description: Elimina un fichero de un phar
source_url: https://www.php.net/manual/es/phar.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/offsetUnset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64320
---

Phar::offsetUnset

Elimina un fichero de un phar

## Descripción

```php
public Phar::offsetUnset(string $localName): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Esta es una implementación de la interfaz ArrayAccess que permite la manipulación directa del contenido de un archivo Phar utilizando los corchetes de acceso al array. offsetUnset se utiliza para eliminar un fichero existente y es llamado por la función `unset`.

## Parámetros

`localName`  
El nombre del fichero (en ruta relativa) a buscar en el Phar.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Si [phar.readonly](#ini.phar.readonly) está a `1`, se lanza una excepción `BadMethodCallException`, ya que modificar un Phar solo es permitido cuando phar.readonly está a `0`. Se lanza una excepción `PharException` si ha habido un problema al escribir los cambios del archivo Phar en el disco.

## Ejemplos

Un ejemplo con `Phar::offsetUnset`

```
<?php
$p = new Phar('/ruta/al/mon.phar', 0, 'mon.phar');
try {
    // elimina archivo.txt de mon.phar llamando a offsetUnset
    unset($p['archivo.txt']);
} catch (Exception $e) {
    echo 'No se puede eliminar archivo.txt: ', $e;
}
?>

    
```php

## Véase también

`Phar::offsetExists`, `Phar::offsetGet`, `Phar::offsetSet`, `Phar::unlinkArchive`, `Phar::delete`
