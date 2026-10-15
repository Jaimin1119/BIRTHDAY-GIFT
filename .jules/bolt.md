## 2024-05-24 - Canvas Geometry Caching
**Learning:** Canvas rendering performance heavily relies on caching static or fully-grown geometry (e.g., quadratic curve segments, widths, gradients) during `requestAnimationFrame` loops to prevent severe CPU overhead from redundant calculations.
**Action:** Pre-calculate and store unchanging geometry (like fully-grown branch segments) during scene construction rather than recalculating them on every frame.
