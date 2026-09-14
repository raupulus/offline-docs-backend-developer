---
title: sapi_windows_generate_ctrl_event
description: Envía un evento CTRL a otro proceso
source_url: https://www.php.net/manual/es/function.sapi-windows-generate-ctrl-event.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/sapi-windows-generate-ctrl-event.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 658c808b5
order: 47200
---

sapi_windows_generate_ctrl_event

Envía un evento CTRL a otro proceso

## Descripción

```php
sapi_windows_generate_ctrl_event(int $event, [int $pid]): bool
```php

Envía un evento CTRL a otro proceso en el mismo grupo de procesos.

## Parámetros

`event`  
El evento `CTRL` a enviar; puede ser `PHP_WINDOWS_EVENT_CTRL_C` o `PHP_WINDOWS_EVENT_CTRL_BREAK`.

`pid`  
El identificador del proceso al cual enviar el evento. Si se proporciona `0`, el evento se envía a todos los procesos del grupo de procesos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Uso básico de `sapi_windows_generate_ctrl_event`

Este ejemplo muestra cómo enviar un evento `CTRL+BREAK` a un proceso hijo. En este caso, el proceso hijo muestra `I'm still alive` cada segundo, hasta que el usuario presiona `CTRL+BREAK`, lo que provoca la detención del proceso hijo.

```
<?php
// agregar el evento CTRL+BREAK al proceso hijo
sapi_windows_set_ctrl_handler('sapi_windows_generate_ctrl_event');

// crear un proceso hijo que muestra un mensaje cada segundo
$cmd = ['php', '-r', 'while (true) { echo "I\'m still alive\n"; sleep(1); }'];
$descspec = array(['pipe', 'r'], ['pipe', 'w'], ['pipe', 'w']);
$options = ['create_process_group' => true];
$proc = proc_open($cmd, $descspec, $pipes, null, null, $options);
while (true) {
    echo fgets($pipes[1]);
}
?>

   
```php

## Véase también

proc_open

sapi_windows_set_ctrl_handler
