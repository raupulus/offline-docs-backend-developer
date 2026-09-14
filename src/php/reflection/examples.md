---
title: Ejemplos
source_url: https://www.php.net/manual/es/reflection.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_revision: af4410a7e
order: 68920
---

## Ejemplos

Existen muchos ejemplos en la documentación de Reflection, por lo general dentro de la documentación de \_\_construct de cada clase.

Ejemplo de Reflection desde Shell (un terminal)

```php
$ php --rf strlen
$ php --rc finfo
$ php --re json
$ php --ri dom

  
```

Resultado del ejemplo anterior es similar a:

    Function [ <internal:Core> function strlen ] {

      - Parameters [1] {
        Parameter #0 [ <required> $str ]
      }
    }

    Class [ <internal:fileinfo> class finfo ] {

      - Constants [0] {
      }

      - Static properties [0] {
      }

      - Static methods [0] {
      }

      - Properties [0] {
      }

      - Methods [4] {
        Method [ <internal:fileinfo, ctor> public method finfo ] {

          - Parameters [2] {
            Parameter #0 [ <optional> $options ]
            Parameter #1 [ <optional> $arg ]
          }
        }

        Method [ <internal:fileinfo> public method set_flags ] {

          - Parameters [1] {
            Parameter #0 [ <required> $options ]
          }
        }

        Method [ <internal:fileinfo> public method file ] {

          - Parameters [3] {
            Parameter #0 [ <required> $filename ]
            Parameter #1 [ <optional> $options ]
            Parameter #2 [ <optional> $context ]
          }
        }

        Method [ <internal:fileinfo> public method buffer ] {

          - Parameters [3] {
            Parameter #0 [ <required> $string ]
            Parameter #1 [ <optional> $options ]
            Parameter #2 [ <optional> $context ]
          }
        }
      }
    }

    Extension [ <persistent> extension #23 json version 1.2.1 ] {

      - Constants [10] {
        Constant [ integer JSON_HEX_TAG ] { 1 }
        Constant [ integer JSON_HEX_AMP ] { 2 }
        Constant [ integer JSON_HEX_APOS ] { 4 }
        Constant [ integer JSON_HEX_QUOT ] { 8 }
        Constant [ integer JSON_FORCE_OBJECT ] { 16 }
        Constant [ integer JSON_ERROR_NONE ] { 0 }
        Constant [ integer JSON_ERROR_DEPTH ] { 1 }
        Constant [ integer JSON_ERROR_STATE_MISMATCH ] { 2 }
        Constant [ integer JSON_ERROR_CTRL_CHAR ] { 3 }
        Constant [ integer JSON_ERROR_SYNTAX ] { 4 }
      }

      - Functions {
        Function [ <internal:json> function json_encode ] {

          - Parameters [2] {
            Parameter #0 [ <required> $value ]
            Parameter #1 [ <optional> $options ]
          }
        }
        Function [ <internal:json> function json_decode ] {

          - Parameters [3] {
            Parameter #0 [ <required> $json ]
            Parameter #1 [ <optional> $assoc ]
            Parameter #2 [ <optional> $depth ]
          }
        }
        Function [ <internal:json> function json_last_error ] {

          - Parameters [0] {
          }
        }
      }
    }

    dom

    DOM/XML => enabled
    DOM/XML API Version => 20031129
    libxml Version => 2.7.3
    HTML Support => enabled
    XPath Support => enabled
    XPointer Support => enabled
    Schema Support => enabled
    RelaxNG Support => enabled
