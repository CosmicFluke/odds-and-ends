def num_routes(dim: int, x: int=0, y: int=0, routes: dict=None) -> int:
    if routes == None:
        routes = {(dim, dim): 1}
    if (x, y) in routes:
        return routes[(x,y)]
    x_routes = (x < dim) and num_routes(dim, x + 1, y, routes)
    y_routes = (y < dim) and num_routes(dim, x, y + 1, routes)
    routes[(x, y)] = x_routes + y_routes
    return routes[(x, y)]


print(num_routes(20))