---
title: exec
description: Ejecuta un programa externo
source_url: https://www.php.net/manual/es/function.exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: b412bbd26
order: 20550
---

exec

Ejecuta un programa externo

## Descripción

```php
exec(string $command, [array $output], [int $result_code]): string
```php

`exec` ejecuta el comando `command`.

## Parámetros

`command`  
El comando a ejecutar.

`output`  
Si el argumento `output` está presente, entonces este array será rellenado por las líneas devueltas por el comando. Los espacios al inicio y al final de la cadena, como `\n`, no serán incluidos en este array. Cabe señalar que si este array contiene elementos, `exec` añadirá las nuevas líneas al final del array. Si no se desean concatenar los nuevos elementos, utilice la función `unset` con este array antes de pasárselo a `exec`.

`result_code`  
Si el argumento `result_code` está presente además del array `output`, entonces el estado de retorno de ejecución será escrito en esta variable.

## Valores devueltos

La última línea del resultado del comando. Para ejecutar un comando y obtener el resultado sin ningún tratamiento, debe utilizarse la función `passthru`.

Devuelve `false` en caso de error.

Para recuperar la salida del comando ejecutado, asegúrese de definir y utilizar el parámetro `output`.

## Errores/Excepciones

Emite una advertencia `E_WARNING` si `exec` no puede ejecutar el comando `command`.

Levanta una excepción `ValueError` si `command` está vacío o contiene bytes nulos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si `command` está vacío o contiene bytes nulos, `exec` levanta ahora una excepción `ValueError`. Anteriormente, se emitía una advertencia `E_WARNING` y se devolvía `false`. |

## Ejemplos

Ejemplo con `exec`

```
<?php
// Muestra el nombre de usuario que ejecuta el proceso php/http
// (en un sistema que tenga "whoami" en el camino de ejecutables)
$output=null;
$retval=null;
exec('whoami', $output, $retval);
echo "Devuelto con estado $retval y salida:\n";
print_r($output);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Devuelto con estado 0 y salida:
    Array
    (
        [0] => cmb
    )

## Notas

> [!WARNING]
> Si los datos provenientes de los usuarios tienen permiso de ser pasados a esta función, utilice `escapeshellarg` o `escapeshellcmd` para asegurarse de que los usuarios no puedan hacer que el sistema ejecute comandos arbitrarios.

> [!NOTE]
> Si un programa es iniciado con esta función y se ejecuta en segundo plano, la salida del programa debe ser redirigida a un fichero, o a otro flujo de salida. De lo contrario, PHP se bloqueará hasta el final de la ejecución del programa.

> [!NOTE]
> En Windows `exec` iniciará primero cmd.exe para ejecutar el comando. Si se desea iniciar un programa externo sin ejecutar cmd.exe utilice `proc_open` definiendo la opción `bypass_shell`.

## Véase también

`system`, `passthru`, `escapeshellcmd`, `pcntl_exec`, [comillas invertidas](#language.operators.execution)
