## 2024-10-10 - Canvas Rendering Optimization
**Learning:** Canvas rendering performance heavily relies on caching static or fully-grown geometry (e.g., quadratic curve segments, widths, gradients) during `requestAnimationFrame` loops to prevent severe CPU overhead from redundant calculations.
**Action:** Always pre-calculate and cache static geometry like paths, points, and widths during initialization, rather than recalculating them on every frame in the render loop.
