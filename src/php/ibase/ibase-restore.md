---
title: ibase_restore
description: Inicia una tarea de restauración en el gestor de servicios y devuelve
  inmediatamente
source_url: https://www.php.net/manual/es/function.ibase-restore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-restore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30490
---

ibase_restore

Inicia una tarea de restauración en el gestor de servicios y devuelve inmediatamente

## Descripción

```php
ibase_restore(resource $service_handle, string $source_file, string $dest_db, [int $options], [bool $verbose]): mixed
```php

Esta función transmite los argumentos al servidor de base de datos (remoto). Allí, comienza un nuevo proceso de restauración. Por lo tanto, no se obtendrá ninguna respuesta.

## Parámetros

`service_handle`  
Una conexión al servidor de base de datos creada previamente.

`source_file`  
La ruta absoluta en el servidor donde se encuentra el fichero de respaldo.

`dest_db`  
La ruta para crear la nueva base de datos en el servidor. También se puede utilizar un alias de base de datos.

`options`  
Opciones adicionales a transmitir al servidor de base de datos para la restauración. El parámetro `options` puede ser una combinación de las siguientes constantes: `IBASE_RES_DEACTIVATE_IDX`, `IBASE_RES_NO_SHADOW`, `IBASE_RES_NO_VALIDITY`, `IBASE_RES_ONE_AT_A_TIME`, `IBASE_RES_REPLACE`, `IBASE_RES_CREATE`, `IBASE_RES_USE_ALL_SPACE`, `IBASE_PRP_PAGE_BUFFERS`, `IBASE_PRP_SWEEP_INTERVAL`, `IBASE_RES_CREATE`. Leer la sección sobre [???](#ibase.constants) para más información.

`verbose`  
Dado que el proceso de restauración se realiza en el servidor de base de datos, no hay posibilidad de obtener su salida. Este argumento es inútil.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Dado que el proceso de restauración se realiza en el servidor (remoto), esta función solo transmite los argumentos. Mientras los argumentos sean legales, no se obtendrá `false`.

## Ejemplos

Ejemplo con `ibase_restore`

```
<?php
// Adjuntar al servidor por dirección IP y puerto.
$service = ibase_service_attach ('10.1.11.200/3050', 'sysdba', 'masterkey');

// Iniciar el proceso de restauración en el servidor de base de datos
// Restaurar el respaldo de employee a la nueva base de datos emps.fdb
// No utiliza argumentos especiales
ibase_restore($service, '/srv/backup/employees.fbk', '/srv/firebird/emps.fdb');

// Libera la conexión adjunta
ibase_service_detach ($service);
?>

   
```php

Ejemplo de `ibase_restore` con argumentos

```
<?php

// Adjuntar al servidor por nombre y puerto por defecto
$service = ibase_service_attach ('fb-server.contoso.local', 'sysdba', 'masterkey');

// Iniciar el proceso de restauración en el servidor de base de datos
// Restaurar la base de datos employee utilizando un alias.
// Restaurar sin índice, Reemplazar la base de datos existente.
ibase_restore($service, '/srv/backup/employees.fbk', 'employees.fdb', IBASE_RES_DEACTIVATE_IDX | IBASE_RES_REPLACE);

// Libera la conexión adjunta
ibase_service_detach ($service);
?>

   
```php

## Véase también

ibase_backup
