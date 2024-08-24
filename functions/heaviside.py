def heaviside(x,center=0,lim=0.5): 
    match result := x - center:
        case _ if result > 0:
            return 1.0
        case _ if result < 0:
            return 0.0
        case _:
            return lim

