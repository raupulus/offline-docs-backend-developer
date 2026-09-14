---
title: wincache_unlock
description: Libera un bloqueo exclusivo sobre una clave dada
source_url: https://www.php.net/manual/es/function.wincache-unlock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-unlock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 8b6d16942
order: 101810
---

wincache_unlock

Libera un bloqueo exclusivo sobre una clave dada

## Descripción

```php
wincache_unlock(string $key): bool
```php

Libera un bloqueo exclusivo que se obtuvo en una clave dada mediante `wincache_lock`. Si cualquier otro proceso fue bloqueado en espera de el bloqueo en esta clave, este proceso será capaz de obtener el bloqueo.

> [!WARNING]
> Usando `wincache_lock` y `wincache_unlock` puede causar bloqueos al ejecutar los scripts PHP en un entorno de multi-proceso, como FastCGI. No utilice estas funciones a menos que esté absolutamente seguro de que necesitan para su uso. Para la mayoría de las operaciones en la caché de usuario no es necesario el uso de estas funciones.

## Parámetros

`key`  
Nombre de la llave en la caché para liberar el bloqueo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Usar `wincache_unlock`

```
<?php
$fp = fopen("/tmp/lock.txt", "r+");
if (wincache_lock(“lock_txt_lock”)) { // hacer un bloqueo exclusivo
    ftruncate($fp, 0); // truncate file
    fwrite($fp, "Escribir algo aquí\n");
    wincache_unlock(“lock_txt_lock”); // liberar el bloqueo
} else {
    echo "No se pudo obtener el bloqueo!";
}
fclose($fp);
?>

    
```php

## Véase también

`wincache_lock`, `wincache_ucache_set`, `wincache_ucache_get`, `wincache_ucache_delete`, `wincache_ucache_clear`, `wincache_ucache_exists`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`
