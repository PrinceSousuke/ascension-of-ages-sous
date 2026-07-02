# K — Reference-Pack Quest-Design Study (for AoA)

Research date: 2026-07-02. Method: web research (WebSearch / WebFetch) across pack
wikis, CurseForge/ATLauncher pages, review aggregators, GitHub issue trackers, and
FTB documentation. Purpose: mine quest-design philosophy from four progression packs
to inform the Ascension of Ages (AoA) questbook, then synthesize actionable takeaways
judged against AoA's own canon (teach-the-mechanic prose, no filler, crossing-free
layouts, required-chapter spines with one age-grant capstone, density welcome but no
exact-duplicate item quests).

AoA's stated philosophical parent is **SevTech: Ages**, so that pack gets the deepest
treatment.

---

## 1. SevTech: Ages — the philosophical parent

Sources:
- Official wiki: https://sevtechages.fandom.com/wiki/SevTech:_Ages_Wiki
- ATLauncher pack page: https://atlauncher.com/pack/sevtechages
- Modded Minecraft Reviews (SevTech): https://mmcreviews.com/all/modpacks/sevtech-ages/
- How-to-play guide: https://sevtechages.fandom.com/wiki/How_to_play_guide_for_SevTech:_Ages
- Issue tracker: https://github.com/DarkPacks/SevTech-Ages/issues

### Age / chapter architecture
Ordered historical ages: Stone Age → Bronze Age → Medieval / Middle Ages → Industrial
Age → Modern Age → Futuristic/Space (informally a "Creative" tail). Each age is a
band of content revealed only when the prior age's terminal advancement fires. The
pack frames its own goal literally as "follow through the advancement system from the
stone age all the way into space." This is the exact shape AoA inherited: an ordered
ladder of eras, each a gate.

### Gating mechanism (the core lesson)
Two layers stacked:
1. **Advancements as the progression spine.** "Hundreds of custom advancements"
   drive the arc and *reveal new mods* to work through. Advancements are the visible
   roadmap; completing the terminal advancement of an age unlocks the next.
2. **GameStages as the enforcement layer.** GameStages gates dimensions, mobs,
   recipes, and *items* by player progress. The signature move is **hiding content
   entirely until its age**: "hiding ore until unlocked, dynamically hidden items and
   recipes based on progress," plus new mobs that appear only as advancements unlock.
   Unlocked-later ore is invisible and uncraftable. Players start with almost nothing
   (no map, no WAILA/HWYLA) and progressively unlock thousands of blocks.
3. **Player-based, not server-based.** Progression is per-player, so late joiners
   advance independently instead of being dragged to the host's age.

The deep lesson for AoA: SevTech's magic is not the quests, it is the **reveal**. You
never see the diving suit, the reactor, the ore until you have earned the age. That
sense of a world unfolding is what players remember. AoA already replicates the
enforcement half via AStages item locks + FTBQ progressive-reveal
(`hide_until_deps_complete` on rootless-gated chapter entries); the *experiential*
half is the payoff to protect.

### How mechanics are TAUGHT vs checklisted
SevTech's strongest praise is for **cross-mod integration**: it "requires players to
use items from multiple mods together to progress, rather than focusing on individual
mods in isolation." Progression *is* the teaching — you learn a mod because the next
gate forces you through it, and the pack chains "thematically different mods" so each
age feels like a distinct technological world rather than a mod checklist. This is the
opposite of a kitchen-sink "one chapter per mod, grab one of each item" layout.

### Boss / capstone pacing
SevTech is not boss-forward; its capstones are *technological thresholds* (build the
multiblock, reach the dimension, craft the tier item) rather than kill-walls. The
age boundary is the achievement. Worth noting because AoA is *more* boss-gated than
its parent (Maledictus, Obsidilith, Void Titan, the macabre quartet, Leviathan,
Draconic Guardian) — a deliberate divergence, not an inheritance.

### Duplicate / variant handling
Not a quest-density problem for SevTech because it does not "quest every item" — the
advancement tree tracks milestones, not inventory completeness, so it never invites
the one-of-each padding that FTBQ item-chapters do.

### Top community complaints (what to avoid)
- **The back half turns tedious.** Reviewers agree early-to-mid game is the sweet
  spot; the pack "became more tedious towards the end." **Age 4 specifically** has "a
  higher amount of somewhat tedious processes and odd design decisions."
