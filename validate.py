from typing import List
import os

WORDLISTS_DIR = "wordlists"


def _extract_and_sort_wordlist(file_path: str) -> List[str]:
    with open(file_path, "r") as f:
        return sorted([i.strip().lower() for i in f.readlines()])


def _write_validated_wordlist(filepath: str, validated_wordlist: List[str]) -> None:
    with open(filepath, "w") as new_file:
        for word in validated_wordlist:
            new_file.write(f"{word}\n")


def main():
    for wordlist_file in os.listdir(WORDLISTS_DIR):
        file_path_to_wordlist = f"{WORDLISTS_DIR}/{wordlist_file}"
        sorted_wordlist = _extract_and_sort_wordlist(file_path_to_wordlist)
        _write_validated_wordlist(file_path_to_wordlist, sorted_wordlist)


if __name__ == "__main__":
    main()
