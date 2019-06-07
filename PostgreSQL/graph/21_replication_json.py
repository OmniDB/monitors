from random import randint

result = {
    "container": None,
    "boxSelectionEnabled": False,
    "autounselectify": True,
    "layout": {
        "name": "spread",
        "minDist": 1000
    },
    "style": [
        {
            "selector": "node",
            "style": {
                "content": "data(label)",
                "text-opacity": 1,
                "text-valign": "top",
                "text-halign": "right",
                "text-wrap": "wrap",
                "color": "gray",
                "text-rotation": "autorotate",
                "font-size": 12
            }
        },
        {
            "selector": "node.node_local",
            "style": {
                "background-color": "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")",
                "shape": 'square'
            }
        },
        {
            "selector": "node.node_remote",
            "style": {
                "background-color": "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")",
            }
        },
        {
            "selector": "edge",
            "style": {
                "curve-style": "bezier",
                "control-point-step-size": 40,
                "target-arrow-shape": "triangle",
                "text-opacity": 1,
                "width": 2,
                "control-point-distances": 50,
                "content": "data(label)",
                "text-wrap": "wrap",
                "line-style": "solid",
                "width": 1,
                "color": "gray",
                "text-outline-color": 'gray',
                "text-outline-width": 0
            }
        }
    ],
    "elements": {
        "nodes": None,
        "edges": None
    }
}
