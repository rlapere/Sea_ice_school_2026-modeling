def blockPrint():
    import sys,os
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    import sys,os
    sys.stdout = sys.__stdout__


def build_cmap(colors, N=100, reverse=''):
    from matplotlib.colors import LinearSegmentedColormap
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    '''
    Build a custom colormap from a list of colors
    The colors are linearly interpolated
    The number of colors in the final colormap is N
    You can reverse the colormap by setting reverse='r'
    Originally created by Theodore Khadir
    ''' 
    if reverse == 'r':
        colors = [colors[len(colors)-1-i] for i in range(0, len(colors))]
        cmap = LinearSegmentedColormap.from_list('name', colors, N=N)
    else:
        cmap = LinearSegmentedColormap.from_list('name', colors, N=N)
    return cmap
