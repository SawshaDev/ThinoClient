Thino Client
==================

Easy to use Python wrapper for **Thino's API**

Key Features
------------
- Modern Pythonic Interface
- Easy to use


Installing
----------

**Python 3.8 or higher**

To install the library, run the following command

.. code:: sh

  #Linux/macOS
  python3 -m pip install -U git+https://github.com/VarMonke/ThinoClient
  
  #Windows
  py -m pip install -U git+https://github.com/VarMonke/ThinoClient
  
Quick Example
-------------
  
.. code:: py
  
  import thino
  import asyncio
  
  async def main():
    client = thino.Client()
    return await client.femboy()

  femboy = asyncio.run(main())
  print(femboy)
  print(femboy.url)

.. code:: sh
  <Femboy url: 'https://i.thino.pics/72elu40mjkm81.jpg', status: 200>
  https://i.thino.pics/72elu40mjkm81.jpg

 
