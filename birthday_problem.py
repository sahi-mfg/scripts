"""
    If there are n people in a room, How large does n need to be for at least 
    50% chance of alteast two people sharing the same birthday?
"""

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def birthday_problem(n: int) -> float:
    """
    Compute the probability of atleast two people sharing the same birthday in a room of n people

    Args: 
        n : int : Number of people in the room
    
    Returns:
        float : Probability of atleast two people sharing the same birthday
    """
    # Total number of days in a year
    days: int  = 365
    # Probability of atleast two people sharing the same birthday
    probability: float = 1.0
    for i in range(n):
        probability *= (days - i) / days
    return 1 - probability


if __name__ == '__main__':
    for i in range(1, 100):
        probability = birthday_problem(i)
        logging.info(f"Number of people: {i}, Probability: {probability * 100:.2f}%")
        if probability >= 0.5:
            break
    logging.info(f"Number of people needed for atleast 50% chance of sharing the same birthday: {i}")