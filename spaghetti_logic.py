def apply_tax(value, rate=1.15):
    return value * rate


def format_result(value):
    return f"Total: {value:.2f}"


def log_results(results, filepath="log.txt"):
    with open(filepath, "a") as f:
        f.write(str(results) + "\n")


def process_data(data):
    results = []
    for item in data:
        taxed = apply_tax(item)
        print(format_result(taxed))
        results.append(taxed)
    log_results(results)
    return results
