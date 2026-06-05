import assert from "node:assert/strict";
import fc from "fast-check";

function directDivision(value: number, y: number): number {
  return value / y;
}

function reciprocalMultiply(value: number, inv: number): number {
  return value * inv;
}

const finiteNumber = fc.double({ noNaN: true, noDefaultInfinity: true });
const nonZeroFiniteNumber = fc.oneof(
  fc.double({ max: -Number.MIN_VALUE, noNaN: true, noDefaultInfinity: true }),
  fc.double({ min: Number.MIN_VALUE, noNaN: true, noDefaultInfinity: true }),
);

fc.assert(
  fc.property(finiteNumber, nonZeroFiniteNumber, (value, y) => {
    const inv = 1.0 / y;
    assert.deepStrictEqual(reciprocalMultiply(value, inv), directDivision(value, y));
  }),
);
