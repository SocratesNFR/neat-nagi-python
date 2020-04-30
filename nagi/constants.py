# SNN
TIME_STEP_IN_MSEC = 0.1
THRESHOLD_THETA_INCREMENT_RATE = 0.2
THRESHOLD_THETA_DECAY_RATE = 0.01 * TIME_STEP_IN_MSEC  # (0, 1), lower value means slower decay
MAX_THRESHOLD_THETA = 20.0
LIF_MEMBRANE_POTENTIAL_THRESHOLD = 1.0
LIF_SPIKE_VOLTAGE = 1.0
IZ_MEMBRANE_POTENTIAL_THRESHOLD = 30.0
IZ_SPIKE_VOLTAGE = 100

# Izikhevich parameters
REGULAR_SPIKING_PARAMS = {'a': 0.02, 'b': 0.20, 'c': -65.0, 'd': 8.00}
INTRINSICALLY_BURSTING_PARAMS = {'a': 0.02, 'b': 0.20, 'c': -55.0, 'd': 4.00}
CHATTERING_PARAMS = {'a': 0.02, 'b': 0.20, 'c': -50.0, 'd': 2.00}
FAST_SPIKING_PARAMS = {'a': 0.10, 'b': 0.20, 'c': -65.0, 'd': 2.00}
THALAMO_CORTICAL_PARAMS = {'a': 0.02, 'b': 0.25, 'c': -65.0, 'd': 0.05}
RESONATOR_PARAMS = {'a': 0.10, 'b': 0.25, 'c': -65.0, 'd': 2.00}
LOW_THRESHOLD_SPIKING_PARAMS = {'a': 0.02, 'b': 0.25, 'c': -65.0, 'd': 2.00}

# LIF parameters
LIF_NEURON_CAPACITANCE = 10
LIF_NEURON_RESISTANCE = 1
LIF_REFRACTORY_PERIOD = 0  # in ms
LIF_RESTING_MEMBRANE_POTENTIAL = 0
LIF_MEMBRANE_DECAY_RATE = 0.01 * TIME_STEP_IN_MSEC
LIF_TAU = LIF_NEURON_CAPACITANCE * LIF_NEURON_RESISTANCE
LIF_BIAS = 1.0e-3

# STDP
ASYMMETRIC_HEBBIAN_PARAMS = {'a_plus': 1, 'a_minus': 1, 'tau_plus': 10, 'tau_minus': 10}
SYMMETRIC_HEBBIAN_PARAMS = {'a_plus': 10.6, 'a_minus': 44.0, 'std_plus': 3.5, 'std_minus': 20}
NEURON_WEIGHT_BUDGET = 5.0
STDP_PARAMS = {'sigma': 1.0, 'w_max': 1.0, 'w_min': 0.0}
STDP_LEARNING_WINDOW = 40.0

# NEAT
ENABLE_MUTATE_RATE = 0.01
ADD_NODE_MUTATE_RATE = 0.1
ADD_CONNECTION_MUTATE_RATE = 0.1
INHIBITORY_MUTATE_RATE = 0.05
LEARNING_RULE_MUTATE_RATE = 0.05
STDP_PARAMETERS_MUTATE_RATE = 0.05
STDP_PARAMETERS_REINIT_RATE = 0.01
PREDETERMINED_DISABLED_RATE = 0.75
INITIAL_CONNECTION_RATE = 0.5
BIAS_MUTATE_RATE = 0.1
BIAS_INIT_PROBABILITIES = [0.2, 0.8]  # Distribution of neurons initiated with/without bias, [True, False]

LEARNING_RULE_DISTRIBUTION_BIAS = 0.7  # [0.5, 1], lower value means more equal distribution.
INHIBITORY_PROBABILITIES = [(1 - LEARNING_RULE_DISTRIBUTION_BIAS) / 2, LEARNING_RULE_DISTRIBUTION_BIAS / 2,
                            (1 - LEARNING_RULE_DISTRIBUTION_BIAS) / 2, LEARNING_RULE_DISTRIBUTION_BIAS / 2]
