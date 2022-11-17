import random
import time
from tabulate import tabulate


class Sort:
    class_mapping = []
    student_mapping = {}
    pos = [0, 0]  # 当前位置
    square = [0, 0]
    relations_v1_mapping = {}  # 有世仇的同学关系映射
    relations_v2_mapping = {}  # 吵闹的同学关系映射
    counter = [0, 0]  # 循环计数器与步长计数器

    def __init__(self, width=8, length=6, student_names="names.txt",
                 relation_v1_config="rel_v1.txt", relation_v2_config="rel_v2.txt"):
        self.square = [width, length]
        self.class_mapping = [[0 for _ in range(width)] for _ in range(length)]

        try:
            f1 = open(student_names, "r", encoding="utf8")
            f2 = open(relation_v1_config, "r", encoding="utf8")
            f3 = open(relation_v2_config, "r", encoding="utf8")

        except IOError as e:
            print(f"无法读取文件: {e}")
            exit(0)

        else:
            f = f1.readlines()
            for line in f:
                self.student_mapping[f.index(line) + 1] = line.strip()
            # 初始化关系映射为数组
            self.relations_v1_mapping = {_ + 1: [] for _ in range(len(f))}
            self.relations_v2_mapping = {_ + 1: [] for _ in range(len(f))}
            # 初始化学生索引基准数组
            self.student_mapping["index"] = [_ + 1 for _ in range(len(f))]

            f = f2.readlines()
            for line in f:
                li = line.strip().split("-")
                mapping = self.relations_v1_mapping[int(li[0])]
                mapping.append(int(li[1]))
                self.relations_v1_mapping[int(li[0])] = mapping

                mapping = self.relations_v1_mapping[int(li[1])]
                mapping.append(int(li[0]))
                self.relations_v1_mapping[int(li[1])] = mapping

            f = f3.readlines()
            for line in f:
                li = line.strip().split("-")
                mapping = self.relations_v2_mapping[int(li[0])]
                mapping.append(int(li[1]))
                self.relations_v2_mapping[int(li[0])] = mapping

                mapping = self.relations_v2_mapping[int(li[1])]
                mapping.append(int(li[0]))
                self.relations_v2_mapping[int(li[1])] = mapping

    def next_step(self):
        self.counter[1] += 1

        if self.pos[0] + 1 == self.square[0]:
            self.pos = [0, self.pos[1] + 1]
        else:
            self.pos[0] += 1

    def back_step(self):
        self.counter[1] += 1

        if self.pos[0] == 0:
            self.pos = [self.square[0] - 1, self.pos[1] - 1]
        else:
            self.pos[0] -= 1

    def validator(self):
        return True

    # 打印结果
    def print_result(self):
        table = list(map(lambda x: list(map(lambda y: self.student_mapping[y], x)), self.class_mapping))
        print(tabulate(table))

    def exec(self):
        student_index: list = self.student_mapping["index"]

        while self.pos[0] < self.square[0] and self.pos[1] < self.square[1]:
            self.counter[0] += 1

            try:
                self.class_mapping[self.pos[1]][self.pos[0]] = random.choice(student_index)

            except IndexError:  # 如果索引数组为空则返回上一步
                self.class_mapping[self.pos[1]][self.pos[0]] = 0
                self.back_step()
                student_index = self.student_mapping["index"]
                student_index.append(self.class_mapping[self.pos[1]][self.pos[0]])
                self.student_mapping["index"] = student_index
                student_index.remove(self.class_mapping[self.pos[1]][self.pos[0]])
                self.class_mapping[self.pos[1]][self.pos[0]] = 0

            else:  # 不为空则写入班级数组
                if self.validator():  # 判断是否符合规则
                    student_index = self.student_mapping["index"]
                    student_index.remove(self.class_mapping[self.pos[1]][self.pos[0]])  # 避免重复
                    self.student_mapping["index"] = self.student_mapping["index"]
                    self.next_step()
                else:
                    student_index.remove(self.class_mapping[self.pos[1]][self.pos[0]])

        print("Result:")
        self.print_result()
        print(f"步长: {self.counter[1]},循环次数: {self.counter[0]},进程执行时间: {time.perf_counter()}秒")
