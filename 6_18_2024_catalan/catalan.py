import catalan
import os
import time
import matplotlib.pyplot as plt
dirname = os.path.dirname("./")
import itertools

def parenthesizations(n):
  """
  Returns a set of all possible parenthesizations of length n.

  Parameters:
    n (int): The length of the parenthesizations.

  Returns:
    A set of strings, where each inner string represents a valid parenthesization of length n.
  
  Example:
  >>> parenthesizations(3)
  {'((()))', '(()())', '(())()', '()(())', '()()()'}
  """
  
  if n == 0:
        return [""]
  else:
      output = []
      for i in range(n):
          for left in parenthesizations(i):
              for right in parenthesizations(n - 1 - i):
                  output.append(f"({left}){right}")
      return output

def save_parenthesizations(n, filepath):
    parens = parenthesizations(n)
    with open(filepath, 'w') as f:
        for p in parens:
            f.write(p + '\n')

os.makedirs('data', exist_ok=True)
os.makedirs('figures', exist_ok=True)

times = []

for n in range(1, 11):
    start_time = time.time()
    filepath = f'data/catalan_parenthesizations_{n}.txt'
    save_parenthesizations(n, filepath)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
    print(f"n={n}, time={elapsed_time:.4f} seconds")

plt.figure()
plt.plot(range(1, 11), times, marker='o')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time taken to generate Catalan Parenthesizations')
plt.grid(True)
plt.savefig('figures/catalan_parenthesizations.png')
plt.show()













def product_orders(n):
  """
  Returns a set of all possible ways to multiply of n elements.

  Parameters:
    n (int): The number of elements multiplied.

  Returns:
    A set of strings where each string represents a way to multiply n elements.
  
  Example:
  >>> product_orders(4)
  {'((?*?)*?)*?', '(?*(?*?))*?', '(?*?)*(?*?)', '?*((?*?)*?)', '?*(?*(?*?))'}
  """
  
  if n == 0:
    return {""}
  elif n == 1:
    return {"?"}
  elif n == 2:
    return {"?*?"}
  else:
    results = []
    for i in range(1, n):
        left = product_orders(i)
        right = product_orders(n - i)
        for L in left:
            for R in right:
                if i == 1:
                    left_part = f"{L}"
                else:
                    left_part = f"({L})"
                if (n - i) == 1:
                    right_part = f"{R}"
                else:
                    right_part = f"({R})"
                results.append(f"{left_part}*{right_part}")
    return results

os.makedirs("data", exist_ok=True)
os.makedirs("figures", exist_ok=True)

ns = list(range(2, 12))
times = []

for n in ns:
    start_time = time.time()
    orders = product_orders(n)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
    
    with open(f"data/catalan_product_orders_{n}.txt", "w") as f:
        for order in orders:
            f.write(order + "\n")

plt.figure()
plt.plot(ns, times, marker='o')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time to Generate Product Orders')
plt.savefig("figures/catalan_product_orders.png")
plt.show()









"""def permutations_avoiding_231(n):"""
"""
  Returns a set of permutations of length n avoiding the pattern 2-3-1.
  
  Parameters:
    n (int): The length of the permutation.
  
  Returns:
    A set of permutations of length n that do not contain the pattern 2-3-1.
  
  Example:
  >>> permutations_avoiding_231(4)
  {(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 2, 1, 4), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 3, 1, 2), (4, 3, 2, 1)}
  """
"""
  if n < 3:
    return set(itertools.permutations(range(1, n+1)))
  else:
    # TODO
    pass
  """
from itertools import permutations
def is_231_avoiding(perm):
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if perm[j] > perm[i] > perm[k]:
                    return False
    return True

def permutations_avoiding_231(n):
    if n < 3:
        return set(permutations(range(1, n+1)))
    else:
        all_perms = permutations(range(1, n + 1))
        avoiding_perms = {perm for perm in all_perms if is_231_avoiding(perm)}
        return avoiding_perms


data_dir = 'data'
figures_dir = 'figures'
os.makedirs(data_dir, exist_ok=True)
os.makedirs(figures_dir, exist_ok=True)

times = []

for n in range(1, 11):
    start_time = time.time()
    avoiding_231_perms = permutations_avoiding_231(n)
    end_time = time.time()
    
    with open(f'{data_dir}/catalan_permutations_{n}.txt', 'w') as file:
        for perm in avoiding_231_perms:
            file.write(' '.join(map(str, perm)) + '\n')
    
    times.append(end_time - start_time)

plt.figure()
plt.plot(range(1, 11), times, marker='o')
plt.title('Time to Generate 231-Avoiding Permutations')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.savefig(f'{figures_dir}/catalan_permutations.png')
plt.show()










def triangulations(n):
  """
  Returns a set of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a tuple of internal edges. Vertices are labeled 0 through n-1 clockwise.

  Parameters:
    n (int): The number of sides of the polygon.

  Returns:
    A set of tuple of pairs, where each pair represents an internal edge in the triangulation.
  
  Example:
  >>> triangulations(5)
  {((0, 3), (1, 3)), ((1, 4), (2, 4)), ((1, 3), (1, 4)), ((0, 2), (2, 4)), ((0, 2), (0, 3))}
  """
  if n < 3:
    return set()
  elif n == 3:
    return {tuple()}
  dp = [[set() for _ in range(n)] for _ in range(n)]
    
  for length in range(2, n):
      for i in range(n - length):
          j = i + length
          for k in range(i + 1, j):
              left_triangulations = dp[i][k]
              right_triangulations = dp[k][j]
              
              if not left_triangulations:
                  left_triangulations = {frozenset()}
              if not right_triangulations:
                  right_triangulations = {frozenset()}
              
              for lt in left_triangulations:
                  for rt in right_triangulations:
                      triangulation = lt.union(rt).union({(i, k), (k, j)})
                      dp[i][j].add(frozenset(triangulation))
  
  result = dp[0][n - 1]
  
  filtered_result = set()
  for triangulation in result:
      valid_edges = {edge for edge in triangulation if not ((edge[0] == 0 and edge[1] == n - 1) or (edge[0] == 0 and edge[1] == 1) or (edge[0] == n - 1 and edge[1] == 0))}
      filtered_result.add(frozenset(valid_edges))

  return {tuple(sorted(edge)) for triangulation in filtered_result for edge in triangulation}
# Code generated by AI tools


os.makedirs('data', exist_ok=True)
os.makedirs('figures', exist_ok=True)

times = []
ns = range(3, 13)

for n in ns:
    start_time = time.time()
    result = triangulations(n)
    end_time = time.time()
    
    with open(f'data/catalan_triangulations_{n}.txt', 'w') as f:
        for triangulation in result:
            f.write(f"{triangulation}\n")
    
    times.append(end_time - start_time)

plt.figure()
plt.plot(ns, times, marker='o')
plt.xlabel('Number of Sides (n)')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken to Generate Triangulations for n-sided Polygon')
plt.grid(True)
plt.savefig('figures/catalan_triangulations.png')
plt.show()

