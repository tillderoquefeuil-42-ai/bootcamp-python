
class ColorFilter():
    
    def ft_map(self, array, func):
        tr = True if array.shape[2] == 4 else False

        for i in range(0, array.shape[0]):
            for j in range(0, array.shape[1]):
                pixel = array[i,j]
                pixels = func(pixel)
                if tr == True:
                    array[i,j] = (pixels[0], pixels[1], pixels[2], 1.0)
                else:
                    array[i,j] = pixels
        return array


    # Takes a NumPy array of an image as an argument and returns an array with inverted color.
    # Authorized function : None
    # Authorized operator: -
    def invert(self, array):
        func = lambda p: (1-p[0], 1-p[1], 1-p[2])
        array = self.ft_map(array, func)
        return array
    
    # Takes a NumPy array of an image as an argument and returns an array with a blue filter.
    # Authorized function : .zeros, .shape
    # Authorized operator: None
    def to_blue(self, array):
        func = lambda p: (0, 0, p[2])
        array = self.ft_map(array, func)
        return array
    
    # Takes a NumPy array of an image as an argument and returns an array with a green filter.
    # Authorized function : None
    # Authorized operator: *
    def to_green(self, array):
        func = lambda p: (0, p[1], 0)
        array = self.ft_map(array, func)
        return array
    
    # Takes a NumPy array of an image as an argument and returns an array with a red filter.
    # Authorized function : green, blue
    # Authorized operator: -, +
    def to_red(self, array):
        func = lambda p: (p[0], 0, 0)
        array = self.ft_map(array, func)
        return array
    
    # Takes a NumPy array of an image as an argument, and returns an array with a celluloid shade filter. 
    # The celluloid filter must display at least four thresholds of shades. 
    # Be careful! You are not asked to apply black contour on the object here (you will have to, but later. . . ), you only have to work on the shades of your images. 
    # Authorized function: arange, linspace
    def celluloid(self, array):
        def func(p):
            # don't ask me why i'm doing this i've absolutly no idea
            luminance = (0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2])
            luminance = self.threshold(luminance)

            p[0] = (luminance - 0.7152 * p[1] - 0.0722 * p[2]) / 0.2126
            p[1] = (luminance - 0.2126 * p[0] - 0.0722 * p[2]) / 0.7152
            p[2] = (luminance - 0.2126 * p[0] - 0.7152 * p[1]) / 0.0722
            return p
    
        array = self.ft_map(array, func)
        return array

    def threshold(self, c):
        return int(c * 10)/10

    # Takes a NumPy array of an image as an argument and returns an array in grayscale. The method takes another argument to select between two possible grayscale filters. Each filter has specific authorized functions and operators.
    #     – ‘mean’ or ‘m’ : Takes a NumPy array of an image as an argument and returns an array in grayscale created from the mean of the RBG channels.
    #     Authorized function : .sum, .shape, reshape, broadcast_to, (as_type?)
    #     Authorized operator: /
    #     – ‘weighted’ or ‘w’ : Takes a NumPy array of an image as an argument and returns an array in weighted grayscale. This argument should be selected by default if not given.
    #     The usual weighted grayscale is calculated as : 0.299 * R_channel + 0.587 * G_channel + 0.114 * B_channel.
    #     Authorized function : .sum, .shape, .tile Authorized operator: *
    def to_grayscale(self, array, filter):
        def func(p):
            gray = (p[0] + p[1] + p[2])/3
            return (gray, gray, gray)
    
        array = self.ft_map(array, func)
        return array