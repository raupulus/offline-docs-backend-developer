---
title: Only allow pnpm
source_repo: pnpm/pnpm.io
source_ref: main
source_commit: 92a41bf66
source_path: only-allow-pnpm.md
technology: pnpm
version: main
license: MIT
retrieved_at: '2026-08-02'
order: 1060
---

When you use pnpm on a project, you don't want others to accidentally run
`npm install` or `yarn`. To prevent devs from using other package managers,
you can add the following `preinstall` script to your `package.json`:

```json
{
	"scripts": {
		"preinstall": "npx only-allow pnpm"
	}
}
```

Now, whenever someone runs `npm install` or `yarn`, they'll get an
error instead and installation will not proceed.

If you use npm v7, use `npx -y` instead.
