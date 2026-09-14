---
title: La clase SplFileObject
source_url: https://www.php.net/manual/es/class.splfileobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 84640
---

## Introducción

La clase SplFileObject ofrece una interfaz orientada a objetos para un fichero.

## Sinopsis de la clase

SplFileObject

extends

SplFileInfo

implements

RecursiveIterator

SeekableIterator

Constantes

public

const

int

SplFileObject::DROP_NEW_LINE

public

const

int

SplFileObject::READ_AHEAD

public

const

int

SplFileObject::SKIP_EMPTY

public

const

int

SplFileObject::READ_CSV

Métodos

Métodos heredados

## Constantes predefinidas

`SplFileObject::DROP_NEW_LINE`  
Colocar nuevas líneas al final de una línea.

`SplFileObject::READ_AHEAD`  
Leer sobre rewind/next.

`SplFileObject::SKIP_EMPTY`  
Saltar líneas vacías en el fichero. Esto requiere que la bandera `READ_AHEAD` esté activada para que funcione como se tenía previsto.

`SplFileObject::READ_CSV`  
Leer líneas como filas CSV.
