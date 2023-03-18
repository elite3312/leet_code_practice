# Leet Code Practice
# Illustrations
## 48 Rotate Image
<details>

Start from the outer layer, rotate each layer, until you reach the core.  
![alt](./assets/48.jpg)
</details>

## 1472 Design Browser History
<details>

```ps
╒════════════════════╤══════════════╤══════════════╕
│ operation          │ output       │ expected     │
╞════════════════════╪══════════════╪══════════════╡
│ init               │ None         │ None         │
├────────────────────┼──────────────┼──────────────┤
│ visit google.com   │ None         │ None         │
├────────────────────┼──────────────┼──────────────┤
│ visit facebook.com │ None         │ None         │
├────────────────────┼──────────────┼──────────────┤
│ visit youtube.com  │ None         │ None         │
├────────────────────┼──────────────┼──────────────┤
│ back 1             │ facebook.com │ facebook.com │
├────────────────────┼──────────────┼──────────────┤
│ back 1             │ google.com   │ google.com   │
├────────────────────┼──────────────┼──────────────┤
│ forward 1          │ facebook.com │ facebook.com │
├────────────────────┼──────────────┼──────────────┤
│ visit linkedin.com │ None         │ None         │
├────────────────────┼──────────────┼──────────────┤
│ forward 2          │ linkedin.com │ linkedin.com │
├────────────────────┼──────────────┼──────────────┤
│ back 2             │ google.com   │ google.com   │
├────────────────────┼──────────────┼──────────────┤
│ back 7             │ leetcode.com │ leetcode.com │
╘════════════════════╧══════════════╧══════════════╛
```
</details>

