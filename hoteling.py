# %%

# Reference netlogo model: https://www.netlogoweb.org/launch#https://www.netlogoweb.org/assets/modelslib/Sample%20Models/Social%20Science/Economics/Hotelling's%20Law.nlogo
# i = store
# color of the square = min(distance_i + price_i)

"""
For each timestep:
1. Compute metrics (revenue / length) per store
1. Compute the color of the squares
2. For each store, compute candidate actions (action: price up / price down / move up / move down)
3. For each store, move to the candidate actions if marginally profitable
   - Movement is on the (price, position) coordinates

## Actions

- Price Up: current_price * (1 + change_price_param)
- Price down: current_price * (1 - change_price_param)
- Move up: position + 1
- Move down: position - 1
"""

# %%
# TODO sort out initialization logic
from cadCAD_tools.execution import easy_run
from random import random

Store = int  # Store 1, Store 2, Store 3
Position = int # or Square
Price = float

N_STORES = 3
N_SQUARES = 15

INITIAL_POSITIONS: dict[Store, Position] = {
    i: i for i in range(N_STORES)
}

INITIAL_PRICES: dict[Store, Price] = {
    i: random() for i in range(N_STORES)
}

# [1, 2, 3, o, o, o, o, o, o, o]


state_variables = {
    ###
    # Metrics

    ## Store metrics
    'areas_per_store': {i: -1 for i in range(N_STORES)},
    'revenues_per_store': {i: -1 for i in range(N_STORES)},

    ## Square metrics
    'colors_per_square': {i: -1 for i in range(N_SQUARES)},
    # eg. what is the store that dominates each position?

    # Fundamental Variables
    'prices_per_store': INITIAL_PRICES,
    'positions_per_store': INITIAL_POSITIONS,
}


params = {
    'price_sensitivity': [0.5]  # Related to how much the price changes each turn
}


def s_areas(params, _2, _3, state, _4):
    return ('areas_per_store', None)


def s_revenues(params, _2, _3, state, _4):
    """
    Revenue = (# of dominated squares) * store_price
    """
    return ('revenues_per_store', None)


def s_colors(params, _2, _3, state, _4):
    return ('colors_per_store', None)


def s_positions(params, _2, _3, state, _4):
    return ('positions_per_store', None)


def s_prices(params, _2, _3, state, _4):
    return ('prices_per_store', None)


partial_state_update_blocks = [
    {
        'label': 'Compute Metrics',
        'policies': {

        },
        'variables': {
            'areas_per_store': s_areas,
            'revenues_per_store': s_revenues,
            'colors_per_store': s_colors
        }
    },
    {
        'label': 'Perform Store Actions',
        'policies': {

        },
        'variables': {
            'positions_per_store': s_positions,
            'prices_per_store': s_prices,
        }
    }
]

# %%


df = easy_run(state_variables,
              params,
              partial_state_update_blocks,
              N_timesteps=10,
              N_samples=1)

# %%
