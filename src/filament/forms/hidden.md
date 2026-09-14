---
title: Hidden
source_repo: filamentphp/filament
source_ref: 4.x
source_commit: 38eb676bc
source_path: forms/docs/21-hidden.md
technology: filament
version: 4.x
license: MIT
retrieved_at: '2026-08-02'
section: forms
order: 21
---

## Introduction

The hidden component allows you to create a hidden field in your form that holds a value.

```php
use Filament\Forms\Components\Hidden;

Hidden::make('token')
```

Please be aware that the value of this field is still editable by the user if they decide to use the browser's developer tools. You should not use this component to store sensitive or read-only information.
