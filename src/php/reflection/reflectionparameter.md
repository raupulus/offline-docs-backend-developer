---
title: La clase ReflectionParameter
source_url: https://www.php.net/manual/es/class.reflectionparameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 4d17b7b49
order: 71420
---

## Introducción

La clase `ReflectionParameter` recupera las informaciones sobre los argumentos de las funciones o de los métodos.

Para realizar una introspección sobre los argumentos de las funciones, primero se crea una instancia de la clase `ReflectionFunction` o de la clase `ReflectionMethod` y luego se utiliza el método ReflectionFunctionAbstract::getParameters para recuperar un array de los argumentos.

## Sinopsis de la clase

ReflectionParameter

implements

Reflector

Propiedades

public

string

name

Métodos

## Propiedades

`name`  
Nombre del argumento. Solo lectura, genera `ReflectionException` al intentar escribir.

## Historial de cambios

| Versión | Descripción                                    |
|---------|------------------------------------------------|
| 8.0.0   | ReflectionParameter::export ha sido eliminado. |
