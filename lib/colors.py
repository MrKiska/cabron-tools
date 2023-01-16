
def rgbToSimilarName(col:list):
    import colorsys
    
    hsv = colorsys.rgb_to_hsv(col[0], col[1], col[2])
    deg = round(hsv[0]*360)
    light = colorsys.rgb_to_hls(col[0], col[1], col[2])[1]/256
    # basic color ranges (8 colors, 22,5 - 45  degrees for each)
    orange = range(22,44)
    yellow = range(45,67)
    lime = range(68,90)
    green = range(91,135)
    turquoise = range(136,157)
    cyan = range(158, 180)
    lblue = range(181,202)
    blue = range(203,247)
    purple = range(248,292)
    pink = range(293,315)

    if light<0.2:
        return "black"
    elif light>0.8:
        return "white"

    # red is from 316 to 22
    if deg in orange: return "orange"
    elif deg in yellow: return "yellow"
    elif deg in lime: return "lime"
    elif deg in green: return "green"
    elif deg in turquoise: return "turquoise"
    elif deg in cyan: return "cyan"
    elif deg in lblue: return "light blue"
    elif deg in blue: return "blue"
    elif deg in purple: return "purple"
    elif deg in pink: return "pink"
    else: return "red"
