---
title: 'Interface: Dialog'
description: Docker extension API reference
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: reference/api/extensions-sdk/Dialog.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: reference
order: 8120
---

Allows opening native dialog boxes.

**`Since`**

0.2.3

## Methods

### showOpenDialog

▸ **showOpenDialog**(`dialogProperties`): `Promise`<[`OpenDialogResult`](opendialogresult.md)\>

Display a native open dialog. Lets you select a file or a folder.

```typescript
ddClient.desktopUI.dialog.showOpenDialog({properties: ['openFile']});
```

#### Parameters

| Name | Type | Description |
| :------ | :------ | :------ |
| `dialogProperties` | `any` | Properties to specify the open dialog behaviour, see https://www.electronjs.org/docs/latest/api/dialog#dialogshowopendialogbrowserwindow-options. |

#### Returns

`Promise`<[`OpenDialogResult`](opendialogresult.md)\>
