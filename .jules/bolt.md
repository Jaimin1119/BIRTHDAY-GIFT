## 2024-11-02 - Tree Geometry Caching
**Learning:** In canvas-based generative tree applications (like Act 4 in `birthday.js`), static geometry (like branches) that relies on complex math like `quadraticCurveTo` approximations or interpolation (`lerp`, `quad()`) inside an rAF loop introduces massive CPU overhead.
**Action:** When working on canvas rendering of living elements, cache fully grown or static geometry calculations per element (e.g., segment lines and widths) to save mathematical operations, replacing math with simple array iteration in the `requestAnimationFrame` render loop.
