from typing import List, Dict
from nagi.constants import MEMBRANE_POTENTIAL_THRESHOLD, ASYMMETRIC_HEBBIAN_PARAMS, STDP_PARAMS, STDP_LEARNING_WINDOW
from nagi.stdp import *


class SpikingNeuron(object):
    """Class representing a single spiking neuron."""

    def __init__(self, bias: float, a: float, b: float, c: float, d: float, inputs: Dict[int, float]):
        """
        a, b, c, and d are the parameters of the Izhikevich model.

        :param bias: The bias of the neuron.
        :param a: The time-scale of the recovery variable.
        :param b: The sensitivity of the recovery variable.
        :param c: The after-spike reset value of the membrane potential.
        :param d: The after-spike reset value of the recovery variable.
        :param inputs: A dictionary of incoming connection weights.
        """

        self.bias = bias
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.inputs = inputs

        self.membrane_potential = self.c
        self.membrane_recovery = self.b * self.membrane_potential
        self.fired = 0
        self.current = self.bias

        # Variables containing time elapsed since last input and output spikes.
        self.output_spike_timing: float = 0
        self.input_spike_timings: Dict[int, float] = {key: 0 for key in self.inputs.keys()}
        self.has_fired = False

    def advance(self, dt: float):
        """
        Advances simulation time by the given time step in milliseconds.

        Update of membrane potential "v" and membrane recovery "u" given by formulas:
            v += dt * (0.04 * v^2 + 5v + 140 - u + I)
            u += dt * a * (b * v - u)

        Once membrane potential exceeds threshold:
            v = c
            u = u + d

        :param dt: Time step in milliseconds.
        """

        v = self.membrane_potential
        u = self.membrane_recovery

        self.membrane_potential += dt * (0.04 * v ** 2 + 5 * v + 140 - u + self.current)
        self.membrane_recovery += dt * self.a * (self.b * v - u)

        self.fired = 0
        self.output_spike_timing += dt

        for key in self.input_spike_timings.keys():
            # STDP update on received input spike.
            if self.input_spike_timings[key] == 0 and self.has_fired:
                self.stpd_update(key)

            self.input_spike_timings[key] += dt

        if self.membrane_potential > MEMBRANE_POTENTIAL_THRESHOLD:
            self.fired = 1
            self.has_fired = True
            self.output_spike_timing = 0
            self.membrane_potential = self.c
            self.membrane_recovery += self.d

            # STDP on output spike.
            for key in self.input_spike_timings.keys():
                self.stpd_update(key)

    def reset(self):
        """ Resets all state variables."""

        self.membrane_potential = self.c
        self.membrane_recovery = self.b * self.membrane_potential

        self.fired = 0
        self.current = self.bias

        self.output_spike_timing = STDP_LEARNING_WINDOW
        self.input_spike_timings = {key: STDP_LEARNING_WINDOW for key in self.inputs.keys()}

    def stpd_update(self, key: int):
        """
        Applies STDP to the weight with the supplied key.

        :param key: The key identifying the synapse weight to be updated.
        :return: void
        """
        # TODO: Make learning rule dynamic. Part of genome?

        delta_t = self.output_spike_timing - self.input_spike_timings[key]
        if abs(delta_t) < STDP_LEARNING_WINDOW:
            weight = self.inputs[key]
            delta_weight = asymmetric_hebbian(delta_t, **ASYMMETRIC_HEBBIAN_PARAMS)
            sigma, w_min, w_max = STDP_PARAMS['sigma'], STDP_PARAMS['w_min'], STDP_PARAMS['w_max']

            if delta_weight > 0:
                self.inputs[key] += sigma * delta_weight * (w_max - weight)
            elif delta_weight < 0:
                self.inputs[key] += sigma * delta_weight * (weight - abs(w_min))


class SpikingNeuralNetwork(object):
    """Class representing a spiking neural network."""

    def __init__(self, neurons: Dict[int, SpikingNeuron], inputs: List[int], outputs: List[int]):
        """
        :param neurons: Dictionary containing key/node pairs.
        :param inputs: List of input node keys.
        :param outputs: List of output node keys.
        :var self.input_values: Dictionary containing input key/voltage pairs.
        """

        self.neurons = neurons
        self.inputs = inputs
        self.outputs = outputs
        self.input_values: Dict[int, float] = {}

    def set_inputs(self, inputs: List[float]):
        """
        Assigns voltages to the input nodes.

        :param inputs: List of voltage values."""

        assert len(inputs) == len(
            self.inputs), f"Number of inputs {len(inputs)} does not match number of input nodes {len(self.inputs)} "

        for key, voltage in zip(self.inputs, inputs):
            self.input_values[key] = voltage

    def advance(self, dt: float) -> List[float]:
        """
        Advances the neural network with the given input values and neuron states. Iterates through each neuron, then
        through each input of each neuron and evaluates the values to advance the network. The values can come from
        either input nodes, or firing neurons in a previous layer.

        :param dt: Time step in miliseconds.
        :return: List of the output values of the network after advance."""

        for neuron in self.neurons.values():
            neuron.current = neuron.bias
            for key, weight in neuron.inputs.items():
                in_neuron = self.neurons.get(key)
                if in_neuron is not None:
                    in_value = in_neuron.fired
                else:
                    in_value = self.input_values[key]

                # Trigger STDP on received input spike.
                if in_value:
                    neuron.input_spike_timings[key] = 0

                neuron.current += in_value * weight
                neuron.advance(dt)

        return [self.neurons[key].fired for key in self.outputs]

    def reset(self):
        """Resets all state variables in all neurons in the entire neural network."""
        for neuron in self.neurons.values():
            neuron.reset()
