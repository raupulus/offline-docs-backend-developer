---
title: sapi_windows_vt100_support
description: Obtiene o define el soporte VT100 para el flujo especificado asociado
  a un búfer de salida de una consola Windows.
source_url: https://www.php.net/manual/es/function.sapi-windows-vt100-support.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/sapi-windows-vt100-support.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 426d9a8f1
order: 47220
---

sapi_windows_vt100_support

Obtiene o define el soporte VT100 para el flujo especificado asociado a un búfer de salida de una consola Windows.

## Descripción

```php
sapi_windows_vt100_support(resource $stream, [bool $enable]): bool
```php

Si `enable` es `null`, la función retorna `true` si el flujo `stream` tiene los códigos de control VT100 activados, de lo contrario `false`.

Si `enable` es un `bool`, la función intentará activar o desactivar las funcionalidades VT100 del flujo `stream`. Si la funcionalidad ha sido activada (o desactivada) con éxito, la función retornará `true`, o `false` en caso contrario.

Al inicio, PHP intenta activar la funcionalidad VT100 de los flujos `STDOUT`/`STDERR`. Por cierto, si estos flujos son redirigidos a un fichero, las funcionalidades VT100 pueden no ser activadas.

Si el soporte VT100 está activado, es posible utilizar secuencias de control tal como son conocidas por el terminal VT100. Estas permiten la modificación de la salida del terminal. En Windows, estas secuencias son llamadas secuencias de terminal virtual de consola (Console Virtual Terminal Sequences).

> [!WARNING]
> Esta función utiliza el flag `ENABLE_VIRTUAL_TERMINAL_PROCESSING` implementado en la API de Windows 10, por lo que la funcionalidad VT100 puede no estar disponible en versiones antiguas de Windows.

## Parámetros

`stream`  
El flujo sobre el cual la función operará.

`enable`  
Si es `bool`, la funcionalidad VT100 será activada (si es `true`) o desactivada (si es `false`).

## Valores devueltos

Si `enable` es `null`: retorna `true` si la funcionalidad VT100 está activada, de lo contrario `false`.

Si `enable` es un `bool`: Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `enable` ahora es nullable. |

## Ejemplos

Estado por defecto de `sapi_windows_vt100_support`

Por omisión, `STDOUT` y `STDERR` tienen la funcionalidad VT100 activada.

```
    php -r "var_export(sapi_windows_vt100_support(STDOUT));echo ' ';var_export(sapi_windows_vt100_support(STDERR));"
   
```php

Resultado del ejemplo anterior es similar a:

    true true

       

Además, si un flujo es redirigido, la funcionalidad VT100 no será activada:

```
    php -r "var_export(sapi_windows_vt100_support(STDOUT));echo ' ';var_export(sapi_windows_vt100_support(STDERR));" 2>NUL
   
```php

Resultado del ejemplo anterior es similar a:

        true false

`sapi_windows_vt100_support` cambiando el estado

No será posible activar la funcionalidad VT100 de `STDOUT` o `STDERR` si el flujo es redirigido.

```
    php -r "var_export(sapi_windows_vt100_support(STDOUT, true));echo ' ';var_export(sapi_windows_vt100_support(STDERR, true));" 2>NUL
   
```php

Resultado del ejemplo anterior es similar a:

    true false

Ejemplo de uso con soporte VT100 activado

```
<?php
$out = fopen('php://stdout','w');
fwrite($out, 'Just forgot a lettr.');
// mueve el cursor dos caracteres hacia atrás
fwrite($out, "\033[2D");
// Inserta un espacio, desplazando el texto existente hacia la derecha -> Just forgot a lett r.
fwrite($out, "\033[1@");
fwrite($out, 'e');
?>

   
```php

El ejemplo anterior mostrará:

    Just forgot a letter.
