---
title: $argc
description: El número de argumentos pasados a un script
source_url: https://www.php.net/manual/es/reserved.variables.argc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/argc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: a6d209f4f
order: 4110
---

\$argc

El número de argumentos pasados a un script

## Descripción

Contiene el número de argumentos pasados al script actual cuando se ejecuta desde la [línea de comandos](#features.commandline).

> [!NOTE]
> El nombre del script es pasado siempre como argumento del script, por lo tanto, el valor mínimo de `$argc` es `1`.

> [!NOTE]
> Esta variable sólo está disponible cuando [register_argc_argv](#ini.register-argc-argv) está activado.

## Ejemplos

Ejemplo de `$argc`

```php
<?php
var_dump($argc);
?>

    
```

Cuando se ejecuta el ejemplo con: php script.php arg1 arg2 arg3

Resultado del ejemplo anterior es similar a:

    int(4)

## Notas

> [!NOTE]
> Esto también está disponible como `$_SERVER['argc']`.

## Véase también

`getopt`, [`$argv`](#reserved.variables.argv)
