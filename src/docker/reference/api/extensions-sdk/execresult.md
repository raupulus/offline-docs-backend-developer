---
title: 'Interface: ExecResult'
description: Docker extension API reference
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: reference/api/extensions-sdk/ExecResult.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: reference
order: 8190
---

**`Since`**

0.2.0

## Hierarchy

- [`RawExecResult`](rawexecresult.md)

  ↳ **`ExecResult`**

## Methods

### lines

▸ **lines**(): `string`[]

Split output lines.

#### Returns

`string`[]

The list of lines.

___

### parseJsonLines

▸ **parseJsonLines**(): `any`[]

Parse each output line as a JSON object.

#### Returns

`any`[]

The list of lines where each line is a JSON object.

___

### parseJsonObject

▸ **parseJsonObject**(): `any`

Parse a well-formed JSON output.

#### Returns

`any`

The JSON object.

## Properties

### cmd

• `Optional` `Readonly` **cmd**: `string`

#### Inherited from

[RawExecResult](rawexecresult.md).[cmd](rawexecresult.md#cmd)

___

### killed

• `Optional` `Readonly` **killed**: `boolean`

#### Inherited from

[RawExecResult](rawexecresult.md).[killed](rawexecresult.md#killed)

___

### signal

• `Optional` `Readonly` **signal**: `string`

#### Inherited from

[RawExecResult](rawexecresult.md).[signal](rawexecresult.md#signal)

___

### code

• `Optional` `Readonly` **code**: `number`

#### Inherited from

[RawExecResult](rawexecresult.md).[code](rawexecresult.md#code)

___

### stdout

• `Readonly` **stdout**: `string`

#### Inherited from

[RawExecResult](rawexecresult.md).[stdout](rawexecresult.md#stdout)

___

### stderr

• `Readonly` **stderr**: `string`

#### Inherited from

[RawExecResult](rawexecresult.md).[stderr](rawexecresult.md#stderr)
