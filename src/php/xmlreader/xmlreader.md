---
title: La clase XMLReader
source_url: https://www.php.net/manual/es/class.xmlreader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlreader/xmlreader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlreader
translation_status: ready
translation_reviewed: true
translation_revision: 66eeca1e7
order: 103360
---

## Introducción

La extensión XMLReader es un analizador XML. El analizador funciona como un cursor que recorre el documento y se detiene en cada nodo.

## Sinopsis de la clase

XMLReader

Constantes

public

const

int

XMLReader::NONE

public

const

int

XMLReader::ELEMENT

public

const

int

XMLReader::ATTRIBUTE

public

const

int

XMLReader::TEXT

public

const

int

XMLReader::CDATA

public

const

int

XMLReader::ENTITY_REF

public

const

int

XMLReader::ENTITY

public

const

int

XMLReader::PI

public

const

int

XMLReader::COMMENT

public

const

int

XMLReader::DOC

public

const

int

XMLReader::DOC_TYPE

public

const

int

XMLReader::DOC_FRAGMENT

public

const

int

XMLReader::NOTATION

public

const

int

XMLReader::WHITESPACE

public

const

int

XMLReader::SIGNIFICANT_WHITESPACE

public

const

int

XMLReader::END_ELEMENT

public

const

int

XMLReader::END_ENTITY

public

const

int

XMLReader::XML_DECLARATION

public

const

int

XMLReader::LOADDTD

public

const

int

XMLReader::DEFAULTATTRS

public

const

int

XMLReader::VALIDATE

public

const

int

XMLReader::SUBST_ENTITIES

Propiedades

public

int

attributeCount

public

string

baseURI

public

int

depth

public

bool

hasAttributes

public

bool

hasValue

public

bool

isDefault

public

bool

isEmptyElement

public

string

localName

public

string

name

public

string

namespaceURI

public

int

nodeType

public

string

prefix

public

string

value

public

string

xmlLang

Métodos

## Propiedades

`attributeCount`  
El número de atributos en el nodo

`baseURI`  
La URI base del nodo

`depth`  
Profundidad del nodo en el árbol comenzando en 0

`hasAttributes`  
Indica si el nodo tiene atributos

`hasValue`  
Indica si el nodo tiene un valor de texto

`isDefault`  
Indica si el atributo es por defecto desde el DTD

`isEmptyElement`  
Indica si el nodo es un elemento vacío

`localName`  
El nombre local del nodo

`name`  
El nombre calificado del nodo

`namespaceURI`  
El URI del espacio de nombres asociado con el nodo

`nodeType`  
El tipo de nodo para el nodo

`prefix`  
El prefijo del espacio de nombres asociado con el nodo

`value`  
El valor de texto del nodo

`xmlLang`  
El ámbito xml:lang en el que reside el nodo

## Constantes predefinidas

## Tipos de nodo XMLReader

`XMLReader::NONE`  
Ningún tipo de nodo

`XMLReader::ELEMENT`  
Elemento de inicio

`XMLReader::ATTRIBUTE`  
Nodo Atributo

`XMLReader::TEXT`  
Nodo texto

`XMLReader::CDATA`  
Nodo CDATA

`XMLReader::ENTITY_REF`  
Nodo de referencia de entidad

`XMLReader::ENTITY`  
Nodo de declaración de entidad

`XMLReader::PI`  
Nodo de instrucción de proceso

`XMLReader::COMMENT`  
Nodo de comentario

`XMLReader::DOC`  
Nodo documento

`XMLReader::DOC_TYPE`  
Nodo de tipo de documento

`XMLReader::DOC_FRAGMENT`  
Nodo de fragmento de documento

`XMLReader::NOTATION`  
Nodo de notación

`XMLReader::WHITESPACE`  
Nodo "espacio"

`XMLReader::SIGNIFICANT_WHITESPACE`  
Nodo "espacio" significativo

`XMLReader::END_ELEMENT`  
Elemento de fin

`XMLReader::END_ENTITY`  
Entidad de fin

`XMLReader::XML_DECLARATION`  
Nodo de declaración XML

## Opciones del analizador XMLReader

`XMLReader::LOADDTD`  
Carga un DTD pero no lo valida

`XMLReader::DEFAULTATTRS`  
Carga un DTD y los atributos por defecto pero no lo valida

`XMLReader::VALIDATE`  
Carga un DTD y valida el documento durante el análisis

`XMLReader::SUBST_ENTITIES`  
Sustituye las entidades y expande las referencias

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
