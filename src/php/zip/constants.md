---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/zip.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 108010
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`ZipArchive` usa constantes de clase. Existen varios tipos de constantes, los principales son: Flags (prefijadas con `FL_`), Flags globales (prefijadas con `AFL_`), errores (prefijados con `ER_`) y modos (sin prefijo).

`ZipArchive::CREATE` (`int`)  
Crea el archivo si no existe.

`ZipArchive::OVERWRITE` (`int`)  
Si existe un archivo, ignora su contenido actual. En otras palabras, lo trata de la misma manera que un archivo vacío.

`ZipArchive::EXCL` (`int`)  
Error si el fichero ya existe.

`ZipArchive::RDONLY` (`int`)  
Abrir archivo en modo de solo lectura. Disponible a partir de PHP 7.4.3 y PECL zip 1.17.1, respectivamente, si se compila con libzip ≥ 1.0.0.

`ZipArchive::CHECKCONS` (`int`)  
Realiza comprobaciones de coherencia adicionales al archivo, producirá un error si falla.

<!-- -->

`ZipArchive::AFL_RDONLY` (`int`)  
Archivo en modo de solo lectura, no se puede borrar. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.0, respectivamente, si se compila con libzip ≥ 1.10.0.

`ZipArchive::AFL_IS_TORRENTZIP` (`int`)  
Sl archivo actual está comprimido en torrentzip. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.0, respectivamente, si se compila con libzip ≥ 1.10.0.

`ZipArchive::AFL_WANT_TORRENTZIP` (`int`)  
Crear archivo en formato torrentzip. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.0, respectivamente, si se compila con libzip ≥ 1.10.0.

`ZipArchive::AFL_CREATE_OR_KEEP_FILE_FOR_EMPTY_ARCHIVE` (`int`)  
No eliminar archivo si el archivo está vacío. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.0, respectivamente, si se compila con libzip ≥ 1.10.0.

<!-- -->

`ZipArchive::FL_NOCASE` (`int`)  
Ignorar mayúsculas el lookup del nombre

`ZipArchive::FL_NODIR` (`int`)  
Ignorar el componente directorio

`ZipArchive::FL_COMPRESSED` (`int`)  
Leer datos comprimidos

`ZipArchive::FL_UNCHANGED` (`int`)  
Usar los datos originales, ignorando cambios.

`ZipArchive::FL_RECOMPRESS` (`int`)  
Forzar la recompresión de los datos. Disponible a partir de PHP 8.0.0 y PECL zip 1.18.0. Obsoleto a partir de PHP 8.3.0 y PECL zip 1.22.1, será eliminado en una futura versión de libzip.

`ZipArchive::FL_ENCRYPTED` (`int`)  
Leer datos encriptados (implica FL_COMPRESSED). Disponible a partir de PHP 8.0.0 y PECL zip 1.18.0.

`ZipArchive::FL_OVERWRITE` (`int`)  
Si existe un archivo con nombre, sobrescríbalo (reemplácelo). Disponible a partir de PHP 8.0.0 y PECL zip 1.18.0.

`ZipArchive::FL_LOCAL` (`int`)  
En la cabecera local. Disponible a partir de PHP 8.0.0 y PECL zip 1.18.0.

`ZipArchive::FL_CENTRAL` (`int`)  
En el directorio central. Disponible a partir de PHP 8.0.0 y PECL zip 1.18.0.

`ZipArchive::FL_ENC_GUESS` (`int`)  
Codificación de la cadena de suposición (guess string) (predeterminado). Disponible a partir de PHP 7.0.8.

`ZipArchive::FL_ENC_RAW` (`int`)  
Obtener la cadena sin modificaciones. Disponible a partir de PHP 7.0.8.

`ZipArchive::FL_ENC_STRICT` (`int`)  
Seguir la especificación estrictamente. Disponible a partir de PHP 7.0.8.

`ZipArchive::FL_ENC_UTF_8` (`int`)  
La cadena está codificada en UTF-8. Disponible a partir de PHP 7.0.8.

`ZipArchive::FL_ENC_CP437` (`int`)  
La cadena está codifica en CP437. Disponible a partir de PHP 7.0.8.

`ZipArchive::FL_OPEN_FILE_NOW` (`int`)  
Abre el archivo cuando se añade en lugar de esperar a que se cierre el archivo comprimido. Tenga en cuenta el consumo de descriptores de archivo. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.1.

<!-- -->

`ZipArchive::CM_DEFAULT` (`int`)  
Mejor para desinflar o almacenar.

`ZipArchive::CM_STORE` (`int`)  
almacenar (no comprimir).

