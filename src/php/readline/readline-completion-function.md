---
title: readline_completion_function
description: Registra una función de completado
source_url: https://www.php.net/manual/es/function.readline-completion-function.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline-completion-function.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: 53208f9bd
order: 68760
---

readline_completion_function

Registra una función de completado

## Descripción

```php
readline_completion_function(callable $callback): bool
```php

Registra una nueva función de completado. Es la misma funcionalidad que cuando se utiliza la tecla de tabulación bajo Bash.

## Parámetros

`callback`  
Debe proporcionarse el nombre de una función que acepte un nombre parcial de comando, y devuelva una lista de funciones completas posibles.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
