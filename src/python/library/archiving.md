---
title: Compresión de datos y archivado
source_url: https://docs.python.org/es/3
source_path: library/archiving.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1530
---

# Compresión de datos y archivado

The modules described in this chapter support data compression with
the zlib, gzip, bzip2, lzma, and zstd algorithms, and the creation of
ZIP- and tar-format archives.  See also Operaciones de archivado
provided by the "shutil" module.

* The "compression" package

* "compression.zstd" --- Compression compatible with the Zstandard
  format

  * Exceptions

  * Reading and writing compressed files

  * Compressing and decompressing data in memory

  * Zstandard dictionaries

  * Advanced parameter control

  * Miscellaneous

  * Examples

* "zlib" --- Compression compatible with **gzip**

* "gzip" --- Support for **gzip** files

  * Ejemplos de uso

  * Command-line interface

    * Command-line options

* "bz2" --- Support for **bzip2** compression

  * (De)compresión de archivos

  * (De)compresión incremental

  * (Des)comprimir en un solo paso

  * Ejemplos de uso

* "lzma" --- Compression using the LZMA algorithm

  * Leyendo y escribiendo ficheros comprimidos

  * Comprimiendo y descomprimiendo datos en memoria

  * Misceláneas

  * Especificando cadenas de filtro personalizadas

  * Constants

  * Ejemplos

* "zipfile" --- Work with ZIP archives

  * ZipFile objects

  * Path objects

  * PyZipFile objects

  * ZipInfo objects

  * Command-line interface

    * Opciones de línea de comando

  * Problemas de descompresión

    * Del archivo mismo

    * File system limitations

    * Limitaciones de recursos

    * Interrupción

    * Comportamientos predeterminados de extracción

* "tarfile" --- Read and write tar archive files

  * Objetos *TarFile*

  * Objetos TarInfo

  * Extraction filters

    * Default named filters

    * Filter errors

    * Hints for further verification

    * Supporting older Python versions

    * Stateful extraction filter example

  * Interfaz de línea de comandos

    * Opciones de línea de comandos

  * Ejemplos

    * Reading examples

    * Writing examples

  * Formatos tar con soporte

  * Problemas unicode
