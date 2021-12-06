# hotelling-law-cadcad
[Collab of IPYNB](https://colab.research.google.com/drive/1mZmOFC7hNmhuaUMkw74yMyh6AcMa04zF#scrollTo=jZDKRa5P9-gP)


An implementation of Hotelling's Law simulation as presented in NetLogo.

Hotelling Paper:
Hotelling, Harold. (1929). “Stability in Competition.” The Economic Journal 39.153: 41 -57. (Stable URL: https://www.jstor.org/stable/2224214).


For the model itself:
Ottino, B., Stonedahl, F. and Wilensky, U. (2009). NetLogo Hotelling’s Law model. [Model](https://ccl.northwestern.edu/netlogo/models/Hotelling'sLaw). Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

Please cite the NetLogo software as:
Wilensky, U. (1999). NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

Consumer behavior:
- Sum the distance to the store and the price of the product (price + distance = decision)
- The store with the lowest sum gets the consumer (revenue += (price * number_of_consumers))
- Next tick stores update their location
