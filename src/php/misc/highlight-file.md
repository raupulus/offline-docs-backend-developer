---
title: highlight_file
description: Coloración sintáctica de un fichero
source_url: https://www.php.net/manual/es/function.highlight-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/highlight-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 443d81b33
order: 47100
---

highlight_file

Coloración sintáctica de un fichero

## Descripción

```php
highlight_file(string $filename, [bool $return]): string
```php

Muestra la sintaxis colorizada del fichero `filename`, utilizando los colores definidos en el motor interno de PHP.

Muchos servidores están configurados para mostrar automáticamente el código fuente colorizado, con la extensión *phps*. Por ejemplo, `example.phps` muestra el código del script. Para activar esta funcionalidad, utilice esta línea en `httpd.conf` :

    AddType application/x-httpd-php-source .phps

      

## Parámetros

`filename`  
La ruta hacia el fichero PHP a colorizar.

`return`  
Al pasar este argumento a `true`, la función devuelve el código colorizado en lugar de mostrarlo.

## Valores devueltos

Si el segundo parámetro opcional `return` vale `true` entonces `highlight_file` devolverá el código generado, en lugar de mostrarlo. Si el segundo parámetro no vale `true` entonces `highlight_file` devolverá `true` en caso de éxito, y `false` en caso contrario.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.3.0   | El HTML resultante ha cambiado. |

## Notas

> [!CAUTION]
> Se debe tener mucho cuidado al utilizar `highlight_file` para asegurarse de que no se revelen información crítica como contraseñas u otra información que podría causar fugas de información.

> [!NOTE]
> Cuando el parámetro `return` es utilizado, esta función utiliza el buffer interno de salida, por lo tanto no puede ser utilizado en la función de devolución de llamada de `ob_start`.

## Véase también

`highlight_string`, [Las directivas INI de coloración](#ini.syntax-highlighting)
