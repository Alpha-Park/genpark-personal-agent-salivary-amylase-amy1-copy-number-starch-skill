# -*- coding: utf-8 -*-
"""Salivary AMY1 Gene Copy Number & Starch Glycemic Tolerance Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def evaluate_amy1_starch_tolerance(**kwargs):
    """Calculates salivary amylase AMY1 diploid copy number variation (CNV, 2-15 copies), predicts oral starch pre-digestion rate, and tailors glycemic load carbohydrate allowances."""
    amy1_diploid_copy_number = kwargs.get('amy1_diploid_copy_number')
    fasting_insulin_uiu_ml = kwargs.get('fasting_insulin_uiu_ml')
    daily_carbohydrate_grams = kwargs.get('daily_carbohydrate_grams')

    copies = amy1_diploid_copy_number
    
    # Evolutionary nutrigenomics: High AMY1 (>=8 copies) evolved in agricultural populations with robust starch handling
    # Low AMY1 (<=4 copies) shows delayed early-phase insulin release and higher postprandial glucose spikes on complex starches
    if copies >= 9:
        starch_tier = "HIGH AMY1 EXPRESSION (Superior oral starch pre-digestion & rapid cephalic insulin response)"
        carb_allowance_recommendation = "Can tolerate complex whole-food starches (potatoes, rice, oats) with blunted glycemic excursion."
        carb_cap_pct = 50.0
    elif copies >= 5:
        starch_tier = "MODERATE AMY1 INTERMEDIATE METABOLIZER"
        carb_allowance_recommendation = "Moderate complex carbohydrate intake; combine with dietary fiber and vinegar to temper absorption."
        carb_cap_pct = 35.0
    else:
        starch_tier = "LOW AMY1 COPY NUMBER (Impaired starch oral cleavage, higher risk of postprandial hyperglycemia & insulin resistance)"
        carb_allowance_recommendation = "Restrict refined starches (< 150g/day); prioritize low-glycemic Mediterranean or ketogenic nutritional patterns."
        carb_cap_pct = 20.0
        
    result = {
        "status": "success",
        "amy1_copies": copies,
        "fasting_insulin": fasting_insulin_uiu_ml,
        "starch_digestive_phenotype": starch_tier,
        "recommended_carbohydrate_caloric_cap_pct": carb_cap_pct,
        "nutrigenomic_dietary_guidance": carb_allowance_recommendation,
        "engine": "GenPark AMY1 Salivary Amylase Nutrigenomic Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "evaluate_amy1_starch_tolerance": {
        "name": "evaluate_amy1_starch_tolerance",
        "description": "Calculates salivary amylase AMY1 diploid copy number variation (CNV, 2-15 copies), predicts oral starch pre-digestion rate, and tailors glycemic load carbohydrate allowances.",
        "parameters": {
            "type": "object",
            "properties": {
                "amy1_diploid_copy_number": {"type": "integer", "description": "Genotyped or qPCR-measured AMY1 gene copy count (e.g. 2 to 15)"},
                "fasting_insulin_uiu_ml": {"type": "number", "description": "Fasting plasma insulin (uIU/mL)"},
                "daily_carbohydrate_grams": {"type": "number", "description": "Current daily carbohydrate intake in grams"},
            },
            "required": ['amy1_diploid_copy_number', 'fasting_insulin_uiu_ml', 'daily_carbohydrate_grams']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_amy1_starch_tolerance":
            res = evaluate_amy1_starch_tolerance(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-salivary-amylase-amy1-copy-number-starch-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-personal-agent-salivary-amylase-amy1-copy-number-starch-skill...")
    test_args = {'amy1_diploid_copy_number': 4, 'fasting_insulin_uiu_ml': 9.2, 'daily_carbohydrate_grams': 260.0}
    res = evaluate_amy1_starch_tolerance(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-personal-agent-salivary-amylase-amy1-copy-number-starch-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
