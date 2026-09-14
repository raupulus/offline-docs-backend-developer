---
title: $php_errormsg
description: El último mensaje de error
source_url: https://www.php.net/manual/es/reserved.variables.phperrormsg.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/phperrormsg.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 4301234c0
order: 4190
---

\$php_errormsg

El último mensaje de error

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0, y *ELIMINADA* a partir de PHP 8.0.0. Depender de esta funcionalidad está altamente desaconsejado.

Utilice `error_get_last` en su lugar.

## Descripción

`$php_errormsg` es una variable que contiene el texto del último error generado por PHP. Esta variable será únicamente accesible en el mismo contexto de ejecución que el de la línea que generó el error, y únicamente si la directiva de configuración [track_errors](#ini.track-errors) está activada (se encuentra desactivada por omisión).

> [!WARNING]
> Si un gestor de errores definido por el usuario está activo (`set_error_handler`), `$php_errormsg` solo será definido si el gestor de errores devuelve `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | La directiva [track_errors](#ini.track-errors) que hace que `$php_errormsg` esté disponible ha sido eliminada. |
| 7.2.0 | La directiva [track_errors](#ini.track-errors) que hace que `$php_errormsg` esté disponible ha sido marcada como obsoleta. |

## Ejemplos

Ejemplo con `$php_errormsg`

```php
<?php
@strpos();
echo $php_errormsg;
?>

    
```

Resultado del ejemplo anterior es similar a:

    Wrong parameter count for strpos()

## Véase también

`error_get_last`
