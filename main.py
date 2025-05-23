def levestain_distance(str1: str, str2: str) -> int:
    """
    Функция вычисляет **Редакционное расстояние (Levenshtein Distance)**,
    то есть минимальное количество операций (вставка, удаление, замена) для
    превращения `str1` в `str2`.

    🔹 Алгоритм (Динамическое программирование O(m * n)):
    1️⃣ Используем `dp[i][j]`, где `dp[i][j]` — минимальное количество операций
       для преобразования `str1[:i]` в `str2[:j]`.
    2️⃣ Базовые случаи:
        - `dp[i][0] = i` (удаляем `i` символов из `str1`).
        - `dp[0][j] = j` (вставляем `j` символов в `str1`).
    3️⃣ Заполняем `dp` по правилам:
        - Если `str1[i-1] == str2[j-1]`, `dp[i][j] = dp[i-1][j-1]` (символы совпадают).
        - Иначе `dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)`,
          где:
            - `dp[i-1][j] + 1` — удаление из `str1`.
            - `dp[i][j-1] + 1` — вставка в `str1`.
            - `dp[i-1][j-1] + 1` — замена символа.
    4️⃣ Итоговый ответ: `dp[len(str1)][len(str2)]`.

    🔹 Временная сложность: **O(m * n)** — два вложенных цикла.
    🔹 Пространственная сложность: **O(m * n)** — `dp` таблица.

    :param str1: str - первая строка.
    :param str2: str - вторая строка.
    :return: int - минимальное количество операций редактирования.
    """

    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 1. Инициализация базовых случаев
    for i in range(m + 1):
        dp[i][0] = i  # Удаляем i символов

    for j in range(n + 1):
        dp[0][j] = j  # Вставляем j символов

    # 2. Заполняем DP таблицу
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:  # Символы совпадают
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Удаление
                    dp[i][j - 1] + 1,  # Вставка
                    dp[i - 1][j - 1] + 1  # Замена
                )

    return dp[m][n]


# 🔹 Тестируем
s1 = "test"
s2 = "tset"
print(levestain_distance(s1, s2))  # ✅ 2

s1 = "kitten"
s2 = "sitting"
print(levestain_distance(s1, s2))  # ✅ 3

s1 = "flaw"
s2 = "lawn"
print(levestain_distance(s1, s2))  # ✅ 2

s1 = "abcdef"
s2 = "azced"
print(levestain_distance(s1, s2))  # ✅ 3
