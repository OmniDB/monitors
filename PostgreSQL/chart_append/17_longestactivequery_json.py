result = {
    "type": "line",
    "data": None,
    "options": {
        "legend": {
            "display": False
        },
        "responsive": True,
        "title":{
            "display":True,
            "text":"Longest Active Query"
        },
        "tooltips": {
            "mode": "index",
            "intersect": False
        },
        "hover": {
            "mode": "nearest",
            "intersect": True
        },
        "scales": {
            "xAxes": [{
                "display": True,
                "scaleLabel": {
                    "display": True,
                    "labelString": "Time"
                }
            }],
            "yAxes": [{
                "display": True,
                "scaleLabel": {
                    "display": True,
                    "labelString": "Duration(s)"
                },
                "ticks": {
                    "beginAtZero": True
                }
            }]
        }
    }
}
