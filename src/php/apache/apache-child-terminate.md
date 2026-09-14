---
title: apache_child_terminate
description: Termina el proceso Apache después de esta petición
source_url: https://www.php.net/manual/es/function.apache-child-terminate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/apache-child-terminate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: f3b9d85f7
order: 4730
---

apache_child_terminate

Termina el proceso Apache después de esta petición

## Descripción

```php
apache_child_terminate(): void
```php

`apache_child_terminate` programa el proceso Apache para que se termine una vez finalizada la petición PHP actual. Esto puede servir para terminar un proceso después de un script que hubiera consumido mucha memoria. En efecto, la memoria es generalmente liberada de manera interna, pero no devuelta al sistema.

Funciona con los servidores web Apache y FastCGI.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.

## Véase también

`exit`
