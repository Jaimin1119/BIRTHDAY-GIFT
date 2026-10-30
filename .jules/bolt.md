## 2026-10-30 - [Performance] Cache fully-grown static canvas geometry
**Learning:** Canvas rendering performance heavily relies on caching static or fully-grown geometry (e.g., branch segments, widths, gradients) during `requestAnimationFrame` loops to prevent severe CPU overhead from redundant calculations.
**Action:** When working on canvas animations, identify static or fully-rendered geometries within continuous loops and cache their states instead of calculating them on every frame.
