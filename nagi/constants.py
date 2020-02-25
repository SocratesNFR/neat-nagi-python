# SNN
TIME_STEP_IN_MSEC = 0.1
MEMBRANE_POTENTIAL_THRESHOLD = 30.0
THRESHOLD_THETA_INCREMENT_RATE = 0.1
THRESHOLD_THETA_DECAY_RATE = 0.3  # (0, 1), lower value means slower decay
MAX_THRESHOLD_THETA = 2.0

# Izikhevich parameters
REGULAR_SPIKING_PARAMS = {'a': 0.02, 'b': 0.20, 'c': -65.0, 'd': 8.00}
INTRINSICALLY_BURSTING_PARAMS = {'a': 0.02, 'b': 0.20, 'c': -55.0, 'd': 4.00}
CHATTERING_PARAMS = {'a': 0.02, 'b': 0.20, 'c': -50.0, 'd': 2.00}
FAST_SPIKING_PARAMS = {'a': 0.10, 'b': 0.20, 'c': -65.0, 'd': 2.00}
THALAMO_CORTICAL_PARAMS = {'a': 0.02, 'b': 0.25, 'c': -65.0, 'd': 0.05}
RESONATOR_PARAMS = {'a': 0.10, 'b': 0.25, 'c': -65.0, 'd': 2.00}
LOW_THRESHOLD_SPIKING_PARAMS = {'a': 0.02, 'b': 0.25, 'c': -65.0, 'd': 2.00}

# STDP
ASYMMETRIC_HEBBIAN_PARAMS = {'a_plus': 1, 'a_minus': 1, 'tau_plus': 10, 'tau_minus': 10}
SYMMETRIC_HEBBIAN_PARAMS = {'a_plus': 10.6, 'a_minus': 44.0, 'std_plus': 3.5, 'std_minus': 20}
NEURON_WEIGHT_BUDGET = 30.0

# SYMMETRIC_ANTI_HEBBIAN_PARAMS = {'a': 20, 'mean': 0, 'std': 10}
STDP_PARAMS = {'sigma': 0.1, 'w_max': 1, 'w_min': 0}
STDP_LEARNING_WINDOW = 40.0

# NEAT
ENABLE_MUTATE_RATE = 0.01
BIAS_MUTATE_RATE = 0.7
ADD_NODE_MUTATE_RATE = 0.3
ADD_CONNECTION_MUTATE_RATE = 0.3
INHIBITORY_MUTATE_RATE = 0.05
LEARNING_RULE_MUTATE_RATE = 0.05
STDP_PARAMETERS_MUTATE_RATE = 0.05
STDP_PARAMETERS_REINIT_RATE = 0.01
PREDETERMINED_DISABLED_RATE = 0.75
INITIAL_CONNECTION_RATE = 0.5
LEARNING_RULE_DISTRIBUTION_BIAS = 0.7  # [0.5, 1], lower number means more equal distribution
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
SYMMETRIC_A_PLUS_INIT_RANGE = (0.0, 10.6)
SYMMETRIC_A_MINUS_INIT_RANGE = (0.0, 44)
SYMMETRIC_STD_INIT_RANGE = (3.5, 20.0)
ASYMMETRIC_A_INIT_RANGE = (0.0, 1.0)
ASYMMETRIC_TAU_INIT_RANGE = (0.0, 10.0)

# STDP parameter mutate scales
SYMMETRIC_A_PLUS_MUTATE_SCALE = 0.2 * (SYMMETRIC_A_PLUS_INIT_RANGE[1] - SYMMETRIC_A_PLUS_INIT_RANGE[0])
SYMMETRIC_A_MINUS_MUTATE_SCALE = 0.2 * (SYMMETRIC_A_MINUS_INIT_RANGE[1] - SYMMETRIC_A_MINUS_INIT_RANGE[0])
SYMMETRIC_STD_MUTATE_SCALE = 0.2 * (SYMMETRIC_STD_INIT_RANGE[1] - SYMMETRIC_STD_INIT_RANGE[0])
ASYMMETRIC_A_MUTATE_SCALE = 0.2 * (ASYMMETRIC_A_INIT_RANGE[1] - ASYMMETRIC_A_INIT_RANGE[0])
ASYMMETRIC_TAU_MUTATE_SCALE = 0.2 * (ASYMMETRIC_TAU_INIT_RANGE[1] - ASYMMETRIC_TAU_INIT_RANGE[0])

# Simulation
MAX_HEALTH_POINTS = 100
FLIP_POINT = int(MAX_HEALTH_POINTS/10)
ACTUATOR_WINDOW = int(0.5 / (TIME_STEP_IN_MSEC / 1000))
DAMAGE_FROM_EATING_CORRECT_FOOD = 1
DAMAGE_FROM_EATING_WRONG_FOOD = 4
DAMAGE_FROM_AVOIDING_FOOD = 2
INPUT_SPIKE_VOLTAGE = 1

# Visualization colors
RED = '#ff7c73'
BLUE = '#74a0f7'
GREEN = '#84db81'
