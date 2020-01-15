import numpy, pandas, os
import matplotlib.pyplot as mpl

def generate():
    mu = 0
    alpha = numpy.random.uniform(5,30)
    n = numpy.random.randint(365,730)
    data = []
    for _ in range(int(n)):
        data.append(mu)
        mu = numpy.random.uniform(mu-alpha,mu+alpha)
    return data

def plot():
    fig = pandas.DataFrame({'observations':generate()}).plot(figsize=(20,10))
    mpl.savefig('test.jpg')
plot()