- **Time-gate mods masquerading as content.** The Twilight Forest is "used more as a
  rudimentary time gate than being truly integrated," and the Betweenlands is a "dark
  and tedious" slog "for obtaining just a few necessary gems." Players resent a
  dimension that exists only to burn hours for one ingredient.
- **Advancement/config mismatches confuse players.** The Cooking-for-Blockheads sink
  is *suggested by an advancement* but configured not to be an infinite water source,
  contradicting player expectation from other packs. Guidance that lies about the
  mechanic is worse than no guidance.

Takeaway direction: keep the reveal, keep cross-mod chaining, but do **not** let any
age (AoA's mid-tier Gilded/Atomic are the risk zone) degrade into obtuse process
grind, and never gate an age behind a dimension the player only visits to grab one
gem. Every gated detour must teach or produce something the player keeps using.

---

## 2. Enigmatica 2: Expert (and E2:E Extended)

Sources:
- Quests wiki: https://e2e.fandom.com/wiki/Quests (paywalled on fetch; corroborated
  via search excerpts)
- Main wiki: https://e2e.fandom.com/wiki/Enigmatica_2:_Expert
- CurseForge: https://www.curseforge.com/minecraft/modpacks/enigmatica2expert
- Player travelogue: https://orian34.github.io/travelogues/posts/enigmatica2expert/
- Extended fork: https://github.com/Krutoy242/Enigmatica2Expert-Extended

### Age / chapter architecture
Not age-banded like SevTech. ~650+ quests organized into **per-mod / per-theme
categories** (Mekanism, Thermal Expansion, AE2, NuclearCraft, EnderIO, Immersive
Engineering on the tech side; Astral Sorcery, Thaumcraft, Botania, Blood Magic, Psi
on magic). The organizing principle is **tech/magic tiers**, and "at every Technology
and Magic tier you'll have the choice between several different mods to progress" up
to the top-tier endgame materials.

### Gating mechanism — the expert-mode signature
E2:E's identity is **recipe rewriting**. Vanilla/default recipes are deleted and
replaced with expert recipes that **force cross-mod dependency**: to make a tier
material you must route through several mod systems simultaneously rather than
crafting it cheaply within one mod. The player travelogue confirms this — "recipes
interconnected to progress," and "expert recipes force players to engage with multiple
mod systems simultaneously rather than rushing endgame content." Dimensions gate the
same way (Nether/End/Twilight portals open only when prerequisites are met).

This is the **recipe-weave** technique AoA already uses (the
`aoa_recipes_*_weaves.js` cross-mod bridges). E2:E is the canonical proof that
recipe-rewrite gating produces the most respected "expert" feel — but also the most
grind complaints, so it is a double-edged tool.

### Quest density + per-mod depth
Dense per-mod questlines that walk you through each mod's machine tree. Quests act as
a **pacing mechanism tied to resource availability**: the traveler noted quests were
scarce while power-constrained, then "unbridled, downing them by the dozen" once RTGs
solved power. So E2:E quests are less "teach me this mechanic" and more "acknowledge
the milestone I just hit by grinding." That is a weaker teaching model than SevTech's
integration-forced learning.

### How mechanics are TAUGHT vs checklisted
Taught primarily *through the expert recipe itself* — the recipe is the lesson, the
quest is the receipt. This works for veteran audiences but is unforgiving for new
players (E2:E assumes you already know the mods).

### Boss / capstone pacing
Endgame is the **"Bragging Rights" questline: craft one of every craftable creative
item**, then unlock **creative-item duplication** (the ultimate ingot dupes in a tank;
creative vending upgrade dupes without restriction). Once infinite duplication lands,
"the pack is basically over." The capstone is a crafting singularity, not a boss.

### Duplicate / variant handling
Deliberately embraces duplication *as the win condition* — the opposite of AoA's
"no exact-duplicate item quests" rule. E2:E can do this because its whole arc points at
creative items; AoA's arc points at ascension through bosses, so dupe-as-goal does not
transfer.

### Top community complaints (what to avoid)
- **Specific recipes are "incredibly obtuse and annoying"** — singularity production
  and the fusion core reactor were called out by name even by a player who liked the
  pack. Obtuse ≠ hard; obtuse means the game did not teach you the step and you had to
  external-wiki it.
- **Assumes prior mod knowledge.** New players bounce off expert recipes with no
  in-quest teaching.
- **Power scarcity as the sole early gate** creates a long flat stretch before RTGs
  suddenly open the floodgates — uneven pacing.

