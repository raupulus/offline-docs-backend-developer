---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration72.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration72/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 87b582706
order: 580
---

## Otros cambios

## Traslado de `utf8_encode` y `utf8_decode`

Las funciones `utf8_encode` y `utf8_decode` han sido trasladadas a la extensión estándar como funciones de string, mientras que antes la extensión [XML](#book.xml) era requerida para que estuvieran disponibles.

## Cambio para `mail` y `mb_send_mail`

El parámetro \$additional_headers de `mail` y `mb_send_mail` acepta ahora un `array` en lugar de un `string`.

## Soporte de LMDB

La extensión [DBA](#book.dba) ahora soporta LMDB.

## Modificaciones en el sistema de construcción de PHP

- Unix: Autoconf 2.64 o superior es ahora necesario para construir PHP.

- Unix: El argumento de configuración `--with-pdo-oci` ya no necesita la versión de Oracle Instant Client.

- Unix: El argumento de configuración `--enable-gd-native-ttf` ha sido eliminado. No ha sido utilizado desde PHP 5.5.0.

- Windows: El argumento de configuración `--with-config-profile` ha sido añadido. Esto puede ser utilizado para guardar configuraciones específicas, un poco como el fichero mágico `config.nice.bat`.

## Cambio en [GD](#book.image)

- `imageantialias` está también disponible si se construye con libgd del sistema.

- `imagegd` almacena imágenes TrueColor como imágenes TrueColor reales. Anteriormente, eran convertidas a paleta.

## Traslado de [MCrypt](#book.mcrypt) a PECL

La extensión [MCrypt](#book.mcrypt) ha sido trasladada del núcleo a PECL. Dado que la biblioteca mcrypt no ha visto actualizaciones desde 2007, su uso está fuertemente desaconsejado. En su lugar, debe utilizarse [OpenSSL](#book.openssl) o la extensión [Sodium](#book.sodium).

## `session_module_name`

Pasar `"user"` a `session_module_name` ahora provoca un error de nivel `E_RECOVERABLE_ERROR`. Anteriormente, esto era ignorado silenciosamente.
