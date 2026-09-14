---
title: pcntl_exec
description: Ejecuta el programa indicado en el espacio actual de procesos
source_url: https://www.php.net/manual/es/function.pcntl-exec.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-exec.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: fcd921429
order: 61210
---

pcntl_exec

Ejecuta el programa indicado en el espacio actual de procesos

## Descripción

```php
pcntl_exec(string $path, [array $args], [array $env_vars]): false
```php

Ejecuta el programa indicado en el espacio actual de procesos.

## Parámetros

`path`  
`path` debe ser la ruta hacia un binario ejecutable o un script con una ruta válida apuntando a un ejecutable en la primera línea (por ejemplo, \#!/usr/local/bin/perl). Ver las páginas de ayuda de su sistema concernientes a execve(2) para más información.

`args`  
`args` es un array de argumentos en forma de strings pasados al programa.

`env_vars`  
`env_vars` es un array de strings que son pasadas al programa como variables de entorno. El array es de la forma nombre =\> valor, la clave es el nombre de la variable de entorno y el valor es el valor de esta variable.

## Valores devueltos

Devuelve `false`.
