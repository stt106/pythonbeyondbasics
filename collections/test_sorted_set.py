import unittest
from sorted_set import SortedSet
from collections.abc import(Sized, Container, Iterable, Sequence, Set)

class TestConstruction(unittest.TestCase):

    def test_default(self):
        s = SortedSet()


    def test_empty(self):
        s = SortedSet([])


    def test_from_sequence(self):
        s = SortedSet([1, 2,3, 5])
        

    def test_with_duplicates(self):
        s = SortedSet([2, 3, 4, 4, 5])
    

    def test_from_iterable(self):
        def gen456():
            yield 4
            yield 5
            yield 6
        g = gen456()
        s = SortedSet(g)
    

class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([3, 2, 9, 4])
    
    def test_positive_contained(self):
        self.assertTrue(3 in self.s)
    
    def test_positive_not_contained(self):
        self.assertTrue(10 not in self.s)
    
    def test_negative_contained(self):
        self.assertFalse(2 not in self.s)
    
    def test_negative_not_contained(self):
        self.assertFalse(4 not in self.s)
        
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Container))

class TestSizedProtocl(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(0, len(s))
    
    def test_one(self):
        s = SortedSet([4])
        self.assertEqual(1, len(s))
    
    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(10, len(s))
    
    def test_duplicate(self):
        s = SortedSet([4, 4, 4, 2])
        self.assertEqual(2, len(s))

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sized))


class TestIterableProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([2, 14, 1, 9, 10])
    
    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 9)
        self.assertEqual(next(i), 10)
        self.assertEqual(next(i), 14)
        self.assertRaises(StopIteration, lambda : next(i))
    
    def test_for_loop(self):
        index = 0
        expected = [1, 2, 9, 10, 14]
        for i in self.s:
            self.assertEqual(i, expected[index])
            index += 1
    
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))

