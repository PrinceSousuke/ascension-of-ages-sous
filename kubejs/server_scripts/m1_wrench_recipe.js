// AoA M1 — Medieval-legal wrench recipe
// Stock Create wrench uses c:plates/gold. Gold is Renaissance-gated per AoA v4.1 §3.1,
// so the stock recipe would make Create unusable through Medieval.
// Swap: gold plates -> brass plates (c:plates/brass). Brass comes online via the
// PMW/Alloyed foundry in M2, so the wrench becomes craftable once the foundry is running.

ServerEvents.recipes(event => {
  event.remove({ id: "create:crafting/kinetics/wrench" });

  event.shaped(
    Item.of("create:wrench"),
    [
      "BB ",
      "BP ",
      "  S"
    ],
    {
      B: "#c:plates/brass",
      P: "create:cogwheel",
      S: "#c:rods/wooden"
    }
  ).id("aoa:m1/wrench_from_brass");
});
