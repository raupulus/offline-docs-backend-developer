---
title: gzeof
description: Prueba de apuntador para EOF de archivo gz
source_url: https://www.php.net/manual/es/function.gzeof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzeof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: 02ba67b51
order: 108780
---

gzeof

Prueba de apuntador para

EOF

de archivo gz

## Descripción

```php
gzeof(resource $stream): bool
```php

Prueba el apuntador de archivo GZ dado en busca del EOF (fin de archivo).

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

## Valores devueltos

Retorna `true` si el apuntador GZ está al EOF del archivo o si ocurrió un error; de lo contrario retorna `false`.

## Ejemplos

Ejemplo de `gzeof`

```
<?php
$gz = gzopen('somefile.gz', 'r');
while (!gzeof($gz)) {
  echo gzgetc($gz);
}
gzclose($gz);
?>

    
```php
