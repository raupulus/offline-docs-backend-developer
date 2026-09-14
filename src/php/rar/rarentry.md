---
title: La clase RarEntry
source_url: https://www.php.net/manual/es/class.rarentry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68640
---

## Introducción

Una entrada RAR, representa un directorio o un archivo comprimido dentro de un archivo RAR.

## Sinopsis de la clase

RarEntry

final

RarEntry

Constantes

const

int

RarEntry::HOST_MSDOS

0

const

int

RarEntry::HOST_OS2

1

const

int

RarEntry::HOST_WIN32

2

const

int

RarEntry::HOST_UNIX

3

const

int

RarEntry::HOST_MACOS

4

const

int

RarEntry::HOST_BEOS

5

const

int

RarEntry::ATTRIBUTE_WIN_READONLY

1

const

int

RarEntry::ATTRIBUTE_WIN_HIDDEN

2

const

int

RarEntry::ATTRIBUTE_WIN_SYSTEM

4

const

int

RarEntry::ATTRIBUTE_WIN_DIRECTORY

16

const

int

RarEntry::ATTRIBUTE_WIN_ARCHIVE

32

const

int

RarEntry::ATTRIBUTE_WIN_DEVICE

64

const

int

RarEntry::ATTRIBUTE_WIN_NORMAL

128

const

int

RarEntry::ATTRIBUTE_WIN_TEMPORARY

256

const

int

RarEntry::ATTRIBUTE_WIN_SPARSE_FILE

512

const

int

RarEntry::ATTRIBUTE_WIN_REPARSE_POINT

1024

const

int

RarEntry::ATTRIBUTE_WIN_COMPRESSED

2048

const

int

RarEntry::ATTRIBUTE_WIN_OFFLINE

4096

const

int

RarEntry::ATTRIBUTE_WIN_NOT_CONTENT_INDEXED

8192

const

int

RarEntry::ATTRIBUTE_WIN_ENCRYPTED

16384

const

int

RarEntry::ATTRIBUTE_WIN_VIRTUAL

65536

const

int

RarEntry::ATTRIBUTE_UNIX_WORLD_EXECUTE

1

const

int

RarEntry::ATTRIBUTE_UNIX_WORLD_WRITE

2

const

int

RarEntry::ATTRIBUTE_UNIX_WORLD_READ

4

const

int

RarEntry::ATTRIBUTE_UNIX_GROUP_EXECUTE

8

const

int

RarEntry::ATTRIBUTE_UNIX_GROUP_WRITE

16

const

int

RarEntry::ATTRIBUTE_UNIX_GROUP_READ

32

const

int

RarEntry::ATTRIBUTE_UNIX_OWNER_EXECUTE

64

const

int

RarEntry::ATTRIBUTE_UNIX_OWNER_WRITE

128

const

int

RarEntry::ATTRIBUTE_UNIX_OWNER_READ

256

const

int

RarEntry::ATTRIBUTE_UNIX_STICKY

512

const

int

RarEntry::ATTRIBUTE_UNIX_SETGID

1024

const

int

RarEntry::ATTRIBUTE_UNIX_SETUID

2048

const

int

RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET

61440

const

int

RarEntry::ATTRIBUTE_UNIX_FIFO

4096

const

int

RarEntry::ATTRIBUTE_UNIX_CHAR_DEV

8192

const

int

RarEntry::ATTRIBUTE_UNIX_DIRECTORY

16384

const

int

RarEntry::ATTRIBUTE_UNIX_BLOCK_DEV

24576

const

int

RarEntry::ATTRIBUTE_UNIX_REGULAR_FILE

32768

const

int

RarEntry::ATTRIBUTE_UNIX_SYM_LINK

40960

const

int

RarEntry::ATTRIBUTE_UNIX_SOCKET

49152

Métodos

## Constantes predefinidas

`RarEntry::HOST_MSDOS`  
Si el valor devuelto por RarEntry::getHostOs es igual a esta constante, MS-DOS fue utilizado para añadir esta entrada. Utilizar en lugar de `RAR_HOST_MSDOS`.

