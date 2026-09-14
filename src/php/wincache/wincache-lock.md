---
title: wincache_lock
description: Obtiene un bloqueo exclusivo en una clave dada
source_url: https://www.php.net/manual/es/function.wincache-lock.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-lock.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_revision: b8758b060
order: 101620
---

wincache_lock

Obtiene un bloqueo exclusivo en una clave dada

## Descripción

```php
wincache_lock(string $key, [bool $isglobal]): bool
```php

Obtiene un bloqueo exclusivo sobre una clave dada. La ejecución del script actual quedará en espera que se pueda obtener el bloqueo. Una vez obtenido el bloqueo, el otro script que intente solicitar dicho bloqueo utilizando la misma clave quedará en espera, hasta que el script actual libere el bloqueo con `wincache_unlock`.

> [!WARNING]
> El uso de `wincache_lock` y `wincache_unlock` puede causar bloqueos de punto muerto al ejecutar scripts de PHP en un entorno multiproceso como FastCGI. No emplear estas funciones a menos que se esté absolutamente seguro de que son necesarias. Para la mayoría de las operaciones en la caché de usuario no es necesario usar estas funciones.

## Parámetros

`key`  
Nombre de la clave en la caché para adquirir el bloqueo.

`isglobal`  
Controla si el ámbito del bloqueo es a nivel de sistema o local. Los bloqueos locales tienen alcance para la «pool» de la aplicación en el caso de FastCGI de IIS o a todos los procesos de php que tengan el mismo identificador de proceso padre.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Empleo de `wincache_lock`

```
<?php
$fp = fopen("/tmp/lock.txt", "r+");
if (wincache_lock(“lock_txt_lock”)) { // realizar un bloqueo exclusivo
    ftruncate($fp, 0); // truncate file
    fwrite($fp, "Write something here\n");
    wincache_unlock(“lock_txt_lock”); // liberar el bloqueo
} else {
    echo "No se pudo obtener el bloqueo";
}
fclose($fp);
?>

    
```php

## Véase también

`wincache_unlock`, `wincache_ucache_set`, `wincache_ucache_get`, `wincache_ucache_delete`, `wincache_ucache_clear`, `wincache_ucache_exists`, `wincache_ucache_meminfo`, `wincache_ucache_info`, `wincache_scache_info`
