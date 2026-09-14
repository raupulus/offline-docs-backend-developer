---
title: Operador de ejecución
source_url: https://www.php.net/manual/es/language.operators.execution.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/execution.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: eb8957c4f
order: 2710
---

## Operador de ejecución

PHP soporta un operador de ejecución: comillas invertidas (``` `` ```). Téngase en cuenta que no se trata de comillas simples. PHP intenta ejecutar el contenido de estas comillas invertidas como un comando shell. El resultado será devuelto (es decir: no será simplemente enviado a la salida estándar, puede ser asignado a una variable). Utilizar las comillas invertidas equivale a utilizar la función `shell_exec`.

Operador de comillas invertidas

```php
<?php
$output = `ls -al`;
echo "<pre>$output</pre>";
?>

   
```

> [!NOTE]
> Este operador está desactivado cuando la función `shell_exec` está desactivada.

> [!NOTE]
> A diferencia de otros lenguajes, las comillas invertidas no tienen un significado especial en una cadena rodeada de comillas dobles.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | El operador de comillas invertidas como alias para `shell_exec` ha quedado obsoleto. |

## Véase también

[Las funciones de ejecución del sistema](#ref.exec), `popen`, `proc_open`, [Utilizar PHP desde la línea de comandos](#features.commandline)