---

## 3. All the Mods 10 (ATM10)

Sources:
- DeepWiki quest-system analysis: https://deepwiki.com/AllTheMods/ATM-10/2-quest-system
- Quest-structure page: https://deepwiki.com/AllTheMods/ATM-10/2.1-quest-structure
- Reward-balance complaint (discussion): https://github.com/AllTheMods/ATM-10/discussions/3539
- Reward-balance complaint (issue): https://github.com/AllTheMods/ATM-10/issues/3293
- Guides hub: https://allthemods.github.io/alltheguides/atm10/

### Age / chapter architecture
No ages. **Chapter groups by theme** — Main Questline, Magic, Technology, Storage,
Resources, Tools/Gear — each group holding per-mod chapters (AE2, Ars Nouveau, Extreme
Reactors, Mekanism, Mekanism Reactors, Powah, Productive Bees, Immersive Engineering,
etc.). Each mod chapter is its own SNBT file. This is the modern kitchen-sink standard:
**one chapter per major mod**, positioned on an x/y grid with dependency lines, grouped
by domain rather than by era.

### Gating mechanism
Minimal hard gating. ATM is a *kitchen sink*: progression is soft, driven by resource
tiers (allthemodium → vibranium → unobtainium) and the ATM Star as the convergence
capstone. There is no stage system hiding content; almost everything is craftable from
the start given materials. Gating is by material rarity and recipe cost, not by locks.

### Quest density + per-mod depth
Dense per mod, but the depth is **inventory-completeness driven** — obtain this
machine, obtain that upgrade. Task types confirmed in use: `item`, `kill`,
`advancement`, and **checkmark (manual-completion) tasks**. Rewards: direct `item`,
`xp`, `xp_levels`, and `random`/loot-table reward tables (loot-bag style choice/
weighted rewards). Quest shapes (square, hexagon, pentagon, gear) encode
importance tiers visually. Decorative images (`atm:textures/questpics/`) add flavor.

