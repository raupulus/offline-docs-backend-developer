---
title: ftp://
description: Acceso a URLs FTP(s)
source_url: https://www.php.net/manual/es/wrappers.ftp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/wrappers/ftp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 8bc832a46
order: 4650
---

ftp://

ftps://

Acceso a URLs FTP(s)

## Descripción

Permite el acceso en lectura a los ficheros existentes, y la creación de ficheros, mediante FTP. Si el servidor no soporta FTP en modo pasivo, la conexión fallará.

Se pueden abrir ficheros en lectura o en escritura, pero no ambas a la vez. Si el fichero remoto ya existe en el servidor ftp y se intenta abrirlo en escritura sin haber especificado la opción `overwrite` en el contexto, la conexión fallará. Si se deben sobrescribir ficheros existentes utilizando ftp, se debe especificar la opción `overwrite` en el contexto y abrir el fichero en escritura. Alternativamente, se puede utilizar la [extensión FTP](#ref.ftp).

Si se ha definido la directiva [from](#ini.from) en el fichero `php.ini`, entonces este valor será enviado como contraseña para los accesos FTP anónimos.

## Uso

- `ftp://example.com/pub/fichero.txt`

- `ftp://user:password@example.com/pub/fichero.txt`

- `ftps://example.com/pub/fichero.txt`

- `ftps://user:password@example.com/pub/fichero.txt`

## Opciones

| Atributo | Soportado |
|----|----|
| Restringido por [allow_url_fopen](#ini.allow-url-fopen) | Sí |
| Permite la lectura | Sí |
| Permite la escritura | Sí (nuevos ficheros/ficheros existentes con el parámetro `overwrite`) |
| Permite el añadido | Sí |
| Permite la lectura y escritura simultáneamente | No |
| Soporte de la función `stat` | `filesize`, `filetype`, `file_exists`, `is_file`, `is_dir`, y `filemtime` únicamente. |
| Soporte de la función `unlink` | Sí |
| Soporte de la función `rename` | Sí |
| Soporte de la función `mkdir` | Sí |
| Soporte de la función `rmdir` | Sí |

Resumen de la envoltura {role="stream_wrapper"}

## Notas

> [!NOTE]
> FTPS solo es soportado cuando la extensión [openssl](#book.openssl) está activa.
>
> Si el servidor no soporta SSL, entonces la conexión pasará automáticamente a una conexión ftp no cifrada.

> [!NOTE]
> El añadido de información a un fichero es posible con el gestor de URL `ftp://`.

## Véase también
