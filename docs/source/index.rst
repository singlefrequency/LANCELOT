.. image:: _static/new_logo.svg
   :align: center

LANCELOT
=======================================
LANCELOT is the library for the Large Scale Structure of the Universe, that implements various modified theories of gravitation, such as :math:`f(Q)`, :math:`f(T)` and 
:math:`f(T,B)` gravities in the presence of massive neutrinos. Our library consists of 24 separate simulations:

- :math:`f(Q)` gravity with regular fluid, Dynamical Dark Energy (DDE) and massive neutrinos :math:`(1+1)\times2` simulations
-  :math:`f(T)` gravity with regular fluid, Dynamical Dark Energy (DDE) and massive neutrinos :math:`(1+1)\times2` simulations
-  :math:`f(T,B)` gravity with regular fluid, Dynamical Dark Energy (DDE) and massive neutrinos :math:`(1+1)\times2` simulations
All aforementioned simulations are carried out with the box size :math:`L_{\mathrm{box}}=500\mathrm{\;Mpc}/h`. However, it is planned to also investigate aforementioned theories of gravitation on the smaller scales with bigger resolution of separate galaxies and galaxy clusters (12 simulations in total). For that case, we assume :math:`L_{\mathrm{box}}=100\mathrm{\;Mpc}/h`. Softening scales are redefined accordingly. The main goals of our project is to:

- Differentiate different novel modified theories of gravity, based on the teleparallelism or symmetric teleparallelism, define whether those theories are  viable or not.
- Investigate and comparate the behaviour of previously mentioned MOG theories with both :math:`\Lambda\mathrm{CDM}` and :math:`\nu\mathrm{CDM}` theories. Constrain the parameter space for all three theories using MCMC (Markov Chain Monte Carlo) approach, study Hubble and :math:`\sigma_8` tensions, matter power spectrum :math:`P(k)` and bispectrum :math:`B(k)`, 2PCF/3PCF and halo mass functions.

Contents
--------

.. toctree::

   usage
   api
