---
title: dio_open
description: Abre (crea si fuera necesario) un fichero a un nivel más bajo que el
  permitido por flujos de entrada y salida de las bibliotecas en C
source_url: https://www.php.net/manual/es/function.dio-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: e2f2172bf
order: 11870
---

dio_open

Abre (crea si fuera necesario) un fichero a un nivel más bajo que el permitido por flujos de entrada y salida de las bibliotecas en C

## Descripción

```php
dio_open(string $filename, int $flags, [int $mode]): resource
```php

`dio_open` abre un fichero y devuelve su descriptor de fichero.

## Parámetros

`filename`  
Ruta del fichero a abrir.

`flags`  
El parámetro `flags` es una máscara OR de bits compuesta a partir de las siguientes banderas. Estos valores *tienen* que incluir alguno de entre `O_RDONLY`, `O_WRONLY`, o `O_RDWR`. Además, podría incluir cualquier combinación del resto de banderas de la lista.

- `O_RDONLY` - abre el fichero con acceso de lectura.

- `O_WRONLY` - abre el fichero con acceso de escritura.

- `O_RDWR` - abre el fichero con acceso de lectura y de escritura.

- `O_CREAT` - crea el fichero, si no existiera ya.

- `O_EXCL` - si tanto `O_CREAT` como `O_EXCL` están habilitados, y el fichero existe, `dio_open` fallará.

- `O_TRUNC` - si el fichero existe, y está abierto con sólo escritura, se truncará a cero.

- `O_APPEND` - las operaciones de escritura añaden los datos al final del fichero.

- `O_NONBLOCK` - asigna el modo no bloqueante.

- `O_NOCTTY` - previene que el SO asigne al fichero abierto como el terminal controlador del proceso cuando se abra un fichero de dispositivo TTY.

`mode`  
Si `flags` contiene `O_CREAT`, `mode` establecerá los permisos del ficher (permisos de creación). `mode` es necesario para un correcto funcionamiento cuando `O_CREAT` se especifica en `flags`, y se ignorará en cualquier otro caso.

Los permisos que realmente se asignan al fichero creado se verán afectados por el *umask* del proceso, como suele suceder.

## Valores devueltos

Descriptor de fichero o `false` en caso de error.

## Ejemplos

Abrir un descriptor de fichero

```
<?php

$fd = dio_open('/dev/ttyS0', O_RDWR | O_NOCTTY | O_NONBLOCK);

dio_close($fd);
?>

   
```php

## Véase también

`dio_close`
