---
title: La clase ArrayObject
source_url: https://www.php.net/manual/es/class.arrayobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: eff22719b
order: 81570
---

## Introducción

Esta clase permite que los objetos funcionen como arrays.

> [!NOTE]
> Envolver objetos con esta clase es fundamentalmente defectuoso, y su utilización con objetos es por lo tanto desaconsejada.

## Sinopsis de la clase

ArrayObject

implements

IteratorAggregate

ArrayAccess

Serializable

Countable

Constantes

public

const

int

ArrayObject::STD_PROP_LIST

public

const

int

ArrayObject::ARRAY_AS_PROPS

Métodos

## Constantes predefinidas

## Opciones de `ArrayObject`

`ArrayObject::STD_PROP_LIST`  
Las propiedades del objeto tienen su funcionamiento normal cuando se accede a ellas desde la lista (`var_dump`, [`foreach`](#control-structures.foreach), etc.).

`ArrayObject::ARRAY_AS_PROPS`  
Los elementos pueden ser accedidos como propiedades (lectura y escritura). La clase `ArrayObject` utiliza su propia lógica para acceder a las propiedades, por lo que no se emite ningún aviso o error al intentar leer o escribir propiedades dinámicas.
