# test_solutions.py
import pytest
from ..coding_solutions import (
    find_duplicates,
    difference_set,
    square_tuple,
    merge_dicts,
    ToDo,
    flatten_list_once
)


def test_find_duplicates():
    """Test the find_duplicates function."""
    # Test with duplicates
    result = find_duplicates([1, 2, 2, 3, 4, 4, 5])
    assert set(result) == {2, 4}
    
    # Test with no duplicates
    result = find_duplicates([1, 2, 3, 4, 5])
    assert result == []
    
    # Test with all duplicates
    result = find_duplicates([1, 1, 1, 1])
    assert set(result) == {1}
    
    # Test with empty list
    result = find_duplicates([])
    assert result == []


def test_difference_set():
    """Test the difference_set function."""
    # Test basic case
    result = difference_set({1, 2, 3}, {2, 3, 4})
    assert result == {1}
    
    # Test with no common elements
    result = difference_set({1, 2}, {3, 4})
    assert result == {1, 2}
    
    # Test with identical sets
    result = difference_set({1, 2}, {1, 2})
    assert result == set()
    
    # Test with empty first set
    result = difference_set(set(), {1, 2})
    assert result == set()


def test_square_tuple():
    """Test the square_tuple function."""
    # Test basic case
    result = square_tuple((1, 2, 3))
    assert result == (1, 4, 9)
    
    # Test with negative numbers
    result = square_tuple((-1, -2, 0))
    assert result == (1, 4, 0)
    
    # Test with single element
    result = square_tuple((5,))
    assert result == (25,)
    
    # Test with empty tuple
    result = square_tuple(())
    assert result == ()


def test_merge_dicts():
    """Test the merge_dicts function."""
    # Test basic case
    result = merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    assert result == {'a': 1, 'b': 5, 'c': 4}
    
    # Test with no common keys
    result = merge_dicts({'a': 1}, {'b': 2})
    assert result == {'a': 1, 'b': 2}
    
    # Test with empty second dict
    result = merge_dicts({'a': 1, 'b': 2}, {})
    assert result == {'a': 1, 'b': 2}
    
    # Test with both empty dicts
    result = merge_dicts({}, {})
    assert result == {}


def test_todo_class():
    """Test the ToDo class."""
    # Test initialization
    todo = ToDo()
    assert todo.list_tasks() == []
    
    # Test adding tasks
    todo.add_task("Buy milk")
    assert todo.list_tasks() == ["Buy milk"]
    
    todo.add_task("Read book")
    assert todo.list_tasks() == ["Buy milk", "Read book"]
    
    # Test removing tasks
    todo.remove_task("Buy milk")
    assert todo.list_tasks() == ["Read book"]
    
    # Test removing non-existent task (should not raise error)
    todo.remove_task("Non-existent task")
    assert todo.list_tasks() == ["Read book"]
    
    # Test that list_tasks returns a copy
    tasks = todo.list_tasks()
    tasks.append("New task")
    assert todo.list_tasks() == ["Read book"]


def test_flatten_list_once():
    """Test the flatten_list_once function."""
    # Test basic case
    result = flatten_list_once([[1, 2], [3, 4], 5])
    assert result == [1, 2, 3, 4, 5]
    
    # Test with mixed elements
    result = flatten_list_once([[1], 2, [3, 4], 5])
    assert result == [1, 2, 3, 4, 5]
    
    # Test with empty list
    result = flatten_list_once([])
    assert result == []
    
    # Test with no nested lists
    result = flatten_list_once([1, 2, 3])
    assert result == [1, 2, 3]
    
    # Test with empty nested lists
    result = flatten_list_once([[], [1, 2], []])
    assert result == [1, 2]
