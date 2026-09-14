---
title: MessageFormatter::formatMessage
description: Formatea rápidamente un mensaje
source_url: https://www.php.net/manual/es/messageformatter.formatmessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/format-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: dacb2d9a9
order: 42040
---

MessageFormatter::formatMessage

msgfmt_format_message

Formatea rápidamente un mensaje

## Descripción

Estilo orientado a objetos

```php
public static MessageFormatter::formatMessage(string $locale, string $pattern, array $values): string
```php

Estilo procedimental

```php
msgfmt_format_message(string $locale, string $pattern, array $values): string
```

Función de formato rápido que formatea una cadena sin necesidad de crear explícitamente un objeto de formato. Utilice esta función cuando la operación de formato se realiza una sola vez y no es necesario conservar parámetros o estados, o cuando se desea personalizar la salida proporcionando directamente un contexto adicional a ICU.

## Parámetros

`locale`  
La configuración local a utilizar para el formato

`pattern`  
El `string` en el cual se deben insertar los datos. El patrón utiliza una sintaxis que acepta comillas; Ver [Quoting/Escaping](https://unicode-org.github.io/icu/userguide/format_parse/messages/#quotingescaping) para más detalles.

`values`  
El `array` de valores a insertar en la cadena de formato.

## Valores devueltos

La cadena formateada, o bien `false` si ocurre un error.

## Ejemplos

Ejemplo con `msgfmt_format_message`, estilo procedimental

```php
<?php
echo msgfmt_format_message("en_US", "{0,number,integer} monkeys on {1,number,integer} trees make {2,number} monkeys per tree\n", array(4560, 123, 4560/123));
echo msgfmt_format_message("de", "{0,number,integer} Affen auf {1,number,integer} Bäumen sind {2,number} Affen pro Baum\n", array(4560, 123, 4560/123));
echo msgfmt_format_message("en", 'You finished {place, selectordinal, one {#st} two {#nd} few {#rd} other {#th}}!', ['place' => 3]), "\n";
echo msgfmt_format_message("en",
        "There {apple, plural,
            =0 {are no apples}
            =1 {is one apple...}
            other {are # apples!}
        }",
    ['apple' => 0]
), "\n";

   
```

Ejemplo con `msgfmt_format_message`, estilo procedimental

```php
<?php
echo MessageFormatter::formatMessage("en_US", "{0,number,integer} monkeys on {1,number,integer} trees make {2,number} monkeys per tree\n", array(4560, 123, 4560/123));
echo MessageFormatter::formatMessage("de", "{0,number,integer} Affen auf {1,number,integer} Bäumen sind {2,number} Affen pro Baum\n", array(4560, 123, 4560/123));
echo MessageFormatter::formatMessage("en", 'You finished {place, selectordinal, one {#st} two {#nd} few {#rd} other {#th}}!', ['place' => 3]), "\n";
echo MessageFormatter::formatMessage("en",
        "There {apple, plural,
            =0 {are no apples}
            =1 {is one apple...}
            other {are # apples!}
        }",
    ['apple' => 0]
), "\n";

   
```

El ejemplo anterior mostrará:

    4,560 monkeys on 123 trees make 37.073 monkeys per tree
    4.560 Affen auf 123 Bäumen sind 37,073 Affen pro Baum
    You finished 3rd!
    There are no apples

Solicitar a ICU que formatee la moneda con el símbolo monetario común y con el símbolo monetario corto.

Requiere ICU ≥ 67.

```php
<?php
echo msgfmt_format_message("cs_CZ", "{0, number, :: currency/CAD}", array(123.45));
echo msgfmt_format_message("cs_CZ", "{0, number, :: currency/CAD unit-width-narrow}", array(123.45));

   
```

El ejemplo anterior mostrará:

    123,45 CA$
    123,45 $

## Véase también

`msgfmt_create`, `msgfmt_parse`, `msgfmt_get_error_code`, `msgfmt_get_error_message`