### How mechanics are TAUGHT vs checklisted
Heavily **checklisted**. The DeepWiki description ("requires the player to obtain
specific items") and the reliance on checkmark tasks confirm the model is *acknowledge
what you did*, not *teach how to do it*. This is the kitchen-sink trade-off: breadth
over pedagogy.

### Reward philosophy — and the community revolt against it
This is ATM10's most instructive lesson for AoA. Two parallel complaints
(discussion #3539 and issue #3293) attacked the reward tables for **breaking
progression**:
- A basic 4-nugget crafting pad rewarded an **Allthemodium Ore Sight Charm**, directly
  undoing the devs' deliberate "hard to find / hard to mine" design for that ore. The
  reporter: "the ore might as well be given to you when you spawn."
- Rewards handed out **dragon eggs, ender chests, and Ultimate Universal Cables**
  when players "had barely crafted a dozen of basic ones" — endgame-tier items given
  before intermediate crafting.
- Multiplayer amplifies it: duplicated rewards across a team snowball.
- Reporter's verdict: "almost everything IMO should be revisited and a general balance
  pass should be made."

The maintainer response (TheBedrockMaster) **disagreed**: in a kitchen-sink pack an
ender chest or cables "don't inherently break progression," only ATM Stars would, and
the rewards "are popular with players." The debate went unresolved.

The takeaway is not who was right — it is that **reward-vs-progression mismatch is the
single loudest quest complaint in a modern pack**, and it is exactly the failure mode
AoA's age-tier discipline is built to prevent. A reward that hands you a later-age item
in an earlier age is, in AoA terms, a hard cross-age inversion / softlock risk. ATM can
shrug it off because it has no ages; AoA cannot.

### Top community complaints (what to avoid)
- Rewards that skip "arbitrary progression steps for no reason."
- Endgame-tier reward items in early chapters.
- Checkmark/manual-completion tasks as filler (AoA already bans these outright).

---

## 4. Age of Fate

Sources:
- CurseForge: https://www.curseforge.com/minecraft/modpacks/age-of-fate
- Modpack Index: https://www.modpackindex.com/modpack/29878/age-of-fate
- Reviews: https://mmcreviews.com/all/modpacks/age-of-fate/

### Age / chapter architecture
Very large: ~730+ mods, **4,800+ quests across 16 chapter groups / 72 quest chapters**.
Marketed as a "fully guided progression from novice to legendary hero." Age/gate
progression requires completing earlier chapters before later ones unlock.

### Gating mechanism
Chapter-based sequential gating plus **stages/gates that must be unlocked**, and
critically **boss drops as gate keys**: bosses feature "progressive difficulty scaling"
and their drops are "required for endgame crafting." This is the most boss-gated of the
four and is the closest structural analog to AoA's boss-proof spine (kill boss → obtain
proof item → craft/advance). The endgame is the **Nexus of Fate**: collect 20 rare
mystical stones (via exploration + boss defeats) → Stone of Transcendence → Essence of
Fate → Nexus of Fate. A long convergence chain, structurally similar to AoA's
capstone-convergence fan-ins.

### Quest density + per-mod depth
Extremely dense (4,800 quests / 72 chapters ≈ 65 quests per chapter average). Density
is a headline selling point here, not a liability the pack apologizes for.

### How mechanics are TAUGHT vs checklisted
Story-driven ("narrative that unfolds as you play") layered over guided quests. Less
documented on per-quest teaching quality; the marketing emphasizes narrative arc and
difficulty over pedagogy.

### Top community complaints (what to avoid)
- **"Many modpacks/mods don't integrate well"** — the breadth (730 mods) outruns
  cohesion; mods sit side-by-side rather than weaving. This is the anti-SevTech
  failure: quantity without integration.
- **"Too many overpowered items acquirable within 10–20 hours."** Same disease as
  ATM10 — rewards/recipes leak power too early and flatten the curve.
- **"Nice system of progression but not fully polished yet."** Ambition outran QA.

---

## 5. General FTB Quests design best-practice notes

Sources:
- FTB Docs — Tips & Tricks: https://docs.feed-the-beast.com/mod-docs/mods/suite/Quests/Player/Questbook/Tips_Tricks/
- FTB Docs — Chapter Settings: https://docs.feed-the-beast.com/mod-docs/mods/suite/Quests/Developer/Chapters/Settings/
- Dependency-line feature request: https://github.com/FTBTeam/FTB-Mods-Issues/issues/1474
- Chapter-link feature request: https://github.com/FTBTeam/FTB-Mods-Issues/issues/987

- **Dependency-line readability is a known pain point.** A common author trick:
  place a *hidden* child quest under a main node to draw the dependency line, and turn
  dependency lines OFF on the main node so they only render on hover. This keeps the
  map clean while preserving traceability — directly relevant to AoA's crossing-free
  hard constraint.
- **Two independent reveal settings**: "Hide until Dependencies Visible" and "Hide
  until Dependencies Complete." AoA already uses the latter for progressive reveal.
- **Chapter links / chapter-link object**: quests can appear in multiple chapters as
  "Linked" copies, and chapters can flow into one another via the quest map for
  cohesion. Useful for AoA's age-to-age handoff without duplicating structure.
- **Optional flag + progression mode + sequential tasks** are first-class per-quest.
- **Reward tables** (loot-crate/weighted) live in `reward_tables/` and support
  choice/random distribution — the mechanism behind ATM's loot bags.

---

## 6. Synthesis — actionable takeaways for AoA

Each tagged [adopt] / [adapt] / [avoid], judged against AoA canon.

1. **[adopt] Protect the reveal, not just the lock.** SevTech's lasting magic is that
   later-age content is *invisible* until earned, so each age feels like a new world
   unfolding. AoA already enforces locks (AStages + `hide_until_deps_complete`); treat
   the *player-facing surprise* of an age opening as a first-class design goal, not a
   side effect. Audit that no earlier chapter previews later-age items in text or icon.

2. **[adopt] Cross-mod chaining is the teaching, checklists are not.** SevTech's top
   praise and Age of Fate's top complaint are the same axis: integration vs
   side-by-side. Keep authoring quests that force two mods to feed each other (AoA's
   recipe-weave scripts), because the chain itself teaches. This aligns with AoA's
   "teach the mechanic" prose rule.

3. **[adopt] Reward discipline is the loudest failure mode in modern packs.** Both
   ATM10 complaints and Age of Fate's "OP items in 10–20 hours" are reward/recipe
   power-leak. AoA's age-tier discipline already forbids later-age items in earlier
   chapters — extend that vigilance explicitly to *reward tables*, not just task items.
   A reward that grants a next-age item is a cross-age inversion / softlock risk.

4. **[adapt] Recipe-rewrite gating (E2:E) is the strongest "expert" tool AND the
   biggest grind risk.** Keep using cross-mod recipe weaves, but pair every obtuse
   expert recipe with instruction-first prose that teaches the step. E2:E's named
   failures (singularity, fusion core) were "obtuse," meaning untaught — exactly what
   AoA prose is supposed to prevent.

5. **[avoid] Do NOT let any mid-tier age degrade into process grind.** SevTech Age 4
   is the textbook warning: "tedious processes and odd design decisions" in the middle
   of the arc. AoA's Gilded/Atomic band is the equivalent risk zone (Mekanism +
   nuclear + logistics density). Density is welcome per canon, but each dense quest
   must produce or teach something kept; audit those chapters against the anti-bloat
   rubric specifically.

