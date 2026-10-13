## 2025-02-12 - Canvas Geometry Caching
**Learning:** Canvas rendering performance in Vanilla JS/requestAnimationFrame loops can suffer significantly from repeated math calculations for static objects. In `birthday.js`, the quadratic bezier points for branch segments were continuously calculated even when fully grown.
**Action:** Always pre-calculate and cache fixed geometry (like quadratic curve segments, width arrays) outside the main render loop to skip math overhead for static parts.
