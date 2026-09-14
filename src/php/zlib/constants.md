---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/zlib.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: ac6c09ba8
order: 108680
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`FORCE_GZIP` (`int`)  

`FORCE_DEFLATE` (`int`)  

`ZLIB_ENCODING_RAW` (`int`)  
Algoritmo DEFLATE según RFC 1951.

`ZLIB_ENCODING_DEFLATE` (`int`)  
Algoritmo de compresión ZLIB según RFC 1950.

`ZLIB_ENCODING_GZIP` (`int`)  
Algoritmo GZIP según RFC 1952.

`ZLIB_FILTERED` (`int`)  

`ZLIB_HUFFMAN_ONLY` (`int`)  

`ZLIB_FIXED` (`int`)  

`ZLIB_RLE` (`int`)  

`ZLIB_DEFAULT_STRATEGY` (`int`)  

`ZLIB_BLOCK` (`int`)  

`ZLIB_NO_FLUSH` (`int`)  

`ZLIB_PARTIAL_FLUSH` (`int`)  

`ZLIB_SYNC_FLUSH` (`int`)  

`ZLIB_FULL_FLUSH` (`int`)  

`ZLIB_FINISH` (`int`)  

`ZLIB_VERSION` (`string`)  
Número de versión de `zlib` como `string`.

`ZLIB_VERNUM` (`int`)  
Número de versión de `zlib` como `int`.

`ZLIB_OK` (`int`)  
No hay errores o información adicional de estado.

`ZLIB_STREAM_END` (`int`)  
El stream terminó exitosamente.

`ZLIB_NEED_DICT` (`int`)  
Se necesita un diccionario preestablecido.

`ZLIB_ERRNO` (`int`)  
Error en la operación de archivo.

`ZLIB_STREAM_ERROR` (`int`)  
El estado del stream es inconsistente o un parámetro es inválido.

`ZLIB_DATA_ERROR` (`int`)  
Los datos de entrada están corruptos.

`ZLIB_MEM_ERROR` (`int`)  
Memoria insuficiente.

`ZLIB_BUF_ERROR` (`int`)  
No se puede progresar debido a espacio de buffer insuficiente o finalización inesperada de un stream de entrada.

`ZLIB_VERSION_ERROR` (`int`)  
La versión de la biblioteca `zlib` es incompatible con la versión asumida por el llamador.
