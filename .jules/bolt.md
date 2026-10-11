## 2026-10-11 - Canvas Branch Caching
**Learning:** In canvas rendering for `birthday.js`, recalcuating bezier curves for fully-grown static branch segments in every frame causes immense CPU overhead.
**Action:** When animating geometry in canvas, cache static or fully-completed segments (e.g., coordinates, widths) and draw from the cache instead of recalculating during `requestAnimationFrame` loops.
