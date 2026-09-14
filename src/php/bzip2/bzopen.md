---
title: bzopen
description: Abre un archivo comprimido con bzip2
source_url: https://www.php.net/manual/es/function.bzopen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bzip2/functions/bzopen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bzip2
translation_status: ready
translation_reviewed: true
translation_revision: 5fdeb11b1
order: 6470
---

bzopen

Abre un archivo comprimido con bzip2

## Descripción

```php
bzopen(string $file, string $mode): resource
```php

`bzopen` abre un archivo bzip2 (`.bz2`) en modo escritura o lectura.

## Parámetros

`file`  
El nombre del fichero a abrir o un recurso de flujo existente.

`mode`  
Los modos `'r'` (para lectura), y `'w'` (para escritura) son soportados. Cualquier otra opción hará que la función `bzopen` retorne `false`.

## Valores devueltos

Si la apertura falla, `bzopen` retorna `false`, de lo contrario, retorna un puntero al fichero abierto.

## Ejemplos

Ejemplo con `bzopen`

```
<?php

$file = "/tmp/foo.bz2";
$bz = bzopen($file, "r") or die("Imposible abrir el fichero $file para lectura");

bzclose($bz);

?>

   
```php

## Véase también

bzclose
