---
title: Phar::delete
description: Elimina un fichero dentro de un archivo phar
source_url: https://www.php.net/manual/es/phar.delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 64060
---

Phar::delete

Elimina un fichero dentro de un archivo phar

## Descripción

```php
public Phar::delete(string $localName): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Elimina un fichero dentro de un archivo phar. Es equivalente a la llamada a `unlink` en un contexto de flujo, como se describe en el siguiente ejemplo...

## Parámetros

`localName`  
Ruta del fichero a eliminar dentro del archivo.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Genera una excepción `PharException` si se producen errores durante la escritura en el disco.

## Ejemplos

Un ejemplo con `Phar::delete`

```
<?php
try {
    $phar = new Phar('monphar.phar');
    $phar->delete('efface/moi.php');
    // es equivalente a:
    unlink('phar://monphar.phar/efface/moi.php');
} catch (Exception $e) {
    // manejo de errores
}
?>

    
```php

## Véase también

`PharData::delete`, `Phar::unlinkArchive`
