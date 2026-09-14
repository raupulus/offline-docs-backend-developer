---
title: ReflectionClass::export
description: Exporta una clase
source_url: https://www.php.net/manual/es/reflectionclass.export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 69060
---

ReflectionClass::export

Exporta una clase

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
public static ReflectionClass::export(mixed $argumento, [bool $return]): string
```php

Exporta una clase reflejada.

## Parámetros

`argumento`  
La reflexión a exportar.

`return`  
Definirlo a `true` retornará la exportación en lugar de emitirla. Definirlo a `false` (por defecto) hará lo contrario.

## Valores devueltos

Si el parámetro `return` se establece a `true`, entonces la exportación se devuelve como un `string`, de lo contrario se devuelve `null`.

## Ejemplos

Uso básico de ReflectionClass::export

```
<?php
class Apple {
    public $var1;
    public $var2 = 'Orange';

    public function type() {
        return 'Apple';
    }
}
ReflectionClass::export('Apple');
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Class [ <user> class Apple ] {
      @@ php shell code 1-8

      - Constants [0] {
      }

      - Static properties [0] {
      }

      - Static methods [0] {
      }

      - Properties [2] {
        Property [ <default> public $var1 ]
        Property [ <default> public $var2 ]
      }

      - Methods [1] {
        Method [ <user> public method type ] {
          @@ php shell code 5 - 7
        }
      }
    }

## Véase también

ReflectionClass::getName, ReflectionClass::\_\_toString
