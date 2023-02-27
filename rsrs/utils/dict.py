#!/usr/bin/env python
# coding: utf-8


def change_dict_key(d: dict, old_key: str, new_key: str, default_value=None):
    """Change dict key.

    Args:
        d (dict): Target dict.
        old_key (str): Old key.
        new_key (str): New key.
        default_value (Any): Value to be added as a new element when a non-existent key is selected. (default=None)

    Example:
        >>> d = {'k1': 1, 'k2': 2, 'k3': 3}
        >>> change_dict_key(d, 'k1', 'k10')
        >>> print(d)
        >>> # {'k2': 2, 'k3': 3, 'k10': 1}

        >>> d = {'k1': 1, 'k2': 2, 'k3': 3}
        >>> change_dict_key(d, 'k10', 'k100')
        >>> print(d)
        >>> # {'k1': 1, 'k2': 2, 'k3': 3, 'k100': None}

        >>> d = {'k1': 1, 'k2': 2, 'k3': 3}
        >>> change_dict_key(d, 'k10', 'k100', 100)
        >>> print(d)
        >>> # {'k1': 1, 'k2': 2, 'k3': 3, 'k100': 100}
    """
    d[new_key] = d.pop(old_key, default_value)


def get_swap_dict(d: dict):
    """Get dict that key and value have been swapped.

    Args:
        d (dict): Target dict.

    Returns:
        (dict): Swapped dict.

    Examples:
        >>> d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
        >>> d_swap = get_swap_dict(d)
        >>> print(d_swap)
        >>> # {'val1': 'key1', 'val2': 'key2', 'val3': 'key3'}
    """
    return {v: k for k, v in d.items()}


def get_key_from_list_in_value(d: dict, query: str):
    """Get key from list in value of dict.

    Args:
        d (dict): Target dict.
        query (str): String to search.

    Returns:
        key (str): Swapped dict.

    Examples:
        >>> d = {'key1': ['val1-1', 'val1-2'], 'key2': ['val2-1', 'val2-2', 'val2-3']}
        >>> query = 'val1-2'
        >>> target_key = get_key_from_list_in_value(d, query)
        >>> print(target_key)
        >>> # key1
    """
    for key, value in d.items():
        if query in value:
            return key
