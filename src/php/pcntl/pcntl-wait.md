---
title: pcntl_wait
description: Espera o devuelve el estado de un proceso hijo
source_url: https://www.php.net/manual/es/function.pcntl-wait.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-wait.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 61374bbe2
order: 61420
---

pcntl_wait

Espera o devuelve el estado de un proceso hijo

## Descripción

```php
pcntl_wait(int $status, [int $flags], [array $resource_usage]): int
```php

La función wait suspende la ejecución del proceso actual hasta que uno de los procesos hijos haya terminado, o hasta que se envíe una señal para terminar el proceso actual o para llamar a un gestor. Si el proceso ya ha terminado en el momento de la llamada a la función, es decir, si el proceso es un zombie, entonces la función termina inmediatamente. Todos los recursos del sistema utilizados por el proceso hijo son liberados. Consulte el manual de su sistema en wait(2) para obtener detalles específicos sobre el funcionamiento de wait() en él.

> [!NOTE]
> Esta función es equivalente a llamar a la función `pcntl_waitpid` con un `-1` `process_id` y sin `flags`.

## Parámetros

`status`  
`pcntl_wait` almacenará la información de estado en el parámetro `status` que puede ser leído con las siguientes funciones: `pcntl_wifexited`, `pcntl_wifstopped`, `pcntl_wifsignaled`, `pcntl_wexitstatus`, `pcntl_wtermsig` y `pcntl_wstopsig`.

`flags`  
Si wait3 está disponible en su sistema (esto es el caso de la mayoría de los sistemas BSD-), puede añadir el parámetro opcional `flags`. Si no se proporciona, wait() será utilizado para la llamada al sistema. Si wait3 no está disponible, el parámetro `flags` no tendrá efecto. El valor de `flags` es la combinación de cero o más de las siguientes dos constantes con el operador `OR`:

|  |  |
|----|----|
| `WNOHANG` | Termina inmediatamente si ningún proceso ha terminado. |
| `WUNTRACED` | Termina para los procesos que están detenidos, y para aquellos cuyo resultado no ha sido reportado. |

Valores posibles para `flags`

## Valores devueltos

`pcntl_wait` devuelve el identificador de proceso que ha terminado, -1 en caso de error o cero si WNOHANG ha sido proporcionado como opción (disponible en los sistemas wait3), y ningún proceso hijo estaba disponible.

## Véase también

`pcntl_fork`, `pcntl_signal`, `pcntl_wifexited`, `pcntl_wifstopped`, `pcntl_wifsignaled`, `pcntl_wexitstatus`, `pcntl_wtermsig`, `pcntl_wstopsig`, `pcntl_waitpid`
