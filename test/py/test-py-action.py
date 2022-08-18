print(f'{__name__} executed')

import geocoder
print( geocoder.arcgis('南投市彰南路2段8號').json )
