---
title: readline_callback_handler_install
description: Inicializa la interfaz y el terminal de devolución de llamada de readline,
  muestra el prompt y retorna inmediatamente
source_url: https://www.php.net/manual/es/function.readline-callback-handler-install.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline-callback-handler-install.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: be246a268
order: 68720
---

readline_callback_handler_install

Inicializa la interfaz y el terminal de devolución de llamada de readline, muestra el prompt y retorna inmediatamente

## Descripción

```php
readline_callback_handler_install(string $prompt, callable $callback): true
```php

Define una interfaz de devolución de llamada para readline, muestra el `prompt` y retorna inmediatamente. Llamar a esta función dos veces sin borrar previamente la interfaz de devolución de llamada anterior borrará automáticamente y correctamente la interfaz antigua.

La funcionalidad de devolución de llamada es muy útil cuando se combina con la función `stream_select` que permite la interconexión IO / entrada de usuario, a diferencia de `readline`.

## Parámetros

`prompt`  
El mensaje de prompt.

`callback`  
La función `callback` toma un argumento: la entrada de usuario retornada.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.5.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo de interfaz de devolución de llamada de Readline

```
<?php
function rl_callback($ret)
{
    global $c, $prompting;

    echo "You entered: $ret\n";
    $c++;

    if ($c > 10) {
        $prompting = false;
        readline_callback_handler_remove();
    } else {
        readline_callback_handler_install("[$c] Entrar algo: ", 'rl_callback');
    }
}

$c = 1;
$prompting = true;

readline_callback_handler_install("[$c] Entrar algo: ", 'rl_callback');

while ($prompting) {
    $w = NULL;
    $e = NULL;
    $n = stream_select($r = array(STDIN), $w, $e, null);
    if ($n && in_array(STDIN, $r)) {
        // lee un carácter, llamará a la función de devolución de llamada cuando se ingrese una nueva línea
        readline_callback_read_char();
    }
}

echo "El prompt está desactivado. Todo ha sido realizado.\n";
?>

   
```php

## Véase también

readline_callback_handler_remove

readline_callback_read_char

stream_select
