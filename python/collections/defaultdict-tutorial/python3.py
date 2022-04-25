# Enter your code here. Read input from STDIN. Print output to STDOUT
# harder way
# if __name__ == "__main__":
#     n, m = input().split()
#     arr_a = list()
#     arr_b = list()
#     for _ in range(0, int(n)):
#         arr_a.append((input()))
#     for _ in range(0, int(m)):
#         arr_b.append((input()))
#     for i in arr_b:
#         output_index_arr = list()
#         for j in range(0, len(arr_a)):
#             if arr_a[j] == i:
#                 output_index_arr.append(str(j+1))
#         if len(output_index_arr) == 0:
#             output_index_arr.append("-1")
#         print(" ".join(output_index_arr))

# easier way when leveraging defaultdict
from collections import defaultdict

n, m = map(int, input().split())

a_dict = defaultdict(list)
[a_dict[input()].append(str(i+1)) for i in range(0, n)]

for _ in range(0, m):
    m_value = input()
    print(" ".join(a_dict[m_value]) if len(a_dict[m_value]) > 0 else "-1")