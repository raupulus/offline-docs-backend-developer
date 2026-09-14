---
title: Parle\RLexer::push
description: Añade una regla de análisis
source_url: https://www.php.net/manual/es/parle-rlexer.push.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle/rlexer/push.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: be295015d
order: 60740
---

Parle\RLexer::push

Añade una regla de análisis

## Descripción

```php
public Parle\RLexer::push(string $regex, int $id, [int $userId]): void
```php

```php
public Parle\RLexer::push(string $state, string $regex, int $id, string $newState, [int $userId]): void
```

```php
public Parle\RLexer::push(string $state, string $regex, string $newState): void
```php

Añade un patrón para el reconocimiento de lexemas.

Un 'estado de inicio' y un 'estado de salida' pueden ser especificados utilizando una firma adecuada. Un 'estado de inicio' (start state) y un 'estado de salida' (exit state) pueden ser especificados utilizando una firma adecuada.

## Parámetros

`regex`  
Expresión regular utilizada para el reconocimiento de lexemas.

`id`  
El identificador del token. Si la instancia del analizador léxico está destinada a ser utilizada sola, puede ser un número arbitrario. Si la instancia del analizador léxico debe ser pasada al analizador, debe ser un identificador devuelto por Parle\RParser::tokenid.

`state`  
Nombre del estado. Si '\*' se utiliza como estado de inicio, entonces la regla se aplica a todos los estados del analizador léxico.

`newState`  
El nuevo nombre del estado, después de la aplicación de la regla.

Si '.' se especifica como estado de salida, entonces el estado del analizador léxico no se modifica cuando esta regla coincide. Un estado de salida con '\>' antes del nombre significa empujar. Utilice la firma sin id para la continuación o para comenzar la coincidencia, cuando se requiere una continuación o recursión.

Si '\<' se especifica como estado de salida, esto significa extraer. En este caso, la firma que contiene el id puede ser utilizada para identificar la coincidencia. Es importante señalar que incluso en el caso de que un id sea especificado, la regla terminará primero cuando todas las empujes previas hayan sido eliminadas.

## Valores devueltos

No se retorna ningún valor.
