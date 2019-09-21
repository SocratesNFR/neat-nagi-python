from math import exp


def asymmetric_hebbian(delta_t: float, a_plus: float, a_minus: float, tau_plus: float, tau_minus: float) -> float:
    """
    Exponential Synaptic Weight Modification function used in STDP based learning.

    :param delta_t: Difference in relative timing of pre- and postsynaptic spikes, in milliseconds.
    :param a_plus: Constant when delta_t > 0.
    :param a_minus: Constant when delta_t < 0.
    :param tau_plus: Time constant when delta_t > 0, in milliseconds.
    :param tau_minus: Time constant when delta_t < 0, in milliseconds.
    :return: Weight modification in decimal percentage.
    """

    if delta_t > 0:
        return -a_plus * exp(-delta_t / tau_plus)
    else:
        return a_minus * exp(delta_t / tau_minus)


def asymmetric_anti_hebbian(delta_t: float, a_plus: float, a_minus: float, tau_plus: float, tau_minus: float) -> float:
    """
    Exponential Synaptic Weight Modification function used in STDP based learning.

    :param delta_t: Difference in relative timing of pre- and postsynaptic spikes, in milliseconds.
    :param a_plus: Constant when delta_t > 0.
    :param a_minus: Constant when delta_t < 0.
    :param tau_plus: Time constant when delta_t > 0, in milliseconds.
    :param tau_minus: Time constant when delta_t < 0, in milliseconds.
    :return: Weight modification in decimal percentage.
    """

    if delta_t > 0:
        return a_plus * exp(-delta_t / tau_plus)
    else:
        return -a_minus * exp(delta_t / tau_minus)

