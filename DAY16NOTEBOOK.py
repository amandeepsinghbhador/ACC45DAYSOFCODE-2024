T = int(input())

for _ in range(T):
    N = int(input())

    pages_per_kg = 1000
    pages_per_notebook = 100
    total_pages = N * pages_per_kg
    notebooks = total_pages // pages_per_notebook
    print(notebooks)