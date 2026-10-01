## 2026-10-01 - Canvas Render Loop String Allocations
**Learning:** High frequency render loops (like canvas drawing at 60fps) can suffer from garbage collection pressure due to generating many new string objects, especially template literals.
**Action:** Always hoist invariant string allocations (like color definitions that are constant per-frame) out of any loops inside the render loop to reuse memory.
