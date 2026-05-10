# GitHub Workflow

This repository is the source tracker for Ascension of Ages. It should stay useful as a history, release log, and collaboration surface without becoming a full CurseForge instance mirror.

## Branches

- `main`: stable source state suitable for public notes or pack export.
- `work`: active development if you want a separate branch for experiments.
- `release/<version>`: optional release-prep branch for larger updates.

## Day-To-Day Updates

1. Make pack changes in the CurseForge instance.
2. Check what changed with `git status`.
3. Review risky changes before staging, especially quest files, KubeJS, and progression gates.
4. Stage intentional files with `git add <path>`.
5. Commit with a short message, for example `git commit -m "Tune early Create progression"`.
6. Push with `git push`.

## Player-Facing Release Notes

Use `CHANGELOG.md` for changes players care about:

- Progression changes
- Quest additions or repairs
- Gating changes
- Major config changes
- Known compatibility issues
- World-impacting changes

## GitHub Releases

When you export a pack build, create a GitHub release with:

- A version tag such as `v0.1.0-alpha`
- A concise changelog copied from `CHANGELOG.md`
- Any exported pack artifact you explicitly want attached

Do not commit generated export zips into the repository. Attach them to releases instead.

## Mod Jars

Do not commit `mods/` or jar files. Use CurseForge exports, manifests, or documented mod lists for distribution. This avoids repository bloat and keeps mod redistribution/licensing cleaner.
