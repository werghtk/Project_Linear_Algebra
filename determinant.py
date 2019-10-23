import copy


def minorize(matrix, row, column):
    """    Функция находит минор элемента матрицы.

    Функция принимает в качестве аргументов матрицу, представленную в виде списка списков,
    минор которой нужно найти, номер строки и номер столбца элемента, к которому нужно
    найти минор. Создается копия матрицы и из нее удаляются строка и столбец с указанными номерами."""
    try:
        minor = copy.deepcopy(matrix)
        [minor[i].pop(column) for i in range(len(minor))]
        minor.pop(row)
        return minor
    except:
        raise ValueError('Incorrect elements of matrix')


def determinant(matrix):
    """    Функция считает числовое значение определителя квадратной матрицы.

    Функция принимает в качестве аргумената квадратную матрицу, представленную в виде
    списка списков и вычисляет значение её определителя методом алгебраических
    дополнений. Для этого находится сумма всех произведений элементов первого столбца
    определителя на их алгебраические дополнения. Миноры, соответствующие этим
    алгебраическим дополнениям, находит вызываемая функция minorize(), а их числовые
    значения вычисляются рекурсивно.
    В случае, если матрица не является квадратной и/или её элементы не являются
    числами, возвращается ошибка.
    В противном случае функция возвращает числовое значение определителя."""
    try:
        if len(matrix) != len(matrix[0]):
            raise ValueError('Incorrect dimensions')
        det = 0
        if len(list(matrix)) == 1:
            return matrix[0][0]
        for j in range(len(matrix[0])):
            det += (-1)**j * matrix[0][j] * determinant(minorize(matrix, 0, j))
        return det
    except:
        raise ValueError('Incorrect elements of matrix')

