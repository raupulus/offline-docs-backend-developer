---
title: function_exists
description: Indica si una función está definida
source_url: https://www.php.net/manual/es/function.function-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/funchand/functions/function-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: funchand
translation_status: ready
translation_reviewed: false
translation_revision: c44475e1f
order: 24800
---

function_exists

Indica si una función está definida

## Descripción

```php
function_exists(string $function): bool
```php

Verifica la lista de funciones definidas por el usuario así como las internas a PHP para encontrar `function`.

## Parámetros

`function`  
El nombre de la función, en forma de `string`.

## Valores devueltos

Devuelve `true` si la función `function` existe y es una función, `false` en caso contrario.

> [!NOTE]
> Tenga en cuenta que `function_exists` devolverá `false` para las sentencias como `include_once` y `echo`.

## Ejemplos

Ejemplo con `function_exists`

```
<?php
if (function_exists('imap_open')) {
    echo "Las funciones IMAP están disponibles.<br />\n";
} else {
    echo "Las funciones IMAP no están disponibles.<br />\n";
}
?>

    
```php

## Notas

> [!NOTE]
> Un nombre de función puede existir incluso si la función misma no es utilizable debido a una configuración o a una opción de compilación (como con las funciones [image](#ref.image) por ejemplo).

## Véase también

`method_exists`, `is_callable`, `get_defined_functions`, `class_exists`, `extension_loaded`
