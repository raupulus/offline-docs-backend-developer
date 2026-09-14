---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/filesystem.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 68ca0a46a
order: 23260
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SEEK_SET` (`int`)  

`SEEK_CUR` (`int`)  

`SEEK_END` (`int`)  

`LOCK_SH` (`int`)  

`LOCK_EX` (`int`)  

`LOCK_UN` (`int`)  

`LOCK_NB` (`int`)  

<!-- -->

`FILE_USE_INCLUDE_PATH` (`int`)  
Busca el `filename` en [include_path](#ini.include-path).

`FILE_NO_DEFAULT_CONTEXT` (`int`)  

`FILE_APPEND` (`int`)  
Añade contenido a un archivo existente.

`FILE_IGNORE_NEW_LINES` (`int`)  
Quita caracteres EOL.

`FILE_SKIP_EMPTY_LINES` (`int`)  
Salta líneas vacías.

`FILE_BINARY` (`int`)  
Modo texto

> [!WARNING]
> Esta constante no tiene efecto, y está obsoleta a partir de PHP 8.1.0.

`FILE_TEXT` (`int`)  
Text mode.

> [!WARNING]
> Esta constante no tiene efecto, y está obsoleta a partir de PHP 8.1.0.

<!-- -->

`GLOB_AVAILABLE_FLAGS` (`int`)  
Todas las flags `GLOB_*` combinadas. Equivalente a `0` \| `GLOB_BRACE` \| `GLOB_MARK` \| `GLOB_NOSORT` \| `GLOB_NOCHECK` \| `GLOB_NOESCAPE` \| `GLOB_ERR` \| `GLOB_ONLYDIR`

`GLOB_BRACE` (`int`)  
Expande {a,b,c} para coincidir con 'a', 'b' o 'c'.

> [!NOTE]
> `GLOB_BRACE` no está disponible en algunos systemas non GNU, como Solaris o Alpine Linux.

`GLOB_ERR` (`int`)  
Detenerse ante errores de lectura (como directorios ilegibles), por defecto los errores son ignorados.

`GLOB_MARK` (`int`)  
Añade una barra (una barra invertida en Windows) a cada directorio devuelto.

`GLOB_NOCHECK` (`int`)  
Devolver el patrón de búsqueda si no se encontraron archivos que coincidan con él.

`GLOB_NOESCAPE` (`int`)  
Las barras invertidas no citan metacaracteres.

`GLOB_NOSORT` (`int`)  
Devolver los archivos tal como aparecen en el directorio (sin ordenar). Cuando no se usa este falg, los nombres de ruta se ordenan alfabéticamente.

`GLOB_ONLYDIR` (`int`)  
Devolver solo las entradas de directorio que coincidan con el patrón.

<!-- -->

`PATHINFO_ALL` (`int`)  
Todas las partes de pathinfo son devueltas como un array asociativo.

`PATHINFO_DIRNAME` (`int`)  
La ruta del directorio o archivo.

`PATHINFO_BASENAME` (`int`)  
El nombre del directorio o el nombre y la extensión del archivo.

`PATHINFO_EXTENSION` (`int`)  
La extensión del archivo.

`PATHINFO_FILENAME` (`int`)  
El nombre del archivo (sin la extensión) o del directorio.

<!-- -->

`INI_SCANNER_NORMAL` (`int`)  
Modo de escaneo INI normal.

`INI_SCANNER_RAW` (`int`)  
Modo de escaneo INI en bruto (RAW).

`INI_SCANNER_TYPED` (`int`)  
Modo de escaneo INI tipado.

<!-- -->

`FNM_NOESCAPE` (`int`)  
Deshabilita el escapado de la barra invertida.

`FNM_PATHNAME` (`int`)  
Una barra en un string sólo concide con otra en el patrón dado.

`FNM_PERIOD` (`int`)  
Un punto en un string debe coincidir exactamente con otro en el patrón dado.

`FNM_CASEFOLD` (`int`)  
Comparación insensible a mayúsculas-minúsculas. Parte de la extensión GNU.

<!-- -->

`UPLOAD_ERR_CANT_WRITE` (`int`)  
Error al escribir el archivo en el disco. El valor de la constante es `7`.

`UPLOAD_ERR_EXTENSION` (`int`)  
Una extensión de PHP detuvo la subida del archivo. PHP no proporciona una forma de determinar qué extensión causó la detención de la subida del archivo; examinar la lista de extensiones cargadas con `phpinfo` puede ayudar. El valor de la constante es `8`.

`UPLOAD_ERR_FORM_SIZE` (`int`)  
El archivo subido excede la directiva *MAX_FILE_SIZE* especificada en el formulario HTML. El valor de la constante es `2`.

`UPLOAD_ERR_INI_SIZE` (`int`)  
El archivo subido excede la directiva [upload_max_filesize](#ini.upload-max-filesize) en `php.ini`. El valor de la constante es `1`.

`UPLOAD_ERR_NO_FILE` (`int`)  
No se ha subido ningún archivo. El valor de la constante es `4`.

`UPLOAD_ERR_NO_TMP_DIR` (`int`)  
Directorio temporal no encontrado. El valor de la constante es `6`.

`UPLOAD_ERR_OK` (`int`)  
No hay error, el archivos se ha subido correctamente. El valor de la constante es `0`.

`UPLOAD_ERR_PARTIAL` (`int`)  
El archivo solo se ha subido parcialmente. El valor de la constante es `3`.
