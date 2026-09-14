---
title: ob_start
description: Activa el temporizador de salida
source_url: https://www.php.net/manual/es/function.ob-start.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-start.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: e58094c45
order: 59860
---

ob_start

Activa el temporizador de salida

## Descripción

```php
ob_start([callable $callback], [int $chunk_size], [int $flags]): bool
```php

Esta función activa el almacenamiento en búfer de la salida. Cuando el almacenamiento en búfer está activo, ninguna salida es enviada desde el script; en su lugar, la salida se almacena en un búfer interno. Consulte [???](#outcontrol.what-output-is-buffered) para saber exactamente qué salidas están afectadas.

Los búferes de salida son apilables, es decir `ob_start` puede ser llamada mientras otro búfer está activo. Si varios búferes de salida están activos, la salida es filtrada secuencialmente a través de cada uno de ellos en el orden de anidación. Consulte [???](#outcontrol.nesting-output-buffers) para más detalles.

Consulte [???](#outcontrol.user-level-output-buffers) para una descripción detallada de los búferes de salida.

## Parámetros

`callback`  
Un `callback` `callable` opcional puede ser especificado. También puede ser omitido pasando `null`.

`callback` es invocado cuando el búfer de salida es vaciado (enviado), limpiado, o cuando el búfer de salida es vaciado al final del script.

La firma del `callback` es la siguiente:

```php
handler(string $buffer, [int $phase]): string
```

`buffer`  
Contenido del buffer de salida.

`phase`  
Máscara de bits de las constantes [ `PHP_OUTPUT_HANDLER_*` ](#constant.php-output-handler-start). Consulte [???](#outcontrol.flags-passed-to-output-handlers) para más detalles.

Si `callback` devuelve `false`, el contenido del búfer es enviado. Consulte [???](#outcontrol.output-handler-return-values) para más detalles.

> [!WARNING]
> Llamar a alguna de las siguientes funciones desde un manejador de salida provocará un error fatal: `ob_clean`, `ob_end_clean`, `ob_end_flush`, `ob_flush`, `ob_get_clean`, `ob_get_flush`, `ob_start`.

Consulte [???](#outcontrol.output-handlers) y [???](#outcontrol.working-with-output-handlers) para más detalles sobre los `callback`s (manejadores de salida).

`chunk_size`  
Si el parámetro opcional `chunk_size` es pasado, la función de devolución de llamada es llamada cada nueva línea después de `chunk_size` bytes de salida. El valor por omisión `0` significa que toda la salida es almacenada en búfer hasta que el búfer sea desactivado. Consulte [???](#outcontrol.buffer-size) para más detalles.

`flags`  
El parámetro `flags` es una máscara que controla las operaciones que pueden ser realizadas sobre el búfer de salida. Por omisión, permite que el búfer de salida sea limpiado, enviado y eliminado, lo cual puede ser definido explícitamente con los [ indicadores de control del búfer ](#outcontrol.constants.buffer-control-flags). Consulte [???](#outcontrol.operations-on-buffers) para más detalles.

Cada flag controla el acceso a un conjunto de funciones, tal como se describe a continuación:

| Constante | Funciones |
|----|----|
| `PHP_OUTPUT_HANDLER_CLEANABLE` | `ob_clean`, |
| `PHP_OUTPUT_HANDLER_FLUSHABLE` | `ob_flush`, |
| `PHP_OUTPUT_HANDLER_REMOVABLE` | `ob_end_clean`, `ob_end_flush` y `ob_get_clean`. `ob_get_flush`. |

> [!NOTE]
> Antes de PHP 8.4.0, el parámetro flags podía definir los [flags de estado del manejador de salida](#outcontrol.constants.flags-returned-by-handler) también.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de manejo de salida con función de devolución de llamada

```php
<?php

function handler($buffer)
{
  // reemplaza todas las patatas por zanahorias
  return (str_replace("pommes de terre", "carottes", $buffer));
}

ob_start("handler");

?>
<html>
<body>
<p>Es como comparar zanahorias y patatas.</p>
</body>
</html>
<?php

ob_end_flush();

?>

    
```

El ejemplo anterior mostrará:

    <html>
    <body>
    <p>Es como comparar zanahorias y zanahorias.</p>
    </body>
    </html>

Crea un búfer de salida no eliminable

```php
<?php

ob_start(null, 0, PHP_OUTPUT_HANDLER_STDFLAGS ^ PHP_OUTPUT_HANDLER_REMOVABLE);

?>

    
```

## Véase también

`ob_get_contents`, `ob_end_clean`, `ob_end_flush`, `ob_implicit_flush`, `ob_gzhandler`, `ob_iconv_handler`, `mb_output_handler`, `ob_tidyhandler`
