# AoA FTBQuests Chapter Authoring Rules

These instructions apply specifically to SNBT chapter files in this directory.

## Mission

Author, audit, expand, or rebuild AoA chapter SNBT files to the project's hard standard.

This directory contains player-facing progression chapters. Chapter architecture, meaningful quest count, text quality, layout, and dependency flow all matter.

## Chapter Workflow

For every chapter touched:

1. Identify chapter type.
2. Identify chapter identity.
3. Identify macro-shape.
4. Audit meaningful quest count.
5. Remove filler first.
6. Expand only with meaningful content.
7. Fix dependencies and coordinates.
8. Verify icons/IDs before finalizing.

Never start by blindly adding quests.

Before any write, also read `docs/live/SNBT_WRITE_SAFETY.md` from the instance root. Its backup, atomic-write, validation, and in-game round-trip gates are mandatory for every live chapter SNBT edit.

## Mandatory Authoring Rules

### Meaningful Count Floor

Every main progression chapter in this directory must end at 30+ meaningful quests.

If under 30, deepen real chains, add real branches, add convergence, add mastery, add infrastructure/throughput/retrofit/environmental proofs, or fold in a nearby fitting system only if it truly strengthens chapter identity.

Do not inflate with junk.

### Description Length Rule

Description length is benchmarked against current live AoA descriptions, not against a fixed line count.

Before authoring or rewriting a quest description, read 5-10 nearby quest descriptions in the same chapter (or the closest equivalent existing chapter) inside `lang/en_us.snbt`. Match their length, voice, and density. The right length is whatever the chapter's already-shipping descriptions are doing.

Hard rules that still apply regardless of length:

- no prose on purely mechanical quests
- no narrative titles on ordinary mechanics (functional titles only)
- descriptions live in `lang/en_us.snbt`, never inline in the chapter SNBT

### Legal Checkmark Uses Only

Checkmarks are only legal for:

- chapter intro
- convergence gate
- boss-readiness acknowledgment

Never use checkmarks as placeholders.

### Functional Titles Only

Ordinary quest titles should name:

- the item
- the mechanic
- the proof
- the milestone

Do not write poetic or narrative titles on ordinary mechanics.

### Dependencies

Every non-entry quest must have a dependency.

Standard patterns:

- linear spine
- branch from one parent
- convergence from branch endpoints
- capstone from convergence or final endpoints

Never leave floating nodes.

### Layout / Visual Grammar

Choose a macro-shape before editing:

- linear spine
- two-branch convergence
- three-branch convergence
- hub and spoke
- vertical ladder
- catalog grid
- regional clustering

If 40+ quests, divide into regions, add deliberate spacing, use bridge nodes, and maintain a readable zoomed-out silhouette.

### Structural Quest Roles

Every quest must have a role:

- entry
- progression
- branch-proof
- convergence
- capstone
- optional mastery

If it has no role, delete it.

## Current Local Scope Rules

- no Small Ships progression lane by default
- no ordinary Alex's Mobs wildlife quests
- no Alex's Caves material/shard branch by default
- no vanilla/basic-tier filler
- no catalog spam unless the content is genuinely a catalog-worthy system
- no decorative chains
- no food busywork

## Chapter Expansion Methods That Are Allowed

Use only these methods to grow a thin chapter:

1. Deepen a real recipe/progression chain.
2. Add a meaningful parallel branch.
3. Add an optional mastery branch that is still meaningful.
4. Add convergence proofs.
5. Fold in a nearby compatible mod/system only if it strengthens chapter identity.
6. Add retrofit, throughput, infrastructure, or environmental mastery proofs.

## Expansion Methods That Are Forbidden

Never use these to reach 30:

- vanilla tutorials
- ordinary wildlife
- basic food chains
- decorative ladders
- generic ore collection
- prep clusters
- loot show-quests
- random machine catalogs
- generic "have one of everything"

## Required Outputs When Finishing A Pass

Always report:

- meaningful quest count before
- meaningful quest count after
- what was removed
- what was added
- IDs/mechanics deferred for verification
- any remaining structural weakness
- SNBT write-safety validation status, including backup path, no BOM, no null bytes, balanced braces/brackets, sane file size, dependency/ID checks, and whether in-game round-trip is still pending
