import re


def apply_rules(df, rules):
    results = []

    for rule in rules:
        col = rule["column"]
        name = rule["name"]
        rtype = rule["type"]

        if rtype == "not_null":
            failures = df[df[col].isnull()]

        elif rtype == "unique":
            failures = df[df[col].duplicated()]

        elif rtype == "range":
            failures = df[(df[col] < rule["min"]) | (df[col] > rule["max"])]

        elif rtype == "regex":
            pattern = re.compile(rule["pattern"])
            failures = df[~df[col].astype(str).str.match(pattern)]

        elif rtype == "duplicate":
            failures = df[df.duplicated(subset=[col])]

        results.append({
            "rule": name,
            "failed_rows": len(failures),
            "status": "PASS" if len(failures) == 0 else "FAIL"
        })

    return results
