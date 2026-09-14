---
title: highlight_string
description: Aplica la sintaxis colorizada a código PHP
source_url: https://www.php.net/manual/es/function.highlight-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/highlight-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: ba50f222e
order: 47110
---

highlight_string

Aplica la sintaxis colorizada a código PHP

## Descripción

```php
highlight_string(string $string, [bool $return]): string
```php

Muestra o devuelve el código HTML de la versión colorizada del código PHP contenido en el argumento `str`, utilizando los colores del sistema interno de coloración de PHP.

## Parámetros

`string`  
El código PHP a colorizar. Debe incluir también las etiquetas de apertura.

`return`  
Definir este argumento a `true` para que esta función devuelva el código colorizado.

## Valores devueltos

Si el segundo argumento opcional `return` es proporcionado, y vale `true` entonces `highlight_string` devolverá la cadena colorizada en lugar de mostrarla inmediatamente. Si el segundo argumento no vale `true` entonces `highlight_string` devolverá `true`.

## Historial de cambios

| Versión | Descripción                                                  |
|---------|--------------------------------------------------------------|
| 8.4.0   | El tipo de retorno ha pasado de `stringbool` a `stringtrue`. |
| 8.3.0   | El HTML resultante ha cambiado.                              |

## Ejemplos

Ejemplo con `highlight_string`

```
<?php
highlight_string('<?php phpinfo(); ?>');
?>

    
```php

El ejemplo anterior mostrará:

    <code><span style="color: #000000">
    <span style="color: #0000BB">&lt;?php phpinfo</span><span style="color: #007700">(); </span><span style="color: #0000BB">?&gt;</span>
    </span>
    </code>

        

Resultado del ejemplo anterior en PHP 8.3:

    <pre><code style="color: #000000"><span style="color: #0000BB">&lt;?php phpinfo</span><span style="color: #007700">(); </span><span style="color: #0000BB">?&gt;</span></code></pre>

## Notas

> [!NOTE]
> Cuando el parámetro `return` es utilizado, esta función utiliza el buffer interno de salida, por lo tanto no puede ser utilizado en la función de devolución de llamada de `ob_start`.

El código HTML generado está sujeto a cambios.

## Véase también

`highlight_file`, [Las directivas INI de coloración](#ini.syntax-highlighting)
