
https://pythonspot.com/en/pyqt5-matplotlib/
http://eli.thegreenplace.net/2009/01/20/matplotlib-with-pyqt-guis/
https://pythonspot.com/en/matplotlib/

# 绘图: matplotlib核心剖析
http://www.cnblogs.com/vamei/archive/2013/01/30/2879700.html

# 用Matplotlib来做K线图
http://bluegene8210.is-programmer.com/posts/24606.html

http://matplotlib.org/faq/usage_faq.html#what-is-interactive-mode
http://matplotlib.org/faq/usage_faq.html#what-is-a-backend

https://segmentfault.com/a/1190000004879349

通过pip来安装 Matplotlib
```
pip install matplotlib
```

注：安装Python时记得勾选"tcl/tk ..."，否则PyQt + Matplotlib可能不工作。

Summary
----------
- 各图形元素都来自于一个叫做 Artist 的基类
- 对于每个Artist类的对象，都有findobj()方法，来显示该对象所包含的所有下层对象。
- 使用obj.__class__.__name__来查询对象所属的类
- Canvas对象(FigureCanvas)代表了真正进行绘图的后端(backend)，Artist 只是在程序逻辑上的绘图，它必须连接后端绘图程序才能真
正在屏幕上绘制出来（或保存为文件）。我们可以将canvas理解为绘图的物理（或者说硬件）实现。

# Artist对象都具有的一些属性：
alpha : 透明度，值在0到1之间，0为完全透明，1为完全不透明
animated : 布尔值，在绘制动画效果时使用
axes : 此Artist对象所在的Axes对象，可能为None
 clip_box : 对象的裁剪框
clip_on : 是否裁剪
clip_path : 裁剪的路径
contains : 判断指定点是否在对象上的函数
figure : 所在的Figure对象，可能为None
 label : 文本标签
picker : 控制Artist对象选取
transform : 控制偏移旋转
visible : 是否可见
zorder : 控制绘图顺序

Artist对象的所有属性都通过相应的 get_* 和 set_* 函数进行读写
fig.set_alpha(0.5*fig.get_alpha())

如果你想用一条语句设置多个属性的话，可以使用set函数：
fig.set(alpha=0.5, zorder=2)

使用 matplotlib.pyplot.getp 函数可以方便地输出Artist对象的所有属性名和值。
plt.getp(fig.patch)
