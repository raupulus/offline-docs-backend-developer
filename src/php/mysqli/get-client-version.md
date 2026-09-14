---
title: mysqli::$client_version
description: Devuelve la versión del cliente MySQL como un entero
source_url: https://www.php.net/manual/es/mysqli.get-client-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-client-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: d68e83b71
order: 55080
---

mysqli::\$client_version

mysqli_get_client_version

Devuelve la versión del cliente MySQL como un entero

## Descripción

Estilo orientado a objetos

int

mysqli-\>client_version

Estilo procedimental

```php
mysqli_get_client_version(): int
```php

Devuelve la versión del cliente MySQL como un entero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un número que representa la versión de la biblioteca cliente MySQL en este formato: `versión_principal*10000 + versión_menor *100 + subversión`. Por ejemplo, la versión 4.1.0 se devuelve como 40100.

Esta función es útil para determinar la versión de la biblioteca cliente para saber si existen características específicas.

## Ejemplos

Ejemplo con `mysqli_get_client_version`

```
<?php

/* No necesitamos una conexión para
   determinar la versión de la biblioteca cliente mysql */

printf("Versión de la biblioteca cliente: %d\n", mysqli_get_client_version());
?>

    
```php

## Véase también

`mysqli_get_client_info`, `mysqli_get_server_info`, `mysqli_get_server_version`
