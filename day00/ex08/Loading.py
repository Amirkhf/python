import os


def ft_tqdm(lst: range):
    """generateur qui affiche une barre de progression comme tqdm"""
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    for i, elem in enumerate(lst, 1):
        yield elem
        info = f"| {i}/{len(lst)}"
        n = width - len(info) - 8
        bar = "=" * (n * i // len(lst)) + ">"
        print(f"\r{i * 100 // len(lst):3d}%|[{bar:<{n + 1}}]{info}",
              end="", flush=True)
