# Monte Carlo π Estimation

This experiment uses the **Monte Carlo method** to estimate the value of π through random sampling.

---

## How It Works
1. Generate random (x, y) points inside a square of side 2 (from -1 to 1).  
2. Count how many points fall within the unit circle (`x² + y² ≤ 1`).  
3. The ratio of points inside the circle to total points ≈ π / 4.  
4. Multiply by 4 → π estimate.

---

## Observation
- As the number of samples increases, the estimate converges to **3.14159...**.  
- Small sample sizes fluctuate more due to randomness.

---

## Requirements

numpy
matplotlib (for visualization)

Install with:

pip install numpy matplotlib

---

## Run It
```bash
python montecarlo_pi.py --samples 100000

---

## Example output

- Estimated π: 3.1428
- Error: 0.0012