`RarEntry::HOST_OS2`  
Si el valor devuelto por RarEntry::getHostOs es igual a esta constante, OS/2 fue utilizado para añadir esta entrada. Destinado para sustituir a `RAR_HOST_OS2`.

`RarEntry::HOST_WIN32`  
Si el valor devuelto por RarEntry::getHostOs es igual a esta constante, Microsoft Windows fue utilizado para añadir esta entrada. Destinado para sustituir a `RAR_HOST_WIN32`.

`RarEntry::HOST_UNIX`  
Si el valor devuelto por RarEntry::getHostOs es igual a esta constante, un Sistema Operativo UNIX no especificado fue utilizado para añadir esta entrada. Destinado para sustituir a `RAR_HOST_UNIX`.

`RarEntry::HOST_MACOS`  
Si el valor devuelto por RarEntry::getHostOs es igual a esta constante, un Sistema Operativo Mac fue utilizado para añadir esta entrada.

`RarEntry::HOST_BEOS`  
Si el valor devuelto por RarEntry::getHostOs es igual a esta constante, un Sistema Operativo BeOS fue utilizado para añadir esta entrada. Destinado para sustituir a `RAR_HOST_BEOS`.

`RarEntry::ATTRIBUTE_WIN_READONLY`  
Bit que representa una entrada de Windows con un atributo de sólo lectura. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_HIDDEN`  
Bit que representa una entrada de Windows con un atributo oculto. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_SYSTEM`  
Bits que representa una entrada de Windows con un atributo del sistema. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_DIRECTORY`  
Bit que representa una entrada de Windows con un atributo de directorio (entrada es un directorio). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows. Véase también RarEntry::isDirectory, que también trabaja con entradas que no fueron añadidas en WinRAR.

`RarEntry::ATTRIBUTE_WIN_ARCHIVE`  
Bit que representa una entrada de Windows con un atributo de archivo. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_DEVICE`  
Bit que representa una entrada de Windows con un atributo de dispositivo. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_NORMAL`  
Bit que representa una entrada de Windows con un atributo de archivo normal (entrada NO es un directorio). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows. Véase también RarEntry::isDirectory, que también trabaja con entradas que no fueron añadidas en WinRAR.

`RarEntry::ATTRIBUTE_WIN_TEMPORARY`  
Bit que representa una entrada de Windows con un atributo temporal. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_SPARSE_FILE`  
Bit que representa una entrada de Windows con un atributo de archivo disperso (archivo es un archivo disperso NTFS). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_REPARSE_POINT`  
Bit que representa una entrada de Windows con un atributo punto de re-análisis (entrada es un punto de re-análisis NTFS, por ejemplo, un directorio enlace o un sistema de montaje de archivos). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_COMPRESSED`  
Bit que representa una entrada de Windows con un atributo comprimido (sólo NTFS). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_OFFLINE`  
Bit que representa una entrada de Windows con un atributo fuera de línea (entrada es desconectada y no accesible). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_NOT_CONTENT_INDEXED`  
Bit que representa una entrada de Windows con un atributo de contenido no indexado (entrada deberá ser indexada). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_ENCRYPTED`  
Bit que representa una entrada de Windows con un atributo cifrado (sólo NTFS). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_WIN_VIRTUAL`  
Bit que representa una entrada de Windows con un atributo virtual. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es Microsoft Windows.

