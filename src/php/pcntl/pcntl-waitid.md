---
title: pcntl_waitid
description: Espera a que un proceso hijo cambie de estado
source_url: https://www.php.net/manual/es/function.pcntl-waitid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-waitid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_revision: 4fbe06913
order: 61430
---

pcntl_waitid

Espera a que un proceso hijo cambie de estado

## Descripción

```php
pcntl_waitid([int $idtype], [int $id], [array $info], [int $flags], [array $resource_usage]): bool
```php

Obtiene información de estado relacionada con eventos de terminación, parada y/o continuación en uno de los procesos hijos del llamador.

A menos que se pase el flag `WNOHANG`, el proceso que llama quedará bloqueado hasta que ocurra un error, o hasta que la información de estado sea disponible y cumpla con todas las siguientes condiciones:

- La información de estado proviene de uno de los procesos hijos en el conjunto de procesos hijos especificado por los argumentos `idtype` y `id`.

- El cambio de estado en la información de estado coincide con uno de los flags de cambio de estado establecidos en el argumento `flags`.

Si la información de estado coincidente está disponible antes de la llamada a `pcntl_waitid`, el retorno será inmediato. Si la información de estado coincidente está disponible para dos o más procesos hijos, el orden en que se informa su estado no está especificado.

> [!NOTE]
> Esta documentación cubre la especificación POSIX de la función `waitid`, junto con algunos parámetros adicionales específicos de las implementaciones en Linux, NetBSD y FreeBSD. Consulte la página del manual `waitid(2)` de su sistema para obtener detalles específicos sobre cómo funciona `waitid` en su sistema.

## Parámetros

`idtype`; `id`  
Los argumentos `idtype` y `id` se utilizan para especificar qué hijos esperar.

|  |  |
|----|----|
| Si `idtype` es `P_ALL` | esperar cualquier proceso hijo, `id` se ignora. |
| Si `idtype` es `P_PID` | esperar al hijo con ID de proceso igual a `id`. |
| Si `idtype` es `P_PGID` | esperar cualquier hijo con ID de grupo de procesos igual a `id`. |

Argumentos estándar POSIX `idtype` y `id`

|  |  |
|----|----|
| Si `idtype` es `P_PIDFD` (desde Linux 5.4) | esperar al hijo referenciado por el descriptor de archivo PID especificado en `id`. (Consulte la página del manual de Linux `pidfd_open(2)` para obtener más información sobre los descriptores de archivo PID.) |

Argumentos específicos de Linux `idtype` y `id`

|  |  |
|----|----|
| Si `idtype` es `P_UID` | esperar procesos cuyo ID de usuario efectivo es igual a `id`. |
| Si `idtype` es `P_GID` | esperar procesos cuyo ID de grupo efectivo es igual a `id`. |
| Si `idtype` es `P_SID` | esperar procesos cuya ID de sesión es igual a `id`. Si el proceso hijo inició su propia sesión, su ID de sesión será igual a su ID de proceso. De lo contrario, la ID de sesión de un proceso hijo coincidirá con la ID de sesión del llamador. |

Argumentos específicos de NetBSD y FreeBSD `idtype` y `id`

|  |  |
|----|----|
| Si `idtype` es `P_JAILID` | esperar procesos dentro de una cárcel cuya identificador de cárcel es igual a `id`. |

Argumentos específicos de FreeBSD `idtype` y `id`

`info`  
El parámetro `info` se establece en un array que contiene información sobre la señal.

El array `info` puede contener las siguientes claves: `signo`: Número de señal, `errno`: Número de error del sistema, `code`: Código de señal, `status`: Valor de salida o señal, `pid`: ID del proceso emisor, `uid`: ID de usuario real del proceso emisor, `utime`: Tiempo de usuario consumido, `stime`: Tiempo de sistema consumido

`flags`  
El valor de `flags` es el valor de cero o más de las siguientes constantes combinadas con OR:

|  |  |
|----|----|
| `WCONTINUED` | Se devolverá el estado de cualquier proceso hijo continuado cuyo estado no ha sido reportado desde que continuó de una parada por control de trabajos o ha sido reportado solo por llamadas a `pcntl_waitid` con el flag `WNOWAIT` establecido. |
| `WEXITED` | Esperar procesos que han finalizado. |
| `WNOHANG` | No bloquear si no hay estado disponible; devolver inmediatamente. |
| `WNOWAIT` | Mantener el proceso cuyo estado se devuelve en `info` en un estado esperable. Esto no afectará el estado del proceso; el proceso puede ser esperado de nuevo después de que esta llamada se complete. |
| `WSTOPPED` | Se devolverá el estado de cualquier hijo que se haya detenido al recibir una señal, y cuyo estado no ha sido reportado desde que se detuvo o ha sido reportado solo por llamadas a `pcntl_waitid` con el flag `WNOWAIT` establecido. |

Valores posibles para `flags`

`resource_usage`  
El parámetro `resource_usage` se establece en un array que contiene estadísticas de uso de recursos del proceso hijo. Esto se admite ya sea si la llamada al sistema wait6 está disponible (por ejemplo, en FreeBSD), o en Linux a través de la llamada al sistema waitid en bruto.

## Valores devueltos

`pcntl_waitid` devuelve `true` si `WNOHANG` fue especificado y no hay estado disponible para ningún proceso especificado por `idtype` y `id`.

`pcntl_waitid` devuelve `true` debido al cambio de estado de uno de sus hijos.

De lo contrario, se devuelve `false` y `pcntl_get_last_error` puede usarse para obtener el número de error `errno`.

> [!NOTE]
> Una vez obtenido un número de error `errno`, `pcntl_strerror` puede usarse para obtener el mensaje de texto asociado a él.

## Errores/Excepciones

|  |  |
|----|----|
| `ECHILD` | El proceso que llama no tiene procesos hijos no esperados existentes. |
| `EINTR` | `pcntl_waitid` fue interrumpido por una señal. |
| `EINVAL` | Se especificó un valor no válido para `flags`, o `idtype` y `id` especifican un conjunto no válido de procesos. |

Valores del número de error (`errno`)

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.5.0   | Se ha añadido `resource_usage`. |

## Véase también

`pcntl_waitpid`, `pcntl_wait`, `pcntl_fork`, `pcntl_signal`, `pcntl_wifexited`, `pcntl_wifstopped`, `pcntl_wifsignaled`, `pcntl_wexitstatus`, `pcntl_wtermsig`, `pcntl_wstopsig`
