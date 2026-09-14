---
title: sapi_windows_set_ctrl_handler
description: Establece o elimina un gestor de eventos CTRL
source_url: https://www.php.net/manual/es/function.sapi-windows-set-ctrl-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/sapi-windows-set-ctrl-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: eee245cdb
order: 47210
---

sapi_windows_set_ctrl_handler

Establece o elimina un gestor de eventos CTRL

## Descripción

```php
sapi_windows_set_ctrl_handler(callable $handler, [bool $add]): bool
```php

Establece o elimina un gestor de eventos `CTRL`, que permite a los procesos CLI de Windows interceptar o ignorar los eventos `CTRL+C` y `CTRL+BREAK`. Tenga en cuenta que en entornos multihilo, esto solo es posible cuando se llama desde el hilo principal.

## Parámetros

`handler`  
Una función de retrollamada a establecer o eliminar. Si se establece, esta función será llamada cada vez que ocurra un evento <span class="keycombo"> +CTRL+ +C+ </span> o <span class="keycombo"> +CTRL+ +BREAK+ </span>. La función debe tener la siguiente firma:

```php
handler(int $event): void
```

`event`  
El evento CTRL que se ha recibido; ya sea `PHP_WINDOWS_EVENT_CTRL_C` o `PHP_WINDOWS_EVENT_CTRL_BREAK`.

Establecer un `null` `handler` hace que el proceso ignore los eventos <span class="keycombo"> +CTRL+ +C+ </span> o <span class="keycombo"> +CTRL+ +BREAK+ </span>.

`add`  
Si `true`, el gestor se establece. Si `false`, el gestor se elimina.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Uso básico de `sapi_windows_set_ctrl_handler`

Este ejemplo muestra cómo interceptar los eventos `CTRL`.

```php
<?php
function ctrl_handler(int $event)
{
    switch ($event) {
        case PHP_WINDOWS_EVENT_CTRL_C:
            echo "Se ha presionado CTRL+C\n";
            break;
        case PHP_WINDOWS_EVENT_CTRL_BREAK:
            echo "Se ha presionado CTRL+BREAK\n";
            break;
    }
}

sapi_windows_set_ctrl_handler('ctrl_handler');
while (true); // bucle infinito, para que el gestor pueda ser activado
?>

   
```

## Véase también

sapi_windows_generate_ctrl_event
