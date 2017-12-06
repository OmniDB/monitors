max_connections = connection.ExecuteScalar('SHOW max_connections')

result = {
    "type": "pie",
    "data": None,
    "options": {
        "responsive": True,
        "title":{
            "display":True,
            "text":"Backends (max_connections: " + str(max_connections) + ")"
        }
    }
}
