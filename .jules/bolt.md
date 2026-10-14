## 2026-10-14 - Optimize caching in Canvas render loop
**Learning:** Canvas rendering performance in `birthday.js` heavily relies on caching static or fully-grown geometry (e.g., quadratic curve segments, widths, gradients) during `requestAnimationFrame` loops to prevent severe CPU overhead from redundant calculations.
**Action:** When working on Canvas animations like the tree growing, look for redundant geometry calculations that can be cached when a branch or object is fully grown.
