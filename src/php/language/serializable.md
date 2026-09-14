---
title: La interfaz Serializable
source_url: https://www.php.net/manual/es/class.serializable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/serializable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 4b06b2d5c
order: 3920
---

## Introducción

Interfaz que permite personalizar la serialización.

Las clases que implementan esta interfaz ya no soportan [\_\_sleep()](#object.sleep) y [\_\_wakeup()](#object.wakeup). El método de serialización es llamado cada vez que una instancia debe ser serializada. No llama al método \_\_destruct() y no tiene ningún efecto sobre el contenido de este método. Cuando los datos son serializados, la clase es conocida y el método unserialize() apropiado es llamado como constructor en lugar de llamar a \_\_construct(). Si es necesario llamar al constructor estándar, se puede hacer en el método.

> [!WARNING]
> A partir de PHP 8.1.0, una clase que implemente Serializable sin también implementar [\_\_serialize()](#object.serialize) y [\_\_unserialize()](#object.unserialize) generará una advertencia de deprecación.

## Sinopsis de la interfaz

Serializable

Métodos

## Ejemplos

Ejemplo simple

```php
<?php
class obj implements Serializable {
    private $data;
    public function __construct() {
        $this->data = "Mis datos privados";
    }
    public function serialize() {
        return serialize($this->data);
    }
    public function unserialize($data) {
        $this->data = unserialize($data);
    }
    public function getData() {
        return $this->data;
    }
}

$obj = new obj;
$ser = serialize($obj);

var_dump($ser);

$newobj = unserialize($ser);

var_dump($newobj->getData());
?>

    
```

Resultado del ejemplo anterior es similar a:

    Deprecated: obj implements the Serializable interface, which is deprecated. Implement __serialize() and __unserialize() instead (or in addition, if support for old PHP versions is necessary) in script on line 2
    string(38) "C:3:"obj":23:{s:19:"Mis datos privados";}"
    string(19) "Mis datos privados"
