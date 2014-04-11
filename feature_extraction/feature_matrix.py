__author__ = 'Alexey'

import numpy

def cost(a, b):
    """
    cost function - Euclidean distance between A and B matrices

    >>> cost(numpy.matrix([1,1]), numpy.matrix([2,2]))
    2
    >>> cost(numpy.matrix([1,1]), numpy.matrix([1,1]))
    0
    """
    dif = 0
    for i in range(numpy.shape(a)[0]):
        for j in range(numpy.shape(b)[1]):
            dif += pow(a[i,j] - b[i,j], 2)
    return dif

class FeatureMatrixBuilder(object):
    """
    Calculates feature matrix V = WH

    >>> matrix = numpy.matrix([[22, 28], [49, 64]])
    >>> fm = FeatureMatrixBuilder(matrix, 1, 100)
    >>> w, h = fm.get_matrix()
    >>> w * h

    """
    def __init__(self, messages_matrix, features_number = 10, iterations = 50):
        self._v = messages_matrix
        self._dimension1 = numpy.shape(self._v)[0]
        self._dimension2 = numpy.shape(self._v)[1]
        self._features_number = features_number
        self._iterations = iterations

    def get_matrix(self):
        w = numpy.matrix([[numpy.random.random() for j in range(self._features_number)]
                          for i in range(self._dimension1)])
        h = numpy.matrix([[numpy.random.random() for i in range(self._dimension2)]
                          for i in range(self._features_number)])

        for i in range (self._iterations):
            wh = w * h

            cost_result = cost(self._v, wh)

            if cost_result == 0:
                break

            hn = numpy.transpose(w) * self._v
            hd = numpy.transpose(w) * w * h

            h = numpy.matrix(numpy.array(h) * numpy.array(hn) / numpy.array(hd))

            wn = self._v * numpy.transpose(h)
            wd = w * h * numpy.transpose(h)

            w = numpy.matrix(numpy.array(w) * numpy.array(wn) / numpy.array(wd))

            return w, h

