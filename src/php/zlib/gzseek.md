---
title: gzseek
description: Ubica el apuntador a un archivo gz
source_url: https://www.php.net/manual/es/function.gzseek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzseek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 02ba67b51
order: 108890
---

gzseek

Ubica el apuntador a un archivo gz

## Descripción

```php
gzseek(resource $stream, int $offset, [int $whence]): int
```php

Establece el indicador de posición para el apuntador al archivo dado en el desplazamiento de bytes fijado en el flujo del archivo. Es equivalente a llamar (en C) a `gzseek(zp, offset, SEEK_SET)`.

Si el archivo está abierto para lectura, ésta función es emulada pero puede ser extremadamente lenta. Si el archivo está abierto para escritura, sólo está soportada la búsqueda hacia adelante; entonces `gzseek` comprime una secuencia de ceros hasta la nueva posición de inicio.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

`offset`  
El desplazamiento buscado.

`whence`  
Los valores de `whence` son: `SEEK_SET` - Establece la posición igual al `offset` de bytes., `SEEK_CUR` - Establece la posición en la posición actual más el `offset`.

Si `whence` no se especifica, se asume que es `SEEK_SET`.

## Valores devueltos

En caso de éxito, retorna 0; en caso contrario, devuelve -1. Notese que buscar pasado el EOF no es considerado un error.

## Ejemplos

Ejamplo de `gzseek`

```
<?php
$gz = gzopen('somefile.gz', 'r');
gzseek($gz,2);
echo gzgetc($gz);
gzclose($gz);
?>

    
```php

## Véase también

`gztell`, `gzrewind`
