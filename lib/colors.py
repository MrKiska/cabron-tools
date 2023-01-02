
def rgbToSimilarName(col:list):
    import colorsys
    
    colorsys.rgb_to_hsv(col[0]/256, col[1]/256, col[2]/256)
