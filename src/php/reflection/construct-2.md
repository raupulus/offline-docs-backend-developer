---
title: ReflectionClass::__construct
description: Construye una ReflectionClass
source_url: https://www.php.net/manual/es/reflectionclass.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: d52f1e690
order: 69050
---

ReflectionClass::\_\_construct

Construye una ReflectionClass

## Descripción

```php
public ReflectionClass::__construct(object $objectOrClass)
```php

Construye un nuevo objeto `ReflectionClass`.

## Parámetros

`objectOrClass`  
Puede ser un `string` que contenga el nombre de la clase a reflejar, o un `object`.

## Errores/Excepciones

Se lanza una `ReflectionException` si la clase a reflejar no existe.

## Ejemplos

Uso simple de ReflectionClass

```
<?php
$reflection = new ReflectionClass('Exception');
echo $reflection;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Class [ <internal:Core> class Exception implements Stringable, Throwable ] {

      - Constants [0] {
      }

      - Static properties [0] {
      }

      - Static methods [0] {
      }

      - Properties [7] {
        Property [ protected $message = '' ]
        Property [ private string $string = '' ]
        Property [ protected $code = 0 ]
        Property [ protected string $file = '' ]
        Property [ protected int $line = 0 ]
        Property [ private array $trace = [] ]
        Property [ private ?Throwable $previous = NULL ]
      }

      - Methods [11] {
        Method [ <internal:Core> private method __clone ] {

          - Parameters [0] {
          }
          - Return [ void ]
        }

        Method [ <internal:Core, ctor> public method __construct ] {

          - Parameters [3] {
            Parameter #0 [ <optional> string $message = "" ]
            Parameter #1 [ <optional> int $code = 0 ]
            Parameter #2 [ <optional> ?Throwable $previous = null ]
          }
        }

        Method [ <internal:Core> public method __wakeup ] {

          - Parameters [0] {
          }
          - Tentative return [ void ]
        }

        Method [ <internal:Core, prototype Throwable> final public method getMessage ] {

          - Parameters [0] {
          }
          - Return [ string ]
        }

        Method [ <internal:Core, prototype Throwable> final public method getCode ] {

          - Parameters [0] {
          }
        }

        Method [ <internal:Core, prototype Throwable> final public method getFile ] {

          - Parameters [0] {
          }
          - Return [ string ]
        }

        Method [ <internal:Core, prototype Throwable> final public method getLine ] {

          - Parameters [0] {
          }
          - Return [ int ]
        }

        Method [ <internal:Core, prototype Throwable> final public method getTrace ] {

          - Parameters [0] {
          }
          - Return [ array ]
        }

        Method [ <internal:Core, prototype Throwable> final public method getPrevious ] {

          - Parameters [0] {
          }
          - Return [ ?Throwable ]
        }

        Method [ <internal:Core, prototype Throwable> final public method getTraceAsString ] {

          - Parameters [0] {
          }
          - Return [ string ]
        }

        Method [ <internal:Core, prototype Stringable> public method __toString ] {

          - Parameters [0] {
          }
          - Return [ string ]
        }
      }
    }

## Véase también

ReflectionObject::\_\_construct, [Los constructores](#language.oop5.decon.constructor)
