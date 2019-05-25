import numpy as np
import matplotlib.pyplot as plt



class point():
    def __init__(self, x=0, y=0, c=0):
        self._x = x
        self._y = y
        self._c = c

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, val):
        self._c = val

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val


class Leach():

    def __init__(self, num_unit, p):
        self.num = num_unit
        self.p = p   #概率
        self.r = 1   #当前轮数
        self.circle = 1  # int(1/p)
        self.core = []  #质心
        self.po = []    #节点存储
        self.dst = []   #节点连接结果
        self.fig = plt.figure(figsize=(20, 20))

    def T(self):
        t = self.p / (1 - self.p * (self.r % (1 / self.p)))
        return t

    def generator(self):
        num = self.num
        t = self.T()
        x, y, w = np.random.rand(3, num)
        for i in range(num):
            if w[i] < t:
                self.core.append(point(x[i], y[i], self.r))
                self.po.append(point(x[i], y[i], self.r))
            else:
                self.po.append(point(x[i], y[i], 0))

    def distance(self):
        for i in range(self.num):
            v1 = np.array([self.po[i].x, self.po[i].y])
            d = []
            for j in self.core:
                v2 = np.array([j.x, j.y])
                d_ = np.linalg.norm(v1 - v2)
                d.append(d_)
            index = np.argmin(d)
            self.dst.append(index)

    def update(self):
        self.dst = []
        self.r += 1
        self.core = []
        t = self.T()
        w = np.random.rand(self.num)
        for i in range(self.num):
            if w[i] < t and self.r - self.po[i].c >= self.circle:
                self.po[i].c = self.r
                self.core.append(self.po[i])
        self.distance()

    def plot(self):
        # fig = plt.figure(figsize=(5,5))
        ax = self.fig.add_subplot(2, 2, self.r, title='第{}轮'.format(str(self.r)))
        for i in range(self.num):
            ax.plot([self.po[i].x, self.core[self.dst[i]].x],
                    [self.po[i].y, self.core[self.dst[i]].y], color='b', linewidth=0.5)
            ax.scatter(self.po[i].x, self.po[i].y, color='b')
        for j in range(len(self.core)):
            ax.scatter(self.core[j].x, self.core[j].y, color='r')

    def test(self):
        self.generator()
        self.distance()
        self.plot()

def point_to_list(points):
    data = []
    for p in points:
        data.append([p.x, p.y])
    return data

def point_to_dict(points):
    data = []
    for i, p in enumerate(points):
        data.append({
            'name':str(i),
            'data':[p.x, p.y]
        })
    return data


def dst_to_list(dst,core):
    data = []
    for d in dst:
        data.append([core[d].x, core[d].y])
    return data


def result(r):
    l = Leach(num_unit=100, p=0.08)
    l.generator()
    l.distance()
    for i in range(int(r)):
        l.update()
    return point_to_list(l.po), dst_to_list(l.dst, l.core)




    #p.fig.savefig('/Users/bujue/Desktop/物联网课件/fig', format='png')
