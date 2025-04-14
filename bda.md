To facilitate a direct comparison with the normal distribution, the Student's t-distribution is rescaled to match a target variance $\sigma^2$, typically estimated from residuals under a Gaussian model. The variance of a standard t-distribution with $\nu > 2$ degrees of freedom is:

$$
\text{Var}(T_\nu) = \frac{\nu}{\nu - 2}
$$

To match this with a normal-based standard deviation $\sigma$, we apply the scaling transformation:

$$
\text{Scale} = \sigma \cdot \sqrt{\frac{\nu - 2}{\nu}} \quad \Rightarrow \quad \text{Var}(\text{Scale} \cdot T_\nu) = \sigma^2
$$

---

### Intent

The purpose of this rescaling is to **control for dispersion**, allowing the t-distribution to be evaluated purely on its **tail behavior**. 
---

### Conclusion

Even after rescaling, the t-distribution will retain its **fat-tailed nature**, exhibiting heavier tail probabilities than the normal distribution. This allows it to more accurately reflect the risk of extreme outcomes, where normality assumptions often underestimate tail risk. That said, even the **normal distribution does provide reasonable coverage** of tail risk as evident from the time series plots presented above. For instance, a 95% upper bound is given by:

$$
\text{Upper} = \mathbb{E}[r_t] + 1.96 \cdot \sigma
$$

This threshold captures even the most extreme drawdown that happened during March 2020. 