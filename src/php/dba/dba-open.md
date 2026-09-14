---
title: dba_open
description: Abre una base de datos DBA
source_url: https://www.php.net/manual/es/function.dba-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dba/functions/dba-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dba
translation_status: ready
translation_revision: b5fce74a6
order: 11620
---

dba_open

Abre una base de datos DBA

## Descripción

```php
dba_open(string $path, string $mode, [string $handler], [int $permission], [int $map_size], [int $flags]): Dba\Connection
```php

`dba_open` establece una conexión a la base identificada por `path` con el modo `mode` y el identificador `handler`.

## Parámetros

`path`  
Ruta en el sistema de archivos.

`mode`  
Puede ser `r` para solo lectura, `w` para lectura/escritura, `c` para lectura/escritura y creación si la base no existe, y `n` para creación, sobrescritura y acceso en lectura/escritura. La base de datos se crea en modo BTree; los otros modos (como Hash o Queue) no son soportados.

Además, se puede elegir el método de bloqueo de la base con el carácter siguiente. Utilice `l` para bloquear la base con un fichero `.lck`, o `d` para bloquear la base misma. Es importante que las aplicaciones utilicen estas opciones de manera coherente.

Si se desea probar la posibilidad de acceso sin esperar la disponibilidad del bloqueo, se puede añadir la letra `t` como tercer carácter. Cuando se está absolutamente seguro de que la base no requiere bloqueo, se puede utilizar el guión `-` en lugar de `l` o `d`. Cuando no se utiliza ni `d`, ni `l` ni `-`, dba bloqueará en modo `d`.

> [!NOTE]
> Solo puede haber un tipo de escritura en la base. Cuando se utiliza dba en un servidor web, y varias peticiones HTTP realizan escrituras, estas solo pueden realizarse una tras otra. De igual manera, la lectura durante la escritura no es posible. La extensión dba utiliza un bloqueo para evitar estos problemas. A continuación se muestra la tabla de bloqueo:
>
> | ya abierta | `mode` = "rl" | `mode` = "rlt" | `mode` = "wl" | `mode` = "wlt" | `mode` = "rd" | `mode` = "rdt" | `mode` = "wd" | `mode` = "wdt" |
> |----|----|----|----|----|----|----|----|----|
> | no abierta | ok | ok | ok | ok | ok | ok | ok | ok |
> | `mode` = "rl" | ok | ok | esperando | `false` | ilegal | ilegal | ilegal | ilegal |
> | `mode` = "wl" | esperando | `false` | esperando | `false` | ilegal | ilegal | ilegal | ilegal |
> | `mode` = "rd" | ilegal | ilegal | ilegal | ilegal | ok | ok | esperando | `false` |
> | `mode` = "wd" | ilegal | ilegal | ilegal | ilegal | esperando | `false` | esperando | `false` |
>
> Bloqueo DBA
>
> ok: La segunda llamada tiene éxito., esperando: La segunda llamada espera a que `dba_close` sea llamada por el primer script., false: La segunda llamada devuelve `false`., ilegal: No se deben mezclar las opciones `"l"` y `"d"` para el parámetro `mode`.

`handler`  
El nombre del [gestor](#dba.requirements) que debe ser utilizado para acceder a `path`. Se pasa a todos los parámetros opcionales dados a `dba_open` y puede actuar en su nombre. Si el parámetro `handler` es `null`, entonces se invoca el gestor por defecto.

`permission`  
Parámetro opcional de tipo `int` que se pasa al controlador. Tiene el mismo significado que el parámetro `permissions` de la función `chmod`, y tiene un valor por omisión de `0644`.

Los controladores `db1`, `db2`, `db3`, `db4`, `dbm`, `gdbm`, Los controladores `ndbm` y `lmdb` soportan el parámetro `permission`.

El controlador `lmdb` soporta dos parámetros adicionales. El primero permite definir el `$filemode` (ver descripción anterior), y el segundo permite definir la `$mapsize`, cuyo valor debería ser un múltiplo del tamaño de página del sistema operativo, o cero para utilizar la mapsize por defecto. El parámetro `$mapsize` es soportado a partir de PHP 7.3.14 y 7.4.2, respectivamente.

`map_size`  
Parámetro opcional de tipo `int` que se pasa al controlador. Su valor debe ser un múltiplo del tamaño de página del sistema operativo, o cero para utilizar el tamaño de mappage por defecto.

Solo el controlador `lmdb` acepta el parámetro `map_size`.

`flags`  
Bandera a pasar a los controladores de base de datos. Si es `null`, se proporcionarán las banderas por defecto. Actualmente, solo el controlador LMDB soporta las siguientes banderas: `DBA_LMDB_USE_SUB_DIR` y `DBA_LMDB_NO_SUB_DIR`.

## Valores devueltos

Devuelve una instancia `Dba\Connection` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

`false` es devuelto y se emite un error de nivel `E_WARNING` cuando el parámetro `handler` es `null`, pero no hay ningún gestor por defecto disponible.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora devuelve una instancia de `Dba\Connection`; anteriormente se devolvía un `resource`. |
| 8.2.0 | Se añade el parámetro `flags`. |
| 8.2.0 | El parámetro `handler` ahora es nullable. |
| 7.3.14, 7.4.2 | El controlador `lmdb` ahora soporta un parámetro adicional `map_size`. |

## Véase también

dba_popen

dba_close
