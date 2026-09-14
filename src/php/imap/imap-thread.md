---
title: imap_thread
description: Devuelve el árbol de mensajes organizados por hilo
source_url: https://www.php.net/manual/es/function.imap-thread.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-thread.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38590
---

imap_thread

Devuelve el árbol de mensajes organizados por hilo

## Descripción

```php
imap_thread(IMAP\Connection $imap, [int $flags]): array
```php

Devuelve el árbol de mensajes organizados por hilo.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`flags`  

## Valores devueltos

`imap_thread` devuelve un array asociativo que contiene un árbol de mensajes organizados por hilo por `REFERENCES` o `false` en caso de error.

Cada mensaje en el buzón actual será representado por entradas en forma de árbol en el array resultante:

- `$thread["XX.num"]` - número del mensaje actual

- `$thread["XX.next"]`

- `$thread["XX.branch"]`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_thread`

```
<?php

// Aquí, se muestran los hilos de un newsgroup en HTML

$nntp = imap_open('{news.example.com:119/nntp}some.newsgroup', '', '');
$threads = imap_thread($nntp);

foreach ($threads as $key => $val) {
  $tree = explode('.', $key);
  if ($tree[1] == 'num') {
    $header = imap_headerinfo($nntp, $val);
    echo "<ul>\n\t<li>" . $header->fromaddress . "\n";
  } elseif ($tree[1] == 'branch') {
    echo "\t</li>\n</ul>\n";
  }
}

imap_close($nntp);

?>

    
```php