6. **[avoid] No dimension-as-pure-time-gate.** SevTech's Betweenlands/Twilight
   "grab one gem then leave" is a named resentment. AoA gates many dimensions at
   Renaissance (Nether/End/Aether/Undergarden/Otherside/Starlight). Each must have a
   real production or teaching reason to be visited, not a single fetch ingredient.

7. **[avoid] No inventory-completeness checklisting.** ATM10's "obtain one of each
   machine/upgrade" model plus checkmark tasks is the padding AoA already bans. Quest
   milestones and downstream items, never one-of-each variant tours. (Reinforces the
   existing no-vanilla, no-bare-ingot, no-checkmark rules.)

8. **[adapt] Boss-gated capstones — AoA is MORE boss-forward than its parent, so pace
   the build-up deliberately.** SevTech capstones are tech thresholds; Age of Fate and
   AoA gate ages on boss kills + proof items. Age of Fate's Nexus convergence (20
   stones → transcendence chain) mirrors AoA's capstone fan-ins. Lesson: make the
   chapter *before* each boss visibly assemble the gear/proof the fight needs, so the
   boss reads as a culmination, not a wall. (AoA already has boss-proof-item flow; keep
   the pre-boss chapter as the on-ramp.)

9. **[adopt] Advancements/quests must not lie about mechanics.** SevTech's
   Cooking-for-Blockheads sink (advancement suggests infinite water, config says no)
   is a small but repeatedly cited irritation. AoA prose that teaches a mechanic must
   match the actual config/recipe — verify-first applies to prose claims too.

10. **[adopt] Use hidden-child + hover-only dependency lines to keep the map clean.**
    The FTB-documented author trick (hidden node draws the line, main node hides lines)
    is a direct tool for AoA's crossing-free hard constraint on dense chapters.

11. **[adapt] Reward tables for flavor/comfort, never for progression skips.** ATM's
    loot bags are popular *and* controversial. AoA can use `reward_tables/` for
    cosmetic/comfort/material rewards, but progression proofs and gear must stay on
    deterministic quest rewards tied to real tasks — never in a random table that could
    hand a next-age item.

12. **[avoid] Do not let breadth outrun cohesion (Age of Fate's core flaw).** 730 mods
    / 4,800 quests bought density but lost integration ("mods don't integrate well").
    AoA's "quality over density, no filler" canon is the correct counter — resist the
    urge to give every installed mod its own padded chapter; give it a *home* only if
    it earns integration into the age's spine.

13. **[adapt] Per-player progression is the right multiplayer model.** SevTech's
    per-player (not server-wide) advancement lets late joiners catch up. AoA grants
    stages via FTBQ team completion; confirm the team model does not strand a late
    joiner mid-age (mirrors the ATM "duplicated reward snowball in multiplayer" concern
    from the other direction).

14. **[adopt] Terminal-item / convergence capstone as the arc's finish line.** E2:E's
    "craft one of every creative item" and Age of Fate's Nexus both give the arc a
    single legible endpoint. AoA's ascension capstone convergence is the right analog —
    keep one unambiguous final target so the whole ladder points somewhere.

15. **[avoid] Do not adopt creative-item duplication as an endgame.** E2:E ends when
    infinite dupe unlocks and "the pack is basically over." That directly violates
    AoA's "no exact-duplicate item quests" ethos and would collapse the ascension
    fantasy into a spreadsheet. AoA's endgame is transcendence-through-mastery, not a
    dupe machine — keep it that way.

---

*End of report. All claims sourced inline above; SevTech gating detail and community
sentiment corroborated across the ATLauncher page, the SevTech wiki, and the MMC
Reviews aggregator; ATM10 reward-philosophy debate taken directly from the two GitHub
threads; E2:E recipe-rewrite model corroborated by the player travelogue.*
