---
title: feof
description: Prueba el final del archivo
source_url: https://www.php.net/manual/es/function.feof.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/feof.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23400
---

feof

Prueba el final del archivo

## Descripción

```php
feof(resource $stream): bool
```php

Prueba el final del archivo.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

## Valores devueltos

Retorna `true` si el puntero `handle` está al final del archivo o si ocurre un error, de lo contrario, retorna `false`.

## Notas

> [!WARNING]
> Si una conexión abierta con `fsockopen` no es cerrada por el servidor, `feof` se bloqueará. Para evitar este comportamiento, consulte el ejemplo a continuación:
>
> <div class="example">
>
> <div class="title">
>
> Gestión de tiempos de espera excedidos `feof`
>
> </div>
>
> ```
> <?php
> function safe_feof($fp, &$start = NULL) {
>  $start = microtime(true);
>
>  return feof($fp);
> }
>
> /* Supongamos que $fp fue previamente abierto por fsockopen() */
>
> $start = NULL;
> $timeout = ini_get('default_socket_timeout');
>
> while(!safe_feof($fp, $start) && (microtime(true) - $start) < $timeout)
> {
>  /* Gestión */
> }
> ?>
>
>      
> ```
>
> </div>

> [!WARNING]
> Si el puntero de archivo pasado no es válido, se obtendrá un bucle infinito ya que `feof` fallará al retornar `true`.
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo con `feof` y un puntero de archivo inválido
>
> </div>
>
> ```
> <?php
> // Si el archivo no puede ser leído o no existe, la función fopen retorna FALSE
> $file = @fopen("no_such_file", "r");
>
> // FALSE proveniente de fopen emitirá una advertencia y causará un bucle infinito aquí
> while (!feof($file)) {
> }
>
> fclose($file);
> ?>
>
>      
> ```
>
> </div>
