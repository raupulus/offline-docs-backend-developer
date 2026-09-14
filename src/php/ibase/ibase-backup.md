---
title: ibase_backup
description: Inicia una tarea de respaldo en el gestor de servicios y devuelve inmediatamente
source_url: https://www.php.net/manual/es/function.ibase-backup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-backup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30120
---

ibase_backup

Inicia una tarea de respaldo en el gestor de servicios y devuelve inmediatamente

## Descripción

```php
ibase_backup(resource $service_handle, string $source_db, string $dest_file, [int $options], [bool $verbose]): mixed
```php

Esta función transmite los argumentos al servidor de base de datos (remoto). Allí, comienza un nuevo proceso de respaldo. Por consiguiente, no se obtendrá ninguna respuesta.

## Parámetros

`service_handle`  
Una conexión al servidor de base de datos creada previamente.

`source_db`  
La ruta absoluta hacia la base de datos en el servidor de base de datos. También se puede utilizar un alias de base de datos.

`dest_file`  
La ruta absoluta hacia el fichero de respaldo en el servidor de base de datos.

`options`  
Opciones adicionales a transmitir al servidor de base de datos para el respaldo. El parámetro `options` puede ser una combinación de las siguientes constantes: `IBASE_BKP_IGNORE_CHECKSUMS`, `IBASE_BKP_IGNORE_LIMBO`, `IBASE_BKP_METADATA_ONLY`, `IBASE_BKP_NO_GARBAGE_COLLECT`, `IBASE_BKP_OLD_DESCRIPTIONS`, `IBASE_BKP_NON_TRANSPORTABLE` o `IBASE_BKP_CONVERT`. Leer la sección sobre [???](#ibase.constants) para más información.

`verbose`  
Dado que el proceso de respaldo se realiza en el servidor de base de datos, no se tiene ninguna posibilidad de obtener su salida. Este argumento es inútil.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Dado que el proceso de respaldo se realiza en el servidor (remoto), esta función solo transmite los argumentos. Mientras los argumentos sean legales, no se obtendrá `false`.

## Ejemplos

Ejemplo con `ibase_backup`

```
<?php

// Adjuntar al servidor por dirección IP y puerto.
$service = ibase_service_attach ('10.1.11.200/3050', 'sysdba', 'masterkey');

// Iniciar el proceso de respaldo en el servidor de base de datos
// Respaldar la base de datos employee utilizando la ruta completa hacia /srv/backup/employees.fbk
// No utiliza argumentos especiales
ibase_backup($service, '/srv/firebird/employees.fdb', '/srv/backup/employees.fbk');

// Liberar la conexión adjunta
ibase_service_detach ($service);
?>

   
```php

Ejemplo de `ibase_backup` con argumentos

```
<?php

// Adjuntar al servidor por nombre y puerto por defecto
$service = ibase_service_attach ('fb-server.contoso.local', 'sysdba', 'masterkey');

// Iniciar el proceso de respaldo en el servidor de base de datos
// Respaldar la base de datos employee utilizando un alias hacia /srv/backup/employees.fbk.
// Respaldar solo los metadatos. No crear un respaldo transportable.
ibase_backup($service, 'employees.fdb', '/srv/backup/employees.fbk', IBASE_BKP_METADATA_ONLY | IBASE_BKP_NON_TRANSPORTABLE);

// Liberar la conexión adjunta
ibase_service_detach ($service);
?>

   
```php

## Véase también

ibase_restore
