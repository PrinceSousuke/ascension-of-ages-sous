# Ascension of Ages — Update Notes

What's new since the last public build (June 2026).

---

## Quest Book

We went through the whole book and rewrote quest text so it tells you what to build, why it matters, and what comes next — especially in the Gilded and Atomic ages. The book now has **1,820 quests across 55 chapters**, with the biggest growth in those late ages.

Fixed a few progression hiccups along the way: duplicate turn-ins, confusing gate wording, and optional chapters that were accidentally blocking the main path.

**Journey to Ascension** got rebuilt — a spoiler-free roadmap of each age and its gate, with links out to the chapters that matter.

---

## Progression & Multiplayer

Playing with friends? Age stage grants now **sync to your whole FTB team** when anyone completes them. If you log in missing a stage your team already cleared, it should fix itself on login — no need to redo the quest.

**Iron Era / AStages fix:** All progression stages now register with `customizeStage()` so `/astages add` and `/astages list` work. Completing **Entering the Iron Era** should grant `medieval_times` and unlock Medieval chapters. (Codex FTBQ rewards were never removed; the live instance still had stale R5-stripped copies in a non-authoritative path.)

**Config seed layout:** Pack default seeds now live under `config/modpack_defaults/config/` so Config Manager copies into `config/` instead of the instance root. Fresh installs should no longer sprawl hundreds of `.toml` files beside `mods/`.

**Cave spawns:** InControl caps were too aggressive (`perplayer` across all loaded chunks). Underground caps are higher and **per-chunk** now (Y≤20: 24, Y≤64: 40, surface: 40). MonsterPlus cap raised to 10 per chunk; Ancient Hero capped separately at 2 per chunk. **Corrupted Ancient Hero** quest text now clarifies overworld natural spawn (not deepslate-only).

**Fixes:**
- Theurgy IR feedstock quest now asks for the **Sulfur Vessel** (not the Renaissance incubator).
- Industrial Create recap quests are optional again — they won't hold up the age.
- Farmer's Delight cooking pot recipe uses a **stone shovel** (wooden tools aren't craftable under Overgeared).

Several machines and items were moved to the age the quests actually expect — late Immersive Petroleum processing, Integrated Dynamics basins, ProjectRed automation, and some Create redstone parts now unlock in **Industrial Revolution**. Late Atomic and Ascension gear (Oritech duratium, bigger RS Mek storage, Chemical Science machines, advanced Extended Crafting) was pushed to the right tier.

**Boss rewards:** six new prestige boss loot caches (Obsidilith, Maledictus, Void Titan, Geburah, Macabre, Leviathan), plus a broader rebalance of industrial, expedition, ascension, and nuclear reward pools.

---

## Graphics

Updated **Sodium** and **Iris** to fix launch and world-load crashes. A few old Sodium addons had to go because they don't support the new version yet: Sodium Leaf Culling, Reese's Sodium Options, Sodium Options API, and Mekanism Covers.

---

## World Generation

Villages should be easier to find and less likely to spawn on cliffs or in the ocean. Changes only affect **new chunks** — your existing world is fine.

---

## New Guides

- **Gilded Ledger** — in-game guide for the Gilded Age
- **Atomic Dossier** — in-game guide for the Atomic Age

---

## Mod Changes

**Added:** Tombstone (death recovery), FTB Chunks, ExtraQuests, FTB Filter System, FTB Quests Entity Vis, Beautiful Enchanted Books.

**Removed:** Gravestone (replaced by Tombstone), and the Sodium addons listed above.

**Updated:** Occultism, Oritech, Nuclear Science, Cataclysm, Ballistix/Blastcraft, several Create addons, Sophisticated Storage/Backpacks, FTB Quests, JourneyMap, Supplementaries, and more.

---

## Before You Update

1. **Back up your world.**
2. **Gravestone is gone** — Tombstone handles death differently. Old graves won't carry over.
3. On a **team server**, have everyone log in once after updating so stages sync cleanly.
4. Look for the **Gilded Ledger** and **Atomic Dossier** when you reach those ages.
