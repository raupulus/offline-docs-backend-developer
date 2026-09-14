---
title: La clase Spoofchecker
source_url: https://www.php.net/manual/es/class.spoofchecker.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/spoofchecker.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 5e36b489f
order: 42520
---

## Introducción

Esta clase se proporciona porque Unicode contiene un gran número de caracteres y incorpora los diversos sistemas de escritura del mundo, y su uso incorrecto puede exponer programas o sistemas a posibles ataques de seguridad mediante la similitud de caracteres.

Los métodos proporcionados permiten verificar si un string individual es susceptible de ser una tentativa de engaño al lector (`detección de engaño`), como en "pаypаl" escrito con un carácter 'а' cirílico.

## Sinopsis de la clase

Spoofchecker

Constantes

public

const

int

Spoofchecker::SINGLE_SCRIPT_CONFUSABLE

public

const

int

Spoofchecker::MIXED_SCRIPT_CONFUSABLE

public

const

int

Spoofchecker::WHOLE_SCRIPT_CONFUSABLE

public

const

int

Spoofchecker::ANY_CASE

public

const

int

Spoofchecker::SINGLE_SCRIPT

public

const

int

Spoofchecker::INVISIBLE

public

const

int

Spoofchecker::CHAR_LIMIT

public

const

int

Spoofchecker::ASCII

public

const

int

Spoofchecker::HIGHLY_RESTRICTIVE

public

const

int

Spoofchecker::MODERATELY_RESTRICTIVE

public

const

int

Spoofchecker::MINIMALLY_RESTRICTIVE

public

const

int

Spoofchecker::UNRESTRICTIVE

public

const

int

Spoofchecker::SINGLE_SCRIPT_RESTRICTIVE

public

const

int

Spoofchecker::MIXED_NUMBERS

public

const

int

Spoofchecker::HIDDEN_OVERLAY

public

const

int

Spoofchecker::IGNORE_SPACE

public

const

int

Spoofchecker::CASE_INSENSITIVE

public

const

int

Spoofchecker::ADD_CASE_MAPPINGS

public

const

int

Spoofchecker::SIMPLE_CASE_INSENSITIVE

Métodos

## Constantes predefinidas

`Spoofchecker::SINGLE_SCRIPT_CONFUSABLE` `int`  

`Spoofchecker::MIXED_SCRIPT_CONFUSABLE` `int`  

`Spoofchecker::WHOLE_SCRIPT_CONFUSABLE` `int`  

`Spoofchecker::ANY_CASE` `int`  

`Spoofchecker::SINGLE_SCRIPT` `int`  

`Spoofchecker::INVISIBLE` `int`  

`Spoofchecker::CHAR_LIMIT` `int`  

`Spoofchecker::ASCII` `int`  

`Spoofchecker::HIGHLY_RESTRICTIVE` `int`  

`Spoofchecker::MODERATELY_RESTRICTIVE` `int`  

`Spoofchecker::MINIMALLY_RESTRICTIVE` `int`  

`Spoofchecker::UNRESTRICTIVE` `int`  

`Spoofchecker::SINGLE_SCRIPT_RESTRICTIVE` `int`  

`Spoofchecker::MIXED_NUMBERS` `int`  

`Spoofchecker::HIDDEN_OVERLAY` `int`  

`Spoofchecker::IGNORE_SPACE` `int`  

`Spoofchecker::CASE_INSENSITIVE` `int`  
Activa la correspondencia insensible a mayúsculas/minúsculas

`Spoofchecker::ADD_CASE_MAPPINGS` `int`  
Añade todas las correspondencias de mayúsculas/minúsculas para cada elemento del conjunto

`Spoofchecker::SIMPLE_CASE_INSENSITIVE` `int`  
Activa la correspondencia insensible a mayúsculas/minúsculas

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Se añadieron `Spoofchecker::IGNORE_SPACE`, `Spoofchecker::CASE_INSENSITIVE`, `Spoofchecker::ADD_CASE_MAPPINGS`, `Spoofchecker::SIMPLE_CASE_INSENSITIVE`. |
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 7.3.0 | Las constantes de clase utilizadas por `Spoofchecker::setRestrictionLevel` como `Spoofchecker::ASCII`, `Spoofchecker::HIGHLY_RESTRICTIVE`, `Spoofchecker::MODERATELY_RESTRICTIVE`, `Spoofchecker::MINIMALLY_RESTRICTIVE`, `Spoofchecker::UNRESTRICTIVE`, `Spoofchecker::SINGLE_SCRIPT_RESTRICTIVE` han sido añadidas. |
