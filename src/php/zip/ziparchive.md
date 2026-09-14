---
title: La clase ZipArchive
source_url: https://www.php.net/manual/es/class.ziparchive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108660
---

## Introducción

Un fichero, comprimido con Zip.

## Sinopsis de la clase

ZipArchive

implements

Countable

Constantes

public

const

int

ZipArchive::CREATE

public

const

int

ZipArchive::EXCL

public

const

int

ZipArchive::CHECKCONS

public

const

int

ZipArchive::OVERWRITE

public

const

int

ZipArchive::RDONLY

public

const

int

ZipArchive::FL_NOCASE

public

const

int

ZipArchive::FL_NODIR

public

const

int

ZipArchive::FL_COMPRESSED

public

const

int

ZipArchive::FL_UNCHANGED

public

const

int

ZipArchive::FL_RECOMPRESS

public

const

int

ZipArchive::FL_ENCRYPTED

public

const

int

ZipArchive::FL_OVERWRITE

public

const

int

ZipArchive::FL_LOCAL

public

const

int

ZipArchive::FL_CENTRAL

public

const

int

ZipArchive::FL_ENC_GUESS

public

const

int

ZipArchive::FL_ENC_RAW

public

const

int

ZipArchive::FL_ENC_STRICT

public

const

int

ZipArchive::FL_ENC_UTF_8

public

const

int

ZipArchive::FL_ENC_CP437

public

const

int

ZipArchive::FL_OPEN_FILE_NOW

public

const

int

ZipArchive::CM_DEFAULT

public

const

int

ZipArchive::CM_STORE

public

const

int

ZipArchive::CM_SHRINK

public

const

int

ZipArchive::CM_REDUCE_1

public

const

int

ZipArchive::CM_REDUCE_2

public

const

int

ZipArchive::CM_REDUCE_3

public

const

int

ZipArchive::CM_REDUCE_4

public

const

int

ZipArchive::CM_IMPLODE

public

const

int

ZipArchive::CM_DEFLATE

public

const

int

ZipArchive::CM_DEFLATE64

public

const

int

ZipArchive::CM_PKWARE_IMPLODE

public

const

int

ZipArchive::CM_BZIP2

public

const

int

ZipArchive::CM_LZMA

public

const

int

ZipArchive::CM_LZMA2

public

const

int

ZipArchive::CM_ZSTD

public

const

int

ZipArchive::CM_XZ

public

const

int

ZipArchive::CM_TERSE

public

const

int

ZipArchive::CM_LZ77

public

const

int

ZipArchive::CM_WAVPACK

public

const

int

ZipArchive::CM_PPMD

public

const

int

ZipArchive::ER_OK

public

const

int

ZipArchive::ER_MULTIDISK

public

const

int

ZipArchive::ER_RENAME

public

const

int

ZipArchive::ER_CLOSE

public

const

int

ZipArchive::ER_SEEK

public

const

int

ZipArchive::ER_READ

public

const

int

ZipArchive::ER_WRITE

public

const

int

ZipArchive::ER_CRC

public

const

int

ZipArchive::ER_ZIPCLOSED

public

const

int

ZipArchive::ER_NOENT

public

const

int

ZipArchive::ER_EXISTS

public

const

int

ZipArchive::ER_OPEN

public

const

int

ZipArchive::ER_TMPOPEN

public

const

int

ZipArchive::ER_ZLIB

public

const

int

ZipArchive::ER_MEMORY

public

const

int

ZipArchive::ER_CHANGED

public

const

int

ZipArchive::ER_COMPNOTSUPP

public

const

int

ZipArchive::ER_EOF

public

const

int

ZipArchive::ER_INVAL

public

const

int

ZipArchive::ER_NOZIP

public

const

int

ZipArchive::ER_INTERNAL

public

const

int

ZipArchive::ER_INCONS

public

const

int

ZipArchive::ER_REMOVE

public

