---
title: gzgetss
description: Obtiene la línea del apuntador al archivo gz y retira las etiquetas HTML
source_url: https://www.php.net/manual/es/function.gzgetss.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzgetss.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: cb3e68d99
order: 108820
---

gzgetss

Obtiene la línea del apuntador al archivo gz y retira las etiquetas HTML

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.3.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
gzgetss(resource $zp, int $length, [string $allowable_tags]): string
```php

Función identica a `gzgets`, excepto que `gzgetss` intenta retirar cualquier etiqueta HTML y PHP del texto que esta leyendo.

## Parámetros

`zp`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

`length`  
La longitud de los datos a obtener.

`allowable_tags`  
Se puede usar éste parámetro opcional para especificar cuales etiquetas no se deben retirar.

## Valores devueltos

La cadena descomprimida y sin etiquetas o `false` en caso de error.

## Ejemplos

Ejemplo de `gzgetss`

```
<?php
$handle = gzopen('somefile.gz', 'r');
while (!gzeof($handle)) {
   $buffer = gzgetss($handle, 4096);
   echo $buffer;
}
gzclose($handle);
?>

    
```php

## Véase también

`gzopen`, `gzgets`, `strip_tags`
