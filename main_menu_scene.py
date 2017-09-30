# Created by : Sidney Kang
# Created on : 27 Sept. 2017
# Created for : ICS3UR
# Wednesday Assignment - wed_04
# This scene

from scene import * 
import ui

class MainMenuScene(Scene):
      def setup(self):
      #Add Mt blue background colour
          self.background = SpriteNode(position = self.size/2, 
                                       color = (0.61, 0.78, 0.87), 
                                       parent = self,
                                       size = self.size)
