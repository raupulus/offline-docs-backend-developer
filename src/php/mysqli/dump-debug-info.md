---
title: mysqli::dump_debug_info
description: Escribe la información de depuración en los registros
source_url: https://www.php.net/manual/es/mysqli.dump-debug-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/dump-debug-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55000
---

mysqli::dump_debug_info

mysqli_dump_debug_info

Escribe la información de depuración en los registros

## Descripción

Estilo orientado a objetos

```php
public mysqli::dump_debug_info(): bool
```php

Estilo procedimental

```php
mysqli_dump_debug_info(mysqli $mysql): bool
```

Esta función debe ser utilizada por un usuario con el privilegio SUPER y se emplea para escribir cierta información de depuración en el registro para el servidor MySQL relativo a la conexión especificada por el argumento `link`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`mysqli_debug`
