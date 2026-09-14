---
title: output_add_rewrite_var
description: Añade una regla de reescritura de URL
source_url: https://www.php.net/manual/es/function.output-add-rewrite-var.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/output-add-rewrite-var.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: false
translation_revision: ba4d305a7
order: 59870
---

output_add_rewrite_var

Añade una regla de reescritura de URL

## Descripción

```php
output_add_rewrite_var(string $name, string $value): bool
```php

Esta función inicia el gestor de búfer de salida `'URL-Rewriter'` si no está activo, almacena los argumentos `name` y `value`, y cuando el búfer se vacía, reescribe las URLs y los formularios según los argumentos ini aplicables. Las llamadas posteriores a esta función almacenarán todas las parejas nombre/valor adicionales hasta que el gestor sea desactivado.

Cuando el búfer de salida se vacía (al llamar a `ob_flush`, `ob_end_flush`, `ob_get_flush` o al final del script), el gestor `'URL-Rewriter'` añade las parejas nombre/valor como argumentos de consulta a las URLs en los atributos de las etiquetas HTML y añade campos ocultos a los formularios según los valores de las directivas de configuración [url_rewriter.tags](#ini.url-rewriter.tags) y [url_rewriter.hosts](#ini.url-rewriter.hosts).

Cada pareja nombre/valor añadida al gestor `'URL-Rewriter'` se añade a las URLs y/o formularios incluso si esto resulta en argumentos de consulta de URL duplicados o elementos con los mismos atributos de nombre.

> [!NOTE]
> Una vez que el gestor `'URL-Rewriter'` ha sido desactivado, no puede ser reiniciado.

> [!WARNING]
> Antes de PHP 8.4.0, los hosts a reescribir se definían en [session.trans_sid_hosts](#ini.session.trans-sid-hosts) en lugar de [url_rewriter.hosts](#ini.url-rewriter.hosts).

## Parámetros

`name`  
El nombre de la variable.

`value`  
El valor de la variable.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | A partir de PHP 7.1.0, se utiliza un búfer de salida dedicado, [url_rewriter.tags](#ini.url-rewriter.tags) se utiliza únicamente para las funciones de salida y [url_rewriter.hosts](#ini.url-rewriter.tags) está disponible. Anterior a PHP 7.1.0, las variables de reescritura definidas por `output_add_rewrite_var` compartían un búfer de salida con el soporte transparente del ID de sesión (ver [session.trans_sid_tags](#ini.session.trans-sid-tags)). |

## Ejemplos

Ejemplo con `output_add_rewrite_var`

```
<?php
ini_set('url_rewriter.tags', 'a=href,form=');

output_add_rewrite_var('var', 'value');

// Algunos enlaces
echo '<a href="file.php">link</a>
<a href="http://example.com">link2</a>';

// un formulario
echo '<form action="script.php" method="post">
<input type="text" name="var2" />
</form>';

print_r(ob_list_handlers());
?>

    
```php

El ejemplo anterior mostrará:

    <a href="file.php?var=value">link</a>
    <a href="http://example.com">link2</a>

    <form action="script.php" method="post">
    <input type="hidden" name="var" value="value" />
    <input type="text" name="var2" />
    </form>

    Array
    (
        [0] => URL-Rewriter
    )

## Véase también

`output_reset_rewrite_vars`, `ob_flush`, `ob_list_handlers`, [url_rewriter.tags](#ini.url-rewriter.tags), [url_rewriter.hosts](#ini.url-rewriter.hosts)
