import os


def ft_tqdm(lst: range) -> None:
    """generateur qui affiche une barre de progression comme tqdm"""
    total = len(lst)
    width = os.get_terminal_size().columns
    for i, elem in enumerate(lst, 1):
        yield elem
        percent = i * 100 // total
        prefix = f"{percent:3d}%|["
        suffix = f"]| {i}/{total}"
        bar_len = width - len(prefix) - len(suffix) - 2
        filled = bar_len * i // total
        bar = ("=" * filled + ">").ljust(bar_len + 1)
        print(f"\r{prefix}{bar}{suffix}", end="", flush=True)