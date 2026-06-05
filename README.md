# Division Versus Reciprocal Multiplication

Some random tweet suggested the following:

```c
// before: ~3.2 seconds
// 20-40 cycles per iteration
for (int i = 0; i < 1000000; i++)
    arr[i] = arr[i] / 3.14159f;

// after: ~0.8 seconds
// 4 cycles per iteration
float inv = 1.0f / 3.14159f;
for (int i = 0; i < 1000000; i++)
    arr[i] = arr[i] * inv;
```

The snippet above was discussed in this episode of [Standup Podcast](https://www.youtube.com/watch?v=PxNr7k1v-Rk)

Floating-point is a finite representation of numbers. Perhaps doing the proposed is faster but outputs are likely just different.


```python
x / y
```

and:

```python
inv = 1.0 / y
x * inv
```

The implementation for checking equivalence follows *Property-based testing* concept and was done in Python & Hypothesis and TypeScript & fast-check.

Run the Python & Hypothesis tests:

```sh
cd python
uv run pytest
```

Run the TypeScript & fast-check test:

```sh
cd typescript
npm install
npm test
```

The testing frameworks decide on the inputs and will do some effort on finding good failing cases also referenced as *shrinking*.
Your results might be different due some stochasticity.

My observed shrinks:

```text
Python and Hypothesis:
values = [5.0]
y = -3.0
reciprocal_multiply -> [-1.6666666666666665]
direct_division     -> [-1.6666666666666667]

TypeScript and fast-check:
values = [0]
y = 5e-324
reciprocalMultiply -> [NaN]
directDivision     -> [0]
```

If you would like to have a intermediate values run the following:

```sh
cd python
python3 division_table.py 5 3 500 > division_table.txt
```

The table records repeated application from the starting value:

```python
x = x / divisor
```

versus:

```python
x = x * (1.0 / divisor)
```

Columns include `division`, `multiplication`, absolute `difference`, and
`relative error`.
