---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration74.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration74/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 740
---

## Otros cambios

## Mejora del Rendimiento

### Núcleo de PHP

Se ha añadido un opcode de VM especializado para la función `array_key_exists`, lo que mejora el rendimiento de esta función si puede resolverse estáticamente. En el código bajo un espacio de nombres, esto puede requerir escribir `\array_key_exists()` o importar explícitamente la función.

### Expresiones Regulares (Compatible con Perl)

Cuando `preg_match` en modo UTF-8 (modificador `"u"`) se llama repetidamente sobre la misma `string` (pero posiblemente en diferentes posiciones), solo se verificará una vez para la validez UTF-8.

## Cambios en la Gestión de Archivos INI

[zend.exception_ignore_args](#ini.zend.exception-ignore-args) es una nueva directiva INI para incluir o excluir los argumentos de las trazas de pila generadas por las excepciones.

[opcache.preload_user](#ini.opcache.preload-user) es una nueva directiva INI que permite especificar la cuenta de usuario que tiene el rol de ejecutar el código precargado (el usuario root no está permitido por razones de seguridad).

## Migración a pkg-config

Se ha migrado un número de extensiones para usar exclusivamente pkg-config para la detección de dependencias de bibliotecas. Generalmente, esto significa que en lugar de usar `--with-foo-dir=DIR` o similar, solo se usa `--with-foo`. Las rutas de bibliotecas personalizadas pueden especificarse agregando directorios adicionales a `PKG_CONFIG_PATH` o especificando las opciones de compilación explícitamente a través de `FOO_CFLAGS` y `FOO_LIBS`.

Las siguientes extensiones y SAPIs están afectadas:

- CURL:

  - `--with-curl` ya no acepta un directorio.

- Enchant:

  - `--with-enchant` ya no acepta un directorio.

- FPM:

  - `--with-fpm-systemd` ahora usa solo pkg-config para las verificaciones de libsystem. La versión mínima de libsystemd requerida es 209.

- GD:

  - `--with-gd` se convierte en `--enable-gd` (para habilitar la extensión) y `--with-external-gd` (para optar por usar una libgd externa, en lugar de la proporcionada).

  - `--with-png-dir` ha sido eliminado. libpng es requerido.

  - `--with-zlib-dir` ha sido eliminado. zlib es requerido.

  - `--with-freetype-dir` se convierte en `--with-freetype`

  - `--with-jpeg-dir` se convierte en `--with-jpeg`

  - `--with-webp-dir` se convierte en `--with-webp`

  - `--with-xpm-dir` se convierte en `--with-xpm`

- IMAP:

  - `--with-kerberos-systemd` ya no acepta un directorio.

- Intl:

  - `--with-icu-dir` ha sido eliminado. Si se pasa `--enable-intl`, entonces libicu siempre es requerido.

- LDAP:

  - `--with-ldap-sasl` ya no acepta un directorio.

- Libxml:

  - `--with-libxml-dir` ha sido eliminado.

  - `--enable-libxml` se convierte en `--with-libxml`.

  - `--with-libexpat-dir` ha sido renombrado a `--with-expat` y ya no acepta un directorio.

- LiteSpeed:

  - `--with-litespeed` se convierte en `--enable-litespeed`.

- Mbstring:

  - `--with-onig` ha sido eliminado. A menos que se pase `--disable-mbregex`, libonig es requerido.

- ODBC:

  - `--with-iodbc` ya no acepta un directorio.

  - `--with-unixODBC` sin un directorio ahora usa phg-config (preferible). El directorio aún se acepta para versiones antiguas sin libodbc.pc.

- OpenSSL:

  - `--with-openssl` ya no acepta un directorio.

- PCRE:

  - `--with-pcre-regex` ha sido eliminado. En su lugar, `--with-external-pcre` se ofrece para optar por usar una biblioteca PCRE externa, en lugar de la proporcionada.

- PDO_SQLite:

  - `--with-pdo-sqlite` ya no acepta un directorio.

- Readline:

  - `--with-libedit` ya no acepta un directorio.

- Sodium:

  - `--with-sodium` ya no acepta un directorio.

- SQLite3:

  - `--with-sqlite3` ya no acepta un directorio.

- XSL:

  - `--with-xsl` ya no acepta un directorio.

- Zip:

  - `--with-libzip` ha sido eliminado.

  - `--enable-zip` se convierte en `--with-zip`.

## Escape de CSV

`fputcsv`, `fgetcsv`, SplFileObject::fputcsv, SplFileObject::fgetcsv, y SplFileObject::setCsvControl ahora aceptan una `string` vacía como argumento `$escape`, lo que desactiva el mecanismo de escape propietario de PHP.

El comportamiento de `str_getcsv` se ha ajustado en consecuencia (anteriormente, una `string` vacía era igual a usar los valores por defecto).

SplFileObject::getCsvControl ahora también puede devolver una `string` vacía para el tercer elemento del `array`.

## Filtrado de Datos

La extensión [filter](#book.filter) ya no expone `--with-pcre-dir` para los builds Unix y ahora puede compilarse de manera confiable como compartida al usar `./configure`

## GD

El comportamiento de `imagecropauto` en la biblioteca libgd proporcionada se ha sincronizado con el de libgd del sistema:

- `IMG_CROP_DEFAULT` ya no se repliega en `IMG_CROP_SIDES`

- El umbral de recorte (Threshold-cropping) ahora usa el algoritmo de libgd del sistema.

El parámetro por defecto `$mode` de `imagecropauto` se ha cambiado a `IMG_CROP_DEFAULT`; proporcionar `-1` ahora está obsoleto.

`imagescale` ahora soporta la preservación de la relación de aspecto al escalar a una altura fija pasando `-1` a `$new_width`.

## HASH (framework de resúmenes de mensaje)

La extensión [hash](#book.hash) ya no puede ser desactivada y siempre forma parte de cualquier build de PHP, similar a la extensión [date](#book.datetime).

## Intl

La extensión [intl](#book.intl) ahora requiere al menos ICU 50.1.

`ResourceBundle` ahora implementa Countable.

## Protocolo Ligero de Acceso a Directorios (LDAP)

Se ha eliminado el soporte para nsldap y umich_ldap.

## Libxml

Todas las extensiones basadas en libxml requieren libxml 2.7.6 o superior.

## Cadenas Multibyte

La biblioteca oniguruma ya no se proporciona con PHP; en su lugar, libonig debe estar disponible en el sistema. Alternativamente, `--disable-mbregex` puede usarse para desactivar el componente mbregex.

## OPcache

Las opciones de configuración `--disable-opcache-file` y `--enable-opcache-file` han sido eliminadas en favor de la directiva INI [opcache.file_cache](#ini.opcache.file-cache).

## Hash de Contraseña

Las funciones `password_hash` y `password_needs_rehash` ahora aceptan `string` y `int` nullable para el argumento `$algo`.

## PEAR

La instalación de PEAR (incluido PECL) ya no está habilitada por defecto. Esto puede habilitarse explícitamente usando `--with-pear`. Esta opción está obsoleta y podría eliminarse en el futuro.

## Reflection

Los valores numéricos de las constantes de modificador (`IS_ABSTRACT`, `IS_DEPRECATED`, `IS_EXPLICIT_ABSTRACT`, `IS_FINAL`, `IS_IMPLICIT_ABSTRACT`, `IS_PRIVATE`, `IS_PROTECTED`, `IS_PUBLIC`, y `IS_STATIC`) en las clases `ReflectionClass`, `ReflectionFunction`, `ReflectionMethod`, `ReflectionObject`, y `ReflectionProperty` han sido modificados.

## SimpleXML

`SimpleXMLElement` ahora implementa Countable.

## SQLite3

La biblioteca libsqlite integrada ha sido eliminada. Para compilar la extensión [SQLite3](#book.sqlite3) ahora se requiere una libsqlite3 ≥ 3.7.4 del sistema. Para compilar la extensión [PDO_SQLite](#ref.pdo-sqlite) ahora se requiere una libsqlite3 ≥ 3.5.0 del sistema.

La serialización y deserialización de `SQLite3`, `SQLite3Stmt` y `SQLite3Result` ahora está explícitamente prohibida. Anteriormente, la serialización de instancias de estas clases era posible, pero la deserialización generaba objetos inutilizables.

La notación `@param` ahora puede usarse para denotar los parámetros de consulta SQL.

## Zip

La biblioteca libzip integrada ha sido eliminada. Ahora se requiere una libzip \>= 0.11 del sistema para compilar la extensión [zip](#book.zip).
