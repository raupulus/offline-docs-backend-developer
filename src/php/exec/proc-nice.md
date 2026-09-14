---
title: proc_nice
description: Modifica la prioridad de ejecución del proceso actual
source_url: https://www.php.net/manual/es/function.proc-nice.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/proc-nice.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: 4ecb2c1b4
order: 20590
---

proc_nice

Modifica la prioridad de ejecución del proceso actual

## Descripción

```php
proc_nice(int $priority): bool
```php

`proc_nice` modifica la prioridad del proceso actual mediante el argumento especificado `priority`. Un argumento `priority` positivo reducirá la prioridad del proceso actual, mientras que un valor negativo `priority` aumentará la prioridad.

`proc_nice` no está relacionado con `proc_open` ni con sus funciones asociadas de ninguna manera.

## Parámetros

`priority`  
El nuevo valor de prioridad, este valor puede variar según la plataforma.

En Unix, un valor bajo, como `-20` indica una prioridad alta, mientras que un valor positivo indica una prioridad baja.

Para Windows, el argumento `priority` tiene las siguientes significaciones:

| Clase de prioridad                | Valores posibles                     |
|-----------------------------------|--------------------------------------|
| Prioridad alta                    | `priority` `< -9`                    |
| Por encima de la prioridad normal | `priority` `< -4`                    |
| Prioridad normal                  | `priority` `< 5` & `priority` `> -5` |
| Por debajo de la prioridad normal | `priority` `> 5`                     |
| Prioridad inactiva                | `priority` `> 9`                     |

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si ocurre un error, por ejemplo, si el usuario que intenta cambiar la prioridad de un proceso no tiene suficientes permisos para hacerlo, se genera un error de nivel `E_WARNING` y se devuelve `false`.

## Historial de cambios

| Versión | Descripción                                    |
|---------|------------------------------------------------|
| 7.2.0   | Esta función está ahora disponible en Windows. |

## Ejemplos

Uso de `proc_nice` para establecer una prioridad de proceso alta

```
<?php
// Prioridad más alta
proc_nice(-20);
?>

    
```php

## Notas

> [!NOTE]
> `proc_nice` solo está disponible en sistemas que disponen de capacidades NICE. NICE es compatible con: SVr4, SVID EXT, AT&T, X/OPEN, BSD 4.3.

> [!NOTE]
> `proc_nice` cambiará la prioridad del *proceso* actual incluso si PHP ha sido compilado utilizando la seguridad de hilos.

## Véase también

pcntl_setpriority
