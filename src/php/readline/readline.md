---
title: readline
description: Lee una línea
source_url: https://www.php.net/manual/es/function.readline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: 53208f9bd
order: 68830
---

readline

Lee una línea

## Descripción

```php
readline([string $prompt]): string
```php

Devuelve una línea introducida por el usuario. La línea debe ser añadida al historial manualmente, mediante la función `readline_add_history`.

## Parámetros

`prompt`  
Puede especificarse un `string` para utilizarlo como prompt al usuario.

## Valores devueltos

Devuelve un `string` del usuario. La línea devuelta ha sido limpiada del carácter final de nueva línea. Si no hay más datos para leer, entonces se devuelve `false`.

## Ejemplos

Ejemplo con `readline`

```
<?php
// Lee 3 comandos del usuario
for ($i=0; $i < 3; $i++) {
        $line = readline("Comando : ");
        readline_add_history($line);
}

// Lista el historial
print_r(readline_list_history());

// Lista las variables
print_r(readline_info());
?>

   
```php
