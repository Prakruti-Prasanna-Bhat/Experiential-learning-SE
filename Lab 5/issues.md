# Lab 5 – Static Code Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `pickle` import | Security | 1 | Bandit B403 warned that the `pickle` module can introduce security risks. | Removed the unnecessary `pickle` import. |
| Hardcoded password | Security | 6 | Bandit B105 detected the hardcoded password `tower-noc-77` in the source code. | Removed the unused hardcoded password. |
| Unsafe SQL query construction | Security | 11 | Bandit B608 identified a possible SQL injection vulnerability because the query was constructed using string formatting. | Replaced string formatting with a parameterized SQLite query using `?` placeholders. |
| Unsafe pickle deserialization | Security | 43 | Bandit B301 detected the use of `pickle.loads()`, which can be unsafe when processing serialized data. | Removed pickle serialization and directly returned the database query result. |
| Missing module and function docstrings | Code Quality | Multiple | Pylint reported missing documentation for the module and several functions. | Added concise module and function docstrings. |
| Non-Python naming style | Code Quality | Multiple | Functions such as `addTower`, `serviceTower`, and `riskLevel` did not follow snake_case naming conventions. | Renamed them to `add_tower`, `service_tower`, and `risk_level`. |
| Broad exception handling | Code Quality | 20 | The program caught the general `Exception` type. | Replaced it with the more specific `sqlite3.Error`. |
| Use of global variable | Code Quality | 16–17 | `service_count` was managed using the `global` statement. | Removed the global variable and returned the service result from the function instead. |
| Unnecessary `else` after `return` | Code Quality | 36 | Pylint reported an unnecessary `else` block after a return statement. | Removed the `else` and returned the normal risk level directly. |
| Long lines | Style | Multiple | Flake8 reported several lines exceeding the 79-character limit. | Broke long statements into multiple lines. |
| Excess blank lines | Style | 25 | Flake8 reported too many blank lines. | Adjusted blank-line spacing to follow PEP 8. |
| Missing whitespace around operator | Style | 50 | Flake8 reported missing whitespace around `=`. | Added proper spacing around the assignment operator. |
