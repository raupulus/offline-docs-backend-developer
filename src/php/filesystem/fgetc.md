---
title: fgetc
description: Lee un carácter en un fichero
source_url: https://www.php.net/manual/es/function.fgetc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fgetc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23420
---

fgetc

Lee un carácter en un fichero

## Descripción

```php
fgetc(resource $stream): string
```php

Lee un carácter en un fichero.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

## Valores devueltos

Devuelve una cadena que contiene un solo carácter, leído desde el fichero apuntado por `stream`. Devuelve `false` al final del fichero.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Ejemplo con `fgetc`

```
<?php
$fp = fopen('somefile.txt', 'r');
if (!$fp) {
    echo 'No es posible abrir el fichero somefile.txt';
}
while (false !== ($char = fgetc($fp))) {
    echo "$char\n";
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`fread`, `fopen`, `popen`, `fsockopen`, `fgets`
