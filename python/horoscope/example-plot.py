from astropy.coordinates import SkyCoord
from sunpy.coordinates import get_body_heliographic_stonyhurst
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np


obstime = Time('2020-05-15T07:54:00.005')
planet_list = ['earth', 'venus', 'mars', 'mercury', 'jupiter', 'neptune', 'uranus']
planet_coord = [get_body_heliographic_stonyhurst(this_planet, time=obstime) for this_planet in planet_list]

fig = plt.figure()
ax1 = plt.subplot(1, 1, 1, projection='polar')
for this_planet, this_coord in zip(planet_list, planet_coord):
    plt.polar(np.deg2rad(this_coord.lon), this_coord.radius, 'o', label=this_planet)
plt.legend()
plt.show()