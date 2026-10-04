# Regular Expressions — Quick Reference

Use Python raw strings with `r"..."` when writing regular expressions:

| Regex         | Meaning                                                       | Example            |
| ------------- | ------------------------------------------------------------- | ------------------ |
| `r"@"`        | Matches a literal `@` character                               | `user@example.com` |
| `r"[a-z]"`    | Matches **one** lowercase letter from `a` to `z`              | `a`, `m`, `z`      |
| `r"[a-z]{n}"` | Matches exactly **n consecutive** lowercase letters           | `[a-z]{3}` → `abc` |
| `r"[a-z]+"`   | `+` → **1 or more** occurrences                               | `abc`, `hello`     |
| `r"[a-z]*"`   | `*` → **0 or more** occurrences                               | `""`, `abc`        |
| `r"[a-z]?"`   | `?` → **0 or 1** occurrence                                   | `""`, `a`          |
| `r"."`        | `.` → wildcard that matches **one character**                 | `a`, `7`, `@`      |
| `r"\."`       | `\.` → matches a **literal dot `.`**                          | `.`                |
| `r"\w"`       | Matches one **word character** (letters, digits, or `_`)      | `a`, `7`, `_`      |
| `r"sth$"`     | `$` → requires `sth` to be at the **end** of the string       | `hello sth`        |
| `r"^sth"`     | `^` → requires `sth` to be at the **beginning** of the string | `sth hello`        |

## Quantifiers

Quantifiers control **how many times** a preceding pattern can occur:

| Quantifier | Meaning                 |
| ---------- | ----------------------- |
| `{n}`      | Exactly `n` occurrences |
| `+`        | 1 or more occurrences   |
| `*`        | 0 or more occurrences   |
| `?`        | 0 or 1 occurrence       |

## Anchors

| Anchor | Meaning                 |
| ------ | ----------------------- |
| `^`    | Beginning of the string |
| `$`    | End of the string       |

For example:

```python
r"^sth"
```

matches strings that **start with** `sth`.

```python
r"sth$"
```

matches strings that **end with** `sth`.

```python
r"^sth$"
```

matches a string that is **exactly** `sth`.
