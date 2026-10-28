## 2024-10-28 - Optimizing Canvas Path Drawing in rAF
**Learning:** Canvas rendering performance in `birthday.js` heavily relies on caching static or fully-grown geometry (e.g., quadratic curve segments, widths, gradients) during `requestAnimationFrame` loops to prevent severe CPU overhead from redundant calculations.
**Action:** When working on animation frames where objects grow and then stay static, pre-compute the final layout math at object creation to bypass math operations for parts of the animation that have finished growing.
