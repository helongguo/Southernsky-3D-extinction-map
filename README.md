Stellar parameters for 799 million stars, inferred by Green et al. (2019). The four parameters we infer are: 
Distance modulus ("dm")
Reddening ("E")
Absolute rP1 magnitude ("Mr")
Metallicity ("FeH")
These parameters are inferred by modeling the broad-band Pan-STARRS 1 and 2MASS photometry of the stars, as well as their Gaia DR2 parallaxes. We take into account priors on the distribution of stars of different types throughout the Milky Way. Reddening is given in an arbitrary unit, which can be converted to magnitudes of extinction in the PS1 and 2MASS passbands by multiplying by the following coefficients: 
gP1: 3.518
rP1: 2.617
iP1: 1.971
zP1: 1.549
yP1: 1.263
J: 0.7927
H: 0.4690
Ks: 0.3026
The catalog is split into files containing approximately 8 million stars each. Each file contains the following groups: 
metadata: the locations of the stars, as well as a unique identifier for each star
data: The PS1/2MASS photometry and Gaia DR2 parallaxes used to infer the stellar parameters
chisq: The maximum-likelihood χ2/passband for the each star
samples: Samples drawn from the posterior distribution of the stellar parameters, as well as the corresponding log likelihoods and priors
percentiles: 16th, 50th and 84th percentiles of the marginal distribution of each parameter
gaia: Gaia DR2 source_id. Additionally, the 16th, 50th and 84th percentiles of E(BP-RP) and AG reported by Andrae et al. (2018)
Within each group, the stars are divided into datasets corresponding to an nside = 32 HEALPix pixelization of the sky, with nested ordering, in Galactic coordinates. (2019-04-29) 