`ZipArchive::CM_SHRINK` (`int`)  
Reducir

`ZipArchive::CM_REDUCE_1` (`int`)  
reducido con factor 1

`ZipArchive::CM_REDUCE_2` (`int`)  
reducido con factor 2

`ZipArchive::CM_REDUCE_3` (`int`)  
reducido con factor 3

`ZipArchive::CM_REDUCE_4` (`int`)  
reducido con factor 4

`ZipArchive::CM_IMPLODE` (`int`)  
implodado

`ZipArchive::CM_DEFLATE` (`int`)  
Deflactado

`ZipArchive::CM_DEFLATE64` (`int`)  
deflate64

`ZipArchive::CM_PKWARE_IMPLODE` (`int`)  
PKWARE imploding

`ZipArchive::CM_BZIP2` (`int`)  
Algoritmo BZIP2

`ZipArchive::CM_LZMA` (`int`)  
Algoritmo LZMA

`ZipArchive::CM_LZMA2` (`int`)  
Algoritmo LZMA2. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.0, respectivamente, si se compila con libzip ≥ 1.6.0.

`ZipArchive::CM_ZSTD` (`int`)  
Algoritmo Zstandard. Disponible a partir de PHP 8.0.0 y PECL zip 1.19.1, respectivamente, si se compila con libzip ≥ 1.8.0.

`ZipArchive::CM_XZ` (`int`)  
Algoritmo XZ. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente, si se compila con libzip ≥ 1.6.0.

`ZipArchive::CM_TERSE` (`int`)  

`ZipArchive::CM_LZ77` (`int`)  

`ZipArchive::CM_WAVPACK` (`int`)  

`ZipArchive::CM_PPMD` (`int`)  

<!-- -->

`ZipArchive::ER_OK` (`int`)  
Sin errores.

`ZipArchive::ER_MULTIDISK` (`int`)  
Archivos zip multi-disk no soportados.

`ZipArchive::ER_RENAME` (`int`)  
Mantener fichero temporal fallado.

`ZipArchive::ER_CLOSE` (`int`)  
Cerrar fichero zip fallado.

`ZipArchive::ER_SEEK` (`int`)  
Buscar error

`ZipArchive::ER_READ` (`int`)  
Leer error

`ZipArchive::ER_WRITE` (`int`)  
Escribir error

`ZipArchive::ER_CRC` (`int`)  
Error CRC

`ZipArchive::ER_ZIPCLOSED` (`int`)  
Conteniendo el fichero zip que ha sido cerrado

`ZipArchive::ER_NOENT` (`int`)  
No existe el fichero.

`ZipArchive::ER_EXISTS` (`int`)  
El fichero ya existe

`ZipArchive::ER_OPEN` (`int`)  
No se puede abrir el fichero

`ZipArchive::ER_TMPOPEN` (`int`)  
Fallo al intentar crear fichero temporal.

`ZipArchive::ER_ZLIB` (`int`)  
Error de Zlib

`ZipArchive::ER_MEMORY` (`int`)  
Error de asignación de memoria

`ZipArchive::ER_CHANGED` (`int`)  
La entrada a cambiado

`ZipArchive::ER_COMPNOTSUPP` (`int`)  
Método de compresión no soportado.

`ZipArchive::ER_EOF` (`int`)  
EOF precoz.

`ZipArchive::ER_INVAL` (`int`)  
Argumento inválido

`ZipArchive::ER_NOZIP` (`int`)  
No es un archivo zip

`ZipArchive::ER_INTERNAL` (`int`)  
Error interno

`ZipArchive::ER_INCONS` (`int`)  
Fichero Zip inconsistente

`ZipArchive::ER_REMOVE` (`int`)  
No se puede eliminar el fichero

`ZipArchive::ER_DELETED` (`int`)  
La entrada ha sido eliminada

`ZipArchive::ER_ENCRNOTSUPP` (`int`)  
No se admite el método de cifrado. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente.

`ZipArchive::ER_RDONLY` (`int`)  
Archivo de sólo lectura. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente.

`ZipArchive::ER_NOPASSWD` (`int`)  
No se ha proporcionado ninguna contraseña. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente.

`ZipArchive::ER_WRONGPASSWD` (`int`)  
Contraseña incorrecta proporcionada. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente.

`ZipArchive::ER_OPNOTSUPP` (`int`)  
Operación no soportada. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente, si se compila con libzip ≥ 1.0.0.

`ZipArchive::ER_INUSE` (`int`)  
Recurso todavía en uso. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente, si se compila con libzip ≥ 1.0.0.

