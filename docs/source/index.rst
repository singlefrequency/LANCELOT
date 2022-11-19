.. image:: _static/lancelot.svg
   :align: center

LANCELOT
=======================================
LANCELOT is the library for the Large Scale Structure of the Universe, that implements various modified theories of gravitation, such as :math:`f(Q)`, :math:`f(T)` and 
:math:`f(T,B)` gravities in the presence of massive neutrinos. Our library consists of 24 separate simulations:
* :math:`f(Q)` gravity with regular fluid, Dynamical Dark Energy (DDE) and massive neutrinos :math:`(1+1)\times2` simulations
*  :math:`f(T)` gravity with regular fluid, Dynamical Dark Energy (DDE) and massive neutrinos :math:`(1+1)\times2` simulations
*  :math:`f(T,B)` gravity with regular fluid, Dynamical Dark Energy (DDE) and massive neutrinos :math:`(1+1)\times2` simulations
All aforementioned simulations are carried out with the box size :math:`L_{\mathrm{box}}=500\mathrm{\;Mpc}/h`. However, it is planned to also investigate aforementioned theories of gravitation on the smaller scales with bigger resolution of separate galaxies. For that case, we assume :math:`L_{\mathrm{box}}=100\mathrm{\;Mpc}/h`. Softening scales are redefined accordingly.

Contents
--------

.. toctree::

   usage
   api
