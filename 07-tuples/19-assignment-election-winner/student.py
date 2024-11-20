def election_winner(votes):
    if not votes:
        return None

    # Sort votes to bring equal votes together
    sorted_votes = sorted(votes)
    
    # Variables to track the most common candidate and the count
    max_count = 0
    current_count = 1
    winner = sorted_votes[0]

    # Iterate through sorted votes to find the longest run of the same element
    for i in range(1, len(sorted_votes)):
        if sorted_votes[i] == sorted_votes[i - 1]:
            current_count += 1
        else:
            current_count = 1  # Reset count for a new candidate

        # Update winner if the current run is longer than the maximum found
        if current_count > max_count:
            max_count = current_count
            winner = sorted_votes[i]

    return winner