---
title: pcntl_fork
description: Duplica el proceso actual
source_url: https://www.php.net/manual/es/function.pcntl-fork.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcntl/functions/pcntl-fork.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcntl
translation_status: ready
translation_reviewed: true
translation_revision: 58c419eb2
order: 61220
---

pcntl_fork

Duplica el proceso actual

## Descripción

```php
pcntl_fork(): int
```php

`pcntl_fork` crea un proceso hijo, que solo difiere del proceso padre por el identificador de proceso y el identificador PPID. Consulte la página de man fork(2) para obtener detalles sobre el comportamiento de esta función en su sistema.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

En caso de éxito, el PID (identificador de proceso) del hijo es devuelto en el proceso padre, y 0 es devuelto en el proceso hijo. En caso de fallo, -1 es devuelto en el contexto del padre, no se creará ningún proceso hijo y PHP generará un error.

## Ejemplos

Ejemplo con `pcntl_fork`

```
<?php

$pid = pcntl_fork();
if ($pid == -1) {
     die('duplicación imposible');
} else if ($pid) {
     // el padre
     pcntl_wait($status); // Protege contra hijos zombis
} else {
     // el hijo
}

?>

    
```php

## Véase también

`pcntl_rfork`, `pcntl_waitpid`, `pcntl_signal`, `cli_set_process_title`
