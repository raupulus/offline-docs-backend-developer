---
title: mcrypt_generic
description: Cifra los datos
source_url: https://www.php.net/manual/es/function.mcrypt-generic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-generic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45850
---

mcrypt_generic

Cifra los datos

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_generic(resource $td, string $data): string
```php

`mcrypt_generic` cifra los datos `data`. Los datos se completan con "`\0`" para obtener un tamaño múltiplo del tamaño de un bloque. Devuelve los datos cifrados. Tenga en cuenta que la longitud del string devuelto puede ser más larga que la pasada como argumento, debido al relleno.

Si se desea almacenar los datos cifrados en una base de datos asegúrese de almacenar el string completo devuelto por esta función, de lo contrario el string no se descifrará correctamente. Si el string original contiene 10 caracteres y el tamaño de un bloque es de 8 (utilice `mcrypt_enc_get_block_size` para determinar este tamaño), se necesitará al menos 16 caracteres en el campo de la base de datos. Tenga en cuenta que el string devuelto por `mdecrypt_generic` tendrá 16 caracteres de longitud... utilice `rtrim($str, "\0")` para eliminar el relleno.

Por ejemplo, si se almacenan los datos en una base de datos MySQL, recuerde que los campos de tipo VARCHAR eliminan automáticamente los espacios adicionales durante la inserción. Como los datos cifrados pueden terminar con un espacio (ASCII 32), los datos se dañarán por esta eliminación. Almacene los datos en un campo de tipo TINYBLOB/TINYTEXT (o más grande) para que todo funcione normalmente.

## Parámetros

`td`  
El recurso de cifrado.

El manejador de cifrado `td` debe ser inicializado con la función `mcrypt_generic_init`, con una clave y un VI, antes de llamar a esta función. Cuando el cifrado se realiza, se deben liberar los buffers llamando a la función `mcrypt_generic_deinit`. Consulte `mcrypt_module_open` para un ejemplo.

`data`  
Los datos a cifrar.

## Valores devueltos

Devuelve los datos cifrados.

## Véase también

mdecrypt_generic

mcrypt_generic_init

mcrypt_generic_deinit
