---
title: EventBuffer::search
description: Busca en el búfer una ocurrencia de un string
source_url: https://www.php.net/manual/es/eventbuffer.search.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/event/eventbuffer/search.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: event
translation_status: ready
translation_reviewed: false
translation_revision: 23ea6be07
order: 19310
---

EventBuffer::search

Busca en el búfer una ocurrencia de un string

## Descripción

```php
public EventBuffer::search(string $what, [int $start], [int $end]): mixed
```php

Busca en el búfer una ocurrencia del string `what`. El método devuelve la posición numérica del string buscado, o `false` si el string no ha podido ser encontrado.

Si el argumento `start` es proporcionado, será la posición desde la cual la búsqueda debe comenzar; de lo contrario, la búsqueda se realizará desde el inicio del string. Si el argumento `end` es proporcionado, la búsqueda se realizará entre las posiciones de inicio y fin del búfer.

## Parámetros

`what`  
String a buscar.

`start`  
Posición de inicio de la búsqueda.

`end`  
Posición de fin de la búsqueda.

## Valores devueltos

Devuelve la posición numérica de la primera ocurrencia del string en el búfer, o `false` si el string no ha sido encontrado.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Ejemplo con `EventBuffer::search`

```
<?php
// Cuenta el número de ocurrencias del string 'str' en el búfer 'buf'
function count_instances($buf, $str) {
    $total = 0;
    $p     = 0;
    $i     = 0;

    while (1) {
        $p = $buf->search($str, $p);
        if ($p === FALSE) {
            break;
        }
        ++$total;
        ++$p;
    }

    return $total;
}

$buf = new EventBuffer();
$buf->add("Some string within a string inside another string");
var_dump(count_instances($buf, "str"));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    int(3)

## Véase también

EventBuffer::searchEol
