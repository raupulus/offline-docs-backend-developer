---
title: ob_gzhandler
description: Función de recuperación para la compresión automática de pastillas
source_url: https://www.php.net/manual/es/function.ob-gzhandler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/ob-gzhandler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: true
translation_revision: 0fb27c54e
order: 108970
---

ob_gzhandler

Función de recuperación para la compresión automática de pastillas

## Descripción

```php
ob_gzhandler(string $data, int $flags): string
```php

`ob_gzhandler` está destinada a ser usada como función de devolución de llamada por `ob_start` para facilitar el envío de datos comprimidos a los navegadores que soportan páginas comprimidas. Antes de que `ob_gzhandler` envíe los datos comprimidos, determina los tipos de codificación que son soportados por el navegador ("gzip", "deflate" o ninguno) y devuelve el contenido de los búferes de manera apropiada. Todos los navegadores son manejados, ya que es responsabilidad de los navegadores enviar un encabezado indicando los tipos de páginas soportadas. Si el navegador no soporta páginas comprimidas, esta función devolverá `false`.

## Parámetros

`data`  

`flags`  

## Valores devueltos

## Ejemplos

Ejemplo con `ob_gzhandler`

```
<?php

ob_start("ob_gzhandler");

?>
<html>
<body>
<p>Esto debería ser una página comprimida.</p>
</body>
</html>

    
```php

## Notas

> [!NOTE]
> `ob_gzhandler` requiere la extensión [zlib](#ref.zlib).

> [!NOTE]
> No puede usar simultáneamente `ob_gzhandler` y [zlib.output_compression](#ini.zlib.output-compression). Además, tenga en cuenta que [zlib.output_compression](#ini.zlib.output-compression) es preferible a `ob_gzhandler`.

## Véase también

`ob_start`, `ob_end_flush`
