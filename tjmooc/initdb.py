from user.models import User
from course.models import Course, Chapter, Unit
from material.models import Homework, Test, Video, Problem
from user.models import User
from datetime import datetime

superuser = User.objects.get(username='tjmooc')

courses = [
    Course(title='高等数学', subtitle='同济大学', introduction='指相对于初等数学而言，数学的对象及方法较为繁杂的一部分。\
        广义地说，初等数学之外的数学都是高等数学，也有将中学较深入的代数、几何以及简单的集合论初步、逻辑初步称为中等数学的，\
        将其作为中小学阶段的初等数学与大学阶段的高等数学的过渡。\
        通常认为，高等数学是由微积分学，较深入的代数学、几何学以及它们之间的交叉内容所形成的一门基础学科。\
        主要内容包括：极限、微积分、空间解析几何与线性代数、级数、常微分方程。\
        工科、理科研究生考试的基础科目。',
           cover_image='/static/1.png',
           update_time=datetime.now(),
           obligator=superuser),
    Course(title='线性代数', subtitle='同济大学', introduction='线性代数是数学的一个分支，它的研究对象是向量，\
        向量空间（或称线性空间），线性变换和有限维的线性方程组。向量空间是现代数学的一个重要课题',
           cover_image='/static/2.png',
           update_time=datetime.now(),
           obligator=superuser),
    Course(title='概率论与数理统计', subtitle='同济大学', introduction='概率论与数理统计是数学的一个有特色且又十分活跃的分支，\
       一方面，它有别开生面的研究课题，有自己独特的概念和方法，内容丰富，\
        结果深刻;另一方面，它与其他学科又有紧密的联系，\
       是近代数学的重要组成部分。由于它近年来突飞猛进的发展与应用的广泛性，\
       目前已发展成为一门独立的一级学科。',
           cover_image='/static/2.png',
           update_time=datetime.now(),
           obligator=superuser),
]


for course in courses:
    course.save()


chapters = [
    Chapter(title='极限和导数', description='导数是函数的局部性质。一个函数在某一点的导数描述了这个函数在这一点附近的变化率。\
    如果函数的自变量和取值都是实数的话，函数在某一点的导数就是该函数所代表的曲线在这一点上的切线斜率。',
            leacturer=superuser),
    Chapter(title='一元函数微分学', description='元函数微分学知识点 第一章函数与极限 函数会求函数的定义域,对应法则;\
    几种特殊的函数(复合函数、初等函数等); 函数的几种特性(有界性、单调性、...',
            leacturer=superuser),
    Chapter(title='行列式', description='行列式在数学中，是一个函数，其定义域为det的矩阵A，取值为一个标量，写作det(A)或 | A | 。\
    无论是在线性代数、多项式理论，还是在微积分学中（比如说换元积分法中），行列式作为基本的数学工具，都有着重要的应用。',
            leacturer=superuser),
    Chapter(title='矩阵', description='在数学中，矩阵（Matrix）是一个按照长方阵列排列的复数或实数集合[1]，\
    最早来自于方程组的系数及常数所构成的方阵。这一概念由19世纪英国数学家凯利首先提出。',
            leacturer=superuser),
    Chapter(title='随机事件与概率', description='随机事件是在随机试验中，可能出现也可能不出现，\
    而在大量重复试验中具有某种规律性的事件叫做随机事件(简称事件)。',
            leacturer=superuser),
    Chapter(title='等可能概型', description='在随机试验中，随机事件一般是由若干个基本事件组成的。\
    样本空间Ω的任一子集A称为随机事件。属于事件A的样本点出现，则称事件A发生。',
            leacturer=superuser)
]

for chapter in chapters:
    chapter.save()

for i in range(0, 3):
    courses[i].sections = [chapters[i * 2].id, chapters[i * 2 + 1].id]
    courses[i].save()

units = [
    Unit(title='极限', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
    如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='导数', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='微分', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='积分', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='行列式定义', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='行列式计算', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='矩阵的定义', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='矩阵的计算', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='随机事件', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='概率', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='古典概型', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
    Unit(title='古典概型的应用', description='极限思想是微积分的基本思想，是数学分析中的一系列重要概念，\
如函数的连续性、导数（为0得到极大值）以及定积分等等都是借助于极限来定义的。',
         leacturer=superuser),
]


for unit in units:
    unit.save()

for i in range(0, 6):
    chapters[i].units = [units[i * 2].id, units[i * 2 + 1].id]
    chapters[i].save()