`ZipArchive::ER_TELL` (`int`)  
Diga error. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente, si se compila con libzip ≥ 1.0.0.

`ZipArchive::ER_COMPRESSED_DATA` (`int`)  
Los datos comprimidos no son válidos. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente, si se compila con libzip ≥ 1.6.0.

`ZipArchive::ER_CANCELLED` (`int`)  
Operación cancelada. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.1, respectivamente, si se compila con libzip ≥ 1.6.0.

`ZipArchive::ER_DATA_LENGTH` (`int`)  
Longitud de datos inesperada. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.0, respectivamente, si se compila con libzip ≥ 1.10.0.

`ZipArchive::ER_NOT_ALLOWED` (`int`)  
No permitido en torrentzip. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.0, respectivamente, si se compila con libzip ≥ 1.10.0.

`ZipArchive::ER_TRUNCATED_ZIP` (`int`)  
Archivo zip posiblemente truncado o corrupto. Disponible a partir de PHP 8.4.0 y PECL zip 1.22.4, respectivamente, si se compila contra libzip ≥ 1.11.1.

<!-- -->

`ZipArchive::EM_NONE` (`int`)  
No hay encriptación. Disponible a partir de PHP 7.2.0 y PECL zip 1.14.0, respectivamente.

`ZipArchive::EM_TRAD_PKWARE` (`int`)  
Cifrado tradicional PKWARE. Disponible a partir de PHP 8.0.0 y PECL zip 1.19.0, respectivamente.

`ZipArchive::EM_AES_128` (`int`)  
Encriptación AES 128. Disponible a partir de PHP 7.2.0 y PECL zip 1.14.0, respectivamente, si se compila con libzip ≥ 1.2.0.

`ZipArchive::EM_AES_192` (`int`)  
Encriptación AES 192. Disponible a partir de PHP 7.2.0 y PECL zip 1.14.0, respectivamente, si se compila con libzip ≥ 1.2.0.

`ZipArchive::EM_AES_256` (`int`)  
Encriptación AES 256. Disponible a partir de PHP 7.2.0 y PECL zip 1.14.0, respectivamente, si se compila con libzip ≥ 1.2.0.

`ZipArchive::EM_UNKNOWN` (`int`)  
Algoritmo de cifrado desconocido. Disponible a partir de PHP 8.0.0 y PECL zip 1.19.0, respectivamente.

<!-- -->

`ZipArchive::LENGTH_TO_END` (`int`)  
Usa el tamaño del archivo; si el archivo crece, los datos adicionales se ignoran; si el archivo se reduce, se genera un error (`ZipArchive::ER_DATA_LENGTH`). Disponible a partir de PHP 8.3.0 y PECL zip 1.22.2.

`ZipArchive::LENGTH_UNCHECKED` (`int`)  
Usa todos los datos disponibles. Disponible a partir de PHP 8.3.0 y PECL zip 1.22.2, si se compila con libzip ≥ 1.10.1.

<!-- -->

`ZipArchive::LIBZIP_VERSION` (`string`)  
Versión de la biblioteca Zip. Disponible a partir de PHP 7.4.3 y PECL zip 1.16.0.

<!-- -->

`ZipArchive::OPSYS_DOS` (`int`)  

`ZipArchive::OPSYS_AMIGA` (`int`)  

`ZipArchive::OPSYS_OPENVMS` (`int`)  

`ZipArchive::OPSYS_UNIX` (`int`)  

`ZipArchive::OPSYS_VM_CMS` (`int`)  

`ZipArchive::OPSYS_ATARI_ST` (`int`)  

`ZipArchive::OPSYS_OS_2` (`int`)  

`ZipArchive::OPSYS_MACINTOSH` (`int`)  

`ZipArchive::OPSYS_Z_SYSTEM` (`int`)  

`ZipArchive::OPSYS_CPM` (`int`)  

`ZipArchive::OPSYS_WINDOWS_NTFS` (`int`)  

`ZipArchive::OPSYS_MVS` (`int`)  

`ZipArchive::OPSYS_VSE` (`int`)  

`ZipArchive::OPSYS_ACORN_RISC` (`int`)  

`ZipArchive::OPSYS_VFAT` (`int`)  

`ZipArchive::OPSYS_ALTERNATE_MVS` (`int`)  

`ZipArchive::OPSYS_BEOS` (`int`)  

`ZipArchive::OPSYS_TANDEM` (`int`)  

`ZipArchive::OPSYS_OS_400` (`int`)  

`ZipArchive::OPSYS_OS_X` (`int`)  

`ZipArchive::OPSYS_DEFAULT` (`int`)  
Disponible a partir de PECL zip 1.12.4.
