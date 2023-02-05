
def hex_to_rgb(hex_code: str) -> tuple:

    """
        The function translates a color's hex-code 
        into rgb-code.
     """
    
    hex_number = hex_code.replace("#", "")
    
    return tuple(int(hex_number[i:i+2], 16) for i in (0, 2, 4))


print(hex_to_rgb("#FF0000"))