EXCITATORY_PROBABILITIES = [LEARNING_RULE_DISTRIBUTION_BIAS / 2, (1 - LEARNING_RULE_DISTRIBUTION_BIAS) / 2,
                            LEARNING_RULE_DISTRIBUTION_BIAS / 2, (1 - LEARNING_RULE_DISTRIBUTION_BIAS) / 2]

CONNECTIONS_DISJOINT_COEFFICIENT = 1
CONNECTIONS_EXCESS_COEFFICIENT = 1

SPECIES_COMPATIBILITY_THRESHOLD = 1
MATING_CUTTOFF_PERCENTAGE = 0.2
ELITISM = 2
SPECIES_PROTECTION_LIMIT = 30
SPECIES_STAGNATION_LIMIT = 20

# STDP parameter init ranges
SYMMETRIC_A_PLUS_INIT_RANGE = (1.0, 10.6)
SYMMETRIC_A_MINUS_INIT_RANGE = (1.0, 44)
SYMMETRIC_STD_PLUS_INIT_RANGE = (3.5, 10.0)
SYMMETRIC_STD_MINUS_INIT_RANGE = (13.5, 20.0)
ASYMMETRIC_A_INIT_RANGE = (0.1, 1.0)
ASYMMETRIC_TAU_INIT_RANGE = (1.0, 10.0)

# STDP parameter mutate scales
SYMMETRIC_A_PLUS_MUTATE_SCALE = 0.2 * (SYMMETRIC_A_PLUS_INIT_RANGE[1] - SYMMETRIC_A_PLUS_INIT_RANGE[0])
SYMMETRIC_A_MINUS_MUTATE_SCALE = 0.2 * (SYMMETRIC_A_MINUS_INIT_RANGE[1] - SYMMETRIC_A_MINUS_INIT_RANGE[0])
SYMMETRIC_STD_PLUS_MUTATE_SCALE = 0.2 * (SYMMETRIC_STD_PLUS_INIT_RANGE[1] - SYMMETRIC_STD_PLUS_INIT_RANGE[0])
SYMMETRIC_STD_MINUS_MUTATE_SCALE = 0.2 * (SYMMETRIC_STD_MINUS_INIT_RANGE[1] - SYMMETRIC_STD_MINUS_INIT_RANGE[0])
ASYMMETRIC_A_MUTATE_SCALE = 0.2 * (ASYMMETRIC_A_INIT_RANGE[1] - ASYMMETRIC_A_INIT_RANGE[0])
ASYMMETRIC_TAU_MUTATE_SCALE = 0.2 * (ASYMMETRIC_TAU_INIT_RANGE[1] - ASYMMETRIC_TAU_INIT_RANGE[0])

# Simulation
NUM_TIME_STEPS = int(1.0 / (TIME_STEP_IN_MSEC / 1000))
ACTUATOR_WINDOW = int(0.25 / (TIME_STEP_IN_MSEC / 1000))
# 1D
FOOD_SAMPLES_PER_SIMULATION = 40
MAX_HEALTH_POINTS_1D = FOOD_SAMPLES_PER_SIMULATION * NUM_TIME_STEPS
FLIP_POINT_1D = int(FOOD_SAMPLES_PER_SIMULATION / 10)
# 2D
INPUT_SAMPLES_PER_SIMULATION = 32
MAX_HEALTH_POINTS_2D = INPUT_SAMPLES_PER_SIMULATION * NUM_TIME_STEPS
FLIP_POINT_2D = 4

DAMAGE_FROM_EATING_CORRECT_FOOD = 1
DAMAGE_FROM_EATING_WRONG_FOOD = 4
DAMAGE_FROM_AVOIDING_FOOD = 2
DAMAGE_FROM_CORRECT_ACTION = 1
DAMAGE_FROM_INCORRECT_ACTION = 2
DAMAGE_PENALTY_FOR_HIDDEN_NEURONS = 1.00

# Visualization colors
RED = '#ff7c73'
BLUE = '#74a0f7'
GREEN = '#84db81'
PINK = '#ff99dd'
CYAN = '#99f1ff'

# Printing colors
PRINT_GREEN = '\033[92m'
PRINT_RED = '\033[91m'
