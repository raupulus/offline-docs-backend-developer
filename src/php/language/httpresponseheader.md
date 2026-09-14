---
title: $http_response_header
description: Cabeceras de respuesta HTTP
source_url: https://www.php.net/manual/es/reserved.variables.httpresponseheader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/httpresponseheader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: fcf847c11
order: 4180
---

\$http_response_header

Cabeceras de respuesta HTTP

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.5.0. Depender de esta característica está altamente desaconsejado.

Utilice `http_get_last_response_headers` en su lugar.

## Descripción

El `$http_response_header` `array` es similar a la función `get_headers`. Al utilizar el [gestor HTTP](#wrappers.http), `$http_response_header` será rellenado con las cabeceras de respuesta HTTP. `$http_response_header` será creado con un [ ámbito local](#language.variables.scope).

## Ejemplos

Ejemplo con `$http_response_header`

```php
<?php
function get_contents() {
  file_get_contents("http://example.com");
  var_dump($http_response_header); // La variable es rellenada en el ámbito local
}
get_contents();
var_dump($http_response_header); // Una llamada a get_contents() no rellena la variable fuera del ámbito de la función
?>

    
```

Resultado del ejemplo anterior es similar a:

    array(9) {
      [0]=>
      string(15) "HTTP/1.1 200 OK"
      [1]=>
      string(35) "Date: Sat, 12 Apr 2008 17:30:38 GMT"
      [2]=>
      string(29) "Server: Apache/2.2.3 (CentOS)"
      [3]=>
      string(44) "Last-Modified: Tue, 15 Nov 2005 13:24:10 GMT"
      [4]=>
      string(27) "ETag: "280100-1b6-80bfd280""
      [5]=>
      string(20) "Accept-Ranges: bytes"
      [6]=>
      string(19) "Content-Length: 438"
      [7]=>
      string(17) "Connection: close"
      [8]=>
      string(38) "Content-Type: text/html; charset=UTF-8"
    }

    Warning: Undefined variable $http_response_header
    NULL

## Véase también

http_get_last_response_headers

http_clear_last_response_headers