const

int

ZipArchive::ER_DELETED

public

const

int

ZipArchive::ER_ENCRNOTSUPP

public

const

int

ZipArchive::ER_RDONLY

public

const

int

ZipArchive::ER_NOPASSWD

public

const

int

ZipArchive::ER_WRONGPASSWD

public

const

int

ZipArchive::ER_OPNOTSUPP

public

const

int

ZipArchive::ER_INUSE

public

const

int

ZipArchive::ER_TELL

public

const

int

ZipArchive::ER_COMPRESSED_DATA

public

const

int

ZipArchive::ER_CANCELLED

public

const

int

ZipArchive::ER_DATA_LENGTH

public

const

int

ZipArchive::ER_NOT_ALLOWED

public

const

int

ZipArchive::ER_TRUNCATED_ZIP

public

const

int

ZipArchive::AFL_RDONLY

public

const

int

ZipArchive::AFL_IS_TORRENTZIP

public

const

int

ZipArchive::AFL_WANT_TORRENTZIP

public

const

int

ZipArchive::AFL_CREATE_OR_KEEP_FILE_FOR_EMPTY_ARCHIVE

public

const

int

ZipArchive::OPSYS_DOS

public

const

int

ZipArchive::OPSYS_AMIGA

public

const

int

ZipArchive::OPSYS_OPENVMS

public

const

int

ZipArchive::OPSYS_UNIX

public

const

int

ZipArchive::OPSYS_VM_CMS

public

const

int

ZipArchive::OPSYS_ATARI_ST

public

const

int

ZipArchive::OPSYS_OS_2

public

const

int

ZipArchive::OPSYS_MACINTOSH

public

const

int

ZipArchive::OPSYS_Z_SYSTEM

public

const

int

ZipArchive::OPSYS_CPM

public

const

int

ZipArchive::OPSYS_WINDOWS_NTFS

public

const

int

ZipArchive::OPSYS_MVS

public

const

int

ZipArchive::OPSYS_VSE

public

const

int

ZipArchive::OPSYS_ACORN_RISC

public

const

int

ZipArchive::OPSYS_VFAT

public

const

int

ZipArchive::OPSYS_ALTERNATE_MVS

public

const

int

ZipArchive::OPSYS_BEOS

public

const

int

ZipArchive::OPSYS_TANDEM

public

const

int

ZipArchive::OPSYS_OS_400

public

const

int

ZipArchive::OPSYS_OS_X

public

const

int

ZipArchive::OPSYS_DEFAULT

public

const

int

ZipArchive::EM_NONE

public

const

int

ZipArchive::EM_TRAD_PKWARE

public

const

int

ZipArchive::EM_AES_128

public

const

int

ZipArchive::EM_AES_192

public

const

int

ZipArchive::EM_AES_256

public

const

int

ZipArchive::EM_UNKNOWN

public

const

string

ZipArchive::LIBZIP_VERSION

public

const

int

ZipArchive::LENGTH_TO_END

public

const

int

ZipArchive::LENGTH_UNCHECKED

Propiedades

public

readonly

int

lastId

public

readonly

int

status

public

readonly

int

statusSys

public

readonly

int

numFiles

public

readonly

string

filename

public

readonly

string

comment

Métodos

## Propiedades

`lastId`  
Valor de índice de la última entrada añadida (archivo o directorio). Disponible para archivo cerrado, a partir de PHP 8.0.0 y PECL zip 1.18.0.

`status`  
Estado del archivo Zip. Disponible para archivo cerrado, a partir de PHP 8.0.0 y PECL zip 1.18.0.

`statusSys`  
Estado del sistema del archivo Zip. Disponible para archivo cerrado, a partir de PHP 8.0.0 y PECL zip 1.18.0.

`numFiles`  
Número de ficheros en el archivo

`filename`  
Nombre del archivo en le sistema de archivos

`comment`  
Comentario para el archivo
