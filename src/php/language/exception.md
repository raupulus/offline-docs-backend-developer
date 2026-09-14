---
title: Exception
source_url: https://www.php.net/manual/es/class.exception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 462d2bcb3
order: 3390
---

## Introducción

`Exception` es la clase base para todas las excepciones de usuario.

## Sinopsis de la clase

Exception

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
El mensaje de la excepción

`code`  
El código de la excepción

`file`  
El nombre del fichero en el cual la excepción ha sido creada

`line`  
La línea donde la excepción ha sido creada

`previous`  
La excepción lanzada previamente

`string`  
La representación en forma de string de la traza de la pila

`trace`  
La traza de la pila en forma de array
