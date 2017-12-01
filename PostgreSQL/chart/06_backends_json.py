result = {
    "type": "pie",
    "data": {
        "labels": label,
        "datasets": [
            {
                "data": data,
                "backgroundColor": color,
                "label": "Dataset 1"
            }
        ]
    },
    "options": {
        "responsive": True,
        "title":{
            "display":True,
            "text":"Backends (max_connections: " + str(max_connections) + ")"
        }
    }
}
