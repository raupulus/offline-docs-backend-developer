---
title: pcntl_waitpid
description: Espera la finalización de la ejecución de un proceso hijo
source_url: https://www.php.net/manual/es/function.pcntl-waitpid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-waitpid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: false
translation_revision: a747e132c
order: 61440
---

pcntl_waitpid

Espera la finalización de la ejecución de un proceso hijo

## Descripción

```php
pcntl_waitpid(int $process_id, int $status, [int $flags], [array $resource_usage]): int
```php

Suspende la ejecución del proceso actual hasta que un proceso hijo especificado por el parámetro `process_id` haya terminado, una señal haya terminado este proceso o una señal haya llamado a un gestor de señales.

Si el proceso hijo identificado por `process_id` ya ha terminado en el momento de la llamada a esta función (se les llama procesos "zombie"), la función termina inmediatamente. Cualquier recurso del sistema utilizado por el proceso hijo es liberado. Consulte la página de man waitpid(2) para obtener detalles sobre el comportamiento de esta función en su sistema.

## Parámetros

`process_id`  
El valor de `process_id` puede ser uno de los siguientes:

|  |  |
|----|----|
| `< -1` | espera un proceso hijo cuyo identificador de grupo es igual al valor absoluto de `process_id`. |
| `-1` | espera cualquier proceso hijo; esto corresponde al mismo comportamiento que el de la función `pcntl_wait` presente. |
| `0` | espera un proceso hijo cuyo identificador de grupo es igual al del proceso actual. |
| `> 0` | espera el proceso hijo cuyo identificador es igual al valor de `process_id`. |

Valores posibles para `process_id`

> [!NOTE]
> Especificando `-1` como `process_id`, esto equivale a la funcionalidad que proporciona `pcntl_wait` (menos `flags`).

`status`  
`pcntl_waitpid` registrará información sobre el estado actual del proceso en el parámetro `status`, al cual se puede acceder gracias a las siguientes funciones: `pcntl_wifexited`, `pcntl_wifstopped`, `pcntl_wifsignaled`, `pcntl_wexitstatus`, `pcntl_wtermsig` y `pcntl_wstopsig`.

`flags`  
El parámetro `flags` puede tomar el valor cero, o varias de las siguientes constantes globales (combinadas con el operador `OR`):

|  |  |
|----|----|
| `WNOHANG` | retorna inmediatamente si ningún proceso hijo ha terminado. |
| `WUNTRACED` | retorna cuando los procesos hijos están detenidos y su estado no ha sido actualizado. |

Valores posibles de `flags`

## Valores devueltos

`pcntl_waitpid` retorna el identificador de proceso del proceso hijo que ha terminado, o bien -1 en caso de error o cero si `WNOHANG` ha sido utilizado y ningún proceso hijo estaba disponible.

## Véase también

`pcntl_fork`, `pcntl_signal`, `pcntl_wifexited`, `pcntl_wifstopped`, `pcntl_wifsignaled`, `pcntl_wexitstatus`, `pcntl_wtermsig`, `pcntl_wstopsig`
