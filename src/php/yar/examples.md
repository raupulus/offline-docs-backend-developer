---
title: Ejemplos
source_url: https://www.php.net/manual/es/yar.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yar/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yar
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 107470
---

## Ejemplos

Ejemplo de servidor de Yar

```php
<?php

/* Se asume que a esta página se puede acceder mediante http://example.com/operator.php */

class Operator {

    /**
     * Add two operands
     * @param integer
     * @return integer
     */
    public function add($a, $b) {
        return $this->_add($a, $b);
    }

    /**
     * Sub
     */
    public function sub($a, $b) {
        return $a - $b;
    }

    /**
     * Mul
     */
    public function mul($a, $b) {
        return $a * $b;
    }

    /**
     * Protected methods will not be exposed
     * @param integer
     * @return integer
     */
    protected function _add($a, $b) {
        return $a + $b;
    }
}

$servidor = new Yar_Server(new Operator());
$servidor->handle();
?>

  
```

Acceder al servidor desde el navegador (petición GET)

Resultado del ejemplo anterior es similar a:

<img src="en/reference/yar/image/yar.png" width="700" alt="Información del servidor de Yar" />

Ejemplo de cliente de Yar

```php
<?php
$cliente = new yar_client("http://example.com/operator.php");

/* llamar directamente */
var_dump($cliente->add(1, 2));

/* llamar mediante el método 'call' */
var_dump($cliente->call("add", array(3, 2)));

/* _add no puede ser llamado */
var_dump($cliente->_add(1, 2));
?>

  
```

Resultado del ejemplo anterior es similar a:

    int(3)
    int(5)
    PHP Fatal error:  Uncaught exception 'Yar_Server_Exception' with message 'call to api Operator::_add() failed' in *

Ejemplo de cliente concurrente de Yar

```php
<?php
function callback($ret, $callinfo) {
    echo $callinfo['method'] , " result: ", $ret , "\n";
}

/* registrar las llamadas asíncronas a servicios remotos */
Yar_Concurrent_Client::call("http://example.com/operator.php", "add", array(1, 2), "callback");
Yar_Concurrent_Client::call("http://example.com/operator.php", "sub", array(2, 1), "callback");
Yar_Concurrent_Client::call("http://example.com/operator.php", "mul", array(2, 2), "callback");

/* enviar todas las peticiones y esperar una respuesta */
Yar_Concurrent_Client::loop();
?>

  
```

Resultado del ejemplo anterior es similar a:

    mul result: 4
    sub result: 1
    add result: 3
