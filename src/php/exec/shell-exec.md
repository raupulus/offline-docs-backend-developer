---
title: shell_exec
description: Ejecuta un comando a través del Shell y devuelve el resultado en forma
  de string
source_url: https://www.php.net/manual/es/function.shell-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/exec/functions/shell-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: exec
translation_status: ready
translation_reviewed: false
translation_revision: 7973fd533
order: 20620
---

shell_exec

Ejecuta un comando a través del Shell y devuelve el resultado en forma de string

## Descripción

```php
shell_exec(string $command): string
```php

`shell_exec` es idéntico a los [comillas invertidas](#language.operators.execution).

> [!NOTE]
> En Windows, el tubo subyacente se abre en modo texto lo que puede causar que la función falle para salidas binarias. Considerar el uso de `popen` para tales casos.

## Parámetros

`command`  
El comando a ejecutar.

## Valores devueltos

Un `string` que contiene el resultado del comando ejecutado, `false` si el pipe no puede ser establecido, o `null` si ocurre un error o si el comando no produce salida.

> [!NOTE]
> Esta función puede devolver `null` cuando ocurre un error pero también cuando el programa no produce salida. No es posible detectar fallos de ejecución utilizando esta función. La función `exec` debe ser utilizada cuando se desea recuperar el código de salida del programa.

## Errores/Excepciones

Un error de nivel `E_WARNING` es generado cuando el pipe no puede ser establecido.

## Ejemplos

Ejemplo con `shell_exec`

```
<?php
$output = shell_exec('ls -lart');
echo "<pre>$output</pre>";
?>

    
```php

## Véase también

`exec`, `escapeshellcmd`
