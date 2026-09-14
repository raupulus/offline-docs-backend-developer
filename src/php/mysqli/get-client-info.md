---
title: mysqli::$client_info
description: Obtiene información sobre el cliente MySQL
source_url: https://www.php.net/manual/es/mysqli.get-client-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-client-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 9b1673cf1
order: 55070
---

mysqli::\$client_info

mysqli::get_client_info

mysqli_get_client_info

Obtiene información sobre el cliente MySQL

## Descripción

Estilo orientado a objetos

string

mysqli-\>client_info

```php
#[\Deprecated] public mysqli::get_client_info(): string
```php

Estilo procedimental

```php
mysqli_get_client_info([mysqli $mysql]): string
```

Devuelve un `string` que representa la versión de la biblioteca cliente MySQL.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `string` que representa la versión del cliente utilizado por la extensión MySQL.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | La llamada a la `mysqli_get_client_info` con el argumento `mysql` ha sido deprecada. Esta función nunca ha requerido un parámetro, pero lo ha permitido de manera incorrecta como parámetro opcional. |
| 8.1.0 | El estilo orientado a objetos mysqli::get_client_info ha sido deprecado. |

## Ejemplos

Ejemplo con `mysqli_get_client_info`

```php
<?php

/* No es necesaria una conexión para determinar
    la versión del cliente utilizada por la extensión MySQL */

printf("Versión de la biblioteca cliente: %s\n", mysqli_get_client_info());
?>

    
```

## Véase también

`mysqli_get_client_version`, `mysqli_get_server_info`, `mysqli_get_server_version`