`RarEntry::ATTRIBUTE_UNIX_WORLD_EXECUTE`  
Bit que representa una entrada que es ejecutable en el mundo UNIX. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_WORLD_WRITE`  
Bit que representa una entrada que es escribible en el mundo UNIX. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_WORLD_READ`  
Bit que representa una entrada que es leible en el mundo UNIX. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_GROUP_EXECUTE`  
Bit que representa una entrada UNIX que es grupo ejecutable. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_GROUP_WRITE`  
Bit que representa una entrada UNIX que es grupo escribible. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_GROUP_READ`  
Bit que representa una entrada UNIX que es grupo leible. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_OWNER_EXECUTE`  
Bit que representa una entrada UNIX que es propietario ejecutable. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_OWNER_WRITE`  
Bit que representa una entrada UNIX que es propietario escribible. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_OWNER_READ`  
Bit que representa una entrada UNIX que es propietario leible. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_STICKY`  
Bit que representa el sticky bit UNIX. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_SETGID`  
Bit que representa el atributo UNIX setgid. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_SETUID`  
Bit que representa el atributo UNIX setuid. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX.

`RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`  
Máscara para aislar a los últimos cuatro bits (nibble) de atributos UNIX (\_S_IFMT, el tipo de máscara de archivo). Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con las constantes [`RarEntry::ATTRIBUTE_UNIX_FIFO`](#rarentry.constants.attribute-unix-fifo), [`RarEntry::ATTRIBUTE_UNIX_CHAR_DEV`](#rarentry.constants.attribute-unix-char-dev), [`RarEntry::ATTRIBUTE_UNIX_DIRECTORY`](#rarentry.constants.attribute-unix-directory), [`RarEntry::ATTRIBUTE_UNIX_BLOCK_DEV`](#rarentry.constants.attribute-unix-block-dev), [`RarEntry::ATTRIBUTE_UNIX_REGULAR_FILE`](#rarentry.constants.attribute-unix-regular-file), [`RarEntry::ATTRIBUTE_UNIX_SYM_LINK`](#rarentry.constants.attribute-unix-sym-link) and [`RarEntry::ATTRIBUTE_UNIX_SOCKET`](#rarentry.constants.attribute-unix-socket).

`RarEntry::ATTRIBUTE_UNIX_FIFO`  
FIFOs Unix tendrá atributos cuyos últimos cuatro bits tienen este valor. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con la constante [ `RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`](#rarentry.constants.attribute-unix-final-quartet).

`RarEntry::ATTRIBUTE_UNIX_CHAR_DEV`  
Dispositivo de tipo carácter Unix tendrá atributos cuyos últimos cuatro bits tienen este valor. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con la constante [ `RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`](#rarentry.constants.attribute-unix-final-quartet).

`RarEntry::ATTRIBUTE_UNIX_DIRECTORY`  
Directorios Unix tendrá atributos cuyos últimos cuatro bits tienen este valor. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con la constante [ `RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`](#rarentry.constants.attribute-unix-final-quartet). Véase también RarEntry::isDirectory, que también trabaja con entradas que fueron añadidas en otros sistemas operativos.

`RarEntry::ATTRIBUTE_UNIX_BLOCK_DEV`  
Dispositivo de tipo bloque Unix tendrá atributos cuyos últimos cuatro bits tienen este valor. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con la constante [ `RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`](#rarentry.constants.attribute-unix-final-quartet).

`RarEntry::ATTRIBUTE_UNIX_REGULAR_FILE`  
Archivos regular Unix (no directorios) tendrá atributos cuyos últimos cuatro bits tienen este valor. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con la constante [ `RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`](#rarentry.constants.attribute-unix-final-quartet). Véase también RarEntry::isDirectory, ue también trabaja con entradas que fueron añadidas en otros sistemas operativos.

`RarEntry::ATTRIBUTE_UNIX_SYM_LINK`  
Enlace simbólico Unix tendrá atributos cuyos últimos cuatro bits tienen este valor. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con la constante [ `RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`](#rarentry.constants.attribute-unix-final-quartet).

`RarEntry::ATTRIBUTE_UNIX_SOCKET`  
Sockets Unix will tendrá atributos cuyos últimos cuatro bits tienen este valor. Para ser utilizado con RarEntry::getAttr en entradas cuyo sistema operativo anfitrión es UNIX y con la constante [ `RarEntry::ATTRIBUTE_UNIX_FINAL_QUARTET`](#rarentry.constants.attribute-unix-final-quartet).
