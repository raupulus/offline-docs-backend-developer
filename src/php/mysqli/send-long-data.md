---
title: mysqli_stmt::send_long_data
description: Envía datos MySQL por paquetes
source_url: https://www.php.net/manual/es/mysqli-stmt.send-long-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/send-long-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55970
---

mysqli_stmt::send_long_data

mysqli_stmt_send_long_data

Envía datos MySQL por paquetes

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::send_long_data(int $param_num, string $data): bool
```php

Estilo procedimental

```php
mysqli_stmt_send_long_data(mysqli_stmt $statement, int $param_num, string $data): bool
```

Envía los datos al servidor por paquetes, si el tamaño de los datos excede el límite de `max_allowed_packet`. Esta función puede ser llamada varias veces para enviar los datos de texto o binarios de campos como BLOB o TEXT.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

`param_num`  
Indica qué parámetro debe asociarse con qué datos. Los parámetros están numerados a partir de 0.

`data`  
Un `string` que contiene los datos a enviar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Estilo orientado a objetos

```php
<?php
$stmt = $mysqli->prepare("INSERT INTO messages (message) VALUES (?)");
$null = NULL;
$stmt->bind_param("b", $null);
$fp = fopen("messages.txt", "r");
while (!feof($fp)) {
    $stmt->send_long_data(0, fread($fp, 8192));
}
fclose($fp);
$stmt->execute();
?>

  
```

## Véase también

`mysqli_prepare`, `mysqli_stmt_bind_param`
