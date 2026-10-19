## 2024-10-19 - Cache static geometry in requestAnimationFrame loops
**Learning:** The continuous `requestAnimationFrame` loop caused severe CPU overhead by recalculating the 12 curve segments (`quad()` and `lerp()`) for every branch, even when fully grown. Canvas rendering performance heavily relies on caching static or fully-grown geometry to prevent redundant calculations.
**Action:** Cache the static point coordinates and widths upon object creation. Only calculate dynamically for the actively interpolating segment.
