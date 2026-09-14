---
title: La clase FilesystemIterator
source_url: https://www.php.net/manual/es/class.filesystemiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/filesystemiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 82100
---

## Introducción

El iterador `FilesystemIterator`.

## Sinopsis de la clase

FilesystemIterator

extends

DirectoryIterator

Constantes

public

const

int

FilesystemIterator::CURRENT_MODE_MASK

public

const

int

FilesystemIterator::CURRENT_AS_PATHNAME

public

const

int

FilesystemIterator::CURRENT_AS_FILEINFO

public

const

int

FilesystemIterator::CURRENT_AS_SELF

public

const

int

FilesystemIterator::KEY_MODE_MASK

public

const

int

FilesystemIterator::KEY_AS_PATHNAME

public

const

int

FilesystemIterator::FOLLOW_SYMLINKS

public

const

int

FilesystemIterator::KEY_AS_FILENAME

public

const

int

FilesystemIterator::NEW_CURRENT_AND_KEY

public

const

int

FilesystemIterator::OTHER_MODE_MASK

public

const

int

FilesystemIterator::SKIP_DOTS

public

const

int

FilesystemIterator::UNIX_PATHS

Métodos

Métodos heredados

## Constantes predefinidas

`FilesystemIterator::CURRENT_AS_PATHNAME`  
FilesystemIterator::current devuelve el nombre del camino.

`FilesystemIterator::CURRENT_AS_FILEINFO`  
FilesystemIterator::current devuelve un objeto `SplFileInfo`.

`FilesystemIterator::CURRENT_AS_SELF`  
FilesystemIterator::current devuelve `$this` (el `FilesystemIterator`).

`FilesystemIterator::CURRENT_MODE_MASK`  
Máscara FilesystemIterator::current.

`FilesystemIterator::KEY_AS_PATHNAME`  
FilesystemIterator::key devuelve el nombre del camino.

`FilesystemIterator::KEY_AS_FILENAME`  
FilesystemIterator::key devuelve el nombre del fichero.

`FilesystemIterator::FOLLOW_SYMLINKS`  
Hace que RecursiveDirectoryIterator::hasChildren siga los enlaces simbólicos.

`FilesystemIterator::KEY_MODE_MASK`  
Máscara FilesystemIterator::key.

`FilesystemIterator::NEW_CURRENT_AND_KEY`  
Idéntico a `FilesystemIterator::KEY_AS_FILENAME | FilesystemIterator::CURRENT_AS_FILEINFO`.

`FilesystemIterator::OTHER_MODE_MASK`  
Máscara utilizada para FilesystemIterator::getFlags y FilesystemIterator::setFlags.

`FilesystemIterator::SKIP_DOTS`  
Ignora los ficheros puntos (`.` y `..`).

`FilesystemIterator::UNIX_PATHS`  
Los caminos utilizan el separador de directorio de tipo Unix, es decir, la barra, independientemente del sistema operativo. Tenga en cuenta que el `camino` que se pasa al constructor no se modifica.
