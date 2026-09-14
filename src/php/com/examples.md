---
title: Ejemplos
source_url: https://www.php.net/manual/es/com.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 28f122648
order: 7670
---

## Ejemplos

## For Each

Se puede utilizar la estructura de control [`foreach`](#control-structures.foreach) de PHP para iterar a través del contenido de un IEnumVariant COM/OLE estándar. Esto significa que se puede utilizar [`foreach`](#control-structures.foreach) en los lugares donde se habría podido utilizar `For Each` en código VB/ASP.

For Each en ASP

```php
<%
Set domainObject = GetObject("WinNT://Domain")
For Each obj in domainObject
  Response.Write obj.Name & "<br />"
Next
%>

    
```

Foreach en PHP

```php
<?php
$domainObject = new COM("WinNT://Domain");
foreach ($domainObject as $obj) {
   echo $obj->Name . "<br />";
}
?>

    
```

## Arrays y propiedades a la manera de arrays de COM

Varios objetos COM exponen sus propiedades como arrays, o utilizando una ruta de acceso a la manera de arrays.

Se puede:

- Acceder a arrays multidimensionales o a propiedades COM que requieren múltiples argumentos como si se accediera a un array. También se pueden escribir estas propiedades utilizando esta técnica.

- Iterar sobre los SafeArrays ("verdaderos" arrays) utilizando la estructura de control [`foreach`](#control-structures.foreach). Esto funciona porque un SafeArrays contiene información sobre su tamaño. Si una propiedad a la manera de arrays implementa IEnumVariant, entonces también se puede utilizar [`foreach`](#control-structures.foreach) para esta propiedad; consulte [For Each](#com.examples.foreach) para más información al respecto.
