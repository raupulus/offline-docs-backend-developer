---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/fileinfo.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/fileinfo/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: fileinfo
translation_status: ready
translation_reviewed: false
translation_revision: 4968cab7d
order: 23130
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`FILEINFO_NONE` (`int`)  
No se realiza ningún tratamiento especial.

`FILEINFO_SYMLINK` (`int`)  
Sigue los enlaces simbólicos.

`FILEINFO_MIME_TYPE` (`int`)  
Devuelve el tipo MIME.

`FILEINFO_MIME_ENCODING` (`int`)  
Devuelve la codificación MIME del fichero.

`FILEINFO_MIME` (`int`)  
Devuelve el tipo MIME y la codificación MIME, tal como se describe en la RFC 2045.

`FILEINFO_COMPRESS` (`int`)  
Descomprime los ficheros comprimidos.

Desactivado debido a las consecuencias en la seguridad de los hilos.

`FILEINFO_DEVICES` (`int`)  
Examina los contenidos de los bloques o dispositivos especiales de caracteres.

`FILEINFO_CONTINUE` (`int`)  
Devuelve todos los datos encontrados, no solo el primero.

`FILEINFO_PRESERVE_ATIME` (`int`)  
Si es posible, conserva el tiempo de acceso al fichero original.

`FILEINFO_RAW` (`int`)  
No traduce los caracteres no imprimibles a representación octal `\ooo`.

`FILEINFO_EXTENSION` (`int`)  
Devuelve la extensión de fichero apropiada para un tipo MIME detectado en el fichero.

Para los tipos que generalmente tienen múltiples extensiones de fichero, tales como las imágenes `JPEG`, el valor devuelto es varias extensiones separadas por una barra oblicua, por ejemplo: `"jpeg/jpg/jpe/jfif"`. Para los tipos desconocidos no disponibles en la base de datos `magic.mime`, el valor devuelto es `"???"`.

Disponible a partir de PHP 7.2.0.

`FILEINFO_APPLE` (`int`)  
Devuelve el creador y tipo de Apple.
