def norm_vector (coordinates):
    norm = 0
    try:
        for coordinate in coordinates:
            float(coordinate)
            norm += coordinate**2
    except:
        raise ValueError('Uncorrect dimensions')
    else:
        return norm**0.5
