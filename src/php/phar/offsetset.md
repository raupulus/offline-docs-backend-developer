---
title: Phar::offsetSet
description: Establece el contenido de un fichero interno en el archivo a partir del
  contenido de un fichero externo
source_url: https://www.php.net/manual/es/phar.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/offsetSet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64310
---

Phar::offsetSet

Establece el contenido de un fichero interno en el archivo a partir del contenido de un fichero externo

## Descripción

```php
public Phar::offsetSet(string $localName, resource $value): void
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Es una implementación de la interfaz ArrayAccess que permite la manipulación directa del contenido de un archivo Phar utilizando los corchetes de acceso al array. offsetSet se utiliza para modificar un fichero existente o para añadir un nuevo fichero al archivo Phar.

## Parámetros

`localName`  
El nombre del fichero (en ruta relativa) a buscar en el Phar.

`value`  
Contenido del fichero.

## Valores devueltos

No se devuelve ningún valor.

## Errores/Excepciones

Si [phar.readonly](#ini.phar.readonly) está a `1`, se lanza una excepción `BadMethodCallException`, ya que modificar un Phar solo es permitido cuando phar.readonly está a `0`. Se lanza una excepción `PharException` si ha habido un problema al escribir los cambios del archivo Phar en el disco.

## Ejemplos

Un ejemplo con `Phar::offsetSet`

offsetSet no debe ser accedido directamente, sino a través del operador de acceso al array, `[]`.

```
<?php
$p = new Phar('/ruta/al/mon.phar', 0, 'mon.phar');
try {
    // llama a offsetSet
    $p['fichero.txt'] = 'Hola';
} catch (Exception $e) {
    echo 'No puede modificar fichero.txt:', $e;
}
?>

    
```php

## Notas

> [!NOTE]
> `Phar::addFile`, `Phar::addFromString` y `Phar::offsetSet` registran un nuevo archivo phar cada vez que son llamadas. Si las prestaciones son una preocupación, `Phar::buildFromDirectory` o `Phar::buildFromIterator` deberían ser utilizadas en su lugar.

## Véase también

`Phar::offsetExists`, `Phar::offsetGet`, `Phar::offsetUnset`
