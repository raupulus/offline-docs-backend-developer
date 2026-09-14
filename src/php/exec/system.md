---
title: system
description: Ejecutar un programa externo y mostrar su salida
source_url: https://www.php.net/manual/es/function.system.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/system.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 20630
---

system

Ejecutar un programa externo y mostrar su salida

## Descripción

```php
system(string $command, [int $result_code]): string
```php

`system` es similar a la versión C de la función de mismo nombre, dado que ejecuta el `command` dado y muestra el resultado.

La llamada a `system` también intenta volcar automáticamente el búfer de salida del servidor web después de cada línea de salida, si PHP está corriendo como un módulo de servidor.

Si necesita ejecutar un comando y recibir de vuelta todo los datos del mismo sin interferencias, use la función `passthru`.

## Parámetros

`comando`  
El comando que será ejecutado.

`result_code`  
Si el argumento `result_code` se encuentra presente, entonces el status devuelto por el comando ejecutado será almacenado en esta variable.

## Valores devueltos

Devuelve la última línea de la salida del comando en caso de tener éxito, y `false` si ocurre un error.

## Ejemplos

Ejemplo de `system`

```
<?php
echo '<pre>';

// Muestra el resultado completo del comando "ls", y devuelve la
// ultima linea de la salida en $ultima_linea. Almacena el valor de
// retorno del comando en $retval.
$ultima_linea = system('ls', $retval);

// Imprimir informacion adicional
echo '
</pre>
<hr />Ultima linea de la salida: ' . $ultima_linea . '
<hr />Valor de retorno: ' . $retval;
?>

    
```php

## Notas

> [!WARNING]
> Si los datos provenientes de los usuarios tienen permiso de ser pasados a esta función, utilice `escapeshellarg` o `escapeshellcmd` para asegurarse de que los usuarios no puedan hacer que el sistema ejecute comandos arbitrarios.

> [!NOTE]
> Si un programa es iniciado con esta función y se ejecuta en segundo plano, la salida del programa debe ser redirigida a un fichero, o a otro flujo de salida. De lo contrario, PHP se bloqueará hasta el final de la ejecución del programa.

## Véase también

`exec`, `passthru`, `popen`, `escapeshellcmd`, `pcntl_exec`, [el operador de comillas invertidas](#language.operators.execution)
