---
title: SplFileObject::flock
description: Bloqueo de ficheros portable
source_url: https://www.php.net/manual/es/splfileobject.flock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/flock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 84390
---

SplFileObject::flock

Bloqueo de ficheros portable

## Descripción

```php
public SplFileObject::flock(int $operation, [int $wouldBlock]): bool
```php

Bloquea o desbloquea el fichero de la misma manera portable que `flock`.

## Parámetros

`operation`  
`operation` es una operación de las siguientes:

- `LOCK_SH` para adquirir un bloqueo compartido (lectura).

- `LOCK_EX` para adquirir un bloqueo exclusivo (escritura).

- `LOCK_UN` para liberar un bloqueo (compartido o exclusivo).

También es posible añadir `LOCK_NB` como máscara de bits a una de las operaciones anteriores, si `flock` no debe bloquearse durante el intento de bloqueo.

`wouldBlock`  
Establecer a `true` si el bloqueo hará que la función quede esperando (condición de errno EWOULDBLOCK).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de SplFileObject::flock

```
<?php
$file = new SplFileObject("/tmp/bloqueado.txt", "w");
if ($file->flock(LOCK_EX)) { // adquirir un bloqueo exclusivo
    $file->ftruncate(0);     // truncar el fichero
    $file->fwrite("Escribir alguna cosa\n");
    $file->flock(LOCK_UN);   // liberar el bloqueo
} else {
    echo "¡No se pudo obtener el bloqueo!";
}
?>

    
```php

## Véase también

`flock`
