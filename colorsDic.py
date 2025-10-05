class Colors:
    def __init__(self):        
        self.color_val = {
            "black":0,"brown":1,"red":2,"orange":3,"yellow":4,
            "green":5,"blue":6,"purple":7,"gray":8,"white":9
        }

        self.color_coe = {
            "silver":-2,"gold":-1,"black":0,"brown":1,"red":2,
            "orange":3,"yellow":4,"green":5,"blue":6,"purple":7
        }

        self.color_tol = {
            "silver":10,"gold":5,"brown":1,"red":2,"green":0.5,
            "blue":0.25,"purple":0.1,"gray":0.05
        }
        
        self.color_ppm ={"brown":100,"red":50,"orange":15,"yellow":25}
        
        self.color_hex = {
            "black": "#302f35",
            "brown": "#795933",
            "red": "#b94648",
            "orange": "#fc8e4f",
            "yellow": "#ecdf6b",
            "green": "#5f8840",
            "blue": "#3b98d6",
            "purple": "#7a38d1",
            "gray": "#6D757C",
            "white": "#eadeda",
            "gold": "#fccc54",
            "silver": "#c0c0c0"
        }