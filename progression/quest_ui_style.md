# Quest UI Style Guide

## Purpose

This file defines how the AoA questbook should look, read, and communicate.

The goal is to keep a very dense questbook readable.

## General Visual Rules

- Each age is a `chapter_group`.
- Future age groups remain hidden until unlocked.
- The map inside a chapter must read left-to-right or top-to-bottom with obvious flow.
- Decorative images are allowed, but they must not obscure routing.
- Mainline routes should be visually distinct from side branches.

## Group Titles

Use these display names:

- `Stone Age`
- `Mechanical Age`
- `Expedition Age`
- `Automation Age`
- `Industrial Age`
- `Nuclear Age`
- `Space Age`
- `Ascension`
- `Annexes`

Avoid renaming these casually. They are structural labels, not flavor one-offs.

## Chapter Naming Rules

Chapter titles should be short, specific, and practical.

Good:

- `Water, Weather, and Wounds`
- `Create Foundations`
- `Dragonfall and the New Scale`
- `Factory Power Grids`

Avoid:

- vague titles
- meme titles
- filler tutorial labels like `Part 1`
- broad labels that hide the actual purpose of the chapter

## Quest Title Rules

Quest titles should be:

- short
- readable on the map
- tied to a concrete task
- framed around capability, not generic completion

Good:

- `Boil Before Travel`
- `A Mill, Not a Factory`
- `Sort the Workshop`
- `Field Rotation`

Avoid:

- `Do the Thing`
- `Progress`
- `Step 3`

## Subtitle Rules

Subtitles explain intent.

Required qualities:

- tell the player why the task matters
- reinforce age identity
- remain concise enough to scan in a single line

The subtitle should usually answer one of these:

- why this matters now
- what problem this solves
- what capability this unlocks

## Description Rules

Descriptions are optional and should usually be omitted.

Default rule:

- no body description

Only add description text when the task would otherwise be unclear from:

- the title
- the subtitle
- the dependency path
- the required item or machine

If description text is needed, use:

- one short line
- practical language
- direct explanation of the action or reason

Avoid:

- walls of lore text
- bloated explanation for simple tasks
- flavor that hides what the player is expected to do
- paragraph-style tutorial writing

## Node Shape Conventions

Use consistent shapes across the book:

- `hexagon`
  - threshold or gate quests
- `square`
  - foundation and assembly quests
- `circle`
  - usage and relief quests
- `gear`
  - machine, automation, or workshop hubs
- `diamond`
  - boss, validator, or special challenge quests

Do not change the meaning of shapes between ages.

## Routing Conventions

Mainline:

- place it centrally and keep dependency lines obvious
- use a clean spine with side branches returning to a visible milestone

Side branches:

- place them above or below the mainline spine
- avoid spaghetti dependency lines

Boss or validator branches:

- place near the end of the age
- make it visually obvious they are challenge or proof content

Connector chapters:

- use a visible threshold quest near the end of the source age
- the first quest of the new age should visually acknowledge the transition

## Image Usage

Allowed image use:

- age banners
- mod logos
- boss silhouettes
- section dividers

Rules:

- images must support orientation
- do not use large decorative art where it makes routing harder
- keep visual density below the quest-node density

## Icon Rules

Chapter icons should be:

- representative of the chapter's central system
- stable across revisions
- immediately readable at a glance

Examples:

- campfire or leather water bottle for early survival
- cogwheel or millstone for Create chapters
- spellbook or source gem for Ars Nouveau
- turbine, cable, or machine block for industrial chapters

## Visibility Rules

- hide future age groups until unlocked
- inside unlocked age groups, hide quests until dependency completion for tightly authored chains
- use visible locked quests sparingly and only when they help orientation
- annex chapters may be visible later than their connector if early visibility would create confusion

## Reward Presentation

Rewards should look supportive, not jackpot-like.

Use:

- small stacks
- utility items
- starter components
- notes and routing aids

Avoid:

- oversized reward piles
- random loot as the main identity of a quest
- rewards that visually imply the questbook is meant to replace progression

## Tone Rules

Tone should match the current AoA scaffold:

- practical
- atmospheric
- survival-aware
- explicit about stakes and utility when text is needed

The book should sound like it understands the pack's hostility and expects the player to prepare intelligently, but it should not narrate every step at length.

## Annex Presentation

Annexes should feel intentionally separated from the mainline.

Rules:

- use explicit prologue chapters to explain why the annex exists
- explain when the player should engage with the annex
- link back to the main progression at the end of connector chapters

## Large-Scale Readability Rules

Because the book is targeting `2200+` authored quests:

- every chapter needs a clear theme
- every branch needs a visible return point
- repeated quest families must still feel purposeful
- count alone is not sufficient; readability is mandatory

## Default Implementation Preferences

- keep chapter maps compact but not cramped
- keep descriptions absent by default
- when text is needed, keep it to one short line
- prefer many short concrete quests over a few oversized catch-all quests
- preserve a sense of momentum in every chapter by ending on a visible capability gain
