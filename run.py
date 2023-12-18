'''Learning Flask'''
from writesage import create_app

import collections 
import sys
if sys.version_info.major == 3 and sys.version_info.minor >= 10:
    from collections.abc import MutableSet
    collections.MutableSet = collections.abc.MutableSet
else: 
    from collections import MutableSet
    
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
 