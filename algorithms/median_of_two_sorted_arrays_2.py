"""https://leetcode.com/problems/median-of-two-sorted-arrays/description/"""

"""
4. Median of Two Sorted Arrays
Hard
Topics
Companies

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            """Если первый массив (nums1) длиннее второго (nums2), то мы меняем их местами. 
             Это обеспечивает, что бинарный поиск всегда выполняется по меньшему массиву (nums1).
             Это важно для оптимальной работы алгоритма.
             """
            # If length first more second
            nums1, nums2 = nums2, nums1

        """Здесь мы вычисляем длины массивов nums1 и nums2. Эти значения нужны для корректного определения границ поиска и индексов."""
        first_array_length = len(nums1)  # Count nums in first massive
        second_array_length = len(nums2)  # Count nums in second massive

        """
        total — общая длина двух массивов.
        total_mid — индекс, разделяющий "левую" и "правую" части объединенного массива.
        left, right — начальные границы бинарного поиска. 
        left указывает на начало, 
        а right — на конец меньшего массива.
        """
        total = first_array_length + second_array_length  # Определяем общую длину массива
        total_mid = total // 2  # Определяем условный центр между массивами.
        left, right = 0, first_array_length - 1  # Определяем два курсора согласно границам массива

        while True:  # run search
            mid_index_by_nums1 = (left + right) // 2  # Определяем индекс текущего диапазона в nums1.
            mid_index_by_nums2 = total_mid - mid_index_by_nums1 - 2  # Определяем индекс текущего диапазона в nums2. Индекс в nums2, который соответствует "зеркальному" разделению с учетом total_mid.

            """
            Алгоритм делит объединенные массивы так, чтобы обе части (левая и правая) содержали примерно одинаковое количество элементов.

            Получение значений на границах разделения:
            """
            left_elem_by_nums1 = nums1[mid_index_by_nums1] if mid_index_by_nums1 >= 0 else float(
                "-inf")  # Проверяем что бы индекс не ушел за границы массивов
            right_elem_by_nums1 = nums1[mid_index_by_nums1 + 1] if (
                                                                               mid_index_by_nums1 + 1) < first_array_length else float(
                "inf")  # Проверяем что бы индекс не ушел за границы массивов
            left_elem_by_nums2 = nums2[mid_index_by_nums2] if mid_index_by_nums2 >= 0 else float(
                "-inf")  # Проверяем что бы индекс не ушел за границы массивов
            right_elem_by_nums2 = nums2[mid_index_by_nums2 + 1] if (
                                                                               mid_index_by_nums2 + 1) < second_array_length else float(
                "inf")  # Проверяем что бы индекс не ушел за границы массивов

            """
            Эти четыре переменные — значения на границах разделения:

            left_elem_by_nums1 и right_elem_by_nums1 — элементы слева и справа от разделения в массиве nums1.
            left_elem_by_nums2 и right_elem_by_nums2 — элементы слева и справа от разделения в массиве nums2.

            Если индекс выходит за пределы массива, используется −∞−∞ или +∞+∞, чтобы корректно обрабатывать граничные случаи.
            """

            """Проверка корректности разделения."""
            median: float
            if left_elem_by_nums1 <= right_elem_by_nums2 and left_elem_by_nums2 <= right_elem_by_nums1:
                """
                Это главное условие алгоритма:

                left_elem_by_nums1 <= right_elem_by_nums2: Максимум левой части массива nums1 должен быть меньше или равен минимуму правой части массива nums2.
                left_elem_by_nums2 <= right_elem_by_nums1: Максимум левой части массива nums2 должен быть меньше или равен минимуму правой части массива nums1.

                Если это условие выполняется, значит, массивы разделены правильно.
                """
                if total % 2:
                    median = min(right_elem_by_nums1, right_elem_by_nums2)

                    return median

                median = (max(left_elem_by_nums1, left_elem_by_nums2) + min(right_elem_by_nums1,
                                                                            right_elem_by_nums2)) / 2

                return median

            elif left_elem_by_nums1 > right_elem_by_nums2:
                """
                 Корректировка границ бинарного поиска

                 Если first_left > second_right, значит, мы слишком далеко сместились вправо в nums1.
                 Нужно уменьшить right.
                 В противном случае сдвигаем left, чтобы продвинуться вправо в nums1.
                """
                right = mid_index_by_nums1 - 1
            else:
                left = mid_index_by_nums1 + 1


if __name__ == '__main__':
    import timeit
    from median_of_two_sorted_arrays import Solution as SolutionDefaultTools

    solution = Solution()

    assert solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]) == 2
    assert solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]) == 2.50
    assert solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2, 4, 5, 6]) == 3.50
    assert solution.findMedianSortedArrays(nums1=[2, 4, 5, 6], nums2=[1, 3]) == 3.50
    assert solution.findMedianSortedArrays(nums1=[2, 4, 6, 7], nums2=[1, 3, 5]) == 4.00

    solution_default = SolutionDefaultTools()

    nums1_ = [i for i in range(1, 1001, 2)]
    nums2_ = [i for i in range(2, 1002, 2)]


    def test_binary_search_solution():
        solution.findMedianSortedArrays(nums1_, nums2_)


    def test_default_solution():
        solution_default.findMedianSortedArrays(nums1_, nums2_)


    my_solution_time = timeit.timeit(test_binary_search_solution, number=1000)
    my_solution_time_2 = timeit.timeit(test_default_solution, number=1000)

    print(f"Время выполнения моего решения: {my_solution_time:.6f} секунд")  # 0.001156 секунд
    print(
        f"Время выполнения решения c помощью стандартных инструментов: {my_solution_time_2:.6f} секунд")  # 8.481053 секунд
