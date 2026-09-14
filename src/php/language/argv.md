---
title: $argv
description: Array de argumentos pasados al script
source_url: https://www.php.net/manual/es/reserved.variables.argv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/argv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 74ba8fee2
order: 4120
---

\$argv

Array de argumentos pasados al script

## Descripción

Contiene un `array` de todos los argumentos pasados al script cuando es llamado desde la [línea de comandos](#features.commandline).

> [!NOTE]
> El primer argumento `$argv[0]` siempre es el nombre que se ha utilizado para ejecutar el script.

> [!NOTE]
> Esta variable no está disponible cuando [register_argc_argv](#ini.register-argc-argv) está desactivado.

> [!WARNING]
> Para verificar si un script es ejecutado desde la línea de comandos, se recomienda utilizar `php_sapi_name` en lugar de verificar si `$argv` o `$_SERVER['argv']` está definido.

## Ejemplos

Ejemplo con `$argv`

```php
<?php
var_dump($argv);
?>

    
```

Cuando se ejecuta el ejemplo con el comando: php script.php arg1 arg2 arg3

Resultado del ejemplo anterior es similar a:

    array(4) {
      [0]=>
      string(10) "script.php"
      [1]=>
      string(4) "arg1"
      [2]=>
      string(4) "arg2"
      [3]=>
      string(4) "arg3"
    }

## Notas

> [!NOTE]
> También disponible en `$_SERVER['argv']`.

## Véase también

`getopt`, [`$argc`](#reserved.variables.argc)
