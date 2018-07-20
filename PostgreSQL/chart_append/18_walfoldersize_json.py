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
            "text":"WAL Folder Size"
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
                    "labelString": "Size(MB)"
                },
                "ticks": {
                    "beginAtZero": True
                }
            }]
        }
    }
}
