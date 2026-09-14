---
title: spl_autoload
description: Implementación por defecto de __autoload()
source_url: https://www.php.net/manual/es/function.spl-autoload.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/spl-autoload.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 87ea6d167
order: 82300
---

spl_autoload

Implementación por defecto de \_\_autoload()

## Descripción

```php
spl_autoload(string $class, [string $file_extensions]): void
```php

Esta función está prevista para ser utilizada como implementación por defecto para `__autoload`. Si no se especifica nada más y que `spl_autoload_register` es llamado sin ningún parámetro, entonces `spl_autoload` será utilizada para todas las futuras llamadas a `__autoload`.

## Parámetros

`class`  
El nombre de la clase instanciada. Al llamar a la función, el nombre de la clase con su espacio de nombres es pasado al parámetro. El `class` no contendrá el carácter backslash inicial de un identificador completamente calificado.

`file_extensions`  
Por omisión, la función verifica todos los [include_path](#ini.include-path) que podrían contener nombres de fichero añadidos por el nombre de clase, utilizando las extensiones `.inc` y `.php`.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `LogicException` cuando la clase no es encontrada, y no hay ningún otro autochargeur registrado.

## Historial de cambios

| Versión | Descripción                          |
|---------|--------------------------------------|
| 8.0.0   | `file_extensions` ahora es nullable. |
