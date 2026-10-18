## 2024-10-18 - Canvas caching
**Learning:** Canvas rendering performance in `birthday.js` heavily relies on caching static or fully-grown geometry during `requestAnimationFrame` loops to prevent severe CPU overhead from redundant calculations.
**Action:** Implement a cache for fully grown branches so that they are not redrawn via computationally expensive functions every frame.
