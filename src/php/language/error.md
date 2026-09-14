---
title: Error
source_url: https://www.php.net/manual/es/class.error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 3250
---

## Introducción

`Error` es la clase base para todos los errores de PHP internos.

## Sinopsis de la clase

Error

implements

Throwable

Propiedades

protected

string

message

""

private

string

string

""

protected

int

code

protected

string

file

""

protected

int

line

private

array

trace

\[\]

private

Throwable

null

previous

null

Métodos

## Propiedades

`message`  
El mensaje de error

`code`  
El código de error

`file`  
El nombre del fichero donde ocurrió el error

`line`  
La línea donde ocurrió el error

`previous`  
La excepción lanzada previamente

`string`  
La representación en cadena del seguimiento de la pila

`trace`  
El seguimiento de la pila como array
