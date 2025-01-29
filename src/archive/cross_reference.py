
def cross_reference_results(results):
    common_links = set.intersection(*[set(res.get("links", [])) for res in results if "links" in res])
    return {
        "common_links": list(common_links),
        "unique_links": {
            result["source"]: list(set(result.get("links", [])) - common_links)
            for result in results
        },
    }
