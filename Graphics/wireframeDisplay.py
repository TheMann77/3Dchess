import pygame
import wireframe

class ProjectionViewer:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background = (10,10,50)
        self.wireframes = {}
        self.displayNodes = True
        self.displayEdges = True
        self.nodeColour = (255,255,255)
        self.edgeColour = (200,200,200)
        self.nodeRadius = 4
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_function:
                        key_to_function[event.key](self)
            self.display()
            pygame.display.flip()
            
            
    def addWireframe(self, name, wireframe):
        self.wireframes[name] = wireframe
        
    def display(self):
        """ Draw the wireframes on the screen. """
        self.screen.fill(self.background)
        for wireframe in self.wireframes.values():
            if self.displayEdges:
                for edge in wireframe.edges:
                    pygame.draw.aaline(self.screen, self.edgeColour, (edge.start.x, edge.start.y), (edge.stop.x, edge.stop.y), 1)
            if self.displayNodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.nodeColour, (int(node.x), int(node.y)), self.nodeRadius, 0)
                    
    def translateAll(self, axis, d):
        """ Translate all wireframes along a given axis by d units. """
        for wireframe in self.wireframes.itervalues():
            wireframe.translate(axis, d)
        
        
    def scaleAll(self, scale):
        """ Scale all wireframes by a given scale, centred on the centre of the screen. """
        centre_x = self.width/2
        centre_y = self.height/2
        for wireframe in self.wireframes.itervalues():
            wireframe.scale((centre_x, centre_y), scale)
        
    def rotateAll(self, axis, theta):
        """ Rotate all wireframe about their centre, along a given axis by a given angle. """
        rotateFunction = 'rotate' + axis
        for wireframe in self.wireframes.itervalues():
            centre = wireframe.findCentre()
            getattr(wireframe, rotateFunction)(centre, theta)
key_to_function = {
    pygame.K_LEFT:   (lambda x: x.translateAll('x', -10)),
    pygame.K_RIGHT:  (lambda x: x.translateAll('x',  10)),
    pygame.K_DOWN:   (lambda x: x.translateAll('y',  10)),
    pygame.K_UP:     (lambda x: x.translateAll('y', -10)),
    pygame.K_EQUALS: (lambda x: x.scaleAll(1.25)),
    pygame.K_MINUS:  (lambda x: x.scaleAll( 0.8)),
    pygame.K_q: (lambda x: x.rotateAll('X',  0.1)),
    pygame.K_w: (lambda x: x.rotateAll('X', -0.1)),
    pygame.K_a: (lambda x: x.rotateAll('Y',  0.1)),
    pygame.K_s: (lambda x: x.rotateAll('Y', -0.1)),
    pygame.K_z: (lambda x: x.rotateAll('Z',  0.1)),
    pygame.K_x: (lambda x: x.rotateAll('Z', -0.1))}
cube = wireframe.Wireframe()
cube.addNodes([(x,y,z) for x in (50,250) for y in (50,250) for z in (50,250)])
cube.addEdges([(n,n+4) for n in range(0,4)]+[(n,n+1) for n in range(0,8,2)]+[(n,n+2) for n in (0,1,4,5)])
pv = ProjectionViewer(400, 300)
pv.addWireframe('cube', cube)
pv.run()