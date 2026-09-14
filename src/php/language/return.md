---
title: return
source_url: https://www.php.net/manual/es/function.return.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/control-structures/return.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: db7aa4f29
order: 2240
---

## return

`return` devuelve el control del programa al módulo llamante. La ejecución se reanuda entonces en la instrucción siguiente a la invocación del módulo.

Si se llama desde una función, el comando `return` termina inmediatamente la función y devuelve el argumento que se le pasa. `return` también interrumpe la ejecución del comando `eval` o de scripts.

Si se llama desde el entorno global, la ejecución del script se interrumpe. Si el script actual fue incluido con la estructura `include` o `require`, entonces el control se devuelve al script llamante. Además, si el fichero del script actual ha sido incluido a través de la instrucción `include`, entonces el valor dado a `return` será devuelto como resultado de la llamada `include`. Si `return` es llamada desde el script principal, entonces la ejecución del script se detiene. Si el script actual es [auto_prepend_file](#ini.auto-prepend-file) o [auto_append_file](#ini.auto-append-file) en el fichero `php.ini`, entonces la ejecución del script se detiene.

Para más información, véase [devolver valores](#functions.returning-values).

> [!NOTE]
> Tenga en cuenta que ya que `return` es una estructura de lenguaje, y no una función, los paréntesis que rodean los argumentos no son necesarios y su uso está desaconsejado.

> [!NOTE]
> Si no se proporciona ningún parámetro, entonces los paréntesis deben ser omitidos y `null` será devuelto. La llamada de `return` con paréntesis pero sin argumento resultará en una alerta de análisis.

A partir de PHP 7.1.0, las declaraciones de retorno sin argumento en la función generan un `E_COMPILE_ERROR`, excepto si el tipo de retorno es `void`, en cuyo caso las declaraciones de retorno con un argumento generan este error.
