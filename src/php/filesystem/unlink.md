---
title: unlink
description: Elimina un fichero
source_url: https://www.php.net/manual/es/function.unlink.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/unlink.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: ea62fb831
order: 24090
---

unlink

Elimina un fichero

## Descripción

```php
unlink(string $filename, [resource $context]): bool
```php

Elimina `filename`. Similar a la función C Unix `unlink()`. En caso de error, se generará una advertencia de nivel `E_WARNING`.

## Parámetros

`filename`  
Ruta de acceso al fichero.

Si el fichero es un enlace simbólico, se eliminará el enlace simbólico. En Windows, para eliminar un enlace simbólico a un directorio, debe utilizarse `rmdir` en su lugar.

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | En Windows, ahora es posible utilizar `unlink` para eliminar ficheros cuyos gestores están en uso, lo cual antes fallaba. Sin embargo, aún no es posible recrear el fichero eliminado hasta que todos sus gestores sean cerrados. |

## Ejemplos

Ejemplo con `unlink`

```
<?php
$fh = fopen('test.html', 'a');
fwrite($fh, '<h1>Hello world!</h1>');
fclose($fh);

unlink('test.html');
?>

    
```php

## Véase también

`rmdir`
