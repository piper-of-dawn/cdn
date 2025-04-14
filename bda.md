---
marp: true
theme: default
---

<!-- Slide 1 -->

# Unconditional Returns of CLOs

- CLO returns often **overshoot** benchmark indices.
- This persistent overshooting leads to **excess kurtosis** (fat tails).
- Visual inspection of kernel density plots shows higher peak and heavier tails than the normal distribution.

---

<!-- Slide 2 -->

# Conditional Returns of CLOs

- After regressing against risk factors, **residuals** show fat-tailed behavior.
- **Normality is violated**, especially in the **left tail**, indicating risk of extreme losses.
- QQ plots confirm deviation from normal, particularly in the lower quantiles.

---

<!-- Slide 3 -->

# MLE Fit with Student's t-distribution

- Using Maximum Likelihood Estimation (MLE), degrees of freedom \( \nu \) is optimized.
- The **KS statistic improves**, indicating **t-distribution fits residuals better**.
- Suggests that returns are **conditionally heavy-tailed** and better modeled with a flexible distribution.

---

<!-- Slide 4 -->

# Robust Conclusions

- CLO returns exhibit **non-normal behavior** both unconditionally and conditionally.
- **Fat tails** are structurally embedded, not just artifacts of noise.
- Modeling with **t-distribution provides robustness**, especially for risk estimation.
- **Risk management models assuming normality** will underestimate extreme outcomes.

---

<!-- Slide 5 -->

# Critical Reflection

- Overshooting could also result from **structural leverage or illiquidity**, not just statistical fat tails.
- KS-stat improvement is useful, but not sufficient — consider **CVaR or tail index** tests for robustness.
- Does residual structure imply **omitted risk factors**? Consider more granular factor modeling.
- Future work: **time-varying volatility** models (e.g., GARCH-t) or regime-switching models.

