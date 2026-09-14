---
title: passthru
description: Ejecuta un programa externo y muestra el resultado sin procesar
source_url: https://www.php.net/manual/es/function.passthru.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/passthru.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: b412bbd26
order: 20560
---

passthru

Ejecuta un programa externo y muestra el resultado sin procesar

## Descripción

```php
passthru(string $command, [int $result_code]): false
```php

`passthru` es similar a la función `exec` ya que ambas ejecutan el comando `command`. Si el argumento `result_code` está presente, el código de estado de respuesta UNIX será colocado allí. Esta función debe preferirse a las funciones `exec` o `system` cuando el resultado esperado es de tipo binario y debe pasarse sin procesar a un navegador. Un uso clásico de esta función es la ejecución de la utilidad pbmplus que puede devolver una imagen. Al establecer el tipo de contenido (Content-Type) a `image/gif` y luego llamar a pbmplus para obtener una imagen gif, se pueden crear scripts PHP que devuelven imágenes.

## Parámetros

`command`  
El comando a ejecutar.

`result_code`  
Si el argumento `result_code` está presente, el estado devuelto por el comando Unix será colocado en esta variable.

## Valores devueltos

Esta función retorna `null` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si `passthru` no puede ejecutar el comando `command`.

Genera una excepción `ValueError` si `command` está vacío o contiene caracteres nulos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si `command` está vacío o contiene caracteres nulos, `passthru` ahora genera una excepción `ValueError`. Anteriormente, se emitía una advertencia `E_WARNING` y se devolvía `false`. |

## Notas

> [!WARNING]
> Si los datos provenientes de los usuarios tienen permiso de ser pasados a esta función, utilice `escapeshellarg` o `escapeshellcmd` para asegurarse de que los usuarios no puedan hacer que el sistema ejecute comandos arbitrarios.

> [!NOTE]
> Si un programa es iniciado con esta función y se ejecuta en segundo plano, la salida del programa debe ser redirigida a un fichero, o a otro flujo de salida. De lo contrario, PHP se bloqueará hasta el final de la ejecución del programa.

## Véase también

`exec`, `system`, `popen`, `escapeshellcmd`, [comillas invertidas](#language.operators.execution)