class TestEqualityProtocol(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(SortedSet() == SortedSet())
    
    def test_positive_equal(self):
        self.assertTrue(SortedSet([1, 3, 2, 19]) == SortedSet([19, 3, 1, 2]))
    
    def test_negative_equal(self):
        self.assertFalse(SortedSet([3, 4, 1, 2]) == SortedSet([1, 2, 3]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([3, 2, 1]) == [3, 2, 1])

    def test_identity(self):
        self.assertTrue(SortedSet([3, 2, 1, 5]) == SortedSet([1, 2, 3, 5]))

    ############ Inequality protocol test ##########
    def test_positive_unequal(self):
        self.assertTrue(SortedSet([4, 2, 15, 3]) != SortedSet([1, 2, 3]))

    def test_negative_unequal(self):
        self.assertFalse(SortedSet([1, 2, 3]) != SortedSet([3, 2, 1]))

    def test_type_mismatch_unequal(self):
        self.assertTrue(SortedSet([1, 2, 3]) != [1, 2, 3])
    
    def test_identical_unequal(self):
        s = SortedSet([1, 2 , 3])
        self.assertFalse(s != s)


class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([13, 1, 8, 4, 7])
    
    def test_index_zero(self):
        self.assertEqual(1, self.s[0])

    def test_index_four(self):
        self.assertEqual(13, self.s[4])
    
    def test_index_beyond_end(self):
        with self.assertRaises(IndexError):
            self.s[5]
    
    def test_index_minus_one(self):
        self.assertEqual(13, self.s[-1])
    
    def test_index_minus_five(self):
        self.assertEqual(1, self.s[-5])
    
    def test_index_beyond_the_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1, 4, 7]))
    
    def test_slice_from_middle(self):
        self.assertEqual(self.s[3:], SortedSet([8, 13]))

    def test_slice_arbitrary_range(self):
        self.assertEqual(self.s[2:4], SortedSet([7, 8]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)    

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedSet())

    def test_reversed(self):
        reversed(self.s)
        self.assertTrue(self.s == SortedSet([13, 8, 7, 4, 1]))

    def test_index_positive(self):
        self.assertTrue(self.s.index(4) == 1)
    
    def test_index_negative(self):
        with self.assertRaises(ValueError):
            self.s.index(0)

    def test_count_zero(self):
        self.assertTrue(self.s.count(12) == 0)
    
    def test_count_one(self):
        self.assertTrue(self.s.count(7) == 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sequence))

    def test_concatenate_disjoint(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet([4, 5, 6])
        expected = SortedSet([1, 2, 3, 4, 5, 6])
        self.assertEqual(expected, s1 + s2)

    def test_concatenate_equal(self):
        s = SortedSet([2, 3, 5])
        self.assertEqual(s, s + s)
    

    def test_concatenate_intersecting(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet([3, 4, 5])
        expected = SortedSet([1, 2, 3, 4, 5])
        self.assertEqual(expected, s1 + s2)


    def test_repetition_zero_right(self):
        s = SortedSet([1, 3, 2])
        self.assertEqual(SortedSet(), s * 0)
    
    def test_repetition_nonzero_right(self):
        s = SortedSet([1, 3, 4])
        self.assertEqual(s, s * 100)

    def test_repetition_nonzero_left(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(s, 100 * s)

    def test_repetition_zero_left(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(SortedSet(), 0 * s)


class TestReprProtocol(unittest.TestCase):

    def test_empty(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr_some(self):
        s = SortedSet([3, 1, 5, 2])
        self.assertEqual(repr(s), "SortedSet([1, 2, 3, 5])")      


class TestSetOperations(unittest.TestCase):

    def test_lt_positive(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet({1, 2, 3, 5})
        self.assertTrue(s1 < s2)
    
    def test_lt_negative(self):
        s1 = SortedSet([1, 2, 3, 4])
        s2 = SortedSet({1, 2, 3, 4})
        self.assertFalse(s1 < s2)

    def test_le_lt_positive(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet({1, 2, 3, 4})
        self.assertTrue(s1 <= s2)
    
    def test_le_eq_positive(self):
        s1 = SortedSet([1, 2, 3, 4])
        s2 = SortedSet({1, 2, 3, 4})
        self.assertTrue(s1 <= s2)

    def test_le_negative(self):
        s1 = SortedSet([1, 2, 3])
        s2 = SortedSet({1, 2})
        self.assertFalse(s1 <= s2)

    
    def test_gt_positive(self):
        s1 = SortedSet([1, 2, 3, 4])
        s2 = SortedSet([2, 3, 4])
        self.assertTrue(s1 > s2)
    
    def test_gt_negative(self):
        s1 = SortedSet([1, 2, 3, 4])
        s2 = SortedSet({2, 3, 4, 5})
        self.assertFalse(s1 >= s2)


    def test_ge_gt_positive(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = SortedSet({1, 2, 3, 4})
        self.assertTrue(s1 >= s2)
    

    def test_ge_eq_positive(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = SortedSet({1, 2, 3, 4, 5})
        self.assertTrue(s1 >= s2)


    def test_ge_negative(self):
        s1 = SortedSet([1, 2, 4, 5, 6])
        s2 = SortedSet({2, 3, 4,5})
        self.assertFalse(s1 >= s2)

    def test_subset_positive(self):
        s1 = SortedSet([1, 2, 3, 4])
        s2 = SortedSet([1, 2, 3, 4])
        self.assertTrue(s1.issubset(s2))
    
    def test_subset_negative(self):
        s1 = SortedSet([2, 3, 4])
        s2 = SortedSet([3, 4, 5])
        self.assertFalse(s1.issubset(s2))

    def test_subset_proper_positive(self):
        s1 = SortedSet([1, 2, 3])
        s2 = {2, 3}
        self.assertTrue(s2 < s1)
    
    def test_subset_proper_negative(self):
        s1 = SortedSet([2, 3, 4, 5])
        s2 = {2, 3, 4, 5}
        self.assertFalse(s1 < s2)
    
    def test_superset_positive(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = SortedSet({2, 3, 4})
        self.assertTrue(s1.issuperset(s2))
    
    def test_superset_proper_positive(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = SortedSet({1, 2, 3})
        self.assertTrue(s1.issuperset(s2))
    
    def test_superset_proper_negative(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = SortedSet({1, 2, 3, 4, 5})
        self.assertTrue(s1.issuperset(s2))

    def test_superset_negative(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = SortedSet({1, 2, 3, 4, 5, 6})
        self.assertFalse(s1.issuperset(s2))

    def test_intersection(self):
        s1 = SortedSet([1, 2,3 , 4])
        s2 = SortedSet([2, 3, 4, 5])
        expected = SortedSet([2, 3, 4])
        self.assertEqual(expected, s1.intersection(s2))
    
    def test_union(self):
        s1 = SortedSet([1, 2, 3, 4])
        s2 = [2, 3, 4, 5]
        expected = SortedSet([1, 2, 3, 4, 5])
        self.assertEqual(expected, s1.union(s2))
    
    def test_symmetric_difference(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = [2, 3, 4, 6]
        expected = SortedSet([1, 5, 6])
        self.assertEqual(expected, s1.symmetric_difference(s2))
    
    def test_difference(self):
        s1 = SortedSet([2, 3, 4, 5, 6])
        s2 = [1, 2, 3, 4]
        expected = SortedSet([5, 6])
        self.assertEqual(expected, s1.difference(s2))
    
    def test_disjoint_positive(self):
        s1 = SortedSet([1, 2, 3, 4])
        s2 = SortedSet([7, 8, 5])
        self.assertTrue(s1.isdisjoint(s2))
    
    def test_disjoint_negative(self):
        s1 = SortedSet([1, 2, 3, 4, 5])
        s2 = SortedSet([2, 6, 7, 8])
        self.assertFalse(s1.isdisjoint(s2))

class TestSetProtocol(unittest.TestCase):
    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Set))


if __name__ == '__main__':
    unittest.main()