class Solution:

    # 207. 课程表
    # https://leetcode.cn/problems/course-schedule/
    def canFinish(self, numCourses: int, prerequisites: list[tuple[int, int]]) -> bool:

        # 深度优先遍历，递归

        # 图中的点有三种状态：
        # "0": not_finished_and_not_considered
        # "1": not_finished_and_being_considered
        # "2": finished

        # 没有遍历前图上的所有节点都是not_finished_and_not_considered状态，
        # 向下遍历的时候走过的节点状态变为not_finished_and_being_considered，
        # 向上回退的时候节点状态变为finished

        # 无法完成课程学习等价于有向图有环，
        # 等价于向下遍历时遇到一个状态为not_finished_and_being_considered的节点

        # 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1
        course_id_to_course_status_map: dict[int, "str"] = {}
        for course in range(numCourses):
            course_id_to_course_status_map[course] = "0"

        # 部分课程没有前置课程所以 course_id_to_course_status_map 里面部分元素
        # 不在 course_to_prerequisites_map 里面。
        course_to_prerequisites_map: dict[int, list[int]] = {}
        for courser1_id, courser2_id in prerequisites:
            if courser1_id not in course_to_prerequisites_map:
                course_to_prerequisites_map[courser1_id] = [courser2_id]
            else:
                course_to_prerequisites_map[courser1_id].append(courser2_id)
        
        def traverse(course_id: int) -> bool:
            if course_id_to_course_status_map[course_id] == "0":
                course_id_to_course_status_map[course_id] = "1"
                # 也许该课程没有前置课程
                course_prerequisites = course_to_prerequisites_map.get(course_id, [])
                for prerequisite in course_prerequisites:
                    loop_found = traverse(prerequisite)
                    if loop_found is True:
                        return True
                course_id_to_course_status_map[course_id] = "2"
                return False
            elif course_id_to_course_status_map[course_id] == "1":  # 存在环
                return True
            elif course_id_to_course_status_map[course_id] == "2":
                return False
        
        # 这个图可能有多个连通分量
        loop_found_: bool = False
        for course in course_id_to_course_status_map:
            loop_found_ = traverse(course)
            if loop_found_ is True:
                break
        return not loop_found_

    # 210. 课程表 II
    # https://leetcode.cn/problems/course-schedule-ii/
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        result: list[int] = []

        course_id_to_course_status_map: dict[int, "str"] = {}
        for course in range(numCourses):
            course_id_to_course_status_map[course] = "0"

        course_to_prerequisites_map: dict[int, list[int]] = {}
        for courser1_id, courser2_id in prerequisites:
            if courser1_id not in course_to_prerequisites_map:
                course_to_prerequisites_map[courser1_id] = [courser2_id]
            else:
                course_to_prerequisites_map[courser1_id].append(courser2_id)

        def traverse(course_id: int) -> bool:
            if course_id_to_course_status_map[course_id] == "0":
                course_id_to_course_status_map[course_id] = "1"
                # 也许该课程没有前置课程
                course_prerequisites = course_to_prerequisites_map.get(course_id, [])
                for prerequisite in course_prerequisites:
                    loop_found = traverse(prerequisite)
                    if loop_found is True:
                        return True
                course_id_to_course_status_map[course_id] = "2"
                result.append(course_id)
                return False
            elif course_id_to_course_status_map[course_id] == "1":  # 存在环
                return True
            elif course_id_to_course_status_map[course_id] == "2":
                return False

        # 这个图可能有多个连通分量
        loop_found_: bool = False
        for course in course_id_to_course_status_map:
            loop_found_ = traverse(course)
            if loop_found_ is True:
                break
        return [] if loop_found_ else result
