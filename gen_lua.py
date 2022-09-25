'''

 ______   
/\  ___\  
\ \ \____ 
 \ \_____\
  \/_____/
                                                   
Generate OBS Lua

This is intended to output a lua script that can be used with OBS to create a user interface.
Ideally for creating scenes and importing items.

I am aware of some python to lua translators but my use case is somewhat specific. C'est la vie.

'''

import os
from luator import luator

class genlua(self):
  
  '''
  Class for running and writing out to a new lua file based off a template
  '''


  def get_lua():

    '''
    Return a file object
    '''
    current_dir = os.path.dirname(__file__)
    lua_template = os.path.join(current_dir, "template.lua")
    print(type(luator.read_lua(lua_template)))



def main():

  '''
  General Run for gen_lua
  '''
  genlua.get_lua()


if __name__ == '__main__':

  main()