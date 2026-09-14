---
title: La clase tidyNode
source_url: https://www.php.net/manual/es/class.tidynode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidynode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 4d17b7b49
order: 94310
---

## Introducción

Un nodo HTML en un fichero HTML, como es detectado por tidy.

## Sinopsis de la clase

final

tidyNode

Propiedades

public

readonly

string

value

public

readonly

string

name

public

readonly

int

type

public

readonly

int

line

public

readonly

int

column

public

readonly

bool

proprietary

public

readonly

int

null

id

public

readonly

array

null

attribute

public

readonly

array

null

child

Métodos

## Propiedades

`value`  
La representación HTML del nodo, incluyendo las etiquetas de los alrededores.

`name`  
El nombre del nodo HTML

`type`  
El tipo de etiqueta (una de las [constantes nodetype](#tidy.constants.nodetype). Por ejemplo, `TIDY_NODETYPE_PHP`)

`line`  
el número de línea en la que la etiqueta está ubicada en el archivo

`column`  
El número de columna en la que la etiqueta está ubicada en el archivo

`proprietary`  
Indica si el nodo es una etiqueta de propiedad

`id`  
EL ID de la etiqueta (una de las [constantes tag](#tidy.constants.tag). Por ejemplo, `TIDY_TAG_FRAME`)

`attribute`  
Un array de cadena, representando los nombres de atributos (como las claves) del nodo actual.

`child`  
Un array de `tidyNode`, representando el hijo del nodo actual.
