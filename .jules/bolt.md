## 2024-05-19 - Canvas Render Optimization

**Learning:** Canvas rendering performance in \`birthday.js\` heavily relies on caching static or fully-grown geometry (e.g., quadratic curve segments, widths, gradients) during \`requestAnimationFrame\` loops to prevent severe CPU overhead from redundant calculations. The branches loop recalculates \`quad()\` path data continuously on every frame even when \`e >= 1\` (fully grown).
**Action:** When a branch animation reaches completion (\`e >= 1\`), cache its segments into a \`cachedPath\` array and replay from there, rather than recalculating quadratics and lerping widths continuously.
