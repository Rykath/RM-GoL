'''
Created on Jun 22, 2016

@author: Rykath
Package: Main

Executing Module
'''

def runMain():
    import Main.core
    import Main.settings
    
    core = Main.core.Core()
    while core.running:
        if Main.settings.gui == 'console':
            prompt = input('>>> ')
            if prompt == 'exit':
                core.running = False

if __name__ == '__main__':
    runMain()