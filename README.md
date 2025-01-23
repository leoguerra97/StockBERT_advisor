# RL Agent with NLP Integration

This repository contains an innovative Reinforcement Learning (RL) agent enhanced with Natural Language Processing (NLP) capabilities. The agent dynamically adapts its investment strategies based on user-defined risk preferences and market data, leveraging a fine-tuned BERT model for natural language understanding.

## Project Structure

The repository consists of three main Jupyter notebooks:

1. **RL_Agent_NB.ipynb**:  
   The main notebook implementing the RL agent. It combines market data and user-defined risk levels to make decisions (buy, sell, hold) for three assets: Google stock (GOOG), the S&P500 index (GSPC), and Gold (GC=F). It uses a two-layer neural network for Q-learning.

2. **TrainBertModel.ipynb**:  
   Contains the implementation for fine-tuning a BERT model to classify user inputs into risk levels: low, medium, or high. The model is trained on a bespoke dataset of 1,000 labeled phrases reflecting investor preferences.

3. **Exploration_NB.ipynb**:  
   A data exploration notebook providing insights into the datasets used for training the agent and NLP model, including detailed analysis of assets, returns, and market volatility.

## Key Features

- **NLP Integration**: A fine-tuned BERT model interprets natural language inputs to classify investor risk levels, influencing the RL agent's decision-making.
- **Market Interaction**: The agent operates on real market data (2016-2022), interacting with three distinct assets.
- **Risk-Adaptive Strategies**: Risk tolerance is integrated into the agent’s reward function and action selection, adapting its trading behavior dynamically.
- **Sharpe Ratio**: Experiments include the impact of incorporating Sharpe ratio estimates for balancing risk-adjusted returns.

## Future Directions

- Enhance the neural network architecture for better learning efficiency.
- Expand the dataset and incorporate additional user preferences (e.g., time horizons).
- Conduct new experiments to analyze the agent's adaptive behavior when user inputs change mid-simulation.

## References

- [BERT Fine-Tuning](https://github.com/theartificialguy/NLP-with-Deep-Learning/tree/master/BERT)
- [Q-Trader Framework](https://github.com/edwardhdlu/q-trader)

For more details, refer to the project documentation and notebooks.
