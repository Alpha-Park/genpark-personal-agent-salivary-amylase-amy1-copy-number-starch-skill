# Salivary AMY1 Gene Copy Number & Starch Glycemic Tolerance Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `evaluate_amy1_starch_tolerance`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates salivary amylase AMY1 diploid copy number variation (CNV, 2-15 copies), predicts oral starch pre-digestion rate, and tailors glycemic load carbohydrate allowances.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Nutrigenomics & Carbohydrate Metabolism)`

## MCP Tool Specification
### `evaluate_amy1_starch_tolerance`
Parameters:
- `amy1_diploid_copy_number` (int): Genotyped or qPCR-measured AMY1 gene copy count (e.g. 2 to 15)
- `fasting_insulin_uiu_ml` (float): Fasting plasma insulin (uIU/mL)
- `daily_carbohydrate_grams` (float): Current daily carbohydrate intake in grams

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-salivary-amylase-amy1-copy-number-starch-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-salivary-amylase-amy1-copy-number-starch-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
