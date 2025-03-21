import json

def save_results_to_json(docs, results):
    """Sauvegarde les résultats d'analyse dans un fichier JSON."""
    data = {"documents": []}
    for i, (doc, result) in enumerate(zip(docs, results)):
        data["documents"].append({
            "file_name": f"document_{i+1}",
            "content": doc,
            "analysis": result
        })
    
    with open("extraction_results.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
