---
title: mysqli::character_set_name
description: Devuelve el juego de caracteres actual para la conexión
source_url: https://www.php.net/manual/es/mysqli.character-set-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/character-set-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 54930
---

mysqli::character_set_name

mysqli_character_set_name

Devuelve el juego de caracteres actual para la conexión

## Descripción

Estilo orientado a objetos

```php
public mysqli::character_set_name(): string
```php

Estilo procedimental

```php
mysqli_character_set_name(mysqli $mysql): string
```

Devuelve el juego de caracteres actual para la conexión especificada por el argumento `link`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

El juego de caracteres actual para la conexión actual.

## Ejemplos

Ejemplo de mysqli::character_set_name

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Establecer el juego de caracteres predeterminado */
$mysqli->set_charset('utf8mb4');

/* Mostrar el juego de caracteres actual */
$charset = $mysqli->character_set_name();
printf("El juego de caracteres actual es %s\n", $charset);

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Establecer el juego de caracteres predeterminado */
mysqli_set_charset($mysqli, 'utf8mb4');

/* Mostrar el juego de caracteres actual */
$charset = mysqli_character_set_name($mysqli);
printf("El juego de caracteres actual es %s\n", $charset);

   
```

Los ejemplos anteriores mostrarán:

    El juego de caracteres actual es utf8mb4

## Véase también

`mysqli_set_charset`, `mysqli_real_escape_string`
