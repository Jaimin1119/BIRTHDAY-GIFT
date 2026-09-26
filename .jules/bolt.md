## 2024-03-24 - Canvas Path Rendering Bottleneck
**Learning:** Drawing thousands of `ctx.stroke()` paths recursively every frame for static branches kills performance in canvas apps.
**Action:** Use an offscreen canvas to cache fully-drawn complex static structures and use `ctx.drawImage()` instead of recalculating/redrawing paths.
