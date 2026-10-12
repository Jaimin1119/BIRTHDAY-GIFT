
## 2024-10-12 - Canvas Path Geometry Caching
**Learning:** In GSAP animations rendering paths incrementally (like branches growing), continually recalculating quadratic curves (`quad()` mapping) and interpolated widths (`lerp()`) for fully-grown segment parts on every frame (60fps) is a major CPU bottleneck, especially as hundreds of elements render.
**Action:** When working with incrementally grown canvas geometry, pre-calculate and cache the static points and widths array during the first frame or initialization. Then, skip heavy recalculation for any completed section, only dynamically computing the exact active leading edge segment.
