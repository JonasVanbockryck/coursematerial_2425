def orbit_chain(orbits, start):
    chain = [start]  # Start the chain with the initial body
    while chain[-1] in orbits:  # Continue if the last body in the chain orbits something
        next_body = orbits[chain[-1]]  # Find what it orbits
        chain.append(next_body)  # Add it to the chain
    return chain