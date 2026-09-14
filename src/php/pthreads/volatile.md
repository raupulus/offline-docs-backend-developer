---
title: La clase Volatile
source_url: https://www.php.net/manual/es/class.volatile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pthreads/volatile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pthreads
translation_status: ready
translation_reviewed: true
translation_revision: bf92d8bd8
order: 66920
---

## Introducción

La clase `Volatile` es nueva en pthreads v3. Su introducción es una consecuencia de las nuevas semánticas de inmutabilidad de los miembros `Threaded` de las clases `Threaded`. La clase `Volatile` permite la mutabilidad de sus miembros `Threaded`, y es igualmente utilizada para almacenar arrays PHP en contextos `Threaded`.

## Sinopsis de la clase

Volatile

Volatile

extends

Threaded

Collectable

Traversable

Métodos heredados

## Ejemplos

Nuevas semánticas de inmutabilidad de Threaded

```php
<?php

class Task extends Threaded
{
    public function __construct()
    {
        $this->data = new Threaded();

        // intenta reemplazar una propiedad Threaded de una clase Threaded (inválido)
        $this->data = new stdClass();
    }
}

var_dump((new Task())->data);

    
```

Resultado del ejemplo anterior es similar a:

    RuntimeException: Threaded members previously set to Threaded objects are immutable, cannot overwrite data in %s:%d

Caso de uso de Volatile

```php
<?php

class Task extends Volatile
{
    public function __construct()
    {
        $this->data = new Threaded();

        // intenta reemplazar una propiedad Threaded de una clase Volatile (válido)
        $this->data = new stdClass();
    }
}

var_dump((new Task())->data);

    
```

Resultado del ejemplo anterior es similar a:

    object(stdClass)#3 (0) {
    }
