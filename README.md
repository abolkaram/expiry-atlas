# Expiry Atlas — field notes from the renewal meridian

A permit is plotted once: holder, bounded scope, conditions, expiry, renewal window, and the hostname of its issuing authority. A replacement record from another origin cannot silently become authoritative.

Anyone may open the renewal phase once the permit crosses its deterministic meridian. Only the holder may submit the renewal. Validators fetch it and independently confirm that scope is unchanged and every frozen condition remains satisfied. The evidence digest and new expiry remain stored. If renewal never arrives, expiry is permissionless.

The interface is an atlas of time zones and a moving meridian—not a setup console.

```bash
genvm-lint contracts/contract.py
python -m pytest -q
```
