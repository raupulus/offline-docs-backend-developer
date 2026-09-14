---
title: Ejemplos
source_url: https://www.php.net/manual/es/dom.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: d8e77acef
order: 14370
---

## Ejemplos

Muchos ejemplos en esta referencia requieren un fichero XML. Utilizaremos `book.xml` que contiene lo siguiente:

book.xml

```php
<!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.1.2//EN"
 "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd" [
]>
<book id="listing">
 <title>Mis listas</title>
 <chapter id="books">
  <title>Mis libros</title>
  <para>
   <informaltable>
    <tgroup cols="4">
     <thead>
      <row>
       <entry>Título</entry>
       <entry>Autor</entry>
       <entry>Idioma</entry>
       <entry>ISBN</entry>
      </row>
     </thead>
     <tbody>
      <row>
       <entry>The Grapes of Wrath</entry>
       <entry>John Steinbeck</entry>
       <entry>en</entry>
       <entry>0140186409</entry>
      </row>
      <row>
       <entry>The Pearl</entry>
       <entry>John Steinbeck</entry>
       <entry>en</entry>
       <entry>014017737X</entry>
      </row>
      <row>
       <entry>Samarcande</entry>
       <entry>Amine Maalouf</entry>
       <entry>fr</entry>
       <entry>2253051209</entry>
      </row>
      <!-- TODO: Tengo muchos libros pendientes de añadir.. -->
     </tbody>
    </tgroup>
   </informaltable>
  </para>
 </chapter>
</book>

   
```
