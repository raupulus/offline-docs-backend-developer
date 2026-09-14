---
title: expect_popen
description: Ejecuta comandos por la shell Bourne, y abre el flujo PTY al proceso
source_url: https://www.php.net/manual/es/function.expect-popen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/expect/functions/expect-popen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: expect
translation_status: ready
translation_revision: ca6054f60
order: 20780
---

expect_popen

Ejecuta comandos por la shell Bourne, y abre el flujo PTY al proceso

## Descripción

```php
expect_popen(string $command): resource
```php

Ejecuta comandos por la shell Bourne, y abre el flujo PTY al proceso.

## Parámetros

`command`  
Comando a ejecutar.

## Valores devueltos

Devuelve un flujo PTY abierto al `stdio`, `stdout`, y `stderr` del prceso.

En caso de error, devuelve `false`.

## Ejemplos

Ejemplo de `expect_popen`

```
<?php
// Entrar en el repositorio CVS de PHP.net
$stream = expect_popen ("cvs -d :pserver:anonymous@cvs.php.net:/repository login");
sleep (3);
fwrite ($stream, "phpfi\n");
fclose ($stream);
?>

   
```php

## Véase también

popen
