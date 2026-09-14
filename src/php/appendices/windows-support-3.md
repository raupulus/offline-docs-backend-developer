---
title: Soporte para Windows
source_url: https://www.php.net/manual/es/migration74.windows-support.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration74/windows-support.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: eee245cdb
order: 760
---

## Soporte para Windows

## Flags `configure`

`configure` soporta las variables de entorno `CFLAGS` y `LDFLAGS`.

## Manejo CTRL

<span class="keycombo"> +CTRL+ +C+ </span> y <span class="keycombo"> +CTRL+ +BREAK+ </span> en la consola pueden ser definidos estableciendo un manejador con la función `sapi_windows_set_ctrl_handler`.

La opción "create_process_group" puede ser pasada a `proc_open` en Windows. Es necesaria si el proceso hijo está destinado a manejar los eventos CTRL.

## OPcache

OPcache ahora soporta un número arbitrario de caches separados por usuario a través de la directiva INI `opcache.cache-id`. Todos los procesos con el mismo identificador de cache y el mismo usuario comparten una instancia OPcache.

## stat

La implementación de stat ha sido refactorizada.

- Un número de inode es proporcionado y se basa en el índice de fichero NTFS.

- El número del dispositivo ahora se basa en el número de serie del volumen.

Tenga en cuenta que ambos valores son derivados del sistema y proporcionados tal cual en sistemas de 64 bits. En sistemas de 32 bits, estos valores pueden exceder el integer de 32 bits en PHP, por lo que son falsos.

## libsqlite3

libsqlite3 ya no se compila estáticamente en `php_sqlite3.dll` y `php_pdo_sqlite.dll`, sino que está disponible como `libsqlite3.dll`. Referirse a las instrucciones de instalación de [SQLite3](#sqlite3.installation) y [PDO_SQLITE](#ref.pdo-sqlite.installation), respectivamente.
