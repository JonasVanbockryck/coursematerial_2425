def desktop(catalog, components):
    total_cost = 0

    for component in components:
        total_cost += catalog.get(component, 0)  # If a component is not found, we add 0 to the total
        
    return total_cost