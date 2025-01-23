import pandas as pd
import numpy as np
from itertools import product
import random

# Seed for reproducibility
random.seed(42)
np.random.seed(42)


def create_df():
    data = []

    sample_phrases = [
        ("Oh, I need money quick and am willing to risk what I have", 2, 0),
        ("I am using my life's saving for a stable retirement", 0, 2),
        ("I've got some extra cash I'd like to grow over the next few years", 1, 1),
        ("I want the safest place to put my emergency fund", 0, 0),
        ("It's time to play big and bet on fast-growing companies", 2, 1),
        ("I'm young and can afford to wait for my investments to flourish", 1, 2),
        ("I prefer investments that are a bit adventurous but not too wild", 1, 1),
        ("Let's secure a fortune for my children's future", 0, 2),
        ("I'm all in for the next big thing, regardless of the risk", 2, 0),
        ("I aim for steady income in my post-retirement years", 0, 2),

        # professional sample phrases with their targets
        ("Seeking a diversified portfolio to mitigate volatility over the next decade", 0, 2),
        ("Interested in capitalizing on emerging markets with a high-risk, high-reward profile", 2, 1),
        ("Pursuing tax-efficient investments with minimal risk exposure for immediate needs", 0, 0),
        ("Exploring opportunities in blue-chip stocks for sustainable, long-term wealth accumulation", 1, 2),
        ("Evaluating fixed-income securities to preserve capital and ensure steady income", 0, 2),
        ("Considering aggressive growth funds to maximize returns in a five-year horizon", 2, 1),
        ("Assessing risk-adjusted returns of tech startups for potential high-growth investments", 2, 1),
        ("Looking to invest in environmentally sustainable projects with medium to long-term commitment", 1, 2),
        ("Exploring short-term, high-yield bonds for better liquidity and return profile", 2, 0),
        ("Seeking to enhance portfolio yield through strategic investments in real estate investment trusts (REITs)", 1, 1),
        ("Contemplating conservative investment strategies to protect retirement savings", 0, 2),
        ("Aiming to leverage quantitative trading strategies for short-term market inefficiencies", 2, 0),
        ("Planning to allocate assets into value stocks with strong fundamentals for medium-term holding", 1, 1),
        ("Investigating global mutual funds for diversified exposure and risk management", 1, 2),
        ("Focusing on sovereign bonds to safeguard principal with a low-risk appetite", 0, 1),
        ("Maximizing portfolio diversification to spread risk across various asset classes.", 0, 1),
        ("Leveraging short-term market trends for accelerated capital growth.", 2,0),
        ("Implementing a conservative asset allocation strategy for retirement planning.", 0, 2),
        ("Identifying high-growth potential startups for strategic venture capital investment.", 2, 1),
        ("Utilizing algorithmic trading strategies to exploit market volatility.", 2, 1),
        ("Investing in government bonds to ensure a stable and predictable income stream.", 0, 1),
        ("Analyzing long-term economic cycles to guide strategic asset allocation.", 0, 2),
        ("Adopting a contrarian investment approach to capitalize on market corrections.", 2, 0),
        ("Exploring international markets for global diversification and risk management.", 0,1),
        ("Prioritizing ESG investments to align with sustainable and ethical values." , 1, 2),
        #Non-Professional Phrases:
        ("I wanna make quick cash from whatever's trending right now.", 2, 0),
        ("Putting some money aside for a rainy day, but hoping it grows a bit too.", 1, 1),
        ("Dreaming of hitting it big with the next tech unicorn.", 2, 1),
        ("Just looking for a safe place to park my savings without losing sleep.", 0, 2),
        ("Trying to get a piece of the action in hot new industries, YOLO.", 2, 0),
        ("Want to grow my wedding fund without too much risk.", 0, 1),
        ("Eyeing retirement with a mix of stocks and bonds to keep things steady.", 1, 2),
        ("Hoping to fund my world tour with some savvy investments.", 1, 1),
        ("Looking for a golden ticket in alternative investments, like crypto or art.", 2, 1),
        ("Saving up for a down payment on a house with some medium-term investments.", 0, 1),
    ]

    # Incorporate these new phrases into the data
    for i, (phrase, risk_level, time_horizon) in enumerate(sample_phrases, start=1):
        data.append({
            "ID": i,
            "risk_level": risk_level,
            "time_horizon": time_horizon,
            "phrase": phrase
        })

    #### MIX AND MATCH PART

    # Define the components
    phrase_beginnings = [
        "Exploring opportunities for",
        "In pursuit of",
        "Focused on achieving",
        "Interested in securing",
        "Aiming to capitalize on",
        "Strategically investing in",
        "Seeking to enhance",
        "Committed to identifying",
        "Eager to explore",
        "Looking to diversify with",
        "I'm looking for",
        "I want",
        "I prefer",
        "I'm interested in",
        "I need",
        "Prioritizing investments in",
        "Geared towards maximizing",
        "Conservatively approaching",
        "Aggressively targeting",
        "Dedicated to finding",
        "Methodically planning for",
        "Optimistically engaging in",
        "Cautiously exploring",
        "Broadening horizons with",
        "Actively seeking out"
    ]

    risk_level_endings = [
        ("safe investment options", 0),
        ("quick profits", 2),
        ("in high-risk, high-reward investments", 2),
        ("low-risk investments with predictable returns", 0),
        ("balanced risk and steady growth", 1),
        ("high-growth ventures with potential for significant returns", 2),
        ("stable, low-volatility assets for consistent gains", 0),
        ("moderately aggressive investments for balanced growth", 1),
        ("high-growth ventures with potential for significant returns", 2),
        ("stable, low-volatility assets for consistent gains", 0),
        ("moderately aggressive investments for balanced growth", 1)
    ]

    time_horizon_endings = [
        ("in the short term, aiming for immediate profits.", 0),
        ("over the long haul, focusing on future security.", 2),
        ("within a medium timeframe, balancing patience and progress.", 1),
        ("and am looking at the medium term", 1),
        ("regardless of time horizon", 1),
        ("in the short term", 0),
        ("over the long haul", 2),
        ("within a medium timeframe", 1),
        ("can invest for medium to long term", 2),
    ]

    # Generate combinations
    combinations = list(product(phrase_beginnings, risk_level_endings, time_horizon_endings))

    # Select random combinations to generate phrases
    selected_combinations = random.sample(combinations, 1000)

    for i, (beginning, (risk, risk_desc), (time, time_desc)) in enumerate(selected_combinations, start=len(data) + 1):
        phrase = f"{beginning} {risk} {time}"
        data.append({
            "ID": i,
            "risk_level": risk_desc,
            "time_horizon": time_desc,
            "phrase": phrase
        })

    # Create df and save to CSV
    df = pd.DataFrame(data)
    df.to_csv("sentiment_dataset.csv", index=False)


if __name__ == "__main__":
    create_df()