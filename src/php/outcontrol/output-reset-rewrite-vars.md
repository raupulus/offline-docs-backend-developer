---
title: output_reset_rewrite_vars
description: Anula la reescritura de URL
source_url: https://www.php.net/manual/es/function.output-reset-rewrite-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/output-reset-rewrite-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: f3f9d2632
order: 59880
---

output_reset_rewrite_vars

Anula la reescritura de URL

## Descripción

```php
output_reset_rewrite_vars(): bool
```php

Esta función elimina todas las variables de reescritura previamente definidas por la función `output_add_rewrite_var`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | Antes de PHP 7.1.0, las variables de reescritura definidas por `output_add_rewrite_var` utilizaban el mismo buffer de salida del módulo de sesión trans sid. Desde PHP 7.1.0, se utiliza un buffer de salida dedicado y `output_reset_rewrite_vars` elimina únicamente las vars de reescritura definidas por `output_add_rewrite_var`. |

## Ejemplos

Ejemplo con `output_reset_rewrite_vars`

```
<?php
ini_set('url_rewriter.tags', 'a=href');

output_add_rewrite_var('var', 'value');

echo '<a href="file.php">link</a>';
ob_flush();

output_reset_rewrite_vars();
echo '<a href="file.php">link</a>';
?>

    
```php

El ejemplo anterior mostrará:

    <a href="file.php?var=value">link</a>
    <a href="file.php">link</a>

## Véase también

`output_add_rewrite_var`, `ob_flush`, `ob_list_handlers`, [url_rewriter.tags](#ini.url-rewriter.tags), [url_rewriter.hosts](#ini.url-rewriter.hosts), [session.trans_sid_tags](#ini.session.trans-sid-tags), [session.trans_sid_hosts](#ini.session.trans-sid-hosts)
