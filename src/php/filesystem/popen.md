---
title: popen
description: Crea un puntero de archivo de proceso
source_url: https://www.php.net/manual/es/function.popen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/popen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23930
---

popen

Crea un puntero de archivo de proceso

## Descripción

```php
popen(string $command, string $mode): resource
```php

Crea un puntero de archivo de proceso, ejecutado mediante un fork de la orden proporcionada por el argumento `command`.

## Parámetros

`command`  
La orden

`mode`  
El modo. Puede ser `'r'` para lectura, o `'w'` para escritura.

En Windows, `popen` utiliza el modo texto por defecto, es decir, todo carácter `\n` escrito o leído del pipe será traducido a `\r\n`. Si esto no es deseado, el modo binario puede ser forzado definiendo el `mode` a `'rb'` y `'wb'`, respectivamente.

## Valores devueltos

Devuelve un puntero de archivo idéntico al devuelto por `fopen`, excepto que será unidireccional (solo lectura, o solo escritura), y debe ser cerrado mediante `pclose`. Este puntero puede ser utilizado con `fgets`, `fgetss` y `fwrite`. Cuando el modo es 'r', el puntero de archivo devuelto equivale al STDOUT de la orden, y cuando el modo es 'w', el puntero de archivo devuelto equivale al STDIN de la orden.

Si ocurre un error, la función devolverá `false`.

## Ejemplos

Ejemplo con `popen`

```
<?php
$handle = popen("/bin/ls", "r");
?>

    
```php

Si la orden a ejecutar no ha podido ser encontrada, se devolverá un recurso válido. Esto puede parecer extraño, pero es práctico. Esto permite acceder a los mensajes de error que han sido devueltos por el Shell:

Ejemplo con `popen`

```
<?php
error_reporting(E_ALL);

/* Añade una redirección para que pueda leer stderr. */
$handle = popen('/path/to/executable 2>&1', 'r');
echo "'$handle'; " . gettype($handle) . "\n";
$read = fread($handle, 2096);
echo $read;
pclose($handle);
?>

    
```php

## Notas

> [!NOTE]
> Si se desea un soporte bidireccional (two-way), utilice la función `proc_open`.

## Véase también

`pclose`, `fopen`, `proc_open`
