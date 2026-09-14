---
title: gzgetc
description: Obtiene el caracter donde está el apuntador al archivo gz
source_url: https://www.php.net/manual/es/function.gzgetc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzgetc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: 02ba67b51
order: 108800
---

gzgetc

Obtiene el caracter donde está el apuntador al archivo gz

## Descripción

```php
gzgetc(resource $stream): string
```php

Retorna una cadena que contiene un solo caracter (sin comprimir) leído del apuntador al archivo gz dado.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

## Valores devueltos

El caracter sin comprimir o `false` en caso de EOF (a diferencia de `gzeof`).

## Ejemplos

Ejemplo de `gzgetc`

```
<?php
$gz = gzopen('somefile.gz', 'r');
while (!gzeof($gz)) {
  echo gzgetc($gz);
}
gzclose($gz);
?>

    
```php

## Véase también

`gzopen`, `gzgets`
