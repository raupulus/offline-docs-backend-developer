---
title: ReflectionClass::__toString
description: Crea una representación textual del objeto
source_url: https://www.php.net/manual/es/reflectionclass.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ec2fe9a59
order: 69680
---

ReflectionClass::\_\_toString

Crea una representación textual del objeto

## Descripción

```php
public ReflectionClass::__toString(): string
```php

Crea una representación textual del objeto.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una representación textual de la instancia actual de `ReflectionClass`

## Ejemplos

Ejemplo para ReflectionClass::\_\_toString

```
<?php
$reflectionClass = new ReflectionClass('Exception');
echo $reflectionClass->__toString();
?>

    
```php

El ejemplo anterior mostrará:

    Class [ <internal:Core> class Exception ] {

      - Constants [0] {
      }

      - Static properties [0] {
      }

      - Static methods [0] {
      }

      - Properties [7] {
        Property [ <default> protected $message ]
        Property [ <default> private $string ]
        Property [ <default> protected $code ]
        Property [ <default> protected $file ]
        Property [ <default> protected $line ]
        Property [ <default> private $trace ]
        Property [ <default> private $previous ]
      }

      - Methods [10] {
        Method [ <internal:Core> final private method __clone ] {
        }

        Method [ <internal:Core, ctor> public method __construct ] {

          - Parameters [3] {
            Parameter #0 [ <optional> $message ]
            Parameter #1 [ <optional> $code ]
            Parameter #2 [ <optional> $previous ]
          }
        }

        Method [ <internal:Core> final public method getMessage ] {
        }

        Method [ <internal:Core> final public method getCode ] {
        }

        Method [ <internal:Core> final public method getFile ] {
        }

        Method [ <internal:Core> final public method getLine ] {
        }

        Method [ <internal:Core> final public method getTrace ] {
        }

        Method [ <internal:Core> final public method getPrevious ] {
        }

        Method [ <internal:Core> final public method getTraceAsString ] {
        }

        Method [ <internal:Core> public method __toString ] {
        }
      }
    }

## Véase también

ReflectionClass::export, [\_\_toString()](#object.tostring)
