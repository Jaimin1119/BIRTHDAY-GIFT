
## 2024-10-27 - Canvas Geometry Caching
**Learning:** Canvas rendering performance heavily relies on caching static or fully-grown geometry (e.g., quadratic curve segments, widths, gradients) during `requestAnimationFrame` loops to prevent severe CPU overhead from redundant calculations.
**Action:** Apply lazy initialization strategies within rendering loops to pre-calculate and cache expensive geometrical paths for objects that have finished their dynamic animations.
